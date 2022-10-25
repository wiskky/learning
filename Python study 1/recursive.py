# This is recursive example in python
# Recursive is the function that call itself 
#To calcaute the sum of the positive integer

def calc_num(n):
    if n == 1:
        return 1
    else:
        return n + calc_num(n - 1)
#calling the function
sum = calc_num(3)
print(sum)

