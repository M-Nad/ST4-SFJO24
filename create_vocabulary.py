from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import json

lemmatizer = WordNetLemmatizer()
eng_dic = words.words()
eng_dic_lemma = set()
untouched = ["us"]

for word in eng_dic:
    if word not in untouched:
        lemmatized = lemmatizer.lemmatize(word)
    else :
        lemmatized = word
    if not lemmatized in stopwords.words('english'):
        eng_dic_lemma.add(lemmatized)

bag_of_words = set()

voc = eng_dic_lemma.union(bag_of_words)

dic_voc = {}
i = 0
for word in voc:
    dic_voc[word]=i
    i+=1

with open('vocabulary_dic.json', 'w') as fp:
    json.dump(dic_voc, fp,  indent=4)