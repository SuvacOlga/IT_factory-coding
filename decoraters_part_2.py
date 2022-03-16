import psutil


def performance_testing(**test_type):
    def inner(func):
        def wrapper(expected):
            if test_type['name'] == 'memory':
                actual_result = psutil.virtual_memory().percent

                if expected - 10 <= actual_result <= expected + 10:
                    print(f'Test passed with {actual_result}')
                else:
                    print(f'Test failed {actual_result}')

            elif test_type['name'] == 'cpu':
                actual_result = psutil.cpu_percent()

                print(f'Test passed {actual_result}')

            else:
                print('This metric is not supported')

            func(expected)

        return wrapper

    return inner


@performance_testing(name='cpu1')
def search_performance(expected):
    print(f'Expected value is: {expected}')


search_performance(60)
