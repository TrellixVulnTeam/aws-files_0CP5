
class ObjectDoesNotExists(Exception):
    pass

def get_count_field_from_object(database_handler, object_id):

    try:
        obj = database_handler.get(id=object_id)

    except Exception:
        raise ObjectDoesNotExists

    return obj.count


class MyClass:
    def __init__(self, name, age):
        import uuid
        self.id = uuid.uuid4()
        self.name = name
        self.age = age 


import time
def get_epoch_time_stamp_as_str():
    return str(time.time())

class TimeOut(Exception):
    pass

def get_stock_price(company_id):
    import requests
    import json
    #from requests.exceptions import TimeOut 
    try:
        response = requests.get(" http://www.mocky.io/v2/5eb664e831000057006999f3")
    except TimeOut:
        raise Exception('Request timedout')
    result = json.loads(response.content)
 
    return result['unit_price_in_inr']



