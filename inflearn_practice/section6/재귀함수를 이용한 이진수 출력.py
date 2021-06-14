#재귀함수를 이용한 이진수 출력

def DFS(x):
  #종료조건!!
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

n=int(input())
DFS(n)


