#from collections import Counter, defaultdict
#dict1 = {"a": 2, "b": 3, "c": 1}
#dict2 = {"b": 4, "c": 5, "d": 7}
#result = defaultdict(int)

#for d in [dict1, dict2]:
#    for k, v in d.items():
#        result[k] += v

#print(result)
#===========================================
#Group and Sum by a Specific Key
#from collections import defaultdict
#data = [{'id':1, 'score':5}, {'id':2, 'score':4}, {'id':1, 'score':7}]
#result = {}
#for item in data:
#    key = item['id']
#    result[key] = result.get(key, 0) + item['score']
#print(result)
#===========================================
#Find the Sum of All Dictionary Values
#d = {'a': 10, 'b': 20, 'c': 30}
#print(sum(d.values()))
#===========================================
#Remove Keys with Duplicate Values
#d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
#values = list(d.values())
#duplicate = set(x for x in values if values.count(x) > 1)
#result = {k: v for k, v in d.items() if v not in duplicate}
#print(result)



