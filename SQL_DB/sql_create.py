import sqlite3

conn = sqlite3.connect("apprentissage.db",)

print("Opened database successfully");

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TWEET (
  tweet_id INT PRIMARY KEY,
  user_id VARCHAR(40) NOT NULL,
  date DATE,
  text TEXT
);
 """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS SCORE (
  tweet_id INT PRIMARY KEY,
  score INT NOT NULL
);
""")

print("Table created successfully");

conn.execute("SHOW DATABASES")

for x in conn:
  print(x)

conn.close()