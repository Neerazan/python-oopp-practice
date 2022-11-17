
'''
Class methods work with class variables and are accessible using the class name rather than its object.
Since all class objects share the class variables, class methods are used to access and modify class variables.
'''
class player:
    teamName = 'Barcelona'

    # def __init__(self,name):
    #     self.name = name

    @classmethod
    def getTeamName(cls): #use can use any other namine insted of self.
        return cls.teamName

print(player.getTeamName())


# class Student:
#     studentName = 'Shristi'
#
#     def __int__(self,name):
#         self.name = name
#
#     def getStudentName(self):
#         return self.studentName
#
# print(Student.getStudentName())