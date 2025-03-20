def remove_substring(main_str, substring):
    if substring in main_str:
        updated_str = main_str.replace(substring, "")
        return updated_str
    return main_str

user_string = input("Enter the string: ")
substring_to_remove = input("Enter the substring: ")

result_string = remove_substring(user_string, substring_to_remove)

if result_string != user_string:
    print("Updated string:", result_string)
else:
    print("Substring not found in the string.")
