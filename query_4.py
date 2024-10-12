import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

results = cur.execute('''
  SELECT title,
         release_year
  FROM video_products
  WHERE (release_year BETWEEN 1965 AND 1990) AND product_type LIKE '%ильм';
''')

for result in results:
    print(result)

con.close()
