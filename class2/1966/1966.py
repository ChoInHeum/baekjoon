# 알고리즘 분류: 구현, 자료 구조, 시뮬레이션, 큐

import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())
count = 0
result = []

while count < test_case:
    doc_count, doc_target_index = map(int, sys.stdin.readline().rstrip().split())
    doc_list = list(map(int, sys.stdin.readline().rstrip().split()))

    que = deque(doc_list)
    print_doc_count = 0

    while que:
        max_doc = max(que)
        cur_doc = que.popleft()

        if cur_doc < max_doc:
            if doc_target_index == 0:
                doc_target_index = len(que)
                que.append(cur_doc)
            else:
                que.append(cur_doc)
                doc_target_index -= 1
        else:
            if doc_target_index == 0:
                result.append(print_doc_count + 1)
                break
            else:
                print_doc_count += 1
                doc_target_index -= 1

    count += 1
    
print(*result, sep='\n')

# ==================== AI 최적화 코드 ==================== #
import sys
from collections import deque

# 1. for문을 사용하여 테스트 케이스 반복
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    # rstrip() 생략 가능
    doc_count, doc_target_index = map(int, sys.stdin.readline().split())
    doc_list = list(map(int, sys.stdin.readline().split()))

    # 2. enumerate를 사용하여 (초기 인덱스, 중요도) 형태로 큐에 저장
    # 예: [(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)]
    que = deque([(i, val) for i, val in enumerate(doc_list)])
    print_doc_count = 0

    while que:
        # 튜플 안의 '중요도(x[1])'를 기준으로 최댓값을 찾음
        max_doc_val = max(que, key=lambda x: x[1])[1]
        cur_doc = que.popleft()

        # 현재 문서의 중요도가 최댓값보다 작으면 뒤로 보냄
        if cur_doc[1] < max_doc_val:
            que.append(cur_doc)
        else:
            # 최댓값이면 출력 (카운트 증가)
            print_doc_count += 1
            
            # 3. 방금 출력한 문서의 원래 인덱스가 우리가 찾는 인덱스라면 종료
            if cur_doc[0] == doc_target_index:
                print(print_doc_count)
                break