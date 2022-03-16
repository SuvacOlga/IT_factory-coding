class RO:
    def capital(self):
        print('Bucharest')

    def language(self):
        print('Romanian')


class DE:
    def capital(self):
        print('Berlin')

    def language(self):
        print('German')


ro = RO()
de = DE()

for i in (ro, de):
    i.capital()
    i.language()
