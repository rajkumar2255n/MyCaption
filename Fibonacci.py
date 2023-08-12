num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

fibonacci_sequence = [0, 1]
for i in range(2, num_terms):
    next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
    fibonacci_sequence.append(next_number)

print("Fibonacci sequence:", fibonacci_sequence)
