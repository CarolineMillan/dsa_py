def count(list_of_lists, target):
    # O(n). counts the number of times target appears in a list of lists
    counter = 0
    for list in list_of_lists:
        counter += list.count(target)
    return counter
