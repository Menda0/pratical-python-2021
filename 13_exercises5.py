## 1. Create a class called athlete
## 2. The class athlete must have the following attributues:
## 2.1 energy -> Int value that contains the athlete energy
## 2.2 name -> Name of the athlete
## 3. Athlete must have the following methods:
## 3.1 Run() -> When athelete run there must be a decrease of one point of energy
## 3.2 Eat() -> when athelete eats there must be an increse of one point of energy

# Francisco Example
class Athlete:

    # attributes
    # variables inside a class are called attributes
    energy = 0
    name = None

    # constructor method
    def __init__(self, energy, name):
        self.energy = energy
        self.name = name

    # Methods
    # Function inside a class are called methods
    def run(self):
        if self.energy >1:
            self.energy = self.energy - 1
            print(f"Person {self.name} run and energy:{self.energy}") 
        else:
            print(f"Person {self.name} not energy:{self.energy}")
        
        return self.energy

    def eat(self):
        self.energy = self.energy + 3
        print(f"Person {self.name} eat and energy:{self.energy}") 

    def runUntilFail(self):
        while self.energy > 1:
            self.run()


    def __repr__(self):
        return f"Text"

sandra = Athlete(20, "Sandra")
sandra.runUntilFail()

manuel = Athlete(15, "Manuel")
manuel.runUntilFail()

'''
count = 1
while sandra.run() > 1:
#while sandra.energy > 1:
    #sandra.run()
    count = count + 1
    # if sandra.energy==0:
    #   break

sandra = Athlete(20, "Sandra")
sandra.run()
sandra.eat()
'''

# 1. Create a class animal
# 2. Animal should have and attribute type that contains the type of animal
#    (Example: bird, mamal, reptile, etc)
# 3. Animal should have the attribute name
#    (Example: "Bear", "Dog", "Cobra", "Fox", "Cat")
# 4. Animal should have a method called noise. 
#    When invoked it must print on the terminal the sound of the animal.
#    (Example: Dog barks, Car Miau)
# 5. Create 3 classes for 3 types of animal
# 6. Types of animals should be a subclass of animal
# 7. Create 6 animal objects of multiple animal types
#    (Example: "Mamal Dog", "Repile Cobra", "Bird Eagle", etc)
# 8. Make every animal speak

# By Daniel Duro
class Animal:

    type = None
    name = None
    sound = None

    def __init__(self,type,name,sound):
        self.type = type
        self.name = name
        self.sound = sound

    def noise (self):
        print(f"The animal with name {self.name} and type {self.type} make the noise {self.sound}")
        

    def __repr__(self):
        return f"Animal with Type:{self.type} and Name:{self.name} and sound:{self.sound}"

    
class Mamal(Animal):
    TYPE ="Mamal"

    def __init__(self,name,sound):
        super().__init__(Mamal.TYPE,name,sound)

class Bird(Animal):
    TYPE ="Bird"
    def __init__(self,name,sound):
        super().__init__(Bird.TYPE,name,sound)

class Reptile(Animal):
    TYPE='Reptile'
    def __init__(self,name,sound):
        super().__init__(Reptile.TYPE,name,sound)

dog=Mamal("Dog","Auau")
cat=Mamal("Cat","Miau")
eagle=Bird("Eagle","Piu")
cobra=Reptile("Cobra","Qql_Coisa")
bear=Mamal("Bear","Qql_coisa")
fox=Mamal("Fox","Qql_coisa")

dog.noise()
cat.noise()
eagle.noise()
cobra.noise()
bear.noise()
fox.noise()
