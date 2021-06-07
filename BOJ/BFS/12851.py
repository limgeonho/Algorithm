from collections import deque
MAX = 200000
check = [False]*MAX
dist = [0]*MAX
cnt = [0]*MAX
n,m = map(int,input().split())
check[n] = True
dist[n] = 0
cnt[n] = 1
q = deque()
q.append(n)
while q:
    now = q.popleft()
    for next in [now-1, now+1, now*2]:
        if 0 <= next < MAX:
            if not check[next]:
                q.append(next)
                check[next] = True
                dist[next] = dist[now]+1
                cnt[next] = cnt[now]
            elif dist[next] == dist[now]+1:
                cnt[next] += cnt[now]
print(dist[m])
print(cnt[m])
