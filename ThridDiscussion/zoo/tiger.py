from animal import Animal


class Tiger(Animal):
    def __init__(self,animal_name,age=5,health_level=55,happiness_level=55,sound="Roar"):
        super().__init__(animal_name, age, health_level, happiness_level)
        self.sound = sound

    def feed(self):
        self.health_level += 15
        self.happiness_level += 10
        return self

    def unique_attribute(self):
        print(f"{self.animal_name}'s sound is {self.sound}")
        return self