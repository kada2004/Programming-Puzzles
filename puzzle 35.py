input_str="(()) ()"

def get_parenthese_groups(input_str):

    result_str=""
    result_list=[]
    
    for pos,elem in enumerate(input_str):

        if(elem=="("):
            result_str+=elem
            print("result_str",result_str)

        elif(elem==")"):
            result_str+=elem
            print("result_str",result_str)

            count_open_brackets=result_str.count("(")
            count_close_brackets=result_str.count(")")

            print("count_open_brackets",count_open_brackets)
            print("count_close_brackets",count_close_brackets)

            if(count_open_brackets==count_close_brackets):
                result_list.append(result_str)
                result_str=""
    return result_list
   
output=get_parenthese_groups(input_str)
print("output",output)