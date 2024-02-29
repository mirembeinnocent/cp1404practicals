COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

while True:
    color_name = input("Enter a color name: ").upper()
    if not color_name:
        break
    try:
        print(f"The hexadecimal code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name")
