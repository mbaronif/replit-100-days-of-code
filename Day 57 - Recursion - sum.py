value = 50

def recursive_sum(n):
    if n == 1:
        print("Done!")
        # Stops the recursion whan it reaches 1
        return 1    
    else:
        # Adds the current number to the result of the recursive call
        return n + recursive_sum(n - 1)
    
# Displays the total sum once recursion finishes
result = recursive_sum(value)
print(f"The sum of all numbers, starting with {value}, is {result}")

