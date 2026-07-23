class Animal:
    def __init__(self, animal_name, age =3 , health_level=50, happiness_level=50):
        self.animal_name = animal_name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(
            f"{self.animal_name} (Age: {self.age}) - Health: {self.health_level} - Happiness: {self.happiness_level}")
        return self

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self


class Lion(Animal):
    def __init__(self,animal_name,age=4,health_level=60,happiness_level=60,favorite_food="Steak"):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.favorite_food = favorite_food 

    def feed(self):
        self.health_level += 10
        self.happiness_level += 20  
        return self
    
    def unique_attribute(self):
        print(f"{self.animal_name} favorite food is {self.favorite_food}")
        return self

class Tiger(Animal):

    def __init__(
        self, animal_name, age=5, health_level=55, happiness_level=55, sound="Ror"):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.sound = sound  

    def feed(self):
        self.health_level += 15
        self.happiness_level += 10
        return self
    
    def unique_attribute(self):
        print(f"{self.animal_name} sound is {self.sound}")
        return self

class Monkey(Animal):

    def __init__(self,animal_name,age=2,health_level=40,happiness_level=70,climbing_speed = 20):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.climbing_speed = climbing_speed  

    def feed(self):
        self.health_level += 5
        self.happiness_level += 25
        return self
    
    def unique_attribute(self):
        print(f"{self.animal_name} climbing speed is {self.climbing_speed}")
        return self
    
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self

    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self

    def add_monkey(self, name):
        self.animals.append(Monkey(name))
        return self

    def print_all_info(self):
        print(self.zoo_name)
        for animal in self.animals:
            animal.display_info()
        return self
    
    def print_all_unique_attribute(self):
        print(self.zoo_name)
        for animal in self.animals:
            animal.unique_attribute()
        return self


zoo1 = Zoo("Alaa's Zoo")
zoo1.add_lion("Leo")
zoo1.add_lion("Simba")
zoo1.add_tiger("Shadow")
zoo1.add_tiger("Hunter")
zoo1.add_monkey("Coco")

zoo1.print_all_info()
print()
zoo1.print_all_unique_attribute()