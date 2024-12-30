import re

def evaluate_password_strength(password):
    """
    Evaluates the strength of a password based on length, 
    uppercase, lowercase, digits, and special characters.

    Args:
        password (str): The password to evaluate.

    Returns:
        str: A message indicating the password strength.
    """
    # Initialize strength score
    strength_score = 0

    # Check length
    if len(password) >= 8:
        strength_score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1

    # Check for digits
    if re.search(r'\d', password):
        strength_score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1

    # Determine password strength based on score
    if strength_score == 5:
        return "Password strength: Strong"
    elif 3 <= strength_score < 5:
        return "Password strength: Moderate"
    else:
        return "Password strength: Weak"

# Example usage
password = input("Enter your password: ")
print(evaluate_password_strength(password))
