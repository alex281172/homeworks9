size_list = input('укажите количество элементов будущего списка: ')
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
        list.append(digit_list, int(digit_new))
list.sort(digit_list)
print(digit_list)
