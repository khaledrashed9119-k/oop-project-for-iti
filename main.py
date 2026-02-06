from classes import Car, Employee, Office

my_car = Car("Fiat", 50)
emp1 = Employee("Ahmed", 1000, 7, 3, 10, my_car, 5000)
my_office = Office("Smart Steps Co.")
my_office.hire(emp1)
print("Current Mood:", emp1.mood)
emp1.work(10)
print("Mood after work:", emp1.mood)
my_office.reduce_salary(10, 500)
print("New Salary:", emp1.salary)
