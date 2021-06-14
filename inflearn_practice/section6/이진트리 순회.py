#이진트리 순회

#print()의 위치에 따라 전위, 중위, 후위 순회
# 전위순회 : 부 - 왼 - 오
# 중위순회 : 왼 - 부 - 오
# 전위순회 : 왼 - 오 - 부

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(v*2)
        DFS(v*2 +1)

DFS(1)