def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("imdb.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("imdb.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

Q1="""select a.fname,a.lname from Actor as a, Cast as c where a.id = c.pid and c.mid=1000;"""
#data=read_data(Q1)
#print(data)
Q2="""select count(c.mid) from Cast as c, Actor as a where a.id = c.pid and (a.fname is 'Harrison (I)' and a.lname is 'Ford');"""
#print(read_data(Q2))
Q3="""select distinct(c.pid) from Cast as c,movie as m where m.id = c.mid and m.name like '%Harry Potter%';"""
#print(read_data(Q3))
Q4="""select count(distinct c.pid) from Cast as c, Movie as m where c.mid = m.id and m.year between 1990 and 2000;"""
#print(read_data(Q4))
#Q5="""select year,count(*) from Movie group by year;"""
#print(read_data(Q5))
#Q5="""select fname from Actor where id in (select pid from Cast where mid in (select id from Movie where year between 1990 and 2000));"""
#print(read_data(Q5))
