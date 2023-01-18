# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку.
# (результаты всех преобразований выводить на экран).
dano_bytes = b'r\xc3\xa9sum\xc3\xa9'
print(dano_bytes)
dano_str = dano_bytes.decode()
print(dano_str)
dano_latin1 = dano_str.encode("Latin1")
print(dano_latin1)
dano_str_1 = dano_latin1.decode('Latin1')
print(dano_str_1)
