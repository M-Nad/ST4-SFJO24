from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
import json
import pandas as pd
import utils.lemma_token as LT

csv_path = '.\csv\database08.csv'

tweet_tokenizer = LT.tweet_tokenizer_lemmatizer

#univers du vocabulaire pour la vectorisation
with open('vocabulary_dic.json') as f:
    voc = json.load(f)

# données d'apprentissage / labels

"""
X_data = ["positive","null","positive","negative"]
Y_label = [1,0,1,-1]
"""
Data = pd.read_csv(csv_path)
X_data = Data["text"].to_list()
Y_label = Data["sentiment"].to_list()


# traitement / vectorisation des entrées
count_vect = CountVectorizer(vocabulary=voc,tokenizer=tweet_tokenizer)
X_train_counts = count_vect.fit_transform(X_data)

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)

# entrainement du classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train_tf, Y_label)

def predict(X_data):
    X_counts = count_vect.fit_transform(X_data)
    X = tf_transformer.transform(X_counts)
    Y_predicted = clf.predict(X)
    return Y_predicted.tolist()


#X=["negative","positive"]
#print(predict(X))
