class Item:

    def __init__(self, name, price, category):
        self._name = name
        if price > 0:
            self._price = price
        else:
            raise ValueError("Invalid value for price, got {}".format(price))
        self._category = category

    def __str__(self):
        return "{}@{}-{}".format(self._name, self._price, self._category)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def category(self):
        return self._category


class Query:

    def __init__(self, field, operation, value):
        self._field = field
        if operation not in ['IN', 'EQ', 'GT', 'GTE', 'LT', 'LTE',
                             'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']:
            raise ValueError("Invalid value for operation, got {}"
                             .format(operation))
        self._operation = operation
        self._value = value

    def __str__(self):
        return "{} {} {}".format(self._field, self._operation, self._value)

    @property
    def field(self):
        return self._field

    @property
    def operation(self):
        return self._operation

    @property
    def value(self):
        return self._value

def check_in_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value in query.value:
            items_list.append(item)
    return items_list

def check_eq_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value == query.value:
            items_list.append(item)
    return items_list

def check_gt_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value > query.value:
            items_list.append(item)
    return items_list

def check_gte_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value >= query.value:
            items_list.append(item)
    return items_list

def check_lt_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value < query.value:
            items_list.append(item)
    return items_list

def check_lte_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value <= query.value:
            items_list.append(item)
    return items_list

def check_starts_with_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value.startswith(query.value):
            items_list.append(item)
    return items_list

def check_ends_with_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if value.endswith(query.value):
            items_list.append(item)
    return items_list

def check_contains_operation(store_list, query):
    items_list = []
    for item in store_list:
        value = getattr(item, query.field)
        if query.value in value:
            items_list.append(item)
    return items_list


class Store:
    def __init__(self, store=""):
        if store == "":
            self.store_list = []
        else:
            self.store_list = store
    def add_item(self, item):
        self.store_list.append(item)
    def filter(self, query):
        store_obj = self.store_list

        if query.operation == 'IN':
            returned_item = check_in_operation(store_obj, query)

        elif query.operation == 'EQ':
            returned_item = check_eq_operation(store_obj, query)

        elif query.operation == 'GT':
            returned_item = check_gt_operation(store_obj, query)

        elif query.operation == 'GTE':
            returned_item = check_gte_operation(store_obj, query)

        elif query.operation == 'LT':
            returned_item = check_lt_operation(store_obj, query)

        elif query.operation == 'LTE':
            returned_item = check_lte_operation(store_obj, query)

        elif query.operation == 'STARTS_WITH':
            returned_item = check_starts_with_operation(store_obj, query)

        elif query.operation == 'ENDS_WITH':
            returned_item = check_ends_with_operation(store_obj, query)

        elif query.operation == 'CONTAINS':
            returned_item = check_contains_operation(store_obj, query)

        return Store(returned_item)

    def exclude(self, query):
        exclude_values = []
        filter_values = self.filter(query)
        for item in self.store_list:
            if item not in filter_values.store_list:
                exclude_values.append(item)
        return Store(exclude_values)

    def __str__(self):
        store_items_length = len(self.store_list)
        if store_items_length:
            string = [str(item) for item in self.store_list]
            items = '\n'.join(string)
        else:
            items = "No items"
        return items

    def count(self):
        counter = len(self.store_list)
        return counter
