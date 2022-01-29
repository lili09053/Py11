import sqlite3

conn = sqlite3.connect("films.sqlite")
cursor = conn.cursor()

# 19

#for row in cursor.execute("""SELECT title FROM films
#        WHERE genre=(
#            SELECT id FROM genres
#            WHERE title = 'детектив') AND year > 1994 AND year < 2001"""):
#    print(str(row).replace('(','').replace(')','').replace(',','').replace('\'',''))

# 20

#for row in cursor.execute("""SELECT title FROM films
#        WHERE title LIKE '%Астерикс%' AND title NOT LIKE '%Обеликс%'"""):
#    print(str(row).replace('(','').replace(')','').replace(',','').replace('\'',''))

# 22

#for row in cursor.execute("""SELECT DISTINCT title FROM genres
#        WHERE id IN(
#             SELECT genre FROM films
#             WHERE year BETWEEN 2010 AND 2011)"""):
#    print(str(row).replace('(','').replace(')','').replace(',','').replace('\'',''))

# 23

#for row in cursor.execute("""SELECT title FROM films
#        WHERE duration < 86"""):
#    print(str(row).replace('(','').replace(')','').replace(',','').replace('\'',''))