#동전교환

# 가방문제와 비슷
# coin[]안에 동전의 종류를 밀 입력받음.
# 입력받은 동전을 하나씩 꺼내서 선택했을 경우의 가치를 최신화(누적)함.
n = int(input())
coin = list(map(int, input().split()))
m = int(input())

dy = [1000] * (m+1)
dy[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        dy[j] = min(dy[j], dy[j - coin[i]] + 1)

print(dy[m])
