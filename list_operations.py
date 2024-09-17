""" Problem: Write a function to flatten a list of lists into a single list. """

def flatten_list(data):
    output = []
    for list_ in data:
        if isinstance(list_,list):
            output.extend(flatten_list(list_))
        else:
            output.append(list_)
    return output
    # [ls_dt for list_ in data for ls_dt in list_]

nested_list = [[1, 2], [3, [4, 5]], 6]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6]

#----------------------------------------------------------------------------------
""" Problem: Write a function that removes duplicates from a list while preserving the order of elements. """

def remove_duplicates(dup_list):
    output = []
    for i in dup_list:
        if i not in output:
            output.append(i)
    return output

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#-------------------------------------------------------------------------------------------------------------------
