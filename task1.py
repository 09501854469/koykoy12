def grade(grades):
    if grades >= 90 and grades <= 100:
        return "Exellent! You did a grate job !"
    elif grades >= 80 and grades <= 89:
        return "Good job! keep i tup!"
    elif grades >= 70 and grades <= 79:
        return "You passed, but there's room for improvement"
    elif grades <= 70:
        return " You field. better luck next time."
    else:
        return "invalid grades"
    

user = int(input("Enter A Grades :"))
print(grade(user)) 



