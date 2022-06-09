import pandas as pd

# Names for database

names = ["C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/database.csv",
         "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/database2.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/database08.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/databasebis05.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/databasebisn.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/databaset2.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/databaset3.csv", "C:/Users/bertd/OneDrive/Bureau/Scolaire 1A CS/EI ST4/ST4-SFJO24/csv/databaset5.csv"]

# read them all
dataframes = []
for elem in names:
    dataframes.append(pd.read_csv(elem))
res = pd.concat(dataframes, ignore_index=True)

res.to_csv("db_apprentissage.csv")
