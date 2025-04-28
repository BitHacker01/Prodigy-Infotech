import re

def check_password_complexity(password):
    criteria = {
        "Length >= 8": len(password) >= 8,
        "Contains uppercase letter": bool(re.search(r'[A-Z]', password)),
        "Contains lowercase letter": bool(re.search(r'[a-z]', password)),
        "Contains digit": bool(re.search(r'\d', password)),
        "Contains symbol": bool(re.search(r'[^\w\s]', password)),
        "No common words": not re.search(r'password|123456|qwerty', password, re.IGNORECASE),
    }

    score = sum(criteria.values())

    for c, met in criteria.items():
        print(f"{c}: {'✓' if met else 'X'}")

    print(f"\nPassword complexity score: {score}/6")
    print(
        "Password is very strong." if score == 6 else
        "Password is strong." if score >= 4 else
        "Password is weak." if score >= 2 else
        "Password is very weak."
    )

password = input("Enter a password to check its complexity: ")
check_password_complexity(password)
