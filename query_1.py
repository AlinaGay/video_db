import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

results = cur.execute('''
  SELECT *
  FROM video_products;
''')

for result in results:
    print(result)

con.close()
