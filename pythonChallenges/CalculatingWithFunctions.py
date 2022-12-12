"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""

def zero(operator=None): #your code here
    if operator == None:
        return "0"
    else:
        return int(eval("0"+operator))
def one(operator=None): #your code here
    if operator == None:
        return '1'
    else:
        return int(eval("1"+operator))
def two(operator=None): #your code here
    if operator == None:
        return "2"
    else:
        return int(eval("2"+operator))
def three(operator=None): #your code here
    if operator == None:
        return "3"
    else:
        return int(eval("3"+operator))
def four(operator=None): #your code here
    if operator == None:
        return "4"
    else:
       return int(eval("4"+operator))
def five(operator=None): #your code here
    if operator == None:
        return "5"
    else:
        return int(eval("5"+operator))
def six(operator=None): #your code here
    if operator == None:
        return "6"
    else:
        return int(eval("6"+operator))
def seven(operator=None): #your code here
    if operator == None:
        return "7"
    else:
        return int(eval("7"+operator))
def eight(operator=None): #your code here
    if operator == None:
        return "8"
    else:
        return int(eval("8"+operator))
def nine(operator=None): #your code here
    if operator == None:
        return "9"
    else:
        return int(eval("9"+operator))

def plus(nxtNum): #your code here
    return f"+{nxtNum}"
def minus(nxtNum): #your code here
    return f'-{nxtNum}'
def times(nxtNum): #your code here
    return f'*{nxtNum}'
def divided_by(nxtNum): #your code here
    return f'/{nxtNum}'


print(eight(minus(three())))