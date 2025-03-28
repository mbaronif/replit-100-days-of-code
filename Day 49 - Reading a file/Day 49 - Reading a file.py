f = open("high.score", "r") # Open the file in read mode

scoreList = [] # Create an empty list to store the scores

while True:
    fileLine = f.readline() # Read the file line by line
    if not fileLine: # If the file is empty, end of file
        break
    highScore = fileLine.strip().split() # Remove the newline character and split the line into a list
    
    if len(highScore) > 1: # If the length of the list is greater than 1, then it is a valid line
        name = highScore[0]
        score = int(highScore[1])

        scoreList.append((name, score)) # Append the second element to the scoreList

print(scoreList)
print("The highest score is: ", max(scoreList)) # Print the highest score
    

f.close() # Close the file



