import sqlite3
import pandas as pd
import numpy as np
from tree_classifier import predict

def db_unscored_to_dataframe(path="./SQL_DB/apprentissage.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.text from TWEET t LEFT JOIN SCORE s ON s.tweet_id = t.tweet_id WHERE s.tweet_id IS Null", conn)
    conn.close()
    return res

def dataframe_to_score_df(dataframe):
    X_data = dataframe["text"].to_list()
    Y_predicted = predict(X_data)
    res = dataframe.drop(columns=["text"])
    res["score"] = Y_predicted
    return res

def score_df_to_db(dataframe,path="./SQL_DB/apprentissage.db"):
    if len(dataframe)>0:
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        query = "INSERT OR IGNORE INTO SCORE VALUES "
        for i in range(len(dataframe)):
            query += "("+str(dataframe["tweet_id"][i])+","+str(dataframe["score"][i])+"), "
        #print(query[:-2])
        cur.execute(query[:-2])
        conn.commit()
        conn.close()
        print("Done")
    else:
        print("Empty INSERT list")

#print(db_unscored_to_dataframe())