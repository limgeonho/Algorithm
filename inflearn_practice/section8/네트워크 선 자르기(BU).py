#네트워크 선 자르기(bottom-up)

# bottom - up 방법: 직관적으로 바로 구할 수 있는 값은 미리 설정한다
# + dy[] => 메모이제이션을 위한 리스트 생성
n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
