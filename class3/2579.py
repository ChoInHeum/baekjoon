# 알고리즘 분류: DP (다이나믹 프로그래밍)

import sys
input = sys.stdin.readline

def main():
    input_number = int(input())
    input_list = [0] + [int(input()) for _ in range(input_number)]

    dp = [0] * (input_number + 1)

    if input_number == 1:
        dp[1] = input_list[1]
    elif input_number == 2:
        dp[2] = input_list[1] + input_list[2]
    else:
        dp[1] = input_list[1]
        dp[2] = input_list[1] + input_list[2]

    for i in range(3, input_number + 1):
        dp[i] = max(dp[i-2] + input_list[i], dp[i-3] + input_list[i-1] + input_list[i])

    print(dp[input_number])

if __name__ == "__main__":
    main()