

input_nums=[7,3,4,5,6,0,56,45]

def get_second_largest_number(input_nums):

    input_nums.sort()

    if(len(input_nums)>1):
        second_largest=input_nums[-2]
        
        return second_largest
    else:
        return None

Output=get_second_largest_number(input_nums)
print("Output : ",Output)