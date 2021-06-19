#등산경로

# 처음 격자판에서 시작점과 마지막점을 구해놓고 DFS탐색을 하면된다
# 미로탐색문제와 같은 4방향 선택문제, (O, X)아님
# 격자판 탐색문제는 ch[]를 통해 왔던 길을 표시하고 돌아갈때는 다시 풀어준다 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt+=1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<n and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0

n = int(input())
board = [[0] * n for _ in range(n)]
ch = [[0] * n for _ in range(n)]
max = -2147000000
min = 2147000000
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]
ch[sx][sy] = 1
cnt = 0
DFS(sx, sy)
print(cnt)
