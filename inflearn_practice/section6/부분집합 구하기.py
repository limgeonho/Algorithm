#부분집합 구하기(DFS)

#부분집합의 원소로 사용할지 안할지 O, X 선택
def DFS(L):
    if L == n+1:
        for i in range(1, n+1):
            if res[i] == 1:
                print(i, end=' ')
        print()
    else:
        res[L] = 1
        DFS(L+1)   
        res[L] = 0
        DFS(L+1) 

n = int(input())
res = [0] * (n+1)
DFS(1)