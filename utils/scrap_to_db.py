import sqlite3
import pandas as pd

path = "../SQL_DB/tweet_SQL_database.db"

# remet au bon format la date twitter
def dateformat(date):
    month = {
        'Jun':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'
    }
    D = date.split()
    M = month[D[1]]
    Y = D[5]
    T = D[3]
    d = D[2]
    return Y + "-" + M + "-" + d + " " + T

def date_only(date):
    return date[:10]

# prend une liste de tweets ( liste de dictionnaires ) issue du scraping et les insert dans la database SQL
def to_db(liste_tweet,path="./SQL_DB/tweet_SQL_database.db"):
    #liste_tweet = [info]
    #info : dict
    #info["id"] = tweet._json["id"]
    #info["date"] = tweet._json["created_at"]
    #info["text"]
    if len(liste_tweet)>0:
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        query = "INSERT OR IGNORE INTO TWEET VALUES "
        cur.execute("SELECT COUNT(*) FROM TWEET")
        i = cur.fetchall()[0][0]
        for info in liste_tweet:
            tweet_text = info["text"].replace("'","''")
            i+=1
            date = info["date"]
            query += "("+str(i)+","+str(info["id"])+",'"+date+"',"+'"'+tweet_text+'"'+"), "
        print(query[:-2])
        cur.execute(query[:-2])
        conn.commit()
        conn.close()
        print("Done")
    else:
        print("Empty INSERT list")

# renvoie une dataframe contenant la note des tweets, leur id et la date
def db_to_dataframe(path="./SQL_DB/tweet_SQL_database.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.date, s.score from SCORE s JOIN TWEET t ON s.tweet_id = t.tweet_id", conn)
    res['date'] = res['date'].apply(date_only)
    conn.close()
    return res

# renvoie une dataframe contenant la note  sentiwordnet des tweets, leur id et la date
def db_to_dataframe_sentiwordnet(path="./SQL_DB/tweet_SQL_database.db"):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    res = pd.read_sql_query("SELECT t.tweet_id, t.date, s.score from SCORE s JOIN TWEET t ON s.tweet_id = t.tweet_id", conn)
    res['date'] = res['date'].apply(date_only)
    conn.close()
    return res


#I1 = {"id":101,"date":"2021-01-02 11:02:33","text":"Tweet test n1"}
#I2 = {"id":102,"date":"2019-02-02 03:56:11","text":"Tweet test n2"}
#L=[I1,I2]