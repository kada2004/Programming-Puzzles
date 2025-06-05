

price_action=[7,6,5,10,11,12,10,9,10]

def count_peaks_valleys(price_action):
    valley=0
    peak=0
    number_of_iteration=len(price_action)-2

    for x in range(number_of_iteration):
        
        element1=price_action[x]
        element2=price_action[x+1]
        element3=price_action[x+2]

        if(element1<element2>element3):
            peak=peak+1
        elif(element1>element2<element3):
            valley=valley+1
    return peak,valley

output=count_peaks_valleys(price_action)
print("output",output)
