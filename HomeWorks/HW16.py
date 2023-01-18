# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.


name = input('your name: ')
surname = input('your surname: ')
date = input('date of birth: ')
place = input('place of birth: ')
print(name, surname, date, place)
f = open('home work16.txt', 'w')
f.write(name + "\n")
f.write(surname + "\n")
f.close()
f = open('home work16.txt', 'a')
f.write(date+"\n")
f.write(place+"\n")
f.close()