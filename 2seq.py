list_my = input('Введите через \',\' любые цифры: ')
list_lenth = len(list_my)
flag = 0
counter = 0

set_my = set()
for counter in list_my:
     if counter != ',':
         set_my.add(counter)
print(*set_my, sep=', ') # Распаковка сета с сепаратором


