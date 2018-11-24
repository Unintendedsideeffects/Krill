import colorsys

def convertRGBtoHLS(red, green, blue):
    rgb = [red, green, blue]
    red, green, blue = [x/255.0 for x in rgb]
    return colorsys.rgb_to_hls(red, green, blue)



#You have to start checking if the color is even in bounds

