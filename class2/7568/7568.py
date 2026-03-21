# 알고리즘 분류: 수학
import sys

input_count = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(input_count)]

for i in range(input_count):
    rank = 1
    for j in range(input_count):
        # 중복 제거
        if i == j: continue

        if input_list[i][0] < input_list[j][0] and input_list[i][1] < input_list[j][1]:
            rank += 1
    input_list[i].append(rank)


print(*(input_list[x][2] for x in range(input_count)))