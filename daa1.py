def fibonacci_iterative(n):
    if n < 1:
        return
    prev1, prev2 = 0, 1
    print(prev1, end=" ")
    if n > 1:
        print(prev2, end=" ")
    for i in range(2, n):
        result = prev1 + prev2
        print(result, end=" ")
        prev1, prev2 = prev2, result
    print()

# Main function
n = int(input("Enter the number of terms: "))
print("Iterative Fibonacci sequence:", end=" ")
fibonacci_iterative(n)
