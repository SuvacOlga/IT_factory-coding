class Student:
    def hello(self, name=None, email=None):
        if name is not None:
            print(f'Hey {name}')
            if email is not None:
                print(email)
        else:
            print('No value provided')


s1 = Student()
s1.hello()
s1.hello('Olga')
s1.hello('Olga', 'suvacolga@gmail.com.com')
s1.hello(email='suvacolga@gmail.com')
