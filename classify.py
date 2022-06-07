FILE = "file.txt"
DELIMITER = "---"

POS = "pos.txt"
NEG = "neg.txt"

content = ""

with open(FILE,"r") as f:
    content = f.read()
    f.close()

tweets = content.split("---")

for i in range (len(tweets)):
    print(tweets[i])
    val = input("Posifif ou Negatif (y/n)?")
    if val == "y":
        with open(POS,"a") as file:
            file.write(tweets[i]+"---")
            file.close()
    elif val == "n":
        with open(NEG,"a") as file:
            file.write(tweets[i]+"---")
            file.close()

