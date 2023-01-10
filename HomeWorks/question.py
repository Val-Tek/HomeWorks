def my_decor(a_func):
    def wrapper():
        print("я- код который выполняется до функци")
        a_func()
        print("я- код который выполняется после функци")

    return wrapper()


@my_decor
def alone_f():
    print('я- функция')

@my_decor
def new_func():
    a = 2 + 4
    print('a = ', a)

print(20 * "____")

alone_f()
print(20 * "____")
# при этом   my_decor(alone_f) срабатывет
# alone_f = my_decor(alone_f)
new_func()