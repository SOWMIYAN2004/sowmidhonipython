num = int(input("Enter a number: "))
Factorial = 1
if num < 0:
    print("sorry,Factorial does not exist for negative numbers")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        Factorial = Factorial*i
    print("The Factorial of",num,"is",Factorial)