def letter_grade(score):
    if score >= 90:
        return "A"
    if 80 <= score < 90:
        return "B"
    if 70 <= score < 80:
        return "C"
    if 60 <= score < 70:
        return "D"
    if 0 <= score < 60:
        return "F"
        
        
print(letter_grade(77))
print(letter_grade(70))
print(letter_grade(94))
print(letter_grade(86))
print(letter_grade(64))
print(letter_grade(98))