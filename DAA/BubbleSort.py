arr = list(map(int,input("Enter the array: ").split()))
n=len(arr)
count =0
for i in range(n-1):
  for j in range(n-i-1):
    count+=1
    if(arr[j]>arr[j+1]):
      temp = arr[j]
      arr[j]=arr[j+1]
      arr[j+1]=temp
print(arr)
print("The number of comparison is: ",count)