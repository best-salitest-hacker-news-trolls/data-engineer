import sqlite3
import pandas as pd
from pandas import DataFrame
import json
from .models import UserModel, CommentModel, ScoreModel
sqlite3.connect('buildweek3.db')


conn = sqlite3.connect('buildweek3.db')
c = conn.cursor()


# Create Table - Leaderboard
c.execute('''CREATE TABLE LEADERBOARD
             ([generated_id] INTEGER PRIMARY KEY,[USER] text, 
             [COMMENT] text, [SCORE] integer)''')

conn.commit()

# Import the data using Pandas

url = 'https://raw.githubusercontent.com/best-salitest-hacker-news-trolls/machine-learning-engineers/master/10000_predictions_extra.json'
df = pd.read_json(url, orient='columns')
df.to_sql('LEADERBOARD', conn, if_exists='append', index = False)

c.execute(''' 
INSERT INTO LEADERBOARD (ID, USER, COMMENT, SCORE)
''')

c.execute('''
SELECT id, user, comment, score FROM leaderboard
WHERE author = 'pg'
ORDER BY score ASC
''')

print(c.fetchall)

df = DataFrame(c.fetchall(), columns = ['User', 'Comment', 'Score'])

print(df)

df.to_sql('LEADERBOARD', conn, if_exists='append', index = False)

conn.commit()


