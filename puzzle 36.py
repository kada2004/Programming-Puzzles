
left_matrix=[[2,3],[4,5]]
right_matrix=[[10,15],[5,1]]

range_lenght=len(left_matrix) + len(right_matrix)
print("range_lenght",range_lenght)


def matrix_multiply(left_matrix,right_matrix):
    output_result=[]
    a,b=0,1
    
    for i in range(range_lenght):
        if(i%2!=0):
            c=1
        else:
            c=0
        if(i<len(right_matrix)):
            d=0
        else:
            d = 1
        result_element_1=left_matrix[c][a] * right_matrix[a][d] + left_matrix[c][b] * right_matrix[b][d]

        output_result.append(result_element_1)
        output_result.sort()
    print("output_result",output_result)

output=matrix_multiply(left_matrix,right_matrix)
#print("output",output)