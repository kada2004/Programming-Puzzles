
input_string=["apple","banana","cherry","date","alphabelt","Gloria"]
new_list=[]
string_letter="a"
def filter_string_containing(input_string):

    for a,b in enumerate(input_string):

        if(string_letter in b):
            new_list.append(b)

    return new_list
    
output=filter_string_containing(input_string)
print("output",output)
