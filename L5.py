from abc import ABC , abstractmethod

class Animal(ABC):
    def __init__(self,name ,habitat ):
        self.name=name
        self.habitat=habitat
    def display(self):
        print("Name:",self.name)
        print("Habitat:",self.habitat)
    @abstractmethod
    def sound(self):
        pass    


class Dog(Animal):
    def __init__(self, name, habitat,breed):
        super().__init__(name, habitat)
        self.bred=breed
    def sound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, habitat,breed):
        super().__init__(name, habitat)
        self.bred=breed
    def sound(self):
        print("Meow")
class Parrot(Animal):
    def __init__(self, name, habitat,breed):
        super().__init__(name, habitat)
        self.bred=breed
    def sound(self):
        print("Chirp")
    
dog=Dog("Bulldog","Land","Mammal")
dog.display()
dog.sound()
parrot=Parrot("Parrot","Land","Bird")
parrot.display()
parrot.sound()
cat=Cat("Persian","Land","Mammal")
cat.display()
cat.sound()

for animal in [dog,parrot,cat]:
    animal.sound()
    animal.display()
    print("___________________________")
    
        