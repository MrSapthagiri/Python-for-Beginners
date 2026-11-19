# Module 14: OOP Fundamentals
# Topic 5: Class variables and multiple objects


class Employee:
    company = "Tech Academy"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1


# Example 1: Create multiple objects.
first_employee = Employee("Asha")
second_employee = Employee("Ravi")
print("Example 1 - Names:",
      first_employee.name, second_employee.name)


# Example 2: Read a class variable through the class.
print("Example 2 - Company:", Employee.company)


# Example 3: Read a class variable through an object.
print("Example 3 - Company:", first_employee.company)


# Example 4: Track how many objects have been created.
print("Example 4 - Employee count:", Employee.employee_count)


# Example 5: Assigning through an object creates an instance attribute.
first_employee.company = "Learning Labs"
print("Example 5 - Object/class company:",
      first_employee.company, Employee.company)


# Example 6: The other object still sees the class variable.
print("Example 6 - Second company:", second_employee.company)


# Example 7: Objects have independent instance variables.
first_employee.name = "Asha K."
print("Example 7 - Names:",
      first_employee.name, second_employee.name)


# Example 8: A mutable class value can be misleading for object data.
class Team:
    members = []

    def __init__(self, name):
        self.name = name

    def add_member(self, member):
        self.members.append(member)


team_one = Team("Alpha")
team_two = Team("Beta")
team_one.add_member("Asha")
print("Example 8 - Shared mutable list:",
      team_one.members, team_two.members)


# Example 9: Prefer instance containers for data that belongs to each object.
class SafeTeam:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)


safe_team_one = SafeTeam("Alpha")
safe_team_two = SafeTeam("Beta")
safe_team_one.add_member("Asha")
print("Example 9 - Separate lists:",
      safe_team_one.members, safe_team_two.members)


# Example 10: Count objects and group their behavior with the class.
class Product:
    tax_rate = 0.18

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self):
        return self.price * (1 + Product.tax_rate)


notebook = Product("Notebook", 100)
print("Example 10 - Total:",
      notebook.name, round(notebook.total_price(), 2))


# Quick review:
# - Class variables are shared by objects unless overridden on an instance.
# - Instance variables belong to one object.
# - Mutable values should usually belong to instances, not to a class.
