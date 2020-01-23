#   Solution to:
#   https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

# Solution for both sorted and unsorted arrays.
# Alternatively, ideal_sum could just use the formula N*(N+1)/2 
# instead of looping.
def solve(N,A):
    actual_sum=0
    ideal_sum=N#alternatively, could just use the formula n*(n+1)/2
    for i in range(0,N-1):
        actual_sum+=A[i]#sums the numbers in array
        ideal_sum+=i+1#sums the numbers that were suposed to be in array
    print(ideal_sum-actual_sum)
    
# Easier solution, but only works for sorted arrays
def solve2(N,A):
    for i in range(0,N-1):
        if i+1!=A[i]:
            print(i+1)
            break
    else:
        print(N)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=[int(x) for x in input().split()]
        solve(N,A)
