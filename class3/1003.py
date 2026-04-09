# 알고리즘 분류: DP (다이나믹 프로그래밍)

import sys

# 기존 코드
result = [0, 0]

def fibonacci (n: int):
    if n == 0:
        result[0] += 1
        return 0
    elif n == 1:
        result[1] += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


test_case = int(sys.stdin.readline())

input_args = [int(sys.stdin.readline()) for _ in range(test_case)]

for i in input_args:
    result = [0, 0]
    fibonacci(i)
    print(*result)

# 시간 단축을 위해 AI를 사용함
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())

    count_0 = 1
    count_1 = 0

    for _ in range(n):
        count_0, count_1 = count_1, count_0 + count_1

    print(count_0, count_1)