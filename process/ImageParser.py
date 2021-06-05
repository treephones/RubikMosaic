import os
import enum
from PIL import Image

class Colors(enum.Enum):
    RED = (246, 0, 0)
    ORANGE = (255, 156, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 217, 0)
    BLUE = (55, 55, 179)
    WHITE = (255, 255, 255)

    @staticmethod
    def values():
        return list(map(lambda col: col.value, Colors))

def get_dimensions(l, w, r):
    image_ratio = l / w
    rectangles = [(1, r)]
    for i in range(r):
        y = r/(i+1)
        if r-2 > i > 0 and y - int(y) == 0:
            x, y = i+1, int(y)
            rectangles.append(((x, y), abs(image_ratio - (x/y))))
    rectangles.append((r, 1))
    closest = min(rectangles, key=lambda rectangle: rectangle[1])
    return tuple([d*3 for d in closest[0]])

def prepare_image(path, n_cubes):
    img = Image.open(path)
    width, length = img.size
    img = img.resize(get_dimensions(width, length, n_cubes)).convert("RGB")
    width, length = img.size
    pixel_num, counter = width*length, 0
    pixels = img.load()
    print("Opened Image.")
    for x in range(width):
        for y in range(length):
            pixel, diffs = pixels[x, y], []
            for color in Colors.values():
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
    path = f"{os.getcwd()}\\statics\\newimage.png"
    img.save(path)
    print("Done.")
    return path



if __name__ == "__main__":
    pass
    #print(prepare_image("C:/Users/moezb/OneDrive/Desktop/Python Projects/RubikMosaic/statics/test.jpg"))
    #print(Colors.values())