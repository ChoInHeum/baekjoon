import sys

input_values = [sys.stdin.readline().strip() for _ in range(3)]

number_index = -1

for i, input_value in enumerate(input_values):
    try:
        num = int(input_value)
        number_index = i
        input_values[i] = num
    except ValueError:
        pass

for i, input_value in enumerate(input_values):
    if i == number_index:
        continue

    input_values[i] = input_values[number_index] + (i - number_index)

target_number = input_values[2] + 1

if target_number % 3 == 0:
    if target_number % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif target_number % 5 == 0:
    print("Buzz")
else:
    print(target_number)
    