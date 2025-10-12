#Transform a Nested Structure
from collections import defaultdict
def transform_a_nested_structure(students):
    result = defaultdict(int)
    for data in students:
        marks = data.get("marks", 0)
        if isinstance(marks, dict):
            for key, value in marks.items():
                result[key] += value /2
    return result



students = [
    {"name": "Alice", "marks": {"math": 90, "eng": 80}},
    {"name": "Bob", "marks": {"math": 85, "eng": 78}},
]


print(transform_a_nested_structure(students))