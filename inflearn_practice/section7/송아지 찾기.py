#송아지 찾기

#기본적인 queue를 이용한 BFS문제 + 중복 확인!
from collections import deque

s, e = map(int, input().split())

ch = [0] * 10001
dis = [0] * 10001

ch[s] = 1
dis[s] = 0
queue = deque()
queue.append(s)
while queue:
    now = queue.popleft()
    if now == m:
        break
    for next in (now-1, now+1, now+5):
        if 1 <= next <= 10001:
            if ch[next] == 0:
                ch[next] = 1
                queue.append(next)
                dis[next] = dis[now] +1 

print(dis[e])
