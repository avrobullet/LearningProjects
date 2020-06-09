class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    # Set student name
    def __init__(self, firstname, lastname, idnum, scores):
        self.person = Person
        self.scores = scores
        self.person.firstName = firstname
        self.person.lastName = lastname
        self.person.idNumber = idnum
        self.grade = 0

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        for score in self.scores:
            self.grade += score
        self.grade = self.grade/len(scores)

        if 90 <= self.grade <= 100:
            return 'O'
        elif 80 <= self.grade < 90:
            return 'E'
        elif 70 <= self.grade < 90:
            return 'A'
        elif 55 <= self.grade < 70:
            return 'P'
        elif 40 <= self.grade < 55:
            return 'D'
        elif self.grade < 40:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())