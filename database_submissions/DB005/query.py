
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



Q1="""SELECT COUNT(*) FROM Movie WHERE year < 1980;"""

Q2="""SELECT AVG(rank) FROM Movie WHERE year = 1991;"""

Q3="""SELECT MIN(rank) FROM Movie WHERE year = 1991;"""

Q4="""SELECT a.fname,a.lname FROM Actor as a, Cast as c WHERE a.id=c.pid  and c.mid IS 1002;"""

Q5="""SELECT COUNT(c.mid) FROM Cast as c, Actor as a where a.id = c.pid and a.fname='Orlando' and a.lname='Galindo';"""

#Q5="""SELECT COUNT(c.mid) FROM Cast as c WHERE pid IN (SELECT id FROM Actor WHERE fname='Orlando' and lname='Galindo');"""

Q6="""SELECT m.name FROM Movie as m WHERE m.name LIKE 'Harry Potter%' AND m.year BETWEEN 2006 AND 2008;"""

Q7="""SELECT DISTINCT fname,lname FROM Director WHERE id IN (SELECT did FROM MovieDirector WHERE mid IN (SELECT id FROM Movie WHERE name LIKE 'Harry Potter%'));"""

Q8="""SELECT name FROM Movie WHERE id IN (SELECT c.mid FROM Cast as c,MovieDirector as md,Actor as a WHERE a.id = c.pid AND a.id = md.did and a.fname='Jackie (I)' and a.lname='Chan');"""

Q9="""SELECT d.fname,d.lname FROM Director as d,MovieDirector as md,Movie as m WHERE d.id=md.did and md.mid=m.id and m.year=2001 GROUP BY md.did HAVING COUNT(md.mid)>=4 ORDER BY d.fname asc,d.lname desc;"""

Q10="""SELECT * FROM Actor WHERE id  NOT IN (SELECT c.pid FROM Cast as c, Movie as m WHERE c.mid = m.id AND m.year BETWEEN 1990 AND 2000)ORDER BY id desc LIMIT 100;"""

Q11="""SELECT gender, COUNT(gender)*100.0/(SELECT COUNT(*) FROM Actor)
  from Actor GROUP BY gender ORDER BY gender desc;""" 

Q12="""SELECT a.name,b.name,a.rank,a.year FROM Movie as a CROSS JOIN Movie as b ON a.year=b.year AND a.rank=b.rank AND a.id < b.id ORDER BY a.name asc LIMIT 100;"""

Q13="""SELECT ac.fname,m.year,avg(m.rank) FROM (Actor as a INNER JOIN Cast as c ON a.id = c.pid) as ac INNER JOIN Movie as m ON m.id = ac.mid GROUP BY ac.pid,m.year ORDER BY ac.fname asc,m.year desc limit 100;"""

Q14="""SELECT d.fname,
			m.name
			FROM Movie AS m 
	    		INNER JOIN MovieDirector AS md 
				ON m.id = md.mid
				INNER JOIN Director AS d ON d.id = md.did
				GROUP BY md.did
				HAVING m.id = MAX(m.id)
				ORDER BY m.name asc
				LIMIT 100;"""

Q15="""SELECT COUNT(m.id)
		FROM Director AS d
		INNER JOIN MovieDirector AS md
		ON d.id = md.did
		INNER JOIN Movie AS m
		ON m.id=md.mid
		WHERE m.year < 2005
		GROUP BY d.id"""
 
Q16=""" """


