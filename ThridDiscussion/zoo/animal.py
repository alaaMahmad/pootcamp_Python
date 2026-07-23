class Animal:
    def __init__(self, animal_name, age=3, health_level=50, happiness_level=50):
        self.animal_name = animal_name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(
            f"{self.animal_name} (Age: {self.age}) - Health: {self.health_level} - Happiness: {self.happiness_level}"
        )
        return self

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self