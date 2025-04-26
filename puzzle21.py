
sequence_number=10

def fibonacci(sequence_number):
    a=0
    b=1
    
    print(a)
    #print(b)

    for x in range(0,sequence_number):
        #print(x)
        c=a+b
        a=b
        b=c
        print(c) 
fibonacci(sequence_number)
