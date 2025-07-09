
alphabet_data="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_alphabet=alphabet_data.lower()

input_str="Hello world!"

rot=13
def rot13(input_str):
    lower_case_input=input_str.lower()
    result_str=""
    
    for element in lower_case_input:
        
        if(element in lower_case_alphabet):

            index_value=lower_case_alphabet.index(element)
             
            count_var_rot=index_value+rot

            if(count_var_rot>len(lower_case_alphabet)-1):
                reset_count=count_var_rot-len(lower_case_alphabet)-1
                reset_count=reset_count+1
               
                slicing_var=lower_case_alphabet[reset_count]
               
                result_str=result_str+slicing_var
            else:
                slicing_var=lower_case_alphabet[count_var_rot]

                result_str=result_str+slicing_var
        else:
            result_str=result_str+element
           
    return result_str


output=rot13(input_str) 
print("output",output)