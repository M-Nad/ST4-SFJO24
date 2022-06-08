import re

FILE = "tweets.txt"
OUTPUT = "output.txt"
DELIMITER = "---"

content = ""

with open(FILE, "r", encoding="utf8") as f:
    content = f.read()
    f.close()

tweets = []
content2 = re.split("'text': '", content)

for elem in content2:
    if (elem[:5] != "{'id'"):
        tweets += [re.split("', 'nombre_likes'", elem)[0]]
# print(len(tweets))

for i in range(len(tweets)):
    tweets[i] = tweets[i].replace(r"\n"," ")
    tweets[i] = re.sub('@\w+',"",tweets[i])

with open(OUTPUT,"w", encoding="utf8") as f:
    f.writelines(tweets)