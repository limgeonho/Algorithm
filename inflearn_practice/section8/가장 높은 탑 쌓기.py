#가장 높은 탑 쌓기

# LIS 문제와 거의 비슷함.
# + 대신 bricks[]에 벽돌의 정보를 담아서 필요한 정보만 빼서 사용
n = int(input())
bricks = []

for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True)

dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])
print(res)