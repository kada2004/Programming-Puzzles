

inputs_nums=[1,2,3,4,5,0,798]
reverse_list=[]
def reverse_elements(inputs_nums):
    for x,y in enumerate(inputs_nums):

        reverse_list.append(y)
    
    reverse_list.reverse()
    return reverse_list

output=reverse_elements(inputs_nums)
print("output",output)