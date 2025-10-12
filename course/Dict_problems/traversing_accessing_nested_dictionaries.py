def get_nested_value(data, keys):
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data    

data = {
    "user": {
        "profile": {
            "name": "Alice",
            "address": {"city": "New York", "zip": 10001}
        }
    }
}
keys= ["user","profile","address","city"]
print(get_nested_value(data, keys))
