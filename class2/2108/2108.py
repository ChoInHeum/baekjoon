import sys
from collections import Counter 

input_count = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline()) for _ in range(input_count)]

input_list.sort()
count = Counter(input_list)

max_freq = max(count.values())
modes = [num for num, freq in count.items() if freq == max_freq]

modes.sort()

print(round(sum(input_list) / len(input_list)))

print(input_list[len(input_list) // 2])

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(input_list[-1] - input_list[0])