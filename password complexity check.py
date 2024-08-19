import re

def check_password_strength(password):
    score = 0
    feedback = ""

    if len(password) > 8:
        score += len(password) - 8

    if re.search(r'[A-Z]', password):
        score += 2

    if re.search(r'[a-z]', password):
        score += 2

    if re.search(r'[0-9]', password):
        score += 2

    if re.search(r'[@$!%*?&#]', password):
        score += 2

    if score <= 3:
        feedback = "Very Weak"
    elif score <= 6:
        feedback = "Weak"
    elif score <= 10:
        feedback = "Strong"
    else:
        feedback = "Very Strong"

    return score, feedback

password = input("Enter a password: ")
score, feedback = check_password_strength(password)
print(f"Password Score: {score}")
print(f"Password Strength: {feedback}")