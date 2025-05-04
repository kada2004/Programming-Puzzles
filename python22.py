n=5

def harmonic_sum(n):
    total=0

    for i in range(1,n+1):
        total=1/i + total
        if(i !=n):
            print(f'1/{i} + ',end="")
        else:
            print(f'1/{i}')
    print("Sum of the series",round(total,3))

harmonic_sum(n)    