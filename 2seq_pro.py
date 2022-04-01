list_my = input('Введите через \',\' или \';\' или \'/\' любые цифры: ')
list_lenth = len(list_my)
flag = 0
flag1 = 0
flag2 = 0

# for counter in range(0, list_lenth, 2):
#     print(list_my[0])

while True:
    if list_lenth == 0: # Проверка на пустой ввод
        list_my = input('Нет данных. Правильно введите через \',\' или \';\' или \'/\' любые цифры: ')
        list_lenth = len(list_my)
    else:
        if not list_my[0].isdigit(): # Проверка на первый символ
            list_my = input('Первый символ не цифра! Правильно введите через \',\' или \';\' или \'/\' любые цифры: ')
            list_lenth = len(list_my)
        else:
            if list_lenth == 3 and list_my[0].isdigit() and not list_my[1].isdigit() and not list_my[2].isdigit(): # Проверка на комбинацию 1//
                list_my = input('Внимательнее! Пропущена цифра: ')
                list_lenth = len(list_my)
            else:
                flag2 = 0
                counter = 0
                for counter2 in range(0, list_lenth - 1, 2):  # Проверка на комбинацию /
                    if list_my[counter2].isdigit() and list_my[counter2 + 1] == '/':
                        continue
                    else:
                        flag2 += 1
                if flag2 == 0:
                    break
                else:
                    flag1 = 0
                    counter1 = 0
                    for counter1 in range(0, list_lenth - 1, 2): # Проверка на комбинацию ;
                        if list_my[counter1].isdigit() and list_my[counter1 + 1] == ';':
                            continue
                        else:
                            flag1 += 1
                    if flag1 == 0:
                        break
                    else:
                        flag = 0
                        counter = 0
                        for counter in range(0, list_lenth - 1, 2): # Проверка на комбинацию ,
                            if list_my[counter].isdigit() and list_my[counter + 1] == ',':
                                continue
                            else:
                                flag += 1
                        if flag == 0:
                            break

                list_my = input('Правильно введите цифры через \',\' или \';\' или \'/\': ')
                list_lenth = len(list_my)
                flag = 0

set_my = set()
for counter3 in list_my: # Добавка в сет значений для автоисключения повторов
     if counter3 != ',' and counter3 != ';' and counter3 != '/':
         set_my.add(counter3)

print(*set_my, sep=', ') # Распаковка сета с сепаратором