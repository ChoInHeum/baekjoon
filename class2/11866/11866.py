# 알고리즘 분류: 큐

import sys

N, K = map(int, sys.stdin.readline().split())

number_list = [x for x in range(1, N + 1)]
result_list = []



pop_index = 0
for _ in range(N):
    pop_index = (pop_index + (K - 1)) % len(number_list)
    result_list.append(number_list.pop(pop_index))

print(f"<{', '.join(map(str, result_list))}>")


# 예제 입력
# 7 3

# 예제 출력
# <3, 6, 2, 7, 5, 1, 4>

# ==================== AI 풀이 (큐 사용) ==================== #
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([x for x in range(1, N + 1)])
result_list = []

while queue:
    for _ in range(K - 1):
        front_person = queue.popleft()
        queue.append(front_person)
    
    target_person = queue.popleft()
    result_list.append(target_person)


print(f"<{', '.join(map(str, result_list))}>")
