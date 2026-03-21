# AI 사용
import sys

a, b, v = map(int, sys.stdin.readline().split())

if v <= a:
    print(1)
else:
    day = (v - a - 1) // (a - b) + 2
    print(day)