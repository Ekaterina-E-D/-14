
def recurs_print(my_list1):
    if my_list1==[]:
        print('Конец списка.')
        return
    elif my_list1    == 0:
        return 0
    elif my_list1 == 1:
        return 1
    recurs_print(my_list1.pop(0))
    print(my_list1)

my_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recurs_print(my_list1)
