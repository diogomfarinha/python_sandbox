#   Solution to:
#   https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

#Works but is too slow...   
def solve(N,S,A):
    for i in range(N):
        for j in range(i+1,N+1):
            s=sum(A[i:j])
            if s==S:
                print(i+1,j)
                return
            elif s>S:
                break
    else: 
        print('-1')
        
#Works but is also too slow...   
def solve2(N,S,A):
    for start in range(N):
        sum=0
        end=start
        while(end<N and sum<S):
            sum+=A[end]
            end+=1
        if sum==S:
            print(start+1,end)
            return
    else: 
        print('-1')

#Works with complexity O(n)
def solve3(N,S,A):
    begin,end,sum = 0,0,0
    while True:
        if sum>S and begin<N:
            sum-=A[begin]
            begin+=1
        elif sum<S and end<N:
            sum+=A[end]
            end+=1
        elif sum==S:
            print(begin+1,end)
            return
        else:
            print(-1)
            return
            
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
       N,S = map(int, input().split())
       A = list(map(int, input().split()))
       solve3(N, S, A)