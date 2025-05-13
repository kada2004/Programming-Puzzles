

input_list_a=[1,2,3,4]
input_list_b=[5,6,7,8,9]
output_list=[]
def my_zip(input_list_a,input_list_b):

    input_lenght=min(len(input_list_a),len(input_list_b))
  
    for i in range(input_lenght):
        output_list.append((input_list_a[i],input_list_b[i]))

    return output_list

output=my_zip(input_list_a,input_list_b)
print("output",output)