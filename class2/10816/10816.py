# 알고리즘 분류: 정렬, 이분 탐색, 집합과 맵, 해시를 사용한 집합과 맵

import sys
from collections import Counter

input_count = int(sys.stdin.readline())
input_list = sys.stdin.readline().split()
count_dict = Counter(input_list)

input_count1 = int(sys.stdin.readline())
input_list1 = sys.stdin.readline().strip().split()

result = [count_dict[item] for item in input_list1]

print(*result)