def evnsum(num):
    total = 0  
    
    for i in range(num):
        n = int(input(f"Enter number {i+1}: "))  
        if n % 2 == 0: 
            total += n  
    
    return total 

num = int(input("Enter how many numbers as the value of N: "))

print(f"Sum of even numbers: {evnsum(num)}")
