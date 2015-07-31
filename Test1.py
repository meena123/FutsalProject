
class Test1:
     'Common base class for all employees'
     empCount = 0


     def __init__(self, name, salary):
         self.name = name
         self.salary = salary
         Test1.empCount += 1
     
     def displayCount(self):
        print "Total Employee %d" % Test1.empCount
 
     def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ",self.salary

     "This would create first object of Employee class"
     emp1 = Test1("Zara", 2000)
     "This would create second object of Employee class"
     emp2 = Test1("Manni", 5000)

    
