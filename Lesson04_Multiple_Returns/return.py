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
# 2
result3 = 0
print(result3 == 0) #True - numeric equality
print(not result3) #True - falsy in boolean context
print(result3 is None) #False - different object
print(result3 is False) #False - different types


# Multiple Returns - Python packs multiple returns into a tuple
def calc_room(length, width):
    area = length * width
    perimeter = 2*(length+width)
    return area, perimeter

result = calc_room(10, 5)
print(result)
print(type(result))
print(type(42))

no_paratheses = 1,2,3
print(type(no_paratheses))


# unpacking
area_result, perimeter_result = calc_room(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")




def analyze_grades(list):
    if not list:
        return 0,0,0,False
    average = sum(list) / len(list)
    highest = max(list)
    lowest = min(list)
    is_pass = average >= 60 
    return average, highest, lowest, is_pass

print(analyze_grades([85, 92, 78, 90]))
print(analyze_grades([]))
print(analyze_grades([80,80,80]))