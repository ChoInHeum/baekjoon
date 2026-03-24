import sys

# 1. 보드 크기 입력 및 전체 보드 저장
N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]

repair_counts = []

# 2. 8x8로 자를 수 있는 모든 시작점 (i, j) 탐색
for i in range(N - 7):
    for j in range(M - 7):
        draw_W = 0 # 'W'로 시작하는 판으로 만들 때 칠해야 하는 개수
        draw_B = 0 # 'B'로 시작하는 판으로 만들 때 칠해야 하는 개수

        # 3. 시작점부터 8x8 구역 검사
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                # r + c가 짝수면 시작점 색과 같아야 하고, 홀수면 달라야 함
                if (r + c) % 2 == 0:
                    if board[r][c] != 'W':
                        draw_W += 1
                    if board[r][c] != 'B':
                        draw_B += 1
                else:
                    if board[r][c] != 'B':
                        draw_W += 1
                    if board[r][c] != 'W':
                        draw_B += 1
        
        # 현재 8x8 구역에서 발생한 두 패턴의 최솟값을 리스트에 추가
        repair_counts.append(draw_W)
        repair_counts.append(draw_B)

# 4. 모든 경우의 수 중 가장 작은 값 출력
print(min(repair_counts))