# 알고리즘 분류: stack
import sys

input_count = int(sys.stdin.readline())

stack = []
result = []

for _ in range(input_count):
    command = sys.stdin.readline().split()
    
    match command[0]:
        case 'push':
            stack.append(int(command[1]))
        case 'top':
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
        case 'size':
            result.append(len(stack))
        case 'empty':
            result.append(1 if not stack else 0)
        case 'pop':
            result.append(-1 if not stack else stack.pop())


print(*result, sep='\n')
        
