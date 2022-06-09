# -*- coding: utf-8 -*-
import pandas as pd
import re

#récupère les tweets au format texte, permet de les noter manuellement puis de créer un fichier csv avec les scores
FILE = "databaseset3.txt"
DELIMITER = "---"

#récupération du texte des tweets 
content = ""

with open(FILE, "r", encoding="utf8") as f:
    content = f.read()
    f.close()
tweets = []
content2 = re.split("'text': '", content)

for elem in content2:
    if (elem[:5] != "{'id'"):
        tweets += [re.split("', 'nombre_likes'", elem)[0]]

lst = []

#scoring manuel des tweets
for i in range(len(tweets)):
    if len(tweets[i]) > 1:
        tweets[i] = tweets[i].strip()
        tweets[i] = tweets[i].replace("\n", "")
        print(tweets[i])
        val = input("Posifif ou Negatif (y/n/h)? \n")
        if val == "y":
            lst += [[tweets[i], 1]]
        elif val == "n":
            lst += [[tweets[i], -1]]
        elif val == "h":
            lst += [[tweets[i], 0]]

#création d'un fichier csv pour stocker les résultats
df = pd.DataFrame(lst, columns=["text", "sentiment"])
df.to_csv("databaset3.csv")
