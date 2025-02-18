

inputs_str = ["cat", "dog", "fish", "elephant","Gloria","Dan"]
lenght_list=[]
def filter_even_lenth_strings(inputs_str):
    for pos,elements in enumerate(inputs_str):

        input_str_length=len(elements)
        if(input_str_length%2==0):
            
            lenght_list.append(elements)

    return  lenght_list
            

output=filter_even_lenth_strings(inputs_str)
print("output",output)