# Question 1
"""
john.smith gmail.com
"""

# Question 2
"""
tqbf
"""

# Question 3
def extract_domain(email):
    count_of_sign = email.count("@")
    if count_of_sign > 1:
        return "Invalid email"
    elif "@" in email:
        sect = email.split("@")
        domain = sect[1].lower()
        return domain
    else:
        return "Invalid email"


print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))


# Question 4
"""
123456
"""

# Question 5
"""
MY_DOCUMENT
"""

# Question 6
"""
banana
"""

# Question 7
def filter_numbers(text):
    revised = ""
    for char in text:
        if not char.isdigit():
            revised += char
    return revised

print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))

# Question 8
"""
https://example.com/users/profile
"""

# Question 9
def count_character_types(text):
    letters = 0
    numbers = 0
    spaces = 0
    for char in text:
        if char.isalpha():
            letters += 1
        if char.isdigit():
            numbers += 1
        if char == " ":
            spaces += 1
    result = f'"Letters": {letters}, "Digits": {numbers}, "Spaces": {spaces}'
    return result

print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))