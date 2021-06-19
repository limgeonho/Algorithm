#미로탐색

# DFS를 활용해서 격자판을 지나갈 때마다 1로 바꿔주고 뒤로갈때 다시 0으로 만들어준다
# 4가지 방향 중 하나를 선택해서 이동함, (O, X)문제 아님
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt+=1

    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0

board = [list(map(int, input().split()))for _ in range(7)]
cnt = 0
board[0][0] = 1
DFS(0, 0)
print(cnt)