import time
n = int(input("How many terms of Fibonacci you want: "))    
def f_dc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f_dc(n-1) + f_dc(n-2)
print("\nDivide and Conquer: ")
for i in range(n):
    print(f_dc(i),end='')

def f_dp(A,n):
    if n == 0:
        A[0] = 0
    elif n == 1:
        A[1] = 1
    else:
        A[n] = A[n-1] + A[n-2]
    return A[n]

print("\nDynamic Programming:--")
A = [0 for i in range(n+1)] 
for i in range(n):
    print(f_dp(A,i),end='')
print("\n")
# Measure execution time for Divide and Conquer
# Example Fibonacci term (you can adjust this value)
start_time = time.time()
result_dc = f_dc(n)
end_time = time.time()
time_dc = end_time - start_time
print(f"Divide and Conquer: Fibonacci({n}) = {result_dc}, Time Taken = {time_dc:.6f} seconds")

# Measure execution time for Dynamic Programming
start_time = time.time()
result_dp = f_dp(A,n)
end_time = time.time()
time_dp = end_time - start_time
print(f"Dynamic Programming: Fibonacci({n}) = {result_dp}, Time Taken = {time_dp:.6f} seconds")
