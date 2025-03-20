def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "$@#"

    if len(password) >= 6:
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True

        if has_upper and has_lower and has_digit and has_special:
            return "Password is valid"
        else:
            return "Invalid password"
    else:
        return "Invalid password"

user_password = input("Enter the password: ")
print(validate_password(user_password))
