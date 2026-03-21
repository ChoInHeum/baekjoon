import sys

input = int(sys.stdin.readline())

number = 666

count = 1

while True:
    if input == 1:
        print(number)
        break
    
    if '666' in str(number):
        if (count == input):
            print(number)
            break
        else:
            count += 1

    number += 1
    

# 알고리즘 분류: 브루트포스 알고리즘