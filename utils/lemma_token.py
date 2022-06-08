from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
untouched = ["us"]

def tweet_tokenizer(text):
    filtered_tokens = []
    txt_formated = text.replace("\\n"," ")
    string_encode = txt_formated.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    tokens = word_tokenize(string_decode)
    for token in tokens:
        if not ("\\" in r"%r" % token):
            filtered_tokens.append(token)
    return filtered_tokens

def tweet_tokenizer_lemmatizer(text):
    tokens = tweet_tokenizer(text)
    tokens_lemmatized = []
    for word in tokens:
        if word not in untouched:
            lemmatized = lemmatizer.lemmatize(word)
        else :
            lemmatized = word
        if not lemmatized in stopwords.words('english'):
            tokens_lemmatized.append(lemmatized)
    return tokens_lemmatized