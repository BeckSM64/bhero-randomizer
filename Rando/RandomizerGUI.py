import tkinter as tk
import random
from Rando.BheroRandomizer import *
from tkinter import filedialog

def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class RandomizerGUI:
    def __init__(self):

        # Setup window
        self.window = tk.Tk()
        self.window.title("Bomberman Hero Randomizer - v1.1.0")
        self.window.iconbitmap(default=resource_path("Assets/BomberMad.ico"))

        self.frame = tk.Frame(master=self.window, relief=tk.FLAT, borderwidth=5)

        # Seed Widgets
        self.seedLabel = tk.Label(master=self.frame, text="Seed")
        self.seedInput = tk.Entry(master=self.frame, width=50)
        self.seedButton = tk.Button(
            master=self.frame, text="New", width=10, command=self.generateSeed
        )

        # Input ROM Widgets
        self.inputRomLabel = tk.Label(master=self.frame, text="Input ROM")
        self.inputRomInput = tk.Entry(master=self.frame, width=50)
        self.inputRomButton = tk.Button(
            master=self.frame,
            text="Select Input",
            width=10,
            command=self.inputFileSelect,
        )

        # Ouput Rom Widgets
        self.outputRomLabel = tk.Label(master=self.frame, text="Output Dir")
        self.outputRomInput = tk.Entry(master=self.frame, width=50)
        self.outputRomButton = tk.Button(
            master=self.frame,
            text="Select Output",
            width=10,
            command=self.outputDirectorySelect,
        )

        # Generate Widgets
        self.generateFrame = tk.Frame(master=self.window, relief=tk.FLAT, borderwidth=5)
        self.generateLabel = tk.Label(master=self.generateFrame, text="Error!")
        self.generateButton = tk.Button(
            master=self.generateFrame,
            text="Generate ROM",
            command=lambda: self.generateButtonPressed(),
        )

        # Setup grid for GUI layout
        self.seedLabel.grid(column=0, row=0)
        self.seedInput.grid(column=1, row=0)
        self.seedButton.grid(column=2, row=0)
        self.inputRomLabel.grid(column=0, row=1)
        self.inputRomInput.grid(column=1, row=1)
        self.inputRomButton.grid(column=2, row=1)
        self.outputRomLabel.grid(column=0, row=2)
        self.outputRomInput.grid(column=1, row=2)
        self.outputRomButton.grid(column=2, row=2)
        self.generateButton.grid(column=0, row=0)
        self.generateLabel.grid(column=1, row=0)
        self.generateLabel.grid_forget()
        self.frame.pack()
        self.generateFrame.pack()
        self.window.resizable(False, False)

        # Run the main loop
        self.window.mainloop()

    def inputFileSelect(self):
        inputFilePath = filedialog.askopenfilename()
        self.inputRomInput.delete(0, tk.END)
        self.inputRomInput.insert(0, inputFilePath)

    def outputDirectorySelect(self):
        outputDir = filedialog.askdirectory()
        self.outputRomInput.delete(0, tk.END)
        self.outputRomInput.insert(0, outputDir)

    def generateSeed(self):
        seed = random.randint(0, 1000000)
        self.seedInput.delete(0, tk.END)
        self.seedInput.insert(0, seed)

    def generateButtonPressed(self):
        if self.seedInput.get() == "" or self.inputRomInput.get() == "" or self.outputRomInput.get() == "":
            success = -1
        else:
            success = generate_rom(self.inputRomInput.get(), self.outputRomInput.get(), int(self.seedInput.get()))

        if success == -1:
            self.generateLabel.configure(text="Error!", fg="#f00")
            self.generateLabel.grid(column=1, row=0)
        else:
            self.generateLabel.configure(text="Success!", fg="#0f0")
            self.generateLabel.grid(column=1, row=0)
