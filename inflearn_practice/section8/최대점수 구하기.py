#최대점수 구하기

# 가방문제와 동일함
# 하지만, dy[]의 마지막부터 탐색(속도 증가)
n, m = map(int, input().split())

dy = [0] * (m+1)

for _ in range(n):
    p, t = map(int, input().split())
    for j in range(m, t-1, -1):
        dy[j] = max(dy[j], dy[j - t] + p)

print(dy[m])