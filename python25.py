input_equation="2+3=5"

def is_valid_equation(input_equation):

    left_side,right_side=input_equation.split("=")
    try:
        left_side_variable=eval(left_side)
        right_side_variable=int(right_side)

        return left_side_variable==right_side_variable

    except:
        return False
    
print(is_valid_equation(input_equation))

