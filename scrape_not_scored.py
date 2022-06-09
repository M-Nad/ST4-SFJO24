import sqlite3
import pandas as pd
import numpy as np

#récupère les tweets non scorés de la database apprentissage.db
def db_to_dataframe(path="./SQL_DB/tweet_SQL_database.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.text from TWEET t LEFT JOIN SCORE s ON s.tweet_id = t.tweet_id WHERE s.tweet_id IS Null", conn)
    conn.close()
    return res.to_numpy()

#print(db_to_dataframe(path="./SQL_DB/apprentissage.db"))