
def extract_even_indexed_chars(input_str):
    even_chars = [input_str[index] for index in range(len(input_str)) if index % 2 == 0]
    return "".join(even_chars)

user_input = input("Enter the string: ")
output_string = extract_even_indexed_chars(user_input)
print("String with even-indexed characters:", output_string)
