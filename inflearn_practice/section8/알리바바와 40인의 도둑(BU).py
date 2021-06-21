#알리바바와 40인의 도둑(bottom - up)

# 직관적으로 알 수 있는 초기값을 세팅한다.
# 맨 윗줄, 맨 왼쪽줄을 바로 세팅한다.
# 위, 왼쪽 중 작은 값을 선택한다...
# 단계적으로 생각하기...dp니까

n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

dy = [[0] * (n) for _ in range(n)]

dy[0][0] = arr[0][0]
for i in range(1, n):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0]
for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
print(dy[n-1][n-1])