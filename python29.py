
tap_code_map = {
    "a": ". .", "b": ". ..", "c": ". ...", "d": ". ....",
    "e": ". .....", "f": ".. .", "g": ".. ..", "h": ".. ...",
    "i": ".. ....", "j": ".. .....", "l": "... .",
    "m": "... ..", "n": "... ...", "o": "... ....",
    "p": "... .....", "q": ".... .", "r": ".... ..",
    "s": ".... ...", "t": ".... ....", "u": ".... ...",
    "v": "..... .", "w": "..... ..", "x": "..... ...",
    "y": "..... ....", "z": "..... ....."
}

input_code=".. ...  .. ....   .. ...  .. ...."

def tap_code_to_english(input_code):
  words_result=""
  result=""

  list_alphabet=[]

  words=input_code.split("   ")

  for word in words:
    
    alphabet=word.split("  ")
    list_alphabet.append(alphabet)
  lenght=len(list_alphabet)
  print("lenght",lenght)
    
  
  for x,y in enumerate(list_alphabet):
    print(x,y)

    for position,element in enumerate(y):
      print(element)

      for keys,values in tap_code_map.items():
        if(element==values):
          words_result=words_result+keys
    
    words_result=words_result+" "
    #print(words_result)
  return words_result

output=tap_code_to_english(input_code)
print("output",output) 