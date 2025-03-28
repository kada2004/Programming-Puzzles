

input_boad=[["X","X","O"],["X","O","O"],["X","O","O"]]

vertical_1, vertical_2 ,vertical_3=[],[],[]

def get_tic_toc_toe_winner(input_boad):
    for x,y in enumerate(input_boad):
        list_lenth=len(y)
        
        #Horizontal slicing
        count_horizontal_x=y.count("X")
        count_horizontal_O=y.count("O")


        if(count_horizontal_x==list_lenth):
            return "X has won horizontal"
        elif(count_horizontal_O==list_lenth):

            return "O has won horizontal"
        
        
        #Vertical slicing
        index_1=y[0]
        index_2=y[1]
        index_3=y[2]

        vertical_1.append(index_1)
        vertical_2.append(index_2)
        vertical_3.append(index_3)

    print("vertical_1",vertical_1)
    print("vertical_2",vertical_2)
    print("vertical_3",vertical_3)

    count_vertical_1_x=vertical_1.count("X")
    count_vertical_2_x=vertical_2.count("X")
    count_vertical_3_x=vertical_3.count("X")

    count_vertical_1_O=vertical_1.count("O")
    count_vertical_2_O=vertical_2.count("O")
    count_vertical_3_O=vertical_3.count("O")

    #diagonal
    diagonal_1=vertical_1[0]
    diagonal_2=vertical_2[1]
    diagonal_3=vertical_3[2]
    

    str_variable= diagonal_1 + "," + diagonal_2 + "," + diagonal_3


    print("str_variable",str_variable)


    count_var_diagonal_x=str_variable.count("X")
    count_var_diagonal_O=str_variable.count("O")
    

    #diagonal_opposite


    diagonal_1_opposite=vertical_1[2]
    diagonal_2_opposite=vertical_2[1]
    diagonal_3_opposite=vertical_3[0]


    str_variable_diagonal= diagonal_1_opposite + "," + diagonal_2_opposite + "," + diagonal_3_opposite

    print("str_variable_diagonal",str_variable_diagonal)

    count_var_diagonal_opposite_x=str_variable_diagonal.count("X")
    count_var_diagonal_opposite_O=str_variable_diagonal.count("O")
 
    if(count_vertical_1_x==list_lenth or count_vertical_2_x==list_lenth or count_vertical_3_x==list_lenth):

        return "X vertical has won"

    elif(count_vertical_1_O==list_lenth or count_vertical_2_O==list_lenth or count_vertical_3_O==list_lenth):

        return "O vertical has won"

    if(count_var_diagonal_x==list_lenth):
        return "X won in diagonal"

    elif(count_var_diagonal_O==list_lenth):

        return "O won in diagonal"

    if(count_var_diagonal_opposite_x==list_lenth):

        return "X won in opposite diagonal"

    elif(count_var_diagonal_opposite_O==list_lenth):

        return "O won in opposite diagonal"


output=get_tic_toc_toe_winner(input_boad)
print("output",output)

    



    