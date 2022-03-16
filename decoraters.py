def print_test_logs(msg):
    threshold = 90

    def logger():
        print(f'Logging memory consumption from {msg} if there is a value higher than {threshold}')

    return logger


x = print_test_logs('Message')
x()


def my_unit_test(func):
    def wrapper(a):
        print(f'My unit test started for {a}')
        func(a)
        print('My unit test ended')

    return wrapper


@my_unit_test  # injection of auxiliar behavior
def my_test_1(a):
    assert a in [1, 2, 3]


#my_test_1(4)

my_unit_test(my_test_1(2))
