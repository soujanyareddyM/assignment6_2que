class Dog:
    def _init_(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

class JackRussellTerrier(Dog):
    def _init_(self, name, age, coat_color, favorite_toy):
        super()._init_(name, age, coat_color)
        self.favorite_toy = favorite_toy

    def play_fetch(self):
        print(f"{self.name} loves to play fetch with their favorite toy, a {self.favorite_toy}.")

    def hunt_rodents(self):
        print(f"{self.name} is a skilled rodent hunter.")

class Bulldog(Dog):
    def _init_(self, name, age, coat_color, weight):
        super()._init_(name, age, coat_color)
        self.weight = weight

    def snore_loudly(self):
        print(f"{self.name} is known to snore loudly.")

    def display_weight(self):
        print(f"{self.name} weighs {self.weight} pounds.")

# Creating objects
dog1 = JackRussellTerrier("Rufus", 3, "white and brown", "tennis ball")
dog2 = Bulldog("Maggie", 5, "brown", 50)

# Calling methods
dog1.description()
dog1.get_info()
dog1.play_fetch()
dog1.hunt_rodents()

dog2.description()
dog2.get_info()
dog2.snore_loudly()
dog2.display_weight()