#   Solution to:
#   https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

def solve(N,A):
    current_max=A[0]
    final_max=A[0]
    for i in range(1,N):
        current_max=max(A[i],current_max+A[i])
        final_max=max(final_max,current_max)
    print(final_max)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=[int(x) for x in input().split()]
        solve(N,A)
