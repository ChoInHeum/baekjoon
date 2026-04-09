# 알고리즘 분류: 구현, 집합과 맵, 비트마스킹

import sys

M = int(sys.stdin.readline())
my_set = set()

for _ in range(M):
    line = sys.stdin.readline().split()
    cmd = line[0]
    
    if cmd == 'all':
        my_set = set(range(1, 21))
    elif cmd == 'empty':
        my_set.clear()
        
    else:
        num = int(line[1])
        
        match cmd:
            case 'add':
                my_set.add(num)
            case 'remove':
                my_set.discard(num)
            case 'check':
                if num in my_set:
                    print("1")
                else:
                    print("0")
            case 'toggle':
                if num in my_set:
                    my_set.discard(num)
                else:
                    my_set.add(num)