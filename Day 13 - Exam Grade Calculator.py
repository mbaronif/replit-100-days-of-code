print("Exam Grade Calculator")
print()
name_of_exam = input("Name of exam: ")
max_score = float(input("Max. Possible Score: "))
your_score = float(input("Your score: "))
print()
percentage = round(your_score / max_score * 100, 2)
if percentage >= 90:
  print("You got", percentage, "% which is an A+")
elif percentage >= 80 and percentage < 90:
  print("You got", percentage, "% which is a A")
elif percentage >= 70 and percentage < 80:
  print("You got", percentage, "% which is a B")
elif percentage >= 60 and percentage < 70:
  print("You got", percentage, "% which is a C")
elif percentage >= 50 and percentage < 60:
  print("You got", percentage, "% which is a D")
else:
  print("You got", percentage, "% which is an U")
