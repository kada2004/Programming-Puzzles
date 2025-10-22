
list_of_int = [2, 3, 4, 10, 40]
value_to_find = 10

def binary_search(list_of_int, value_to_find):
    start = 0
    end = len(list_of_int) -1 

    while start <= end :
        print("start,end",start,end)
        middle = (start + end)//2
        middle_element = list_of_int[middle]

        if value_to_find == middle_element :
            return middle
        elif value_to_find >  middle_element :
            start = middle + 1

        else:
            end = middle - 1 


    return -1  # In case not found
output=binary_search(list_of_int, value_to_find)
print("output",output)
