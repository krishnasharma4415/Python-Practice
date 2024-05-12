def SumOfDigits():
    n1 = int(input("Enter 1st digit"))
    n2 = int(input("Enter 2nd digit"))
    print(n1 + n2)
def Reverse():
    num = int(input("Enter a number"))
    revnum = 0
    while num != 0:
        digit = num % 10
        revnum = (revnum * 10) + digit
        num = int(num / 10)
    print("Reverse of number is" + str(revnum))
def PrimeNo():
    start = int(input("Enter the start value : "))
    end = int(input("Enter the end value : "))
    check = 0
    for i in range(start , end + 1):
        check = 0
        for j in range(1 , i):
            if i % j == 0:
                check += 1
        if check < 2:
            print(i)
def Factorial():
    num = int(input("Enter a number : "))
    fact = 1
    for i in range(1 , num + 1):
        fact = int(fact * i)
    print(fact)
def Count():
    num = int(input("Enter a number : "))
    num2 = num
    check = int(input("Enter the digit to be counted : "))
    while num != 0:
        digit = num % 10
        num = num / 10
        if digit == check:
            c = c + 1
    print("The number of times " , check , "occured in " , num2 , "is " , c)

        
