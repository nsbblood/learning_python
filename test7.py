mySet = set(('a', 'b', 'c'))
print(mySet)


##
mySet.add('d')
print(mySet)


##
animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}
print(animals)
print(animals['a'])
print(animals.keys())
animals.update({'d': 'bison'})
print(animals)


##
names = {
    'a': 'alien',
    'b': 'bear',
    'c': 'cat',
    'd': [],   # If you want to use append to add new items to the list then take care!
}
print(names)
names['d'].append('Dino')
print(names)


