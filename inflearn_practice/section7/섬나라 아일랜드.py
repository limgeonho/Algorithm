#섬나라 아일랜드

# 8방향을 기본으로 세팅 하고 나머지는 단지번호 붙이기와 동일
# 처음 섬시작부분을 찾고 이후부터 BFS탐색
from collections import deque

dx = [-1, 0, 1, 0, -1, 1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]
n = int(input())

board = [list(map(int, input().split()))for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt+=1

print(cnt)

