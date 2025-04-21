number1 = float(input('Enter number 1:'))
number2 = float(input('Enter number 2:'))
checkOperator = input('Enter any of the operator +,-,*,/:')

#Addition
if(checkOperator == '+') :
    result = number1 + number2
    print('the result is:' , result)
elif (checkOperator == '-') :
    result = number1 - number2
    print('the result is:' , result)

elif (checkOperator == '*') :
    result = number1 * number2
    print('the result is:' , result)

elif (checkOperator == '/') :
    if number2 == 0 :
        print('Number cannot be 0')
    result = number1 / number2
    print('the result is:' , result)
else :
    print('Invalid operator.Choose from +,-,*,/')
