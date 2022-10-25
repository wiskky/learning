# Python Program to find the L.C.M. of two input number
...
def lcm(a, x):

   # choose the greater number
   if a > x:
       greater = a
   else:
       greater = x

   while(True):
       if((greater % a == 0) and (greater % x == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

a = 84
X = 56

print("The L.C.M. is", lcm(a, x))
'''
'''
for values in range(10):
    print(values)
'''
for values in range(3,10):
    print(velues)
