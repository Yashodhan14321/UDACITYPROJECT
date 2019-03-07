#!/usr/bin/env python
import psycopg2

DBNAME = "news"
def get_posts():
	db = psycopg2.connect(database = DBNAME)
	c = db.cursor()
	c.execute(" create view nam as select  author , concat('/article/',slug) as slu from articles")
	c.execute("create view name as select path  , count(*) as n from log Join nam on nam.slu like log.path group by path order by n desc")
	c.execute("create view name1 as select author , n from name Join nam on nam.slu like name.path order by n desc")
	c.execute("select name , sum(n) from name1 join authors on authors.id = name1.author group by name order by sum desc")
	file = c.fetchall()
  	db.close()
  	return file