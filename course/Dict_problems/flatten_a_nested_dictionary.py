#Flatten a Nested Dictionary

def flatten_a_nested_dictionary(data, parent_key= '', sep="."):
    result = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}"if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_a_nested_dictionary(value, key, sep=sep))
        else:
            result[new_key] = value
    return result

data =  {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}
print(flatten_a_nested_dictionary(data))