a=1000
def display():
        b=20
        return a+b

class Employee():
    comp_name="sathya"
    @staticmethod
    def displayCompInfo():
        print(Employee.comp_name)

    def assign(self,id,name,sal=0.0):
        self.idno=id
        self.name=name
        self.salary=sal

    def display(self):
        print(self.idno,self.name)
        print(self.salary)

#e1=Employee()
#e1.assign(101,"Ravi")
#e1.display()
#e2=Emloyee()
#e2.assign(103,"krirt")
#e2.display()

