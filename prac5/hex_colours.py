HEX_COLOURS = {"antiqueWhite": "#faeabd7", "aquamarine": "#7fffd4", "azure": "#f0ffff", "bisque": "#ffe4c4",
               "black": "#000000", "white": "#ffffff", "red": "#ff0000", "yellow": "#ffff00", "blue": "#0000ff",
               "gold": "#ffd700"}

colour = input("Enter a colour: ").lower()
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").lower()
