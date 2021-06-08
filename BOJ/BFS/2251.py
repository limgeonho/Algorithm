from collections import deque

moves = list(zip([0,0,1,1,2,2], [1,2,0,2,0,1]))
check = [[False] * 201 for _ in range(201)]
ans = [False] * 201
cup = list(map(int, input().split()))
sum = cup[2]

Q = deque()
Q.append((0, 0))
check[0][0] = True
ans[cup[2]] = True

while Q:
    now = Q.popleft()
    cur = [now[0], now[1], sum - now[0] - now[1]]
    for f, t in moves:
        next = cur[:]
        next[t] += next[f]
        next[f] = 0
        if next[t] >= cup[t]:
            next[f] = next[t] - cup[t]
            next[t] = cup[t]
        if not check[next[0]][next[1]]:
            check[next[0]][next[1]] = True
            Q.append((next[0], next[1]))
            if next[0] == 0:
                ans[next[2]] = True

for i in range(0, cup[2]+1):
    if ans[i]:
        print(i, end=' ')
print()

