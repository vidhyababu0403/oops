class Staff():
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def show(self):
        print(self.name)
        print(self.designation)
vidhya=Staff("swe","asp")
vidhya.show()
class Student(Staff):
    def __init__(self,name,designation,id,dob):
        self.id=id
        self.dob=dob
        Staff.__init__(self,name,designation)
    def view(self):
        print(self.id)
        print(self.dob)
        
a=Student("sin","hod",1098,2003)
a.view()


