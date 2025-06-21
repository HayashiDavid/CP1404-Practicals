COLOURS_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Amethyst": "#9966cc",
    "Aquamarine2": "#76eec6",
    "BlueViolet":"#8a2be2",
    "Baby Blue":"#89cff0",
    "Beige":"#f5f5dc",
    "Boysenberry":"#873260",
    "Brandeis Blue": "#0070ff",
    "Brass": "#b5a642",
    "BrickRed":"#cb4154"}

def main():
    """Validate colour name and print corresponding message"""
    colour_name = validate_colour_name()
    while colour_name != "":
        colour_code = COLOURS_TO_CODE[colour_name]
        print(f"{colour_code}")
        colour_name = validate_colour_name()

def validate_colour_name():
    """Check if the input is one of the colour names"""
    colour_name = input("Colour Name: ").title()
    while colour_name not in COLOURS_TO_CODE:
        print("Invalid Colour Name")
        colour_name = input("Colour Name: ").title()
    return colour_name