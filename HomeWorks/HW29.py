# 1) Реалізувати функцію, яка порахує прибуток по таблиці invoice_items. Сума по замовленню = UnitPrice * Quantity.
# Прибуток = сумма замовлень. Якщо вирішуєте через sql, то необхідно для суми викрористати агрегатну функцію sum.
#
# 2) Реалізувати функцію, которая виведе повторювані FirstName з таблиці customers і кількість їх входжень в таблицю.
# Результат має виглядати як:
# Марія 2
# Микола 3.
# Тобто виводимо тільки ті імена, які повторюються більше одного разу.
# Якщо вирішуєте через sql, то використовуємо count та group by.

import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def get_totalsum():
    s_sql = "SELECT sum(ii.UnitPrice * ii.Quantity) FROM invoice_items ii"
    result = execute_query(s_sql)
    print("total : ", result[0][0])


get_totalsum()


def get_nonuniq_namecounts() -> list:
    query_sql = '''
    SELECT c.FirstName, count(c.FirstName)  
    FROM customers c
    group by c.FirstName
    '''
    namecounts = execute_query(query_sql)
    return [t for t in namecounts if t[1] > 1]


print(*get_nonuniq_namecounts())

