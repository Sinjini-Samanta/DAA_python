def Merged_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr) // 2
  left_half = Merged_sort(arr[:mid])
  right_half = Merged_sort(arr[mid:])
  return merge(left_half,right_half)
def merge(left,right):
  merged = []
  i=j=0
  while(i<len(left) and j<len(right)):
    if left[i]<right[j]:
      merged.append(left[i])
      i+=1
    else:
      merged.append(right[j])
      j+=1
  while i<len(left):
    merged.append(left[i])
    i+=1
  while j<len(right):
    merged.append(right[j])
    j+=1
  return merged
  
if __name__ == "__main__":
  arr = list(map(int, input("Enter the array: ").split()))
  sorted_array = Merged_sort(arr)
  print("The sorted array is: ",sorted_array) 