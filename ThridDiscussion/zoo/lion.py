from animal import Animal

class Lion(Animal):
    def __init__(self,animal_name,age=4,health_level=60,happiness_level=60,favorite_food="Steak"):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.favorite_food = favorite_food

    def feed(self):
        self.health_level += 10
        self.happiness_level += 20
        return self

    def unique_attribute(self):
        print(f"{self.animal_name}'s favorite food is {self.favorite_food}")
        return self