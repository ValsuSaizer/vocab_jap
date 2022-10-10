from datetime import date
from copy import deepcopy
from random import random

class Student:
    def __init__( self, lastname, firstname, birth, admin_number, courses_list=[] ):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.admin_number = admin_number
        self.courses_list = deepcopy( courses_list )
    def __repr__( self ):
        age = date.today() - self.birth
        return "{} {}".format( self.lastname, self.firstname )
    def enroll( self, course ):
        if course not in self.courses_list:
            self.courses_list.append( course.name )
    def age( self ):
        today = date.today()
        years = today.year - self.birth.year
        if today.month < self.birth.month or \
            ( today.month == self.birth.month and \
            today.day < self.birth.day ):
            years -= 1
        return years

class Course:
    def __init__( self, name, number ):
        self.name = name
        self.number = number
    def __repr__( self ):
        return "{}: {}".format( self.number, self.name )

students=[ Student( "DESCORMES", "Pierre", date( 1995, 8, 6 ), 348919 ),
Student( "DURAND", "Albert", date( 1975, 2, 15 ), 34361 ),
Student( "DUPONT", "Tintin", date( 1997, 4, 23 ), 341519 ) ]

courses=[ Course( "Math", 5 ), Course( "Sports", 1 ), Course( "French", 9 ),
Course( "Physics", 4 ), Course( "Science", 6 ), Course( "English", 7 ),
Course( "Philosophy", 2 ) ]

for student in students:
    for course in courses:
        if random() > 0.3:
            student.enroll( course )

for student in students:
    print( str( student.admin_number ) + ":", student.lastname, student.firstname )
    if len( student.courses_list ) == 0:
        print( "\tNo courses" )
    for course in student.courses_list:
        print( "\t" + course )
