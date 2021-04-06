class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammal.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.bird.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammal)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fish)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.bird)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())


for i in range(count):
    spec, animal = input().split()
    zoo.add_animal(spec, animal)

info = input()
print(zoo.get_info(info))
