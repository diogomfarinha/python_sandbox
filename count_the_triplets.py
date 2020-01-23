#   Solution to:
#   https://practice.geeksforgeeks.org/problems/count-the-triplets/0

def solve(N,A):
    A.sort()
    triplets = 0
    max_A = A[-1]
    set_A = set(A)
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            current_sum=A[i]+A[j]
            if current_sum<=max_A:#time optimization
                if current_sum in set_A:
                    triplets+=1
            else:
                break
    print(triplets if triplets>0 else -1)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=[int(x) for x in input().split()]
        solve(N,A)
