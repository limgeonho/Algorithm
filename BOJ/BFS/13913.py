from collections import deque
n, m=map(int, input().split())
Q=deque()
MAX=100000
dis=[0]*MAX
ch=[0]*MAX
ans=[]
Q.append(n)
ch[n]=1
dis[n]=0
while Q:
    now=Q.popleft()
    if now==m:
        break
    for next in(now+1, now-1, 2*now):
        if 0<=n<=MAX:
            if ch[next]==0:
                Q.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])
for i in range(MAX):
    if ch[i]==1:
        print(i, end=' ')