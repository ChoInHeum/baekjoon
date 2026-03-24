# 알고리즘 분류: 수학, 구현, 정렬

import sys
from collections import deque

input_count = int(sys.stdin.readline())
dead_number = int((input_count * 0.15) + 0.5)
average = 0

if input_count > 0:
    input_list = [int(sys.stdin.readline()) for _ in range(input_count)]

    input_deque = deque(sorted(input_list))
    for _ in range(dead_number):
        input_deque.popleft()
        input_deque.pop()

    for item in input_deque:
        average += item
    
    average = int((average / len(input_deque)) + 0.5)
    



print(average)


# 예제 입력
# 5
# 1
# 5
# 5
# 7
# 8

# 예제 출력
# 6