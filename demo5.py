#calling instance variable and method
# from Employee class (static)
from sample import Employee
e1=Employee()
e1.assign(101,"ravi")
e1.display()

e2=Employee()
e2.assign(102,"kumar",185000.00)
e2.display()
Employee.displayCompInfo()