# 알고리즘 분류: 큐

import sys
from collections import deque

input_count = int(sys.stdin.readline())

que = deque()
result = []

for _ in range(input_count):
    command = sys.stdin.readline().split()

    match command[0]:
        case 'push':
            que.append(int(command[1]))
        case 'front':
            result.append(-1 if not que else que[0])
        case 'back':
            result.append(-1 if not que else que[-1])
        case 'size':
            result.append(len(que))
        case 'empty':
            result.append(1 if not que else 0)
        case 'pop':
            result.append(-1 if not que else que.popleft())

print(*result, sep='\n')