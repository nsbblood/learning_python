# Corrected code
fizzbuzz_list = [str(n) if n % 15 != 0 else 'FizzBuzz' if n % 3 == 0 \
                 else 'Fizz' if n % 5 == 0 else str(n) for n in range(1, 101)]

# Print the list
print(fizzbuzz_list)


## use \ to divide the code 