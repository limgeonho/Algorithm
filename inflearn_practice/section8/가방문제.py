#가방문제(냅색 알고리즘)

# 중요한 알고리즘(냅색) - 꼭 기억!!
# 하나씩 정보를 입력받는다.
# 한 가지를 선택했다고 하고 해당 물건의 가치를 추가한다.
# 같은 과정을 반복하면서 새로운 값들로 최신화한다.
n, m = map(int, input().split())
dy = [0] * (m+1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m+1):
        dy[j] = max(dy[j], dy[j - w] + v)

print(dy[m])