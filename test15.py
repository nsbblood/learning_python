def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
print(performOperation(2, 3, 'sum'))

##

def function1(varA, varB):
    message = 'Some local data'
    print(varA)
    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')
        
    inner_function(123, 456)
    

print(function1(1, 2)) 

##

text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
'''

print(text)