value = 50

def reverse(n):
    if n == 0:
        print("Done!")
        # Stops the recursion whan it reaches 1
        return 1
    else:
        # Multiplies the current number to the result of the recursive call
        return n * reverse(n - 1)

# Displays the total factorial once recursion finishes        
result = reverse(value)
print(f"The factorial of {value} is {result}")