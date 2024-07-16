import math

def addNumbers(i):
    if i == 0:
        return 0
    return i + addNumbers(i - 1)
    
print(addNumbers(10))


## Another way for it...

def addNumbersIterative(i):
  total = 0
  for num in range(1, i + 1):
    total += num
    print(total)
  return total

print(addNumbersIterative(10))

## Don't forget to import math!! 
print(math.factorial(11))

## Another way - recursive function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
    
print(factorial(5))


