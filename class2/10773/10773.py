#

import sys

input_count = int(sys.stdin.readline())
stack = []

for _ in range(input_count):
    int_line = int(sys.stdin.readline())

    if int_line != 0:
        stack.append(int_line)
    else:
        stack.pop()

sum = 0

for item in stack:
    sum += item

print(sum)