"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""
class RomanNumerals:
    def to_roman(val):
        romanToNumeral = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        roman = ''
        while val != 0:
            for key, value in romanToNumeral.items():
                IntDiv = val//value
                if IntDiv > 0:
                    roman += key*(IntDiv)
                    val -= value*(IntDiv)
                    break
        
        return roman

    def from_roman(roman_num):
        romanToNumeral = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        sum = 0
        for index, value in enumerate(roman_num):
            if len(roman_num) == 1:
                return romanToNumeral[value]
            
            try:
                first = value
                try:
                    second = roman_num[index+1]
                except:
                    second = None
                    
                if index == 0:
                    pre = None
                else:
                    pre = roman_num[index-1]
                
                if pre == None:
                    if romanToNumeral[first] < romanToNumeral[second]:
                        sum += romanToNumeral[second]-romanToNumeral[first]
                    else:
                        sum += romanToNumeral[first]
                        
                elif second == None:
                    if romanToNumeral[pre] < romanToNumeral[first]:
                        pass
                    else:
                        sum += romanToNumeral[first]
                        
                else:
                    if romanToNumeral[first] < romanToNumeral[second]:
                        sum += romanToNumeral[second]-romanToNumeral[first]
                    elif romanToNumeral[pre] < romanToNumeral[first]:
                        pass
                    else:
                        sum += romanToNumeral[first]                
            except:
                pass

        return sum

print(RomanNumerals.from_roman('I'))