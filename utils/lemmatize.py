import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.dowload("corpora")
# nltk.download("omw-1.4")
# nltk.download("punkt")

# print(stopwords.words('english'))

# import these modules

tweet = "Thank ye gods we have old Etonian Alexander Boris de Pfeffel Johnson and his chums to protect us from the elites"
untouched = ["us"]
lemmatizer = WordNetLemmatizer()

word_tokens = word_tokenize(tweet)

word_tokens_filtered = []
for word in word_tokens:
    if word not in untouched:
        lemmatized = lemmatizer.lemmatize(word)
    else :
        lemmatized = word
    if not lemmatized in stopwords.words('english'):
        word_tokens_filtered += [lemmatized]

print(word_tokens_filtered)

