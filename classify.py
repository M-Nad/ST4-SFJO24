import pandas as pd
import re

FILE = "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/tweets.txt"
DELIMITER = "---"

content = ""

with open(FILE, "r", encoding="utf8") as f:
    content = f.read()
    f.close()
# print(content[:100])
# print(re.split("'text': '",content)[1])
# exit()
tweets = []
content2 = re.split("'text': '", content)

for elem in content2:
    if (elem[:5] != "{'id'"):
        tweets += [re.split("', 'nombre_likes'", elem)[0]]

lst = []

for i in range(len(tweets)):
    if len(tweets[i]) > 1:
        tweets[i] = tweets[i].strip()
        tweets[i] = tweets[i].replace("\n","")
        print(tweets[i])
        val = input("Posifif ou Negatif (y/n)? \n")
        if val == "y":
            lst += [[tweets[i], 1]]
        elif val == "n":
            lst += [[tweets[i], 0]]

df = pd.DataFrame(lst, columns=["text", "sentiment"])

df.to_csv("database.csv")
