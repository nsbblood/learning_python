import math

myList = [1,2]
if bool(myList):
    print('Mylist has some values in it!')


weatherIsNice = True
haveUmbrella = False

if (not haveUmbrella) and (not weatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')



weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print('Go for a walk')
else:
    print('Stay inside')


##

print('My number is: '+str(5))
print(f'My number is: {5}')


print(f'Pi is: {math.pi:.2f}')

