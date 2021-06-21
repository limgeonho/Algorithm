#플로이드 워샬 알고리즘

# 그래프의 노드 간 최단 거리를 구하는 알고리즘
# 노드끼리 직접연결 or 다른 노드를 거쳐서 가는 길 중 최단 거리로 최신화 시킴
n, m = map(int, input().split())
dis = [[5000] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): 
    dis[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c

# 플로이드 워샬 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == 5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()