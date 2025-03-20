def oddevn(num):
    if num==0:
        return("It's zero.")
    elif num%2==0:
        return("It's even.")
    else:
         return("It's odd.")

num=int(input("Enter the number: "))
check=oddevn(num)
print(check)