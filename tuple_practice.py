"""Problem: Write a function that accepts a list of tuples where each tuple contains a name and age. 
    Return a list of names of people older than 30.
"""

def filter_by_age(people):
    output = [name for name,age in people if age >30]
    return output


people = [("Alice", 25), ("Bob", 35), ("Charlie", 40)]
print(filter_by_age(people))  # Output: ["Bob", "Charlie"]

#-----------------------------------------------------------------------------------------------------------------

"""
    Given a tuple, write a function to swap the first and last elements.
"""
# input = (1, 2, 3, 4)
# Output: (4, 2, 3, 1)

def swap_first_last(input_tuple):
    if len(input_tuple) <= 2:
        return input_tuple
    
    return (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)

print(swap_first_last((1, 2, 3, 4)))  

