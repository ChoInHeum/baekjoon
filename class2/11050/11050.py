import sys

n, k = map(int, sys.stdin.readline().split())

def factorial (number: int):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(int(factorial(n) / (factorial(k) * factorial(n - k))))