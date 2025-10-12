#Searching in Nested Structures
def searching_in_nested_structures(data, value):
    for item in data:
        if item.get('info', 0).get("name") == value:
            return item['id']
    return None 

data = [
    {"id": 1, "info": {"name": "Alice"}},
    {"id": 2, "info": {"name": "Bob"}},
]
value = "Bob"
print(searching_in_nested_structures(data, value))