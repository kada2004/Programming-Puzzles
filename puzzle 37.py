num_one=36
num_two=8

def greatest_common_divisor(num_one,num_two):
    divisor_list=[]
    min_max_input_num=min(num_one,num_two)
    
    for i in range(1,min_max_input_num+1):
       
        if(num_one%i==0 and num_two%i==0):
            divisor_list.append(i)
            
        
    if(max(divisor_list)>1):
        output=max(divisor_list)
        return output
    else:
        output=1
        return output
   
output=greatest_common_divisor(num_one,num_two)
print(f'The greatest divisor is {output}')
