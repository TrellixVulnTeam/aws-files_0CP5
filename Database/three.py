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
    CREATE TABLE Student1 (
     sid INT PRIMARY KEY,
     name VARCHAR(16),
     login VARCHAR(32),
     age SMALLINT,
     gpa FLOAT
     );
     """
    write_data(query)
     
    query="""
    CREATE TABLE course (
    cid VARCHAR(32) PRIMARY KEY,
    name VARCHAR(32)
    );
    """
    write_data(query)
    
    query="""
    CREATE TABLE enrolled (
    sid INT FOREIGN KEY REFERENCES Student1 (sid),
    cid VARCHAR(32) FOREIGN KEY REFERENCES course (cid),
    grade CHAR(1)
     );
    """
    
   
    write_data(query)
    
def insert_data():
    student_data=[(1,"Prathap","@prathap",21,7.5),(2,"Naveen","@naveen",22,7.6),(3,"Daya","@daya",23,8.8)]
    for data in student_data:
        query="""INSERT INTO Student1 VALUES{}""".format(data)
        write_data(query)
    
    course_data=[(6502,"DBMS"),(8935,"OOPS"),(2341,"CNS"),(7613,"OS")]
    for data in course_data:
        query="""INSERT INTO course VALUES{}""".format(data)
        write_data(query)
        
    enrolled_data=[(2,6502,'A'),(1,7613,'B'),(3,8935,'C'),(1,2341,'A')]
    for data in enrolled_data:
        query="""INSERT INTO enrolled VALUES{}""".format(data)
        write_data(query)
        
def get_info():
	
	query="""
	SELECT avg(gpa),count(gpa) from student1 where login like '@p%';
	"""
	info1=read_data(query)
	for i in info1:
	    print(i)
	
'''def delete():
    
    query="""
    DROP TABLE Student1;
    """
    write_data(query)'''