#Example of MultiLevel Inhertance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass