N=int(input())
k=(2*N)-1
l=0
h=k-1
val=N
matrix=[[0 for i in range(k)] for j in range(k)]
for i in range(N):
    for j in range(l,h+1):
        matrix[i][j]=val
    for j in range(l+1,h+1):
        matrix[j][i]=val
    for j in range(l+1,h+1):
        matrix[h][j]=val
    for j in range(l+1,h+1):
        matrix[j][h]=val
    l+=1
    h-=1
    val-=1
for i in range(k):
    for j in range(k):
        print(matrix[i][j],end=" ")
    print()