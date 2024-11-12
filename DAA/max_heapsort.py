def Max_heapify(A,i,n):
    largest =i
    l=2*i+1
    r=2*i+2
    if l<=n and A[l]>A[largest]:
        largest =l
    if r<=n and A[r]>A[largest]:
        largest = r
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        Max_heapify(A,largest,n)
def Heap_sort(A):
    n=len(A)-1
    for i in range(n//2,-1,-1):
        Max_heapify(A,i,n)
    for i in range(n,0,-1):
        A[0] ,A[i]= A[i],A[0]
        n=n-1
        Max_heapify(A,0,n)
    return A
if __name__ == "__main__":
    A= list(map(int,input("Entwer the array: ").split()))
    arr = Heap_sort(A)
    print(arr)