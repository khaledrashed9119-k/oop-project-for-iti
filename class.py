class Person:
    def __init__(self, name, money, hours, meals):
        self.name = name
        self.money = money
        self.mood = self.get_mood(hours)
        self.health = self.get_health(meals)
    
    def get_mood(self, hours):
        if hours == 7:
            return "happy"
        elif hours > 7:
            return "lazy"
        else:
            return "tired"
    
    def get_health(self, meals):
        if meals == 3:
            return "100%"
        elif meals == 2:
            return "75%"
        else:
            return "50%"


class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
    
    def drive(self, distance):
        needed = distance * 0.25
        
        if self.fuel >= needed:
            self.fuel -= needed
            print("Car is moving...")
        else:
            print("No fuel!")


class Employee(Person):
    def __init__(self, name, money, hours, meals, emp_id, car, salary):
        super().__init__(name, money, hours, meals)
        self.emp_id = emp_id
        self.car = car
        self.salary = salary
    
    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        else:
            self.mood = "tired"


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def hire(self, employee):
        self.employees.append(employee)
        print(employee.name + " joined " + self.name)
    
    def reduce_salary(self, emp_id, amount):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.salary -= amount
                print("Salary reduced for " + emp.name)
