# 1. Problem: Chunk a List
"""
    Without using itertools.chunked (or other helper libraries), 
    write a function to chunk a given list into sublists of a specified size.
"""
def chunk_list(list_, chunk_size):
    chunks = [list_[dt:dt+chunk_size] for dt in range(0,len(list_),chunk_size) ]
    # print (chunks)
    return chunks

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))  
# Output: [[1, 2, 3], [4, 5, 6], [7]]
#------------------------------------------------------------------------------------------------

# 2. Problem: Cartesian Product
""" Write a function to compute the Cartesian product of two lists without using itertools.product. """

def cartesian_product(list1, list2):
    return [(a,b) for a in list1 for b in list2]
list1 = [1, 2]
list2 = ['a', 'b']
print(cartesian_product(list1, list2))  
# # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
#--------------------------------------------------------------------------------------------------------

# 3. Problem: Grouping Elements by Frequency
dict_ = {}
def group_by_frequency(lst):
    for i in lst:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    return dict_

lst = [1, 2, 2, 3, 3, 3, 4]
print(group_by_frequency(lst))  
# Output: {1: 1, 2: 2, 3: 3, 4: 1}

#-----------------------------------------------------------------------------------
# 9. Problem: Rotate a List

"""Write a function to rotate a list by n positions without using any third-party libraries."""

def rotate_list(lst,num):
    num= num% len(lst)
    print(num)
    return lst[num:] + lst[:num]
lst = [1, 2, 3, 4, 5]
print(rotate_list(lst, 2))  
# Output: [3, 4, 5, 1, 2]

#--------------------------------------------------------------------------------
# 13. Problem: Calculate Factorial

def factorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))  
# Output: 120

#----------------------------------------------------------------------------------