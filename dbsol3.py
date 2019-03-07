#!/usr/bin/env python 
import psycopg2

DBNAME = "news"
def get_posts():
	db = psycopg2.connect(database = DBNAME)
	c = db.cursor()
	c.execute("create view st as select date(time) as date1, count(status) as stat from log group by date(time)")
	c.execute("create view status404 as select date(time) as date1 , status as st from log where status like '4%'")
	c.execute("create view st2 as select date1 , count(st) as notf from status404 group by date1")
	c.execute("create view st5 as select st2.date1 as finaldate ,cast(notf as float) , cast(stat as float) from st join st2 on st.date1 = st2.date1")
	c.execute("select finaldate , (notf*100)/stat from st5 where (notf*100)/stat > 1")
	file = c.fetchall()
  	db.close()
  	return file