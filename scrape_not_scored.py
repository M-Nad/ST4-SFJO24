import sqlite3
import pandas as pd
import numpy as np

def db_to_dataframe(path="./SQL_DB/apprentissage.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.text from TWEET t LEFT JOIN SCORE s ON s.tweet_id = t.tweet_id WHERE s.tweet_id IS Null", conn)
    conn.close()
    return res.to_numpy()

#print(db_to_dataframe(path="./SQL_DB/apprentissage.db"))