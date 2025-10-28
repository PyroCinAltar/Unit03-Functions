# Question 3
def create_username(first_name, last_name):
    concat = first_name + "_" + last_name
    username = concat.lower()
    return username
#   return "f{first_name}_{last_name}".lower()

print(create_username("John", "Smith"))
print(create_username("MARY", "Jones"))
print(create_username("Alex", "TAYLOR"))

# Question 6:

def check_email(email):
    if "@" in email.lower() and email.lower().endswith(".com"):
        return True
    return False

print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))
print(check_email("invalid.com"))
print(check_email("test@school.edu"))


# Question 9:

def create_slug(title):
    return title.strip().lower().replace(" ", "-")

print(create_slug("My First Blog Post"))
print(create_slug("   Python Tutorial   "))
print(create_slug("Web Development 101"))