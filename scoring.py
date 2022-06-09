import sqlite3
import pandas as pd
import numpy as np
from tree_classifier import predict

# renvoie une dataframe pandas depuis la base de données qui comporte les tweets pas encore notés
def db_unscored_to_dataframe(path="./SQL_DB/tweet_SQL_database.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.text from TWEET t LEFT JOIN SCORE s ON s.tweet_id = t.tweet_id WHERE s.tweet_id IS Null", conn)
    conn.close()
    return res

# applique le classifier au tweets
def dataframe_to_score_df(dataframe):
    X_data = dataframe["text"].to_list()
    Y_predicted = predict(X_data)
    res = dataframe.drop(columns=["text"])
    res["score"] = Y_predicted
    return res

# implémente les scores dans la database SQL
def score_df_to_db(dataframe,path="./SQL_DB/tweet_SQL_database.db"):
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

# effectue directement la notation des tweets non notés dans la database SQL 
def score_database(path="./SQL_DB/tweet_SQL_database.db"):
    df = db_unscored_to_dataframe(path)
    score_df = dataframe_to_score_df(df)
    score_df_to_db(score_df,path)