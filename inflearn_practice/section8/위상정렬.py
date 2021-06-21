#위상정렬(그래프 정렬)

# 전체 일의 순서를 짜는 프로그램
# 그래프와 진입차수 리스트를 모두 만들어야함
# 그래프 노드의 진입차수를 저장
# 진입차수가 가장 적은 노드부터 큐에 넣고 돌린다.
# 큐에서 뽑은 노드가 연결하고 있는 다른 노드의 진입차수를 -1 한다.
# 반복한다...

from collections import deque

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1)

Q = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b]+=1

for i in range(1, n+1):
    if degree[i] == 0:
        Q.append(i)

while Q:
    x = Q.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                Q.append(i)