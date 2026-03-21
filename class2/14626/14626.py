# AI 사용
import sys

raw_data = sys.stdin.readline().strip()
number_list = [int(x) if x != '*' else '*' for x in raw_data]

star_index = 0
total = 0

for i in range(len(number_list)):
    if number_list[i] == '*':
        star_index = i
        continue

    if i % 2 == 0:
        total += number_list[i] * 1
    else:
        total += number_list[i] * 3

for x in range(10):
    if star_index % 2 == 0:
        if (total + x) % 10 == 0:
            print(x)
            break
    else:
        if (total + x * 3) % 10 == 0:
            print(x)
            break