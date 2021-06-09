import os
import enum
import numpy as np
import scipy.ndimage
from PIL import Image

class Color():
    def __init__(self, name, rgb):
        self.name = name
        self.rgb = rgb

    def __str__(self):
        return f"{self.name} = {self.rgb}"

class Colors(enum.Enum):
    RED = Color("red", (246, 0, 0))
    ORANGE = Color("orange", (255, 165, 0))
    YELLOW = Color("yellow", (255, 255, 0))
    GREEN = Color("green", (0, 217, 0))
    BLUE = Color("blue", (0, 0, 179))
    WHITE = Color("white", (255, 255, 255))

    @staticmethod
    def values():
        return list(map(lambda col: col.value, Colors))

class CubeNumberEntryException(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Must have at least 4 rubiks cubes! Only {self.num} were provided."

def get_dimensions(l, w, r):
    if r < 4:
        raise CubeNumberEntryException(r)
    image_ratio = l / w
    rectangles = [(1, r)]
    for i in range(r):
        y = r/(i+1)
        if r-2 > i > 0 and y - int(y) == 0:
            x, y = i+1, int(y)
            rectangles.append(((x, y), abs(image_ratio - (x/y))))
    rectangles.append((r, 1))
    closest = min(rectangles, key=lambda rectangle: rectangle[1])
    return tuple([d*3 for d in closest[0]]), closest[0]

def prepare_image(path, n_cubes):
    img = Image.open(path)
    width, length = img.size
    new_dimensions, subregion_dimensions = get_dimensions(width, length, n_cubes)
    img = img.resize(new_dimensions).convert("RGB")
    width, length = img.size
    pixel_num, counter = width*length, 0
    pixels = img.load()
    print("Opened Image.")
    for x in range(width):
        for y in range(length):
            pixel, diffs = pixels[x, y], []
            for color_obj in Colors.values():
                color = color_obj.rgb
                diff = (color,
                        abs(pixel[0] - color[0]) +
                        abs(pixel[1] - color[1]) +
                        abs(pixel[2] - color[2])
                        )
                diffs.append(diff)
            counter += 1
            loaded = counter/pixel_num
            if loaded == 0.5:
                print("Halfway Done!")
            pixels[x, y] = tuple(min(diffs, key=lambda pix: pix[1])[0])
    def average_middle(middles):
        r, g, b = 0, 0, 0
        for middle in middles:
            r += middle[0]
            g += middle[1]
            g += middle[2]
        l = len(middles)
        avg_color, diffs = (int(r/l), int(g/l), int(b/l)), []
        for color in Colors.values():
            diff = (color.rgb,
                    abs(avg_color[0] - color.rgb[0]) +
                    abs(avg_color[1] - color.rgb[1]) +
                    abs(avg_color[2] - color.rgb[2])
                    )
            diffs.append(diff)
        return tuple(min(diffs, key=lambda pix: pix[1])[0])
    middles = []
    for i in range(2):
        for x in range(0, width, 3):
            for y in range(0, length, 3):
                if i == 0:
                    middles.append(pixels[x+1, y+1])
                elif i == 1:
                    pixels[x+1, y+1] = avg_color
        avg_color = average_middle(middles)
    path = f"{os.getcwd()[:-3]}statics\\newimage.png"
    img.save(path)
    print("Done.")
    return path, img, subregion_dimensions

def image_as_subregions(img, scale_factor):
    pixels, subregions = np.array(img), []
    for x in range(0, len(pixels), 3):
        for y in range(0, len(pixels[0]), 3):
            subregions.append(pixels[x:x + 3, y:y + 3])
    return subregions


if __name__ == "__main__":
    pass
    #print(prepare_image("C:/Users/moezb/OneDrive/Desktop/Python Projects/RubikMosaic/statics/test.jpg"))
    #print(Colors.values())