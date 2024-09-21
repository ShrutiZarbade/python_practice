# Bubble sort for sorting a list 

def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j],input_list[j+1] = input_list[j+1],input_list[j]

    return input_list

input_list = [32,67,12,9,0,3,4]
output = bubble_sort(input_list)
print(output)