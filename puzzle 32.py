
input_str="Nohtyp"

right_str="python"
list_python=[]

def contains_python_chars(input_str):

    for alphabets in input_str:
        #print("alphabets",alphabets)

        lower_case=alphabets.lower()
        #print("lower_case",lower_case)

        if(lower_case in right_str):
            list_python.append(True)
            
        else:
            list_python.append(False)
    
    if(False in list_python):
        return False
    else:
        return True       
            
   # return all(list_python)  
                   
print(contains_python_chars(input_str))
