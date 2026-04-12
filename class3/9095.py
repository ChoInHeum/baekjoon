# 2026/04/12
# 알고리즘 분류: dp

import sys

def main():
    input = sys.stdin.readline

    test_case = int(input())
    n_list = [int(input()) for _ in range(test_case)]

    dp = [0] * 11

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    for n in n_list:
        print(dp[n])

if __name__ == "__main__":
    main()