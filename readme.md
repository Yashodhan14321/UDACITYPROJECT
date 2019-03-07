THE FIRST PROJECT
****************
REQUIREMENTS
1.)vagrant 
	you can download vagrant here https://www.vagrantup.com/downloads.html
	install it then go to vagrant directory
	then run vagrant up to download virtual machine make sure your have oracle virtualbox
2.) oracle virtualbox
3.) newsdata.sql file
********THE QUESTIONS WERE********
The file newsdata.sql contains all the database download it from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
now for viewing it go to vagrant directory in gitbash
run vagrant up the run vagrant ssh
now run command 
psql -d news -f newsdata.sql
this will create and connect you to database named news
now use \dt command to view all schemas name
for getting some info about particular table as the news database conatins 3 tables named as articles , authors, log
now for getting some info about tables use \d (tablename)
example \d authors
**********************************
1) What are the most popular three articles?
 The answer for this question is stored in sol1.py and its database file is dbsol1.py
 the sol1 is running on port 8080
 to run this we should have to go in vagrant directory using git then run vagrant up and vagrant ssh
 then type cd /vagrant for moving in vagrant directory 
 then we have to go to solution directory where all the files like sol1 , dbsol1 are kept then run
 python sol1.py
 the command will rull the file on port 8080
 then go to chrome or anyother browser and search for localhost:8080 this will provide you the solution of first question

 Working 
 c.execute("create view nam as select title , concat('/article/',slug) as slu from articles") #this will create view that contain article name and their path
 c.execute("create view name as select path  , count(*) as n from log Join nam on nam.slu like log.path group by path order by n desc limit 3") #this will create a view that contain path and number of visitors of that particular path
 and at last we had displayed the title of the articles and number of views per article 
***********************************
2) Who are the most popular authors?
 The answer for this question is stored in sol2.py and its database file is dbsol2.py
 the sol1 is running on port 8000
 to run this we should have to go in vagrant directory using git then run vagrant up and vagrant ssh
 then type cd /vagrant for moving in vagrant directory 
 then we have to go to solution directory where all the files like sol2 , dbsol2 are kept then run
 python sol2.py
 the command will rull the file on port 8000
 then go to chrome or anyother browser and search for localhost:8000 this will provide you the solution of first question

 Working 
c.execute("create view name1 as select author , n from name Join nam on nam.slu like name.path order by n desc") #the query will store author name and views per article in this view
 and at last we had displayed the name of the author and number of views per author 
***********************************
3) Print the errors per date if greater than 1%?
 The answer for this question is stored in sol3.py and its database file is dbsol3.py
 the sol1 is running on port 8080
 to run this we should have to go in vagrant directory using git then run vagrant up and vagrant ssh
 then type cd /vagrant for moving in vagrant directory 
 then we have to go to solution directory where all the files like sol3 , dbsol3 are kept then run
 python sol2.py
 the command will rull the file on port 8080
 then go to chrome or anyother browser and search for localhost:8080 this will provide you the solution of first question

 Working 
 c.execute("create view st as select date(time) as date1, count(status) as stat from log group by date(time)")
 c.execute("create view status404 as select date(time) as date1 , status as st from log where status like '4%'")
 c.execute("create view st2 as select date1 , count(st) as notf from status404 group by date1")
 c.execute("create view st5 as select st2.date1 as finaldate ,cast(notf as float) , cast(stat as float) from st join st2 on st.date1 = st2.date1")

 and at last we had displayed the date and % of error per date if greater than 1 

