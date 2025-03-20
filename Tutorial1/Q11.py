def sum_of_even_cubes(n):
    total = 0 

    for i in range(2, n + 1, 2): 
        total += i ** 3 

    return total

n = int(input("Enter a +ve integer: "))
while n <= 0:
    print("Number Invalid. Try again: ")
    n = int(input())
else:
    print(f"Sum of cubes of even numbers up to {n}: {sum_of_even_cubes(n)}")
