
def check_symmetry(string):
    length = len(string)
    start = 0
    for idx in range(0, length // 2):
        if string[idx] != string[length - idx - 1]:
            return False
    return True

user_string = input("Enter the string: ")
if check_symmetry(user_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
