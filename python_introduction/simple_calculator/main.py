#Simple calculator
print("Hello . Input operation from 24*3 , Type E to end!")
go = 1
while go == 1:
    x = input("type first number")
    x1 = int(x)
    op = input("type operator + or - or / or *")
    if op == 'E':
        go = 0
        print("Program end E pressed")
        break
    y = input("type second number")
    y1 = int(y)

    if op == '+':
        res = x1 + y1
    if op == '-':
        res = x1 - y1
    if op == '/':
        res = x1 / y1
    if op == '*':
        res = x1 * y1
    print("The result of operation is = ", res, "\n")