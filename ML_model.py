from operator import index
from os import path
import re
import pickle
from sklearn.datasets import load_files
from nltk.corpus import stopwords
import spacy
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


MATRIX_FILE="Database/Dataset_credibility/matrix_4.csv"

def train_model(matrix_file, model_name):
    """
    train a machine learning model (Random Forest) given a data binary matrix and return the model in a file named 
    like model_name
    RETURN : metrics of the model
    """
    matrix_df= pd.read_csv(matrix_file)

    X= matrix_df.drop(labels=['id','isRumor'], axis=1).values.tolist() #examples 
    y=matrix_df['isRumor'].tolist() #features

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train) 

    y_pred = classifier.predict(X_test)
    #print(X_test[0], len(X_test[0]))
    with open("ML_models/"+ model_name, 'wb') as picklefile:
        pickle.dump(classifier,picklefile)
    
    # METRICS
    conf_matrix = confusion_matrix(y_test,y_pred)
    class_report = classification_report(y_test,y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    return conf_matrix,class_report,accuracy


def new_features(text,lang='en'):
    """
    create a new list of features for a machine learning model according to a text document given as input
    Also pre process the document file to extract words in good format
    """
    stemmer = WordNetLemmatizer()
    documents = []
    for sen in range(0, len(text)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(text[sen]))
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)
        #Removing figures
        document = re.sub(" \d+", " ", document)
        # Converting to Lowercase
        document = document.lower()
        # Lemmatization
        if lang == 'fr':
            nlp = spacy.load('fr_core_news_md')
            doc = nlp(document)
            document = [word.lemma_ for word in doc]
        else:
            document = document.split()
            document = [stemmer.lemmatize(word) for word in document]

        document = ' '.join(document)
        documents.append(document)

    ##### create a set of features ###############
    tfidfconverter = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    tfidfconverter.fit_transform(documents)
    features = tfidfconverter.get_feature_names_out()

    return(features, documents)


def create_docs(docs,database): 
    """
    create a unique list of string containing all the text from the different files in the credibility corpus
    Also provides a list of 0 and 1 of the same length to indicate whether the tweet is a fake news or not
    """
    isRumor = [1 for k in range(len(docs))]
    for dataset in database:
        if dataset in ['pin', 'hollande', 'lemon', 'swine-flu']:
            df = pd.read_csv('Database/Dataset_credibility/'+ dataset+'.txt',
        names=['user_name','text','nb','nb2'], index_col=None,skiprows=1,sep=';')
            tweets = df['text'].values.tolist()
            docs += new_features(tweets)[1]
            isRumor += [1 for k in range(len(tweets))]
        else: 
            df= pd.read_csv('Database/Dataset_credibility/'+ dataset+'.txt',
        names=['text', 'non'], index_col=None,skiprows=1,sep='"')
            tweets=df['text'].values.tolist()
            docs += new_features(tweets)[1]
            isRumor += [0 for k in range(len(tweets))]
    return docs, isRumor



    
import random as rd
def create_matrix(f, docs, is_rumor):
    """
    create a matrix csv file which matches the input format for training_model
    This matrix contains the features given as parameters
    need to provide the list is_rumor to label the data
    """
    features_list = list(set(f)) #get  unique words as features
  
    features_df  = pd.DataFrame(data=features_list, columns=["ML_features"]) # create dataframe
    matrix_2=features_df
    has_article =[] 
    neg = []
    subjectiv = []
    c=0
    for doc in docs:
        try :  # try to translate the tweet in english if it is written in an other language 
            r=rd.random()
 
            #merge the two dataframes to know if each words of doc is in the features list
            matrix_2= matrix_2.merge(pd.DataFrame(data=TextBlob(doc).translate(to="en").split(), columns=[r]).drop_duplicates(), how='left', left_on='ML_features', right_on=r)
            neg.append(TextBlob(doc).translate(to="en").sentiment.polarity)
            subjectiv.append(TextBlob(doc).translate(to="en").sentiment.subjectivity)
 
            if doc.find('http')>=0 or doc.find('www')>=0: # to see if the tweet contains an article or not
                has_article+=[1]
            else:
                has_article+=[0]
        except:
  
            matrix_2= matrix_2.merge(pd.DataFrame(data=doc.split(), columns=[r]).drop_duplicates(), how='left', left_on='ML_features', right_on=r)
            neg.append(TextBlob(doc).sentiment.polarity)
            subjectiv.append(TextBlob(doc).sentiment.subjectivity)

            if doc.find('http')>=0 or doc.find('www')>=0:
                has_article+=[1]
            else:
                has_article+=[0]
        c+=1
        print(c) # compteur d'itérations 
    # fill na with 0 == the feature is not in the tweet
    matrix_2= matrix_2.fillna(0)

    mask = matrix_2.loc[:, matrix_2.columns != 'ML_features'].applymap(lambda x: isinstance(x, (int, float))) #find string in dataframe == word in tweet and features list
    matrix_2.loc[:, matrix_2.columns != 'ML_features'] = matrix_2.loc[:, matrix_2.columns != 'ML_features'].where(mask) # mask them
   
    matrix_2= matrix_2.fillna(1) # fill those string with 1 
  
    matrix_2=matrix_2.T # transpose the dataframe
    matrix_2.columns= matrix_2.iloc[0] # set features as column
    matrix_2=matrix_2[1:]
    matrix_2.reset_index(drop=True, inplace=True)
    matrix_2.index.names = ['id']
    matrix_2.insert(0, "isRumor", is_rumor, True)
    matrix_2.insert(1, "has_article", has_article, True)
    matrix_2.insert(2, "neg", neg, True)
    matrix_2.insert(3, "subjectiv", subjectiv, True)
    matrix_2['neg'] = matrix_2['neg'].apply(lambda x: 1 if x<0 else 0)
    matrix_2['subjectiv'] = matrix_2['subjectiv'].apply(lambda x: 1 if x>0.5 else 0)
    matrix_2.to_csv('Database/Dataset_credibility/matrix_4.csv')



################ To create the matrux containing the tweet credibility corpus ############
# with open("Database/Dataset_credibility/rumors_disinformation.txt", encoding='utf8') as f:
#     rumors = f.readlines()

# nf=new_features(rumors)
# features = list(nf[0])
# try:
#     features.remove('desinformation')
# except:
#     try: 
#         features.remove('rumor')
#     except:
#         features
# features += pd.read_csv("Database\Dataset_credibility\matrix.csv").columns.tolist()[2:]

# docs=nf[1][1:]

# database=['pin', 'hollande', 'lemon', 'swine-flu','randomtweets1','randomtweets2','randomtweets4']

# docs_rumor = create_docs(docs,database)
# create_matrix(features,docs_rumor[0],docs_rumor[1])

    



