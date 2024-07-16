import time

myVar = 44

if type(myVar) == int:
    print('myVar is an integer!')
if type(myVar) != int:
    print('myVar is NOT an integer!')

#...

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    print(str(i) + '. step total ' + str(s))
    time.sleep(1)

print('Total' + str(s)) 

#When you output int and string at the same time then you should be careful
#use str()... to convert int value to string
#In Python, you can't directly concatenate (add) strings and integers. 
#The + operator expects operands of the same type for addition.