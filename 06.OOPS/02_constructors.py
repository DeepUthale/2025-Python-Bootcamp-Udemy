class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def print_info(self):
        print(f"The Name of the Employee is {self.name}. Salary is {self.salary} and Bond is for {self.bond} years.")

e1 = Employee(34000, "Jane Doe", 4)
print(e1.get_salary())
e1.print_info()
