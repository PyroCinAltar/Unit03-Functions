# Problem 1
def remove_duplicates(items):
    edit_list = []
    for item in items:
        if item not in edit_list:
            edit_list.append(item)
        else:
            continue
    return(edit_list)

print(remove_duplicates([1, 2, 2, 3, 1, 4]) )
print(remove_duplicates(["a","b","a","c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))


# Problem 2
def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2:
            common.append(item)
    return common


print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(["a", "b"], ["c", "d"]))
print(find_common([1, 1, 2], [2, 2, 3]))
print(find_common([], [1, 2]))


# # Problem 3
def reverse_sublists(data, size):
    modified_list = []
    temp_list = []
    for x in range(0, len(data), size):
        section = data[x:x+size]
        section.reverse()
        for i in section:
            modified_list.append(i)
    return modified_list


print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))
print(reverse_sublists([1, 2, 3, 4, 5], 3))
print(reverse_sublists([1, 2, 3, 4], 1))
print(reverse_sublists([1, 2, 3], 5))


# # Problem 4
def rotate_list(items, position):
    new_list = []
    for i in range(len(items)):
        rotate = (i - position) % len(items)
        new_list.append(items[rotate])
    return new_list

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5],-2))
print(rotate_list([1, 2, 3], 0))
print(rotate_list([1, 2, 3], 5))
