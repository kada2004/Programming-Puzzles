

input_nums=[1,2,3,4,5,6,7,8,9,10,-1,12]
list_lenght=len(input_nums)
#print("list_lenght",list_lenght)
prime_list=[]
def find_primes(input_nums):

    for elements in input_nums:
        if(elements<=1):
            print("Not prime")

        else:

            is_prime=True
            for i in range(2,list_lenght):
                #print("i",i)
                if(elements !=i and elements%i==0):
                    is_prime=False
                    break
                    #print("elements",elements)   
            if(is_prime==True):
                  #  print("Prime",elements)
                    prime_list.append(elements)

    print("prime_list",prime_list)

find_primes(input_nums)  

