# 2026/04/13
# 알고리즘 분류: 누적합

import sys
from collections import deque

def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    index_deque = deque()
    
    for _ in range(M):
        index_deque.append(list(map(int, input().split())))

    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = dp[i-1] + number_list[i-1]

    while index_deque:
        target_index = index_deque.popleft()
        sum = dp[target_index[1]] - dp[target_index[0]-1]

        print(sum)



if __name__ == "__main__":
    main()