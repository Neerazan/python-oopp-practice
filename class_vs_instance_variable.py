class Player:
    teamName = "Barcelona" # class variable
    def __init__(self,name):
        self.name = name       # instance variable

p1 = Player("Pedri")
p2 = Player("Gavi")

print("Name: ", p1.name)
print("Team Name: ", p1.teamName)
print("Name: ", p2.name)
print("Team Name: ", p2.teamName)