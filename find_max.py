
def find_max(lst, comparison):
    current_max = lst[0]
    for potential_max in lst:
        current_max = comparison(potential_max, current_max)
    return current_max

greater = lambda x,y: x if x > y else y


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(find_max(my_list, greater))