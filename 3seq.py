size_list = input('укажите количество элементов будущего списка #1: ')
size_list = int(size_list)
print('введите', size_list, 'цифр: ')
digit_list = []
for counter in range(size_list):
    message = str('Введите ' + str(counter + 1) + ' элемент: ')
    digit_new = input(message)
    while not digit_new.isdigit() or int(digit_new) < 0 or int(digit_new) >= 10:
        message_new = str('Введите еще раз элемент ' + str(counter + 1) + ' (от 0 до 9): ')
        digit_new = input(message_new)
    else:
        list.append(digit_list, str(digit_new))
digit_list_set = set(digit_list)

size_list1 = input('укажите количество элементов будущего списка #2: ')
size_list1 = int(size_list1)
print('введите', size_list1, 'цифр: ')
digit_list1 = []
for counter in range(size_list1):
    message = str('Введите ' + str(counter + 1) + ' элемент: ')
    digit_new1 = input(message)
    while not digit_new1.isdigit() or int(digit_new1) < 0 or int(digit_new1) >= 10:
        message_new = str('Введите еще раз элемент ' + str(counter + 1) + ' (от 0 до 9): ')
        digit_new1 = input(message_new)
    else:
        list.append(digit_list1, str(digit_new1))

digit_list1_set = set(digit_list1)

digit_list2_set = digit_list_set - digit_list1_set
if len(digit_list2_set) == 0:
    print('-' * 50)
    print('В первом списке не осталось элементов. :(')
    print('-' * 50)
else:
    print('-' * 50)
    print('В первом списке остались элементы:')
    print(*digit_list2_set, sep=',')
    print('-' * 50)

