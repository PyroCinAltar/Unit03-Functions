def safe_divide(a, b):
    try:
        result = a / b
        return result
    # except:
    #     print("Cannot divide by 0")
    #     return None
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return None
    except TypeError:
        print("Thats not a valid number")
        return None
    except:
        print("An error occurred")


# print(safe_divide(10,2))
# print(safe_divide(10, 0))


def safe_operations(a, b, lst, key, d):
    try:
        print(f"division result: {a/b}")
        print("Access List element", lst[2])
        print("access dictionary key", d[key])
        print(f"add numbers: {a+b}")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except IndexError:
        print("List index out of range")
    except KeyError:
        print(f"Key {key} not found in dictionary")
    except TypeError:
        print("Invalid types for operation")
    except Exception as e:
        print("Some other error occurred", e)


# print(safe_operations(10, 2, [1, 2], "Tom", {"John": 15}))
# print(safe_operations(10, "hello", [1, 2], "Tom", {"John": 15}))
# print(safe_operations(10, 0, [1, 2], "Tom", {"John": 15}))


def calculate_price_per_item(total_cost, num_items):
    try:
        return round(total_cost / num_items, 2)
    except ZeroDivisionError:
        return "No itmes to calculate"

# print(calculate_price_per_item(100, 10))
# print(calculate_price_per_item(100, 0))
# print(calculate_price_per_item(100, 3))

def parse_age(age_str):
    try:
        return int(age_str)
    except ValueError:
        return None
    
print(parse_age("10"))
print(parse_age("qwerty"))