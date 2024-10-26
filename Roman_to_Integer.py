roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }
total = 0
roman_input = input("Enter your Roman:").upper()
for i in range(len(roman_input)):
    if  roman_input[i] in roman_numerals:
        if i + 1 < len(roman_input) and roman_numerals[roman_input[i]] <  roman_numerals[roman_input[i+1]]:
            total -= roman_numerals[roman_input[i]]
        else:
            total +=  roman_numerals[roman_input[i]]
print("Roman: "+roman_input+" ->"+" Integer: "+str(total))



