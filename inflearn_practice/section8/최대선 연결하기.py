#최대 선 연결하기

# 앞에 나온 LIS 문제와 동일하다...
n = int(input())
arr = [0] + list(map(int, input().split()))
dy = [0] * (n+1)
dy[1] = 1
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res: 
        res = dy[i]
print(res)