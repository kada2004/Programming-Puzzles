

input_strs=["cat","dog","bird","lizard"]
length_list=[]
def get_longest_string(input_strs):

    for x,y in enumerate(input_strs):
        length=len(y)
        length_list.append(length)
    longest_value=max(length_list)
    if(len(y)== longest_value):
        return y
        
output=get_longest_string(input_strs)
print("output",output)

