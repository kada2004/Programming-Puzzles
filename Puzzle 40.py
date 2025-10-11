input_nums=[5,10,9,11,4]
#input_nums=[-1,-2,-3,-4,-5]
#input_nums = [100, 5, 10]

def inserting_sort(input_nums):
    output_list = []  

    for num in input_nums:
        inserted = False
       # print("outputlist_lenght",len(output_list))
        for i in range(len(output_list)):
            if num < output_list[i]:
                #print("output_list[i]",num,output_list[i])
                  
                output_list.insert(i, num)
                inserted = True
                break
        if not inserted:
            output_list.append(num)  
    return output_list

output = inserting_sort(input_nums)
print("output", output)
