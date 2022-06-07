import sqlite3

conn = sqlite3.connect("./apprentissage.db")

print("Opened database successfully");

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TWEET (
  tweet_id INT PRIMARY KEY,
  user_id VARCHAR(40) NOT NULL,
  date TEXT,
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

print("Table created successfully");

conn.close()