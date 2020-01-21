#   Solution to:
#   https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0/

from collections import defaultdict

#scalable solution using a dictionary, works for any array with many different numbers
def solve(N,A):
    dic = defaultdict(int)
    for index in range(N):
        dic[A[index]]+=1
    keys=list(dic.keys())
    keys.sort()
    result=[]
    for key in keys:
        result+=dic[key]*[key]
    print(*result)
        
#duch national flag solution
def solve2(N,A):
    result=[]
    middle=0
    for index in range(N):
        if A[index]==0:
            result.insert(0,0)
            middle+=1
        elif A[index]==1:
            result.insert(middle,1)
            middle+=1
        else:
            result.append(2)
    print(*result)

if __name__=='__main__':
    T = int(input())
    for i in range(T):
       N = int(input())
       A = [int(x) for x in input().split()]
       solve2(N, A)