class Student:
    college = 'biyani college'
    
    def printInfo(self):
        print('Full name of student is {}'.format(self.name))
        print('Roll number is {}'.format(self.roll_no))
        print('cgpa is {}'.format(self.cgpa))
        print('college is {}'.format(self.college))

gaurav = Student()
gaurav.name = "Gaurav kamble"
gaurav.roll_no = 12
gaurav.address = 'Bhandara'
gaurav.cgpa = 8
#gaurav.college = 'ram meghe'

gaurav.printInfo()

tanu = Student()
tanu.name = 'tanu sahu'
tanu.roll_no=1
tanu.cgpa = 8.5
tanu.printInfo()