def search_data(query):
    if query == "":
        return None
    if query == "empty":
        return 0
    if query == "error":
        return False
    return len(query)


# None
# Absence of value, not set, not found
# Uses: missing data, search faliures, optional parameters
result = None
print(result is None) # True - identity check
print(result == None) # True - equality check
print(not result) # True - falsy check


# False
# Explicit false condition, validation faliure, negative result
# Uses: Validation result, boolean operations, success/faliure/status
result2 = False
print(result2 is False) # True - identity check
print(not result2) # True - boolean negation
print(result2 == 0) # True - falsy check


# 0
# 0 is a VALID numeric value, not absence of value
# 
result3 = 0
print(result3 == 0) #True - numeric equality
print(not result3) #True - falsy in boolean context
print(result3 is None) #False - different object
print(result3 is False) #False - different types