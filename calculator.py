n1 = input("Enter the first number ")
n2 = input("Enter the second number ")
op = input("Enter operation (+,-,*,/) ")

if(op == '+'):
    sum = n1 + n2
    print(sum)
elif(op == '-'):
    difference = n1 - n2
    print(difference)
elif(op == '*'):
    product = n1 * n2
    print(product)
elif(op == '/'):
    quotient = n1 / n2
    print(quotient)
else:
    print("Enter a valid operation")



