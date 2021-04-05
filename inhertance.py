class Animal:
    # we can also inherte the attributes of the base class
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")
        
# Animal is Parent, Base Class
# Mammal is a Child, Sub Class

class Mammal(Animal):

    #Method overloading : means replacing or extendig the method defined in the base class
    def __init__(self):
        self.weight = 5

        #To prevent Method Overloading
        super().__init__()
    
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")

m = Mammal()
m.eat()
m.walk()
print(m.age) 

f = Fish()
f.eat()
f.swim()


