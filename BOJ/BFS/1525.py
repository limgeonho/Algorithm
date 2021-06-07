from collections import deque

def bfs():
    q=deque()
    q.append(aa)

    visited[aa]=0
    while q:
        v=q.popleft()
        if v=='123456789':
            return visited[v]
        
        s=str(v)
        target=s.find('9')
        tx=target//3
        ty=target%3

        for i in range(4):
            x=dx[i]+tx
            y=dy[i]+ty
            if 0<=x<3 and 0<=y<3:
                t=x*3+y
                ts=list(s)
                ts[target], ts[t] = ts[t], ts[target]
                ti=int(''.join(ts))
                if not visited.get(ti):
                    visited[ti]=visited[v]+1
                    q.append(ti)
    return -1






dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited=dict()
aa=''
for i in range(3):
    a=input()
    a=a.replace(' ','')
    aa+=a
aa=int(aa.replace('0', '9'))
print(bfs())