def modify_string(input_str):
    modified_str = input_str.replace(" ", "*")
    modified_str += '$'
    return modified_str

user_input = input("Enter the string: ")
result_string = modify_string(user_input)
print(result_string)
