# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку.
# (результаты всех преобразований выводить на экран).
have_bytes = b'r\xc3\xa9sum\xc3\xa9'
print(have_bytes)
have_str = have_bytes.decode()
print(have_str)
get_latin1 = have_str.encode("Latin1")
print(get_latin1)
get_str = get_latin1.decode('Latin1')
print(get_str)
