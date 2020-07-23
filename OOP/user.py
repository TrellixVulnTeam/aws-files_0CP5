


Store

Let’s say, you have built a store that is filled with different grocery items. You have observed that customers are facing difficulty to find an item. So you have decided to write a program that would make it easy for users to search for items.

AssignmentID -OOP005

Submission Guidelines

Create a folder /home/ec2-user/environment/oop_submissions/{AssignmentID}. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop_submissions/OOP005/
Copy your code file to the submission folder. Make use of the below example command
$ cp store.py /home/ec2-user/environment/oop_submissions/OOP004
Coding Guidelines:

Write all your code in store.py file
Make use of classes built in Assignment 4 and complete the below tasks:

Or

Now that you have built a Store class. Update it so that it should be able to add results of two search Query results.

>>> store = Store()
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")
>>> store.add_item(item)
>>> item = Item(name="Boost Biscuits", price=20, category="Food")
>>> store.add_item(item)
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")
>>> store.add_item(item)
>>> print(store)
Oreo Biscuits@30-Food
Boost Biscuits@20-Food
ParleG Biscuits@10-Food
>>> query = Query(field="price", operation="GT", value=15)
>>> results = store.filter(query)
>>> print(results)
Oreo Biscuits@30-Food
Boost Biscuits@20-Food

>>> results = store.exclude(query) + store.filter(query) # OR Operation
>>> print(results)
Oreo Biscuits@30-Food
Boost Biscuits@20-Food
ParleG Biscuits@10-Food
And

Update Store class so that users should be able to give more than one query to filter or exclude methods. (Do and operation in case of more than one Query object)

>>> store = Store()
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")
>>> store.add_item(item)
>>> item = Item(name="Boost Biscuits", price=20, category="Food")
>>> store.add_item(item)
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")
>>> store.add_item(item)
>>> print(store)
Oreo Biscuits@30-Food
Boost Biscuits@20-Food
ParleG Biscuits@10-Food
>>> query = Query(field="price", operation="GT", value=15)
>>> query = Query(field="name", operation="CONTAINS", value="oo")

>>> results = store.filter(query, query) # should be able to give any number of Query objects as arguments
>>> print(results)
Boost Biscuits@20-Food


>>> results = store.exclude(query, query) # should be able to give any number of Query objects as arguments
>>> print(results)
Oreo Biscuits@30-Food
ParleG Biscuits@10-Food
Back








"""class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        type(self).counter += 1
    def get_counter(self):
        print(User.counter)"""
        
#user_object=User("New User")
#user_object.get_counter()
        
        
"""from user import User
>>> user_object = User("New User")
>>> user_object.get_counter()"""