import time;
import calendar

print("hello");
if True:
	print("true");
else:
	print("false");

num = 78;
a = "test";
print(num);
print(a);

str ="Hello World";
print(str[2:5]);
print str *2
print str + " test"

list = ['abcd', 787 , 2.23 , 'John' , 70.2]
tinylist = [134,'John']
print list
print tinylist
print list + tinylist
var =100
if (var == 100):
     print var
else:
     print("False")

print "My name is %s and my weight is %d kg!" %('meena',43)
ticks = time.time();
print ticks;

localtime = time.localtime(time.time())
print "Local Current Time :",localtime

ltime = time.asctime(time.localtime(time.time()))
print ltime;

cal = calendar.month(2013,9)
print "Here is the Calendar:"
print cal;

def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme("I'm first call to user defined function!");




def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist




def printinfo( name, age ):
     print "Name", name;
     print "Age", age;
     return;


printinfo( age = 26 , name = "meena");



str1 = raw_input("Enter your name: ");

print "Received input is : ",str1
