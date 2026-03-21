import sys

input_count = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

input_count1 = int(sys.stdin.readline())
input_list1 = list(map(int, sys.stdin.readline().split()))

input_list_set = set(input_list)

print('\n'.join(str(1 if x in input_list_set else 0) for x in input_list1))