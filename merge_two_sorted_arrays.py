#   Solution to:
#   https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/

def solve(N1,N2,A1,A2):
   A=A1+A2
   A.sort()
   print(*A)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N1,N2=map(int,input().split())
        A1=[int(x) for x in input().split()]
        A2=[int(x) for x in input().split()]
        solve(N1,N2,A1,A2)



