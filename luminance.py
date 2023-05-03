from math import sqrt

def luminance(pixel, option=1, output_as_int=True):

    # https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color

    if output_as_int:
        if option == 1:
            return int(0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2])
        elif option == 2:
            return int(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])
        elif option == 3:
            return int(sqrt(0.241*pixel[0]**2 + 0.691*pixel[1]**2 + 0.068*pixel[2]**2))
    else:
        if option == 1:
            return 0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2]
        elif option == 2:
            return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]
        elif option == 3:
            return sqrt(0.241*pixel[0]**2 + 0.691*pixel[1]**2 + 0.068*pixel[2]**2)