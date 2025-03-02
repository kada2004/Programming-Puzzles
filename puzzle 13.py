

input_strs=["apple","banana","zyxvb"]
input_strs_with_vowel=[]
def filter_strings_with_vowels(input_strs):

    vowels_list="aeou"

    for x,y in enumerate(input_strs):
        
        for a,b in enumerate(y):

            if(b in vowels_list):
                input_strs_with_vowel.append(y)

    return list(set(input_strs_with_vowel))


output=filter_strings_with_vowels(input_strs)
print("output",output)