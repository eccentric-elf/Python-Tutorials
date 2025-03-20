def separate_elements(input_str):
    chars = list(input_str)
    even_chars = [chars[i] for i in range(len(chars)) if i % 2 == 0]
    odd_chars = [chars[i] for i in range(len(chars)) if i % 2 != 0]
    return chars, even_chars, odd_chars

user_input = input("Enter the string: ")
all_chars, even_chars, odd_chars = separate_elements(user_input)

print("All characters:", all_chars)
print("Even indexed characters:", even_chars)
print("Odd indexed characters:", odd_chars)
