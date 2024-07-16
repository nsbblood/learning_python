from decimal import Decimal, getcontext

# Setting the precision to 5 decimal places
getcontext().prec = 5

a = Decimal('1.23456789')
b = Decimal('2.34567891')

# Performing arithmetic operations with decimal numbers
result = a * b
print(result)  # Output: 2.8965 (rounded to 5 decimal places)


#*
# Setting the precision to 2 decimal places
getcontext().prec = 2

a = Decimal('1.23456789')
b = Decimal('2.34567891')

result = a / b
print(result)  # Output: 0.53 (rounded to 2 decimal places)

# Setting the precision to 6 decimal places
getcontext().prec = 6

result = a / b
print(result)  # Output: 0.526316 (rounded to 6 decimal places)



#The decimal module is used in Python to perform precise mathematical operations
#with decimal numbers. 

#This module is widely used in financial and scientific calculations
#because it offers higher precision compared to the float type.