# 알고리즘 분류: 큐
import sys
from collections import deque

circle_que = deque(range(1, int(sys.stdin.readline().strip()) + 1))

while len(circle_que) > 1:
    circle_que.popleft()
    circle_que.append(circle_que.popleft())

print(*circle_que)