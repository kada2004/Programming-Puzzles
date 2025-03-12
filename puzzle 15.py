
input_strs=["kayak","rotator","dog","racecar","deified","giraffe","deed","a"]
lenght_condition=3

solution_list=[]
def filter_palindromes(input_strs):

    for x,y in enumerate(input_strs):
        if(len(y)>lenght_condition):
            
            variable_01=y[0:3]
            variable_02=y[-3:]

            reverse_element=variable_02[::-1]

           
            if(variable_01==reverse_element):
                solution_list.append(y)

    return solution_list
                                                                                                                                                                                                                                                                                                                                                                             
output=filter_palindromes(input_strs)
print("output",output)