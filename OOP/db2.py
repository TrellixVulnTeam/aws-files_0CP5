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

	Q1=""" CREATE TABLE User (
		user_id INT PRIMARY KEY,
		first_name VARCHAR(200),
		last_name VARCHAR(200),
		address VARCHAR(300),
		phone_number INT NOT NULL
	);
	"""
	write_data(Q1)

	Q2=""" CREATE TABLE Post (
		user_id INT REFERENCES User(user_id),
		post_id INT UNIQUE,
		post_content VARCHAR(500)
	);
	"""
	write_data(Q2)

def insert_data():

	Q3="""INSERT INTO User VALUES(1,"tony","stark","new york",1234567890);"""
	write_data(Q3)
	
	Q4="""INSERT INTO User VALUES(2,"john","wick","la",987654321);"""
	write_data(Q4)
	
	Q5="""INSERT INTO Post VALUES(1,1,"my first post");"""
	write_data(Q5)
	
	Q9="""INSERT INTO Post VALUES(2,2,"My Second Post");"""
	write_data(Q9)

def get_info():

	Q6="""SELECT *FROM User;"""
	query=read_data(Q6)
	
	print(query)
	
	
	Q6="""SELECT *FROM Post;"""
	query=read_data(Q6)
	
	print(query)
	
	Q7="""SELECT first_name,last_name FROM User;"""
	query=read_data(Q7)
	print(query)
	
	Q7="""SELECT user_id,post_id FROM Post;"""
	query=read_data(Q7)
	print(query)

def update():

	Q8="""UPDATE User SET first_name="thor", last_name="ragnarok" where user_id=1;"""
	write_data(Q8)
	
	Q6="""SELECT *FROM User;"""
	query=read_data(Q6)
	
	print(query)

def delete_row():

	Q10="""DELETE FROM User as u WHERE u.user_id=1;"""
	write_data(Q10)

def delete_table():

	Q11="""DROP TABLE Post;"""
	write_data(Q11)