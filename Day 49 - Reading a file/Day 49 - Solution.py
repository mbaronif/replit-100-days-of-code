f = open("high.score", "r")

scores = f.read().split("\n")
f.close()

highScore = 0
name = None

for rows in scores:
    data = rows.split()
    print(data)
    if data != []:
        if int(data[1]) > highScore:
            highScore = int(data[1])
            name = data[0]

print("The highest score is: ", name, "with: ", highScore)