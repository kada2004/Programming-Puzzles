input_a="11110"
input_b="1111"

def xor(input_a,input_b):
    for a,b in zip(input_a,input_b):
        if(a==b):
            print(0 ,end="")
        else:
            print(1,end="")
xor(input_a,input_b)

