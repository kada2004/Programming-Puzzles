
adj_matrix=[[0,1,1,0],
            [1,0,0,1],
            [1,0,0,1],
            [0,1,1,0]]

start_node=2
output=[]
def find_adjacent_nodes(adj_matrix):

    for index,destination in enumerate(adj_matrix[start_node]):

        if(destination==1):
            output.append(index)
    return output
     
output=find_adjacent_nodes(adj_matrix)
print("output",output)
