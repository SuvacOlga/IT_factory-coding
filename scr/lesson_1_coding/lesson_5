num_list = [1, 2, 3, 4, 5, 6, 7]

sum = 0
for i in num_list:
    sum += i
else:
    print('Test completed')

print(sum)

sum = 0
for i in range(0, len(num_list), 2):
    sum += num_list[i]

print(sum)

it = 0
sum = 0

while it < len(num_list):
    sum += num_list[it]
    it += 1
else:
    print('Test completed')

print(sum)

my_dict = {'a': 2,
           'b': {'f': 7},
           'c': 4,
           'd': {'e': 5}}

for key, value in my_dict.items():
    print(key, value)
    if type(value) == dict:
        for x, y in value.items():
            print(x, y)


def log_in(user: str, pwd):
    """
    :type pwd: object
    :type user: object
    """
    return f'The user name is: {user} with password {pwd}'


print(log_in.__doc__)

#log_in(, "popescu")
log_in("pop", "1234")
log_in("pop", "asdf")
x = log_in(10, "qwer")
print(x)
