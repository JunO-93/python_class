class Employee:
    def __init__(self,name='',dailywage=0,weekly=0):
        self.name = name
        self.dailywage = dailywage
        self.weekly = weekly
    def calculateSalary(self):
        return print("Weeklywage :",self.dailywage * self.weekly)
        

emp1 = Employee('Zara',200,5)
emp1.calculateSalary()
print('Name :',emp1.name,',Dailywage :',emp1.dailywage,',weekly :',emp1.weekly)


