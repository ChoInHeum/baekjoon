# 알고리즘 분류: 수학, DP, 그리디 알고리즘
import sys
input_value = int(sys.stdin.readline())

answer = -1

for five in range(input_value // 5, -1, -1):
    remain = input_value - (5 * five)

    if remain % 3 == 0:
        three = remain // 3
        answer = five + three
        break

print(answer)