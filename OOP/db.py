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
    query1="""
    CREATE TABLE Student1 (
     sid INT PRIMARY KEY,
     name VARCHAR(16),
     login VARCHAR(32),
     age SMALLINT,
     gpa FLOAT
     );
     """
     
    query2="""
    CREATE TABLE course (
    cid VARCHAR(32) PRIMARY KEY,
    name VARCHAR(32)
    );
    """
    
    query3="""
    CREATE TABLE enrolled (
    sid INT REFERENCES Student1 (sid),
    cid VARCHAR(32) REFERENCES course (cid),
    grade CHAR(1)
     );
    """
    write_data(query1)
    write_data(query2)
    write_data(query3)
    
def insert_data():
    student_data=[(1,"Prathap","@prathap",21,7.5),(2,"Naveen","@naveen",22,7.6),(3,"Daya","@daya",23,8.8)]
    for data in student_data:
        query1="""
    		INSERT INTO Student1 VALUES{}""".format(data)
        write_data(query1)
    
    course_data=[(6502,"DBMS"),(8935,"OOPS"),(2341,"CNS"),(7613,"OS")]
    for data in course_data:
        query2="""
	        INSERT INTO course VALUES{}""".format(data)
        write_data(query2)
        
    enrolled_data=[(2,6502,'A'),(1,7613,'B'),(3,8935,'C'),(1,2241,'A')]
    for data in enrolled_data:
        query3="""
            INSERT INTO enrolled VALUES{}""".format(data)
        write_data(query3)
def get_info():
	
	query="""
	SELECT sid,name,login,age,gpa FROM Student1;
	"""
	
	info1=read_data(query)
	return info1
	
'''def delete():
    
    query="""
    DROP TABLE student;
    """
    write_data(query)'''