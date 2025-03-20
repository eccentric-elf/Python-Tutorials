def cmpr(num1,num2):
    if num1>num2:
        print(f"{num1} is the largest\n{num2} is the smallest")
    elif num1==num2:
        print(f"{num1} & {num2} are equal")
    else:
        print(f"{num2} is the largest\n{num1} is the smallest")

num1=int(input("Enter the first and second num: "))
num2=int(input())
cmpr(num1,num2)