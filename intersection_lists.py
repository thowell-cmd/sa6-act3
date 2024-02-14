
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [4, 5, 6, 7, 8]

intersect_lst = list(filter(lambda x: x in lst_1, lst_2)) 

print(intersect_lst)