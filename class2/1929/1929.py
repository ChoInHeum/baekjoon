# 알고리즘 분류: 소수 판정
# AI 사용

import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n + 1):
    if i < 2: continue
    if i == 2 or i == 3:
        print(i)
        continue
    if i % 2 == 0 or i % 3 == 0:
        continue

    is_prime = True
    for j in range(5, int(i**0.5) + 1, 6):
        if i % j == 0 or i % (j + 2) == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i)