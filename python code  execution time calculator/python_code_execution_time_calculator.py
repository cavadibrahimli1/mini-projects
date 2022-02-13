from time import time
start = time()

#Acronyms maker
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution sime : ", execution_time)

