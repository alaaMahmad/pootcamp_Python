from lion import Lion
from tiger import Tiger
from monkey import Monkey

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
        print(f"{self.zoo_name} Unique Attributes")
        for animal in self.animals:
            animal.unique_attribute()
        return self


zoo1 = Zoo("Alaa's Zoo")
zoo1.add_lion("Leo").add_tiger("Shadow").add_monkey("Coco")
zoo1.print_all_info()
print()
zoo1.print_all_unique_attribute()