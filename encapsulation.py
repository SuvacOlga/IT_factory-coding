class Encapsulation:
    def public(self):
        print('Everyone can see me')

    def _protected(self):
        print('Access provided only to my kids')

    def __private(self):
        print('No one should touch me')


class Child(Encapsulation):
    def test(self):
        self.public()
        self._protected()
        #self.__private()      ///children don't have access to privete part
  


o = Child()
o.test()
