# При помощи функции filter() из котрежа слов отфильтровать только те, которые являются
# полиндромами (слова которые читаются одинаково в обе стороны), регистр букв не учитывать.

inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
inputdata=tuple(inputdata)


def is_polindrom(word):
    word = word.upper()
    return word[::-1] == word

result = list(filter(is_polindrom, inputdata))
print(result)

polindrom_inputdata = list(filter(lambda w: w[::-1].upper() == w.upper(), inputdata))
print(polindrom_inputdata)


