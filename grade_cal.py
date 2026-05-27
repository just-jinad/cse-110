"""
Author: Tope Jinad

Purpose: Determine and display letter grades, including +/-.
"""

grade = float(input("Enter your grade: "))

if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
    if grade % 10 >= 7:
        letter_grade += "+"
    elif grade % 10 < 3:
        letter_grade += "-"
elif grade >= 70:
    letter_grade = "C"
    if grade % 10 >= 7:
        letter_grade += "+"
    elif grade % 10 < 3:
        letter_grade += "-"
elif grade >= 60:
    letter_grade = "D"
    if grade % 10 >= 7:
        letter_grade += "+"
    elif grade % 10 < 3:
        letter_grade += "-"
else:
    letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")

if grade >= 70:
    print("You passed the course.")
else:
    print("You did not pass the course.")