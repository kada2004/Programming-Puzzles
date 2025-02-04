
input_str="Hello World! Abc aeio"
vowel_str="aeiouAEIOU"
def remove_vowel(input_str):
    result=""
    for element,letters in enumerate(input_str):
        if(letters not in vowel_str):
            result=result + letters

    return result

output=remove_vowel(input_str)
print("output",output)
