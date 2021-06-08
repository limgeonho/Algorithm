#숨바꼭질4
from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    Q = deque()
    Q.append(N)
    while Q:
        tmp = Q.popleft()
        if tmp == K:
            print(dist[tmp])
            path(tmp)
            return tmp
        for i in (tmp+1, tmp-1, tmp*2):
            if 0<= i < 100000 and dist[i] == 0:
                Q.append(i)
                dist[i] = dist[tmp] + 1
                move[i] = tmp 

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
bfs()