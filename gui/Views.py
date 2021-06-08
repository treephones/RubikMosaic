import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
from process.CubeController import CubeController

class MosaicSetupWindow:
    def __init__(self):
        self.view = tk.Tk()
        self.view.title("Required Information")
        self.view.geometry("500x300+20+20")
        self.size = (500, 300)
        self.img_panel = None

    def run(self):
        title = tk.Label(self.view, text="Required Information", font=("Helvetica", 15), fg="black")
        title.pack(pady=(20, 20))
        nCubesLabel = tk.Label(self.view, text="Number of cubes:", font=("Helvetica", 10), fg="black")
        nCubesLabel.pack()
        nCubes = tk.Entry(self.view)
        nCubes.pack()
        chooseFileButton = tk.Button(self.view, text="Choose Image", height=2, width=20, command=lambda: self.displayImage())
        chooseFileButton.pack(pady=(20, 20))
        self.img_panel = tk.Label(self.view, text="", wraplength=500)
        self.view.mainloop()

    def displayImage(self):
        path = tk.filedialog.askopenfilename(title="Choose an image:", filetypes=[("image files", (".png", ".jpg", ".jpeg", ".jfif"))])
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

class MainView:

    def __init__(self):
        self.view = tk.Tk()
        self.view.title("RubikMosaic")
        self.view.geometry("800x500+20+20")
        self.size = (800,500)
        self.freeCube = CubeController()

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
