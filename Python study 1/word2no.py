#To conver word to word i.e thirty to 30

#pip install word2number

from word2number import w2n

my_word = "one two three four"

conv_word = w2n.word_to_num(my_word)

print(str(conv_word))
