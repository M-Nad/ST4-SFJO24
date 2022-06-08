import pandas as pd

# Names for database

names = ["database.csv",
"database2.csv","database2.csv"]

# read them all
dataframes = []
for elem in names:
    dataframes.append(pd.read_csv(elem))
res = pd.concat(dataframes,ignore_index=True)

res.to_csv("db.csv")