from nltk.corpus import words
from nltk.corpus import stopwords
import json
import pandas as pd
import utils.lemma_token as LT

# path vers le csv d'apprentissage
csv_path = '.\csv\database08.csv'

lemmatizer = LT.lemmatizer

# vocabulaire depuis le dictionnaire anglais lemmatisé

eng_dic = words.words()
eng_dic_lemma = set()
untouched = LT.untouched

for word in eng_dic:
    if word not in untouched:
        lemmatized = lemmatizer.lemmatize(word)
    else :
        lemmatized = word
    if not lemmatized in stopwords.words('english'):
        eng_dic_lemma.add(lemmatized)

# vocabulaire sac de mots depuis l'ensemble d'apprentissage

bag_of_words = set()
text_col = pd.read_csv(csv_path)["text"]
text_app = ""
for txt in text_col:
    text_app+= txt+" "
tokens = LT.tweet_tokenizer_lemmatizer(text_app)
for token in tokens:
    bag_of_words.add(token)

# union des 2 vocabulaires 

voc = eng_dic_lemma.union(bag_of_words)

dic_voc = {}
i = 0
for word in voc:
    dic_voc[word]=i
    i+=1

with open('vocabulary_dic.json', 'w') as fp:
    json.dump(dic_voc, fp,  indent=4)