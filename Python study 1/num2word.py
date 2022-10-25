#To convert number to words
#Firstly install num2words module ie pip install num2words
#then import the module like below

from num2words import num2words

my_no = "123456"
no_words = num2words(my_no)

print(f'123456 in words is {no_words}')
