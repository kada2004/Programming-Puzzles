

input_nums=[1,2,3,4,5,6,7,8,9,10]

def reverse_five_positions(input_nums):

    slicing_part_1=input_nums[0:5]
    slicing_part_2=input_nums[5:]
    
    slicing_part_1.reverse()

    print("reverse_list",slicing_part_1)

    new_list= slicing_part_1 + slicing_part_2
    
    return new_list

output=reverse_five_positions(input_nums)
print("output",output)