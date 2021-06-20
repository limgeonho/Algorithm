#안전영역

# 단지번호 붙이기와 섬나라 아일랜드와 다르게 제공되는 격자판을 수정하면 안된다.
# 따라서, ch[][]을 매번 초기화 해준다(h가 달라질 때마다)
# 그리고 전체 DFS탐색 + 4방향 탐색, (O, X)아님
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)

n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
cnt = 0
res = 0
for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and board[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    res = max(res, cnt)
    if cnt == 0:
        break
print(res)
