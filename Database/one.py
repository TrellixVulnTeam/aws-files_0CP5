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
	CREATE TABLE student1(
		student_id INT,
		name VARCHAR(100),
		age INT
		)
	"""
	write_data(query)
	
def insert_data():
	
	#query="""INSERT INTO student1 VALUES(101,"Prathap",21),(102,"Naveen",22),(103,"Daya",23),(104,"Naresh",21),(105,"Hari",22),(106,"Krishna",21);"""
	#write_data(query)
	pass
	
def get_info():
	# select distinct name from Student1;
	#SELECT name,age from Student1 as s where s.age > 21;
	#SELECT *from Student1 as s where s.age > 21 and s.student_id > 102;
	#SELECT *from Student1 as s where s.age > 21 or s.student_id > 102;
	#SELECT *from Student1 as s where NOT s.age > 22;
	#SELECT *from Student1 as s where  s.age > 21 and (s.student_id >103 or s.age <23);
	
	query="""
	SELECT count(*) from Student1 ;
	"""
	
	info1=read_data(query)
	for i in info1:
		print(i)
	