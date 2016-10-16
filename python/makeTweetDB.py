import csv
import sqlite3

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS tweets""")
cur.execute("""CREATE TABLE tweets
            (lat text, long text, party text, tweet_time timestamp)""")

conn.commit()
conn.close()
