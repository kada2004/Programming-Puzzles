input_num=17658689

def format_number_with_commas(input_num):
 
    result= ""
    count_var=0
    input_num_str=str(input_num)

    for x in range(len(input_num_str)-1,-1,-1):
  
        count_var=count_var+1

        iteration=input_num_str[x]

        result=iteration + result

        if(count_var %3==0 and x!=0):
            result="," + result

    return result

output=format_number_with_commas(input_num)
print("output",output)


