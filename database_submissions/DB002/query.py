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
	
Q1="""SELECT * FROM Movie as m ORDER BY m.rank desc LIMIT 10;"""
#print(read_data(Q1))

Q2="""SELECT * FROM Movie as m ORDER BY m.rank desc LIMIT 10 OFFSET 10;"""
#print(read_data(Q2))

Q3="""SELECT name FROM Movie as m WHERE m.year > 2006;"""

Q4="""SELECT name FROM Movie as m WHERE m.rank < 1.1;"""

Q5="""SELECT * FROM Movie as m WHERE m.year BETWEEN 2005 AND 2007;"""

Q6="""SELECT name,year FROM Movie WHERE name LIKE '%Harry Potter%'"""
#print(read_data(Q6))


Q7="""SELECT *FROM Actor as a WHERE a.fname IS 'Christin' and a.lname IS NOT 'Watson';"""

Q8="""SELECT *FROM Actor as a WHERE a.fname IS 'Christin' and a.lname IS 'Watson';"""

Q9="""SELECT name FROM Movie as m WHERE m.year = 1990 and m.rank = 5;"""

Q10="""SELECT *FROM Actor as a WHERE a.fname IS 'Christin' or a.lname IS 'Watson';"""

Q11="""SELECT name FROM Movie as m WHERE m.year BETWEEN 2007 AND 2009;"""

Q12="""SELECT DISTINCT year FROM Movie as m ORDER BY m.year asc;"""

Q13="""SELECT * FROM Actor WHERE (fname IS 'Christin' OR lname IS 'Watson') AND gender IS 'M' order by fname asc limit 10;"""