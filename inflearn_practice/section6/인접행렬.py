#인접행렬

#인접행렬은 뭐... 그냥 입력하면된다...
n, m = map(int, input().split())

p = [([0] * (n+1)) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    p[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(p[i][j], end=' ')
    print()    