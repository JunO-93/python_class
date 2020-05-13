class Employee:
    empCount =0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    def dispalyCount(self):
        print("Total Employee ",Employee.empCount)
    def displayEmployee(self):
        print("Name :",self.name, ", Salary: ",self.salary)