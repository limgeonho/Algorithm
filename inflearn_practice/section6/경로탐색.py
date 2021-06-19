#경로탐색

#선택형 DFS이고 ch[]를 이용해서 중복된 선택을 피한다.
def DFS(v):
    global cnt, path
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0
n, m = map(int, input().split())


g = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

cnt = 0
path = list()
ch[1] = 1
DFS(1)
print(cnt)