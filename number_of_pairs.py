#   Solution to:
#   https://practice.geeksforgeeks.org/problems/number-of-pairs/0/

#   Works but is too slow
def solve(Nx,Ny,X,Y):
    X.sort()
    Y.sort()
    pairs=0
    for ix in range(Nx):
        for iy in range(Ny):
            if X[ix]==0:
                break
            elif Y[iy]==0:
                pairs+=1
            elif X[ix]==1:
                break
            elif Y[iy]==1:
                pairs+=1
            elif X[ix]==2:
                if Y[iy]>4:
                    pairs+=Ny-iy
                    break
            elif X[ix]==3 and Y[iy]==2:
                pairs+=1
            elif X[ix]<Y[iy]:
                pairs+=Ny-iy
                break
    print(pairs)

#   Faster working solution. Saves the number of 0s and 1s as well as the last 
#   relevant index. This allows the next cycle to start from the previous index
#   and not from 0 again.
def solve2(Nx,Ny,X,Y):
    X.sort()
    Y.sort()
    pairs=0
    iy1=0 # number of 0s and 1s in Y if they exist
    iyNext=0 # index to start searching in Y
    for ix in range(Nx):
        pairs+=iy1
        for iy in range(iyNext,Ny):
            if X[ix]==0:
                break
            elif Y[iy]==0:
                pairs+=1
                iy1+=1
                iyNext+=1
            elif X[ix]==1:
                break
            elif Y[iy]==1:
                pairs+=1
                iy1+=1
                iyNext+=1
            elif X[ix]==2:
                if Y[iy]>4:
                    pairs+=Ny-iy
                    break
            elif X[ix]==3 and Y[iy]==2:
                pairs+=1
            elif X[ix]<Y[iy]:
                pairs+=Ny-iy
                if X[ix]>3:# If X is not >3, start counting from the 2s again
                    iyNext=iy
                break
    print(pairs)

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        Nx,Ny=map(int,input().split())
        X=[int(x) for x in input().split()]
        Y=[int(x) for x in input().split()]
        solve2(Nx,Ny,X,Y)

