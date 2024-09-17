""" Problem: Write a function that merges two dictionaries, summing the values of common keys. """

def merge_dicts(dict1,dict2):
    for key,value in dict2.items():
        dict1[key] = dict1.get(key,0) + value
    return dict1
        
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))  

#------------------------------------------------------------------------------------------------

""" Problem: Write a function to sort a dictionary by its values. """

def sort_by_value(d):
    return  dict(sorted(d.items(),key= lambda item:item[1]))
d = {'apple': 3, 'banana': 1, 'cherry': 2}
print(sort_by_value(d))  
# Output: {'banana': 1, 'cherry': 2, 'apple': 3}

#------------------------------------------------------------------------------------------------

""" Problem: Given a list of dictionaries where each dictionary represents a student (with name and score), 
write a function to return the name of the student with the highest score."""

def top_student(students):
    return max(students,key=lambda student:student["score"])["name"]
students = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}, {'name': 'Charlie', 'score': 87}]
print(top_student(students))  # Output: 'Bob'


