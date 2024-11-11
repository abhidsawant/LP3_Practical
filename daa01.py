def print_fibonacci_recursive(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    print_fibonacci_recursive(n - 1, b, a + b)

# Main function
n = int(input("Enter the number of terms: "))
print("Recursive Fibonacci sequence:", end=" ")
print_fibonacci_recursive(n)
print()  # For a newline after the sequence
