import re

def assess_password_strength(password):
    feed = []

    if len(password) < 8:
        feed.append("Password should be at least 8 characters.")
    else:
        feed.append("Length is sufficient.")

    if not re.search(r'[A-Z]', password):
        feed.append("Password should contain at least one uppercase letter.")
    else:
        feed.append("Contains uppercase letters.")

    if not re.search(r'[a-z]', password):
        feed.append("Password should contain at least one lowercase letter.")
    else:
        feed.append("Contains lowercase letters.")

    if not re.search(r'[0-9]', password):
        feed.append("Password should contain at least one number.")
    else:
        feed.append("Contains numbers.")

    if not re.search(r'[^a-zA-Z0-9]', password):
        feed.append("Password should contain at least one special character (e.g., @, #, $, %, etc.).")
    else:
        feed.append("Contains special characters.")

    negative_feedback_count = sum(1 for message in feed if "should" in message)
    if negative_feedback_count == 0:
        strength = "Strong"
    elif negative_feedback_count <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    feed.append(f"Password strength: {strength}")
    return feed

password = input("Enter your password to assess its strength: ")
feedback = assess_password_strength(password)
for message in feedback:
    print(message)
