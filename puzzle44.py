
list_of_int= [5, 7, 8, 1, 2, 4, 99, 77, 56, 43, 12, 98,34,67,100]
def quicksort(list_of_int):
    low = 0
   #base case 
    if len(list_of_int) <= 1:
      return list_of_int
    right_list=[]
    left_list=[]
    if len(list_of_int) %2 == 0:
      middle_index=int(len(list_of_int)/2)
    elif len(list_of_int)%2 != 0:
      middle_index = int((len(list_of_int)+1)/2)

    middle_elem=list_of_int[middle_index]
    # print("middle_elem",middle_elem)
    #print("middle_index",middle_index)
    for x,y in enumerate(list_of_int):
        #print("x,y",x,y)
        if y < middle_elem:
          left_list.append(y)
        elif y > middle_elem :
           right_list.append(y)

    #print("left_list,right_list",left_list,right_list)
        
    quicksort_left=quicksort(left_list)
    quicksort_right=quicksort(right_list)
    #print("quicksort_left,quicksort_right",quicksort_left,quicksort_right)

    return quicksort_left + [middle_elem] + quicksort_right

def quicksort_main(list_of_int):
   
   return quicksort(list_of_int)

print(quicksort_main(list_of_int))