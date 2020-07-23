

Q1="""CREATE TABLE User (
	user_id INTEGER PRIMARY KEY,
	first_name VARCHAR(200) NOT NULL,
	last_name VARCHAR(200) NOT NULL,
	address VARCHAR(300),
	phone_number INTEGER NOT NULL );"""
#write_data(Q1)

Q2="""CREATE TABLE Post (
	user_id INT REFERENCES User(user_id) ON DELETE CASCADE,
	post_id INTEGER PRIMARY KEY AUTOINCREMENT,
	post_content VARCHAR(500) );"""
#write_data(Q2)

Q3="""INSERT INTO User VALUES(1,"tony","stark","new york",1234567890);"""
#write_data(Q3)

Q4="""INSERT INTO User VALUES(2,"john","wick","la",987654321);"""
#write_data(Q4)

Q5="""INSERT INTO Post (user_id,post_content) VALUES(1,"my first post");"""
#write_data(Q5)

Q6="""SELECT *FROM User;"""
#query=read_data(Q6)

#print(query)

Q7="""SELECT first_name,last_name FROM User;"""
#query=read_data(Q7)
#print(query)

Q8="""UPDATE User SET first_name="thor", last_name="ragnarok" where user_id=1;"""
#write_data(Q8)

Q9="""INSERT INTO Post(user_id,post_content) VALUES(2,"My Second Post");"""
#write_data(Q9)

Q10="""DELETE FROM User WHERE first_name='john' and last_name='wick';"""
#write_data(Q10)

Q11="""DROP TABLE Post;"""
#write_data(Q11)