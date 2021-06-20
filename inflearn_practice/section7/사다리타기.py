#사다리타기

# 격자판 문제는 대부분 위에서 시작했지만 이번에는 반대로 아래에서 올라옴
# (O, X)문제와 비슷하게 세 방향 중 하나를 선택...
def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y) 

board = [list(map(int, input().split())) for _ in range(10)]

ch =[[0] * 10 for _ in range(10)]

for i in range(10):
    if board[9][i] == 2:
        DFS(9, i)
