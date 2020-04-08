#   Solution to:
#   https://practice.geeksforgeeks.org/problems/equilibrium-point/0

#Iterate from both left and right until the iterators match
def solve(N,A):
    i=0
    left=0
    j=N-1
    right=0
    while i!=j:
        if left<=right:
            left+=A[i]
            i+=1
        else:
            right+=A[j]
            j-=1
    if left==right and i==j:
        print(i+1)
    else:
        print(-1)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=[int(x) for x in input().split()]
        solve(N,A)
        
solve(5,[1,3,5,2,2])
