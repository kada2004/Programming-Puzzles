list_of_tuples=[(5, 2),
(1, 1000),
(100, 1),
(25, 25),
(2, 1000)]

def solve_knapsack_problem(list_of_tuples):
    max_capacity=5
    weight_list=[]
    value_list=[]
    for elem in list_of_tuples:
        each_capacity=elem[0]

        if each_capacity <= max_capacity :
            #print("each_capacity",each_capacity)
            each_value=elem[1]
            match_capacity=elem[0]
            #print("each_value",each_value,elem,match_capacity )
            value_list.append(each_value)
            weight_list.append(match_capacity)
    #print("value_list",value_list)

    best_value = 0
    best_combination=[]
    for i in range(len(value_list)):
        for j in range(1,len(value_list)+1):
            
            current_Value= value_list[i]
            current_weight = weight_list[i]

            if j > i :
                current_Value = current_Value + value_list[j-1]
                current_weight = current_weight + weight_list[j-1]
    print("Output",current_Value)
            

solve_knapsack_problem(list_of_tuples)
    

    
