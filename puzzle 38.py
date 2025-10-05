input_nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#input_nums=[5,5,5,5]
target=10

def find_pairs_summing_to_target(input_nums):
    lenght_input=len(input_nums)
    if(lenght_input%2!=0):
        len_var=int(lenght_input/2)
        input_nums.pop(len_var)
    else:
        input_nums
    output=[]
    a,b=0,-0
    for x,y in enumerate(input_nums):
        a=a+1
        b=b-1
        last_input=input_nums[b]
        start_input=input_nums[a-1]
        
        combination=(start_input,last_input)
        
        sum_combination=start_input+last_input
             
        if(sum_combination==target):
            output.append(combination)
        else:
            output=[]
    boolean_list=[]

    index_l1=[]
    index_l2=[]
    for index_1,elem in enumerate(output):
        elem_a=elem[0]
        elem_b=elem[1]
    
        for index_2,each_elem in enumerate(output):

            elem_C=each_elem[0]
            elem_d=each_elem[1]

            if(elem_a==elem_C or elem_a==elem_d and elem_b==elem_C or elem_b==elem_d):
                
                if(index_1 not in index_l1 and index_1 not in index_l2):
                    index_l1.append(index_1)

                if(index_2 not in index_l1 and index_2 not in index_l2):
                    index_l2.append(index_2)
    index_l2.sort()
    index_l2.reverse()
    
    for each_index in index_l2:
        #print("each_index",each_index)
        output.pop(each_index)
        
    return output
        #print("output final",output)
result=find_pairs_summing_to_target(input_nums)
print("solution",result)