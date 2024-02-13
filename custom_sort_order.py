
def custom_sort_order(list):
    return sorted(list, key=lambda x: (len(x), x)) #tuple that sorts by length and string alphabet value

my_list = ['yello','hello','thinking','of','longest', 'word']
print(custom_sort_order(my_list))