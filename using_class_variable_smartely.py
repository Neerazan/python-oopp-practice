class Player:
    teamname = "Barcelona"
    teammember =[]

    def __init__(self,name):
        self.name = name
        self.formerTeam = []
        self.teammember.append(self.name)
    
p1 = Player("Frankie")
p2 = Player("Raphinia")

print("Name:", p1.name)
print("Team Members:")
print(p1.teammember)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teammember)