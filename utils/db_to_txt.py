import pandas as pd
import sqlite3

def db_unscored_sentiwordnet_to_dataframe(path="./SQL_DB/tweet_SQL_database.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.text from TWEET t LEFT JOIN SCORE_SENTIWORDNET s ON s.tweet_id = t.tweet_id WHERE s.tweet_id IS Null", conn)
    conn.close()
    return res