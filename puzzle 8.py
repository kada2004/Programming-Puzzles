

input_list=["hello",1,2,"www"]

#input_list=[1,2,3,4,5]
new_list=[]
def filter_type_str(input_list):

    for x,y in enumerate(input_list):
        if(type(y)==str):
            new_list.append(y)

    return new_list

output=filter_type_str(input_list)
print("ouput",output)
