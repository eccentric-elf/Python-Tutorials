def compute_factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def combination(n_value, r_value):
    if r_value > n_value:
        return "r cannot be greater than n"
    return compute_factorial(n_value) // (compute_factorial(r_value) * compute_factorial(n_value - r_value))

n_value = int(input("Enter value for n: "))
r_value = int(input("Enter value for r: "))

print(f"Combination ({n_value}C{r_value}) = {combination(n_value, r_value)}")
