import sys

def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

input_value = int(sys.stdin.readline())

factorial_num = factorial(input_value)
zero_count = 0

while True:
    mod_num = factorial_num % 10
    factorial_num //= 10

    if mod_num == 0:
        zero_count += 1
    else:
        break

print(zero_count)