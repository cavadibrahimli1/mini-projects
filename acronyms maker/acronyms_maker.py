
word = input('Write the word you want to create acronym. -  ')
text = word.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)
