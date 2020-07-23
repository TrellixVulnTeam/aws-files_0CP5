def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
def create_table():
	query="""
	CREATE TABLE R(
		a_id VARCHAR(30),
		b_id INT
		)
	"""
	write_data(query)
	query="""
	CREATE TABLE S(
		a_id VARCHAR(30),
		b_id INT
		)
	"""
	write_data(query)
	
def insert_data():
	
	query="""INSERT INTO R VALUES("a1",101),("a2",102),("a3",103);"""
	write_data(query)
	query="""INSERT INTO S VALUES("a3",103),("a4",104),("a5",105);"""
	write_data(query)
	
	
def get_info():
	# select distinct name from Student1;
	#SELECT name,age from Student1 as s where s.age > 21;
	#SELECT *from Student1 as s where s.age > 21 and s.student_id > 102;
	#SELECT *from Student1 as s where s.age > 21 or s.student_id > 102;
	#SELECT *from Student1 as s where NOT s.age > 22;
	#SELECT *from Student1 as s where  s.age > 21 and (s.student_id >103 or s.age <23);
	
	query="""
	SELECT max(b_id), min(b_id) from S;
	"""
	
	info1=read_data(query)
	#return info1
	for i in info1:
		print(i)
	