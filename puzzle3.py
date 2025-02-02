
input_num=[1,2,3,4,5,6,7,8,9,10]
even_num_sum=0
def sum_even(input_num):
    global even_num_sum
    for x,y in enumerate(input_num):
        if(y%2==0):
            even_num_sum=even_num_sum+y
    return even_num_sum

output=sum_even(input_num)
print("output",output)