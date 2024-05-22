import re

def assess_password_strength(password):
    # Criteria weights
    length_weight = 1
    lowercase_weight = 1
    uppercase_weight = 1
    digit_weight = 1
    special_char_weight = 2
    
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += length_weight
        feedback.append("Length is sufficient.")
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check lowercase letters
    if re.search(r'[a-z]', password):
        score += lowercase_weight
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Password should contain lowercase letters.")
    
    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        score += uppercase_weight
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Password should contain uppercase letters.")
    
    # Check digits
    if re.search(r'\d', password):
        score += digit_weight
        feedback.append("Contains digits.")
    else:
        feedback.append("Password should contain digits.")
    
    # Check special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += special_char_weight
        feedback.append("Contains special characters.")
    else:
        feedback.append("Password should contain special characters.")
    
    return score, feedback

def main():
    while True:
        password = input("Enter your password: ")
        score, feedback = assess_password_strength(password)
        
        print("\nPassword Strength Assessment:")
        print("Score:", score)
        print("Feedback:")
        for comment in feedback:
            print("-", comment)
        
        if score >= 8:
            print("\nYour password is strong!")
        elif score >= 5:
            print("\nYour password is moderate. Consider making it stronger.")
        else:
            print("\nYour password is weak. Please choose a stronger password.")
        
        another = input("\nDo you want to assess another password? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
