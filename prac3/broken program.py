"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def old_program():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")


def main():
    score = get_score()
    display_grade(score)


def get_score():
    score = float(input("enter score: "))
    return score


def display_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")

main()
