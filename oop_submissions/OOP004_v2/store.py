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
        if operation not in ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        else:
            self.operation=operation
        self.value=value
        
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
    
        
class Store(Item,Query):
    
    def __init__(self,store=""):
    
        if store == "":
            self.store_list=[]
        else:
            self.store_list=store
            
        self.counter=0
        
    def add_item(self,item):
        self.counter=0
        self.store_list.append(item)
        for i in self.store_list:
            self.counter+=1
    def filter(self,query):
        
        filter_values=[]
        
        if query.operation == 'IN':
            for i in self.store_list:
                if query.field == 'category' and i.category in query.value:
                    filter_values.append(i)
                elif query.field == 'name' and i.name in query.value:
                    filter_values.append(i)
                elif query.field == 'price' and i.price in query.value:
                    filter_values.append(i)
                    
        elif query.operation == 'EQ':
            for i in self.store_list:
                if query.field == 'name' and i.name == query.value:
                    filter_values.append(i)
                elif query.field == 'category' and i.category == query.value:
                    filter_values.append(i)
                elif query.field == 'price' and i.price == query.value:
                    filter_values.append(i)
                    
        elif query.operation == 'GT':
            for i in self.store_list:
                if query.field == 'price' and i.price > query.value:
                    filter_values.append(i)
                    
        elif query.operation == 'GTE':
            for i in self.store_list:
                if query.field == 'price' and i.price >= query.value:
                    filter_values.append(i)
                    
        elif query.operation == 'LT':
            for i in self.store_list:
                if query.field == 'price' and i.price < query.value:
                    filter_values.append(i)
                    
        elif query.operation == 'LTE':
            for i in self.store_list:
                if query.field == 'price' and i.price <= query.value:
                    filter_values.append(i)
            
        elif query.operation == 'STARTS_WITH':
            for i in self.store_list:
                data=query.value
                if query.field == 'name' and i.name.startswith(data):
                    filter_values.append(i)
                elif query.field == 'category' and i.category.startswith(data):
                    filter_values.append(i)
            
        elif query.operation == 'ENDS_WITH':
            for i in self.store_list:
                data=query.value
                if query.field == 'name' and i.name.endswith(data):
                    filter_values.append(i)
                elif query.field == 'category' and i.category.endswith(data):
                    filter_values.append(i)
                    
        elif query.operation == 'CONTAINS':
            for i in self.store_list:
                data=query.value
                if query.field == 'name' and data in i.name:
                    filter_values.append(i)
                elif query.field == 'category' and data in i.category:
                    filter_values.append(i)
                    
        return Store(filter_values)
        
    def exclude(self,query):
        
        exclude_values=[]
        
        filter_values2=self.filter(query)
        
        for i in self.store_list:
            if i not in filter_values2.store_list:
                exclude_values.append(i)
                
        return Store(exclude_values)
        
    def __str__(self):
        if len(self.store_list) !=0:
            string=[str(item) for item in self.store_list]
            return '\n'.join(string)
        else:
            return "No items"
            
    def count(self):
        return self.counter
    