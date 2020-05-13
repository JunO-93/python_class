class Employee:
    def __init__(self,name='',salary=0):
        self.name = name
        self.salary = salary        

emp1 = Employee('Zara',2000)
print('Name :',emp1.name,',Salary :',emp1.salary)

emp2 = Employee('Manni',5000)
print('Name :',emp2.name,',Salary :',emp2.salary)
