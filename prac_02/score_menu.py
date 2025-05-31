MENU = "(G)et valid score between 0 and 100\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_score(score)}")
        elif choice == "S":
            stars = show_stars(score)
            print(stars)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell my friend. See you next time")

def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a valid score (0- 100): ")
        score = float(input("Enter a valid score (0-100): "))
    return score

def determine_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    return "*" * int(score)

main()