# 알고리즘 분류
import sys

N, M = map(int, sys.stdin.readline().split())

l_set = set([sys.stdin.readline().rstrip() for _ in range(N)])
s_set = set([sys.stdin.readline().rstrip() for _ in range(M)])
result = []

for name in l_set:
    if name in s_set:
        result.append(name)

result.sort()

print(len(result))
print(*result, sep='\n')