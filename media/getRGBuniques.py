'''
Small utility for generating a set of unique RGB values in the
world map. This list is used for keys in a lookup table.
'''

from PIL import Image

'''
Mode to generate the table in. Can be one of:
    'rgb-to-biome'      :   Convert RGB values into biome room types.
'''

# Mapping of modes to various needed things for said mode
IMAGE_FILE = 0

# Set mode
mode = 'rgb-to-biome'

modes = {
    'rgb-to-biome'      :   (   'biomeRGBhA.png',       # Biome (RGB) and height (A) image
                            ),
}

in_image = Image.open(modes[mode][IMAGE_FILE])
inRGB = in_image.load()

RGBvals = []

for y in range(in_image.size[1]):
    for x in range(in_image.size[0]):
        # Scan image pixels
        rgb = (inRGB[x,y][0], inRGB[x,y][1], inRGB[x,y][2])
        if not rgb in RGBvals:
            RGBvals.append(rgb)


def RGBtoColorCode(rgb):
    # Evennia color codes are RGB digits from 0-5, so 6 digits
    # per component. 255 / 6 = 42.5, so to convert from RGB we
    # divide by 42.5 and subtract 1 (because codes start at zero).
    # Round the result and use the integer that results.
    
    r = max(0, int(round(float(rgb[0]) / 42.5 - 1.0)))
    g = max(0, int(round(float(rgb[1]) / 42.5 - 1.0)))
    b = max(0, int(round(float(rgb[2]) / 42.5 - 1.0)))
    
    s = '|' + str(r) + str(g) + str(b)
    
    return s

### TODO The code below is rgb->biome specific, need more generalized rewrite
s = ''
tupleAlign = '\t\t\t\t\t\t'
for rgb in RGBvals:
    colorCode = "'" + RGBtoColorCode(rgb) + "'"
    # Default representation character is U+2592, which is "medium shade" (177) in ANSI
    s += str(rgb) + "\t\t:\t(\n"            + tupleAlign + \
                    "'\\u0a20',\n"           + tupleAlign + \
                    "'\\xb1',\n"             + tupleAlign + \
                    colorCode + ",\n"       + tupleAlign + \
                    "WildBiomeDefault,\n"   + tupleAlign + \
                    "),\n"

with open('rgbUniquesOutput.txt', 'w') as f:
        f.write(s)
