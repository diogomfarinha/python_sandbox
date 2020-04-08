#   Solution to:
#   https://practice.geeksforgeeks.org/problems/inversion-of-array/0/

#Merge sort 
def merge_sort_count(array):
    if len(array)==1:
        return array,0
    left,count_left=merge_sort_count(array[:len(array)//2])
    right,count_right=merge_sort_count(array[len(array)//2:])
    count=count_left+count_right
    sort=[]
    i=j=0
    while(i<len(left) or j<len(right)):
        if i==len(left):#left array has been sorted
            sort+=right[j:len(right)]
            j=len(right)
        elif j==len(right):#right array has been sorted
            sort+=left[i:len(left)]
            i=len(left)
        elif left[i]<=right[j]:#left array element is smaller than right array element 
            sort.append(left[i])
            i+=1
        else:#right array element is bigger than left array element
            sort.append(right[j])
            j+=1
            count+=len(left)-i
    return sort,count

def solve(_,A):
    _,inversions=merge_sort_count(A)
    print(inversions)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=[int(x) for x in input().split()]
        solve(N,A)
