# 인공지능 사요

import sys

n = int(sys.stdin.readline())

stack = []
answer = []
flag = True
current_num = 1

for _ in range(n):
    target = int(sys.stdin.readline())
    
    while current_num <= target:
        stack.append(current_num)
        answer.append('+')
        current_num += 1
        
    if stack[-1] == target:
        stack.pop()
        answer.append('-')
        
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in answer:
        print(i)