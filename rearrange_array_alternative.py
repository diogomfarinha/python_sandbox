#   Solution to:
#   https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/

def solve(N,A):
    s=[]
    for i in range(0,int(N/2)):
        s.append(A[N-1-i])
        s.append(A[i])
    if N%2!=0:
        s.append(A[N-int(N/2)-1])
    print(*s)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=input().split()
        for i in range(N):#Code is longer than usual to save memory
            A[i] = int(A[i])
        solve(N,A)
        