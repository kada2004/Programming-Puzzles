
num_one=23
num_two=25
max_capacity=50
def sum_if_less_than_fifty(num_one,num_two):
    addition=num_one+num_two

    if(addition<max_capacity):
        return addition
    else:
        return None
    
output=sum_if_less_than_fifty(num_one,num_two)
print("output",output)
