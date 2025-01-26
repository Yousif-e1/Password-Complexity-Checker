# Password-Complexity-Checker
- This program is a Password Complexity Checker that evaluates the strength of a password based on specific criteria, including:

1 Length (minimum 8 characters)
2 Presence of uppercase and lowercase letters
3 Inclusion of numbers
4 Use of special characters
5 It provides feedback on each aspect of the password and rates its overall strength as Strong, Moderate, or Weak. This tool helps users create more secure passwords by identifying areas for improvement.

# How it Work
1 Password Input:
- The program prompts the user to enter a password using the input() function.
- The entered password is passed to the assess_password_strength() function for evaluation.
2 Password Evaluation:
- The program checks the password against five criteria:
- Length: At least 8 characters.
- Uppercase Letters: Must contain at least one uppercase letter.
- Lowercase Letters: Must contain at least one lowercase letter.
- Numbers: Must contain at least one numeric digit.
- Special Characters: Must contain at least one special character (e.g., @, #, $, %).
3 Feedback Generation:
- For each criterion, the program appends appropriate feedback to a list (feed).
- If the password meets the criterion, it appends a positive message (e.g., "Contains numbers").
- Otherwise, it appends constructive feedback (e.g., "Password should contain at least one number.").
4 Password Strength Assessment:
- The program counts how many criteria the password fails to meet using the phrase "should" in the feedback messages.
- Based on the number of failed criteria:
- 0 Failures: Password is Strong.
- 1–2 Failures: Password is Moderate.
- 3 or More Failures: Password is Weak.
5 Final Output:
- The program appends the overall password strength to the feedback list.
- It prints all feedback messages, including both the individual evaluations and the overall strength assessment.
  
