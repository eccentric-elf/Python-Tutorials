def binary_to_decimal(binary_str):
    return int(binary_str, 2)

user_binary = input("Enter a binary number: ")

decimal_value = binary_to_decimal(user_binary)

print(f"Decimal representation: {decimal_value}")
