class Dog():
    name = ''
    __age = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def sit(self):
        print(self.name.title() + ' сейчас сидит')

    def roll_over(self):
        print(self.name.title() + ' перекатывается!')
    
    def age_plus(self, age_inc):
        self.__age += age_inc
        print('Собаке по имени ' + self.name + ' исполнилось ' + str(self.__age) + ' лет')

my_dog = Dog('шарик', 3)

my_dog.roll_over()
my_dog.sit()
my_dog.age_plus(2)
my_dog.setAge(1)
print('Моей собаке ' + str(my_dog.getAge()) + ' года')