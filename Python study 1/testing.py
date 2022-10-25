import tkinter as tk

"""

form = tk.Tk()
form.title("My first form")

mylabel = tk.Label(form, text="This is a Label", width=25,
                   height=5, bg="red")
mylabel2 = tk.Label(form, text="This is a Label", width=25,
                   height=5, bg="blue")
mylabel3 = tk.Label(form, text="This is a Label", width=25,
                   height=5, bg="red")
mylabel4 = tk.Label(form, text="This is a Label", width=25,
                   height=5, bg="yellow")

mylabel.pack()
mylabel2.pack()
mylabel3.pack()
mylabel4.pack()


form.mainloop()

#This is only for comment " ''' "

'''''
short_list = [1, 2, 3]
while True:
    value = input('Position [q or Q to quite]?')
    if value == 'q' or value == 'Q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)

    except Exception as other:
        print('Something else broke:', other)
'''''

'''
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayemployee(self):
        print("Name : ", self.name, "  Salary : ", self.salary)


result1 = Employee("Wisdom", 2000)
result2 = Employee("Adeniyi", 18000)
result3 = Employee("Eric", 5000)
result4 = Employee("Sarah", 2500)

Employee.displaycount(1)
result1.displayemployee()
result2.displayemployee()
result3.displayemployee()
result4.displayemployee()



"""

#print("Welcome to the git class")
'''
a = 11
b = 12
c = a + b
d = c / 2
print (f"The division of {c} and 2 is {d}")
print("The sum of the two number is: ", c)
print(f"The sum of {a} and {b} is {c}")
'''
'''
#Program to sum the positive integer 1+2+3+4+.....+n
n = 10
sum = 0
i = 1

while (i <= n):
    sum = sum + i
    i = i + 1
    
print("The sum is : ", sum)

'''
'''
#Using else statement with while loop

counter = 0

while counter < 3:
  print ("Inside loop")
  counter = counter + 1
  
else:
  Print("inside else") 
  
#New If statement is added.

numbber = 5

if numbber > 0:
    print("Number is positive")
print("This is always executed.")
'''
#This programe takes input from the user and calculate the sum \
#untilthe user enters a negative number.

sum = 0

while True: #boolean expression is True
    n = input("Enter a number: ")
    n = float(n) #convertig to float
    
    if n < 0: #check if number is negative
        break
    sum += n

print("sum = ", sum)


