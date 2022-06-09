import sqlite3

conn = sqlite3.connect("./tweet_SQL_database.db")

print("Opened database successfully");

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TWEET (
  tweet_id INT PRIMARY KEY,
  user_id VARCHAR(40) NOT NULL,
  date DATETIME,
  text TEXT, 
  CONSTRAINT U_userID_date UNIQUE (user_id,date)
);
 """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS SCORE (
  tweet_id INT PRIMARY KEY,
  score INT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SCORE_SENTIWORDNET (
  tweet_id INT PRIMARY KEY,
  score_sentiwordnet INT NOT NULL
);
""")

print("Table created successfully");

conn.close()