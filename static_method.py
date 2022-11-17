'''
Static methods are methods that are usually limited to class only and not their objects.
 They have no direct relation to class variables or instance variables. They are used as
  utility functions inside the class or when we do not want the inherited classes to modify
   a method definition.
'''

class Player:
    teamName = "Barcelona"

    # def __init__(self, name):
    #     self.name = name

    @staticmethod
    def demo():
        print("I am a static method")

p1 = Player()
p1.demo()
Player.demo()