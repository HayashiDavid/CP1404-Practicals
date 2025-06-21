"""
Emails
Estimate: 45 Minutes
Actual:
"""

def main():
    email_to_name = {}

    email = validate_email()





def validate_email():
    """ Check if the email is valid or not"""
    email = input("Email: ")
    if email == "":
        return email
    while '@' not in email:
        print("This is not a valid email, try again!")
        email = input("Email: ")
    return email
