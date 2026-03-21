import sys

input_count = int(sys.stdin.readline())

input_list = [[int(x[0]), x[1], i] for i, x in enumerate(sys.stdin.readline().split() for _ in range(input_count))]

sorted_list = sorted(input_list, key=lambda x: (x[0], x[2]))

for i in range(input_count):
    print(*(sorted_list[i][0], sorted_list[i][1]))