def print_fibonacci(length):
   
    
    fibonacci_sequence = []
    
    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    print(fibonacci_sequence)


