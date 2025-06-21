"""
Emails
Estimate: 45 Minutes
Actual:
"""

def main():
    email_to_name = {}

    email = validate_email()



def process_name(email):
    """Determine user email and username"""
    name = email.split()
    name_parts = name.split('.')
    name_parts = [part.title() for part in name_parts]
    name = '.'.join(name_parts)
    return name


def validate_email():
    """ Check if the email is valid or not"""
    email = input("Email: ")
    if email == "":
        return email
    while '@' not in email:
        print("This is not a valid email, try again!")
        email = input("Email: ")
    return email
