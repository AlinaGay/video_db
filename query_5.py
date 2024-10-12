import sqlite3

con = sqlite3.connect('db_video.sqlite')
cur = con.cursor()

results = cur.execute('''
  SELECT title,
       product_type,
       release_year
  FROM video_products
  WHERE (product_type = 'Фильм' OR product_type = 'Сериал')
                      AND release_year = 1993;
''')

for result in results:
    print(result)

con.close()
