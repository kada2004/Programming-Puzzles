
input_nums=[1,2,3,4,5,-9]
def find_zero_sum_triples(input_nums):
    list_combination=[]
    a,b,c=0,1,3
    for k in range(len(input_nums)):

        for i in range(len(input_nums)):
            #print(a,b,c)
            num_1=input_nums[a]
            num_2=input_nums[b]
            num_3=input_nums[c]

            combination=num_1+num_2+num_3

            if(combination==0):

                list_combination.append([num_1,num_2,num_3])
            b=b+1
            c=c+1

            if(a>=len(input_nums)):
                a=a-len(input_nums)

            if(b>=len(input_nums)):
                b=b-len(input_nums)

            if(c>=len(input_nums)):
                c=c-len(input_nums)
        a=a+1
        b=a+1
        c=b+1

        if(a>=len(input_nums)):
                a=a-len(input_nums)

        if(b>=len(input_nums)):
            b=b-len(input_nums)

        if(c>=len(input_nums)):
            c=c-len(input_nums)
    return list_combination

output=find_zero_sum_triples(input_nums)
print("output",output)