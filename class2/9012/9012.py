# AI 사용
# 알고리즘 분류: stack, 문자열
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()
    stack = []
    is_valid = True

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if not stack:
                is_valid = False
                break
            stack.pop()

    if is_valid and not stack:
        print("YES")
    else:
        print("NO")