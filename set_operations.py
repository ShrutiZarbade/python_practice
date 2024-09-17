""" 
    Problem: Write a function that accepts two lists and returns the list of 
    common elements (without duplicates) using set operations.
"""

def common_elements(list_1,list_2):
    return list(set(list_1) & set(list_2))
print(common_elements([1, 2, 2, 3], [2, 3, 4]))  # Output: [2, 3]

#------------------------------------------------------------------------------------------------

""" Problem: Write a function to find the union and intersection of two sets. """

# Output: ({1, 2, 3, 4}, {2, 3})
def union_and_intersection(set1,set2):
    union = set1 | set2
    intersection = set1 & set2
    return union,intersection

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(union_and_intersection(set1, set2))  

#-----------------------------------------------------------------------------------------------

# Summary 
# Union OR operater  "|" 
# Intersection AND operator  "&"
