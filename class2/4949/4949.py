# AI 사용
# 알고리즘 분류: stack, 문자열, 
import sys

results = []

while True:
    input = sys.stdin.readline().rstrip()

    if input == '.':
        break

    stack = []
    is_valid = True

    for ch in input:
        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            stack.pop()
        
        elif ch == ']':
            if not stack or stack[-1] != '[':
                is_valid = False
                break
            stack.pop() 

    if is_valid and not stack:
        results.append("yes")
    else:
        results.append("no")

for result in results:
    print(result)