def reverse_num(n):
    reverse = 0
    
    while n > 0:
        digit = n % 10 
        reverse = reverse * 10 + digit  
        n //= 10
    
    return reverse

num = int(input("Enter a number: "))

if num < 0:
    print(f"Reversed number: -{reverse_num(abs(num))}")
else:
    print(f"Reversed number: {reverse_num(num)}")
