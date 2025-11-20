# Question 1
def search_user_database(query):
    # Check for empty and whitespace string
    if query.strip() == "":
        return None, "No search query", False
    # Check for numbers or special characters
    if not query.isalpha():
        return False, "Invalid characters", False
    # just setting a condition here for RESULTS FOUND
    if query.lower() == ["john", "jane", "bob"]:
        return 3, "Users found", True
    # NO Results Found
    return 0, "No users found", True

# Testing
result, message, success = search_user_database("hello")
print(result)
print(message)
print(success)


# Question 2


def analyze_book_pages(list_of_book_pages):
    # Check for empty string
    if not list_of_book_pages:
        return 0, 0, 0.0, False
    # Count, total, average(rounded)
    count = len(list_of_book_pages)
    total = sum(list_of_book_pages)
    avg = round(total / count, 2)
    # Checking for a 501+ page book, breaks when it finds one
    has_long = False
    for book in list_of_book_pages:
        if book > 500:
            has_long = True
            break
    # Returns results
    return count, total, avg, has_long

# Testing
count_r, total_r, avg_r, has_long_r = analyze_book_pages([501, 400, 300])
print(count_r)
print(total_r)
print(avg_r)
print(has_long_r)