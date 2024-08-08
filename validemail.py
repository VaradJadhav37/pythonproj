def is_valid_email(email):
    if len(email) < 5 or "@" not in email or "." not in email:
        return False

    if email.count("@") != 1 or ".." in email:
        return False
    if email[0].isalpha():
        return True
    else:
        return False
    for char in email:
        if not (char.isalnum() or char in "._@"):
            return False

    return True


email = input("Enter your email: ")
if is_valid_email(email):
    print("Valid email format.")
else:
    print("Invalid email format.")
