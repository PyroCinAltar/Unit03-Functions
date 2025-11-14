# Q1

def combine_values(*values):
    product = 1
    if not values:
        return product
    for v in values:
        product *= v
    return product

print(combine_values(2,3,4))
print(combine_values(5))
print(combine_values())

# Q2

def merge_details(label, **info):
    output = {"label": label}
    # .update() adds from another set, list, tuple; merges key-value pairs from another dict or iterable of key-vlaue pairs
    output.update(info)
    return output

print(merge_details("ItemA", size="Large", cost=12.50))    
print(merge_details("UserX"))    

# Q3

'''
8
10
0
'''

# Q4

'''
{"name": "Alpha", "x": 1, "y": 2, "count": 2}
{"name": "Beta", "count": 0}
'''