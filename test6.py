hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

print(hexNumbers['0'] * 256 + hexNumbers['B'] * 16 + hexNumbers['C'])
print(hexNumbers['1'] * 16 + hexNumbers['3'])


##
hexNum = 'ABC'
print(hexNum[0])
print(hexNum[1])
print(hexNum[2])


##

myList = [1,2,3,4]
myList.append(5) #cool append!
print(myList)


##
a = [1,2,3,4,5]
b = a
a.append(6)
print(b)


##
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)


##

for i in range(20):
    print(i)