from animal import Animal


class Monkey(Animal):
    def __init__(self,animal_name,age=2,health_level=40,happiness_level=70,climbing_speed=20):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.climbing_speed = climbing_speed

    def feed(self):
        self.health_level += 5
        self.happiness_level += 25
        return self

    def unique_attribute(self):
        print(f"{self.animal_name}'s climbing speed is {self.climbing_speed}")
        return self