#self.store_list=[]

class Item:
    
    def __init__(self,name,price,category):
        self.name=name
        if price > 0 :
            self.price=price
        else:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.category=category
        
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
        
    
class Query:
    
    def __init__(self,field,operation,value):
        self.field=field
        if operation == "random":
            raise ValueError("Invalid value for operation, got random")
        else:
            self.operation=operation
        self.value=value
        
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
    
        
class Store(Item,Query):
    
    
    
    def __init__(self,list1=""):
        #self.name=None
        #self.price=0
        #self.category=None
        if list1 == "":
            self.store_list=[]
        else:
            self.store_list=list1
        self.counter=0
        
        
        #self.field=None
        #self.operation=None
        #self.value=0
    
    def add_item(self,other):
        self.counter+=1
        self.store_list.append(other)
        #self.name=other.name
        #self.price=other.price
        #self.category=other.category
        
    
    def filter(self,other):
        
        filter_values=[]
        
        if other.operation == 'IN':
            for i in self.store_list:
                if other.field == 'category' and i.category in other.value:
                    filter_values.append(i)
                elif other.field == 'name' and i.name in other.value:
                    filter_values.append(i)
                elif other.field == 'price' and i.price in other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'EQ':
            for i in self.store_list:
                if other.field == 'name' and i.name == other.value:
                    filter_values.append(i)
                elif other.field == 'category' and i.category == other.value:
                    filter_values.append(i)
                elif other.field == 'price' and i.price == other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'GT':
            for i in self.store_list:
                if other.field == 'price' and i.price > other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'GTE':
            for i in self.store_list:
                if other.field == 'price' and i.price >= other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'LT':
            for i in self.store_list:
                if other.field == 'price' and i.price < other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'LTE':
            for i in self.store_list:
                if other.field == 'price' and i.price <= other.value:
                    filter_values.append(i)
            
        elif other.operation == 'STARTS_WITH':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and i.name.startswith(data):
                    filter_values.append(i)
                elif other.field == 'category' and i.category.startswith(data):
                    filter_values.append(i)
            
        elif other.operation == 'ENDS_WITH':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and i.name.endswith(data):
                    filter_values.append(i)
                elif other.field == 'category' and i.category.endswith(data):
                    filter_values.append(i)
                    
        elif other.operation == 'CONTAINS':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and data in i.name:
                    filter_values.append(i)
                elif other.field == 'category' and data in i.category:
                    filter_values.append(i)
        return Store(filter_values)
      
    """ def exclude(self,other):
        
        filter_values=[]
        
        if other.operation == 'IN':
            for i in self.store_list:
                if other.field == 'category' and i.category not in other.value:
                    filter_values.append(i)
                elif other.field == 'name' and i.name not in other.value:
                    filter_values.append(i)
                elif other.field == 'price' and i.price not in other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'EQ':
            for i in self.store_list:
                if other.field == 'name' and i.name != other.value:
                    filter_values.append(i)
                elif other.field == 'category' and i.category != other.value:
                    filter_values.append(i)
                elif other.field == 'price' and i.price != other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'GT':
            for i in self.store_list:
                if other.field == 'price' and i.price < other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'GTE':
            for i in self.store_list:
                if other.field == 'price' and i.price <= other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'LT':
            for i in self.store_list:
                if other.field == 'price' and i.price > other.value:
                    filter_values.append(i)
                    
        elif other.operation == 'LTE':
            for i in self.store_list:
                if other.field == 'price' and i.price >= other.value:
                    filter_values.append(i)
            
        elif other.operation == 'STARTS_WITH':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and i.name.endswith(data):
                    filter_values.append(i)
                elif other.field == 'category' and i.category.endswith(data):
                    filter_values.append(i)
            
        elif other.operation == 'ENDS_WITH':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and i.name.startswith(data):
                    filter_values.append(i)
                elif other.field == 'category' and i.category.startswith(data):
                    filter_values.append(i)
                    
        elif other.operation == 'CONTAINS':
            for i in self.store_list:
                data=other.value
                if other.field == 'name' and data not in i.name:
                    filter_values.append(i)
                elif other.field == 'category' and data not in i.category:
                    filter_values.append(i)
        return Store(filter_values)"""
    def exclude(self,query):
        filter_values=[]
        filter_values2=self.filter(query)
        #for i in filter_values2.store_list:
         #   print(i)
        for i in self.store_list:
            if i not in filter_values2.store_list:
                filter_values.append(i)
        return Store(filter_values)
         
    def __str__(self):
        if len(self.store_list) !=0:
            string=[str(item) for item in self.store_list]
            return '\n'.join(string)
        else:
            return "No items"
    
    def count(self):
        print(self.counter)
    
    