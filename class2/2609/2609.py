import sys

input_value1, input_value2 = map(int, sys.stdin.readline().split())
GCD, LCM = 0, 0

if (input_value2 > input_value1):
    temp = input_value2
    input_value2 = input_value1
    input_value1 = temp

a, b = input_value1, input_value2

while True:
    if (a % b == 0):
        GCD = b
        break

    temp = a % b
    a = b
    b = temp

LCM = int(input_value1 * input_value2 / GCD)

print(GCD)
print(LCM)

