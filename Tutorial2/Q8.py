
def replace_substring(original_str, old_substring, new_substring):
    if old_substring in original_str:
        return original_str.replace(old_substring, new_substring)
    return original_str

text = input("Enter the string: ")
substring_to_replace = input("Enter the substring to replace: ")
replacement_substring = input("Enter the new substring: ")

updated_text = replace_substring(text, substring_to_replace, replacement_substring)

print(updated_text)
