username = input("Username: \n")
password = input("Password: \n")

password_length = len(password)

obfuscated_password = "*" * password_length

print(f"Hey {username}, your password {obfuscated_password} is {password_length} characters long")
