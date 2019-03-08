#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def get_posts():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view nam as select title,\
        concat('/article/',slug) as slu from articles")
    c.execute("create view name as select path,count(*)\
        as n from log Join nam on nam.slu like log.path \
        group by path order by n desc limit 3")
    c.execute("select title,n from name Join nam on \
        nam.slu like name.path order by n desc")
    file = c.fetchall()
    db.close()
    return file
