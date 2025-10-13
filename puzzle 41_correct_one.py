

roman_map={
    1000:"M",900:"CM",500:"D",400:"CD",100:"C",
    90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",
    4:"IV",1:"I"
}
def into_to_roman(roman_map):

    input_num=4999
    roman_num=""
    for int_values, symbols in roman_map.items():
        #print("int_values, symbols",int_values, symbols)

        #Looping to find numbers which are greater or equal to my input
        while input_num >= int_values:
            #print("int_values, symbols",int_values, symbols)
            roman_num= roman_num + symbols
            input_num= input_num - int_values
            #print("input_num",input_num)

    print(f'the roman number is {roman_num}')

into_to_roman(roman_map)
