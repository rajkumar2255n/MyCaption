def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n < 0:
        raise ValueError("Please enter a non-negative integer.")
    
    result = fibonacci(n)
    print(f"The first {n} Fibonacci numbers are:")
    print(result)
except ValueError as e:
    print(e)
