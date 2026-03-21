# AI 사용
import sys

word_count = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(word_count)]

word_list = sorted(set(word_list), key=lambda x: (len(x), x))

for i in range(len(word_list)):
    print(word_list[i])