
input_str="abcdefg"

def check_if_string_is_happy(input_str):

    list_with_set=len(set(input_str))
    orginal_list_without_set=len(input_str)

    if(list_with_set==orginal_list_without_set):

        return True
    
    else:

        return False

output=check_if_string_is_happy(input_str)
print("output",output)