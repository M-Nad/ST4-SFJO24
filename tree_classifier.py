from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
import json
import pickle
import pandas as pd
import utils.lemma_token as LT

csv_path = '.\csv\db_apprentissage.csv'

def regenerate_classifier(csv_path = '.\csv\database08.csv',filename = 'tree_classifier.sav'):

    tweet_tokenizer = LT.tweet_tokenizer_lemmatizer

    #univers du vocabulaire pour la vectorisation
    with open('vocabulary_dic.json') as f:
        voc = json.load(f)

    # données d'apprentissage / labels
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

    pickle.dump(clf, open(filename, 'wb'))


def predict(X_data,csv_path = '.\csv\database08.csv',filename = 'tree_classifier.sav'):

    # ouverture du classifier et vectorisation des données d'entrée
    with open('vocabulary_dic.json') as f:
        voc = json.load(f)
    tweet_tokenizer = LT.tweet_tokenizer_lemmatizer
    Data = pd.read_csv(csv_path)
    X_train_data = Data["text"].to_list()
    count_vect = CountVectorizer(vocabulary=voc,tokenizer=tweet_tokenizer)
    X_train_counts = count_vect.fit_transform(X_train_data)
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)

    loaded_clf = pickle.load(open(filename, 'rb'))
    X_counts = count_vect.fit_transform(X_data)
    X = tf_transformer.transform(X_counts)
    Y_predicted = loaded_clf.predict(X)
    return Y_predicted.tolist()