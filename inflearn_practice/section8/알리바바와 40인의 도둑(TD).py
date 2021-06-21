#알리바바와 40인의 도둑(top - down)

# top - down 방법: 구하고자 했던 수부터 거꾸로 처음 시작수까지 내려온다.
# 메모이제이션과 재귀함수 활용
# 나머지 방법은 동일함...
def DFS(x, y):
    if dy[x][y]  > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]

n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
dy = [[0] * n for _ in range(n)]
print(DFS(n-1, n-1))
