
num_one= 3
num_two= 4
# 3 in binary = 011,  and 4 in binary = 100 

def bitwise(num_one,num_two):

    while num_two != 0 :

        sum_without_carry = num_one ^ num_two

        carry = (num_one & num_two) << 1

        num_one = sum_without_carry
        num_two = carry

    return num_one
output=bitwise(num_one,num_two)
print("output",output)