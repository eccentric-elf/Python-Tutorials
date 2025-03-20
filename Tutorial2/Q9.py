
def reverse_and_print(input_str):
    length = len(input_str)
    middle = length // 2


    for idx in range(middle - 1, -1, -1):
        print(input_str[idx], end="")

    for idx in range(length - 1, middle - 1, -1):
        print(input_str[idx], end="")

user_input = input("Enter the string: ")
reverse_and_print(user_input)
