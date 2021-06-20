#최대 부분 증가수열

# 자주 사용하는 수열(LIS)
# 초기값을 세팅 + dy[]메모이제이션 활용
# 해당 되는 수의 이전에 있는 수들을 조회해서 작은지 판단하고 작다고 판단된 수들 중 가장 긴 배열 = max
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
    dy[i] = max +1 
    if res < dy[i]:
        res = dy[i]
print(res)