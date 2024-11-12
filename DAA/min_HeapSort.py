def Min_Heapify(A,i,n):
    smallest =i
    l = 2*i+1
    r = 2*i+2
    if l<=smallest and A[l]<A[smallest]:
        smallest =l
    if r<=smallest and A[r]<A[smallest]:
        smallest = r
    if smallest != i:
        A[smallest],A[i]=A[i],A[smallest]
        Min_Heapify(A,smallest,n)

def Heap_sort(A):
    n= len(A)-1
    for i in range(n//2,-1,-1):
        Min_Heapify(A,i,n)
    for i in range(n,0,-1):
        A[0],A[i] = A[i],A[0]
        n= n-1
        Min_Heapify(A,0,n)
    return A

if __name__ == "__main__":
    A= list(map(int,input("Entwer the array: ").split()))
    arr = Heap_sort(A)
    print(arr)