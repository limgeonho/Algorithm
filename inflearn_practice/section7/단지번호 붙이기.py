#단지번호 붙이기

# 격자판에서 4방향 이동을 하면서 큐에 추가하고 삭제하며 BFS탐색
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

board = [list(map(int, input()))for _ in range(7)]
cnt = 0
res = []
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y] == 0:
                        continue
                    board[x][y] = 0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)