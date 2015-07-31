class Employee:
	"Common base Class for all employees"
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ", self.salary

emp1 = Employee("meena",3000)
emp2 = Employee("Tesst",5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 25

hasattr(emp1, 'age')
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
