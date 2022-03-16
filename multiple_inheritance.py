class GrandFather:
    def smoke_weed(self):
        print('Smoking stop Covid-19')


class Mother:
    def make_photo(self):
        print('Taking a screenshot')

    def cooking(self):
        print('Making cookies')


class Father(GrandFather):
    def drive_car(self):
        print('Driving a BMW')

    def drink_beer(self):
        print('Drinking a Peroni')


class Child(Mother, Father):
    def crying(self):
        self.cooking()
        self.drive_car()
        self.smoke_weed()


class NewBorn(Child):
    def drink_milk(self):
        print('Milk is good')


child = Child()
child.crying()
child.drink_beer()
child.cooking()
child.smoke_weed()

n_b = NewBorn()
n_b.smoke_weed()
print(NewBorn.mro())
