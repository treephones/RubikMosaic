import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

from process.CubeController import RubiksCubeController
from process import ImageParser

class ErrorWindow:

    def __init__(self, message):
        self.message = message
        self.view = tk.Tk()
        self.view.title("Error")
        self.view.geometry("250x150+1000+200")
        self.size = (200, 200)

    def run(self):
        tk.Label(self.view, text="Something Went Wrong!", font=("Helvetica", 15), fg="red").pack(pady=(20,20))
        tk.Label(self.view, text=self.message, font=("Helvetica", 10), fg="black").pack()

class MosaicWindow:

    def __init__(self, nCubes, path):
        self.nCubes = nCubes
        self.path = path
        self.view = tk.Toplevel()
        self.view.title("Mosaic")
        self.view.geometry("1000x800+1000+200")
        self.size = (1000, 800)

    def run(self):
        #tk.Label(self.view, text="Mosaic", font=("Helvetica", 20), fg="black").grid(row=0, column=0, pady=1)
        output_path, img, srd = ImageParser.prepare_image(self.path, self.nCubes)
        resize_dimensions = tuple(map(int, (self.size[0] / srd[0], self.size[1] / srd[1])))
        subregions = ImageParser.image_as_subregions(img)
        panels = []
        for y in range(srd[1]):
            for x in range(srd[0]):
                image = Image.fromarray(subregions[y*srd[0]+x])
                image = image.resize(resize_dimensions, Image.NEAREST)
                subregion_image = ImageTk.PhotoImage(image)
                panel = tk.Label(self.view, image=subregion_image)
                panel.image = subregion_image
                panel.grid(row=y+1, column=x+1, pady=(1,1), padx=(1,1))
                panels.append(panel)

        self.view.mainloop()

class MosaicSetupWindow:

    def __init__(self):
        self.view = tk.Tk()
        self.view.title("Required Information")
        self.view.geometry("500x400+1000+200")
        self.size = (500, 400)
        self.img_panel = None
        self.path = None

    def run(self):
        title = tk.Label(self.view, text="Required Information", font=("Helvetica", 15), fg="black")
        title.pack(pady=(20, 20))
        nCubesLabel = tk.Label(self.view, text="Number of cubes:", font=("Helvetica", 10), fg="black")
        nCubesLabel.pack()
        nCubes = tk.Entry(self.view)
        nCubes.pack()
        chooseFileButton = tk.Button(self.view, text="Choose Image", height=1, width=15, command=lambda: self.displayImage())
        chooseFileButton.pack(pady=(20, 20))
        continueButton = tk.Button(self.view, text="Continue", height=2, width=20, command=lambda: self.toImageView(nCubes))
        continueButton.pack(pady=(20, 20))
        self.img_panel = tk.Label(self.view, text="", wraplength=500)
        self.view.mainloop()

    def displayImage(self):
        path = tk.filedialog.askopenfilename(title="Choose an image:", filetypes=[("image files", (".png", ".jpg", ".jpeg", ".jfif"))])
        self.path = path
        # raw_img = Image.open(path)
        # width, height = raw_img.size
        # aspect_ratio = width/height
        # nHeight = 2000
        # nWidth = int(aspect_ratio * nHeight)
        # raw_img = raw_img.resize((nWidth, nHeight))
        # img = ImageTk.PhotoImage(master=self.view, image=raw_img)
        self.img_panel.destroy()
        self.img_panel = tk.Label(self.view, text=f"\nChosen Image:\n\n {path}", wraplength=500)
        self.img_panel.pack()

    def toImageView(self, entry):
        try:
            nCubes = int(entry.get())
            if self.path in [None, ""]:
                raise AttributeError
            MosaicWindow(nCubes, self.path).run()
        except ValueError:
            ErrorWindow("Not a valid number!").run()
        except AttributeError:
            ErrorWindow("No image selected!").run()


class MainView:

    def __init__(self):
        self.view = tk.Tk()
        self.view.title("RubikMosaic")
        self.view.geometry("800x500+20+20")
        self.size = (800,500)
        self.freeCube = RubiksCubeController()

    def run(self):
        title = tk.Label(self.view, text="Welcome to RubikMosaic!", font=("Helvetica", 40), fg="black")
        title.pack(pady=(50,50))
        description = tk.Label(self.view, text="Choose one of the options below:", font=("Helvetica", 15), fg="black")
        description.pack()

        mosaicButton = tk.Button(self.view, text="Create Mosaic", height=2, width=30, command=lambda: self.mosaicWindow())
        mosaicButton.pack(pady=(20,20))
        freeButton = tk.Button(self.view, text="Rubik's Cube", height=2, width=30, command=lambda: self.freeCubeWindow())
        freeButton.pack(pady=(20, 20))
        self.view.mainloop()

    def mosaicWindow(self):
        MosaicSetupWindow().run()

    def freeCubeWindow(self):
        try:
            self.freeCube.run()
        except Exception:
            print("Closed Rubik's Cube Window.")

if __name__ == "__main__":
    m = MainView()
    m.run()
    #RubiksCubeController().run()
