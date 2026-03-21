import sys

input_count = int(sys.stdin.readline())

input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(input_count)]

sorted_list = sorted(input_list, key=lambda x: (x[1], x[0]))

print('\n'.join(f"{x[0]} {x[1]}" for x in sorted_list))