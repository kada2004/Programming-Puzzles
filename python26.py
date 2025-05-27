

inputs_list=[1,2,3,4,5]
rotate_amount=7

def rotate_list_left(inputs_list):

    lenght=len(inputs_list)

    rotate_amount_variable=rotate_amount%lenght

    if(rotate_amount_variable>0):

        first_part_larger_rotate_amount=inputs_list[0:rotate_amount_variable]
        second_part_larger_rotate_amount=inputs_list[rotate_amount_variable:]

        output_list_larger_rotate_amount=second_part_larger_rotate_amount + first_part_larger_rotate_amount

        return output_list_larger_rotate_amount
    else:
        
        return inputs_list
    
output=rotate_list_left(inputs_list)
print("output",output)


