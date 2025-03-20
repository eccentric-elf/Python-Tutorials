def convert_to_binary(decimal_num):
    binary_str = ""
    
    if decimal_num == 0:
        return "0"
    
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str  
        decimal_num = decimal_num // 2
        print(binary_str)
    
    return binary_str


number = int(input("Enter a decimal number: "))

print(f"Binary representation: {convert_to_binary(number)}")
