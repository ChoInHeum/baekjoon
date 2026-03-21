# 풀이 참고
import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    floor = int(sys.stdin.readline())
    index = int(sys.stdin.readline())
    f0 = [x for x in range(1, index + 1)]
    for k in range(floor):
        for i in range(1, index):
            f0[i] += f0[i-1]
    print(f0[-1])