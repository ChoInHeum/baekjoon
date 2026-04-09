# 알고리즘 분류: 그리디 알고리즘, 정렬

import sys

N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

input_list.sort()

sum = 0
for i in range(len(input_list)):
    for j in range(len(input_list)):
        if j <= i:
            sum += input_list[j]
        else:
            break

print(sum)