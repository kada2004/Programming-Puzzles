
input_num=98765

def get_numbers_of_digits(input_num):
    
    x=0
    y=0

    count=0
    
    while input_num > x:

        x=input_num%10
        y=input_num//10

        input_num=y

        count= count + 1

    print("count",count)

get_numbers_of_digits(input_num)

