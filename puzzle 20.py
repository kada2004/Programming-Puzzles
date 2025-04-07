
n=4
symbol="*"

def print_triangle(symbol):
    
    for x in range(n):
        for y  in range(n-x-1):
            print(" ",end="")
        for j in range(2*x+1):
            print(symbol, end="")
        print()
print_triangle(symbol)


