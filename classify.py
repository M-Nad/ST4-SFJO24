import pandas as pd

FILE = "file.txt"
DELIMITER = "---"

content = ""

with open(FILE,"r") as f:
    content = f.read()
    f.close()

tweets = content.split("---")

lst = []

for i in range (len(tweets)):
    print(tweets[i])
    val = input("Posifif ou Negatif (y/n)?")
    if val == "y":
        lst +=[[tweets[i], 1]]
    elif val == "n":
        lst +=[[tweets[i], 0]]

df = pd.DataFrame(lst,columns=["text","sentiment"])

df.to_csv("database.csv")