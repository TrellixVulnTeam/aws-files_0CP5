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
	CREATE TABLE Student(
		student_id INT,
		name VARCHAR(100),
		age INT
		)
	"""
	query2="""
	CREATE TABLE Teacher(
		teacher_id INT,
		name VARCHAR(100),
		department VARCHAR(100),
		age INT
		)
	"""
	write_data(query)
	write_data(query2)
	
def insert_data():
	#student_data=[(101,"Prathap",21),(102,"Naveen",22),(103,"Daya",23)]
	#for data in student_data:
		#print(data[0],data[1],data[2])
	query="""
		INSERT INTO Student VALUES(101,"Prathap",21);
	"""
	write_data(query)
	query="""
		INSERT INTO Student VALUES(102,"Naveen",22);
	"""
	write_data(query)
	query2="""
		INSERT INTO Teacher VALUES(1,"Kesava","Mathematics",30);
		INSERT INTO Teacher VALUES(2,"Ramana","Hindi",40);
		INSERT INTO Teacher VALUES(3,"Bhaskar","English",38);
	"""
	
	#write_data(query2)
	
def get_info():
	
	query="""
	SELECT student_id,name,age FROM Student;
	"""
	query2="""
	SELECT teacher_id,name,department,age FROM Teacher;
	"""
	info1=read_data(query)
	#info2=read_data(query2)
	return info1
	#return info2
	