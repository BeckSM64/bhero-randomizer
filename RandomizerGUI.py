import tkinter as tk
import random
from tkinter import filedialog

class RandomizerGUI:

    def __init__(self):

        # Setup window
        self.window = tk.Tk()
        self.window.title("Bomberman Hero Randomizer - v1.0.0")
        self.window.iconbitmap("BomberMad.ico")

        self.frame = tk.Frame(master=self.window, relief=tk.FLAT, borderwidth=5)

        # Seed Widgets
        self.seedLabel = tk.Label(master=self.frame, text="Seed")
        self.seedInput = tk.Entry(master=self.frame, width=50)
        self.seedButton = tk.Button(master=self.frame, text="New", width=10, command=self.generateSeed)
        
        # Input ROM Widgets
        self.inputRomLabel = tk.Label(master=self.frame, text="Input ROM")
        self.inputRomInput = tk.Entry(master=self.frame, width=50)
        self.inputRomButton = tk.Button(master=self.frame, text="Select Input", width=10, command=self.inputFileSelect)

        # Ouput Rom Widgets
        self.outputRomLabel = tk.Label(master=self.frame, text="Output ROM")
        self.outputRomInput = tk.Entry(master=self.frame, width=50)
        self.outputRomButton = tk.Button(master=self.frame, text="Select Output", width=10, command=self.outputDirectorySelect)

        # Generate Widgets
        self.generateFrame = tk.Frame(master=self.window, relief=tk.FLAT, borderwidth=5)
        self.generateButton = tk.Button(master=self.generateFrame, text="Generate ROM")

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
        self.frame.pack()
        self.generateFrame.pack()

        # Run the main loop
        self.window.mainloop()

    def inputFileSelect(self):
        inputFilePath = filedialog.askopenfilename()
        self.inputRomInput.insert(0, inputFilePath)

    def outputDirectorySelect(self):
        outputDir = filedialog.askdirectory()
        self.outputRomInput.insert(0, outputDir)

    def generateSeed(self):
        seed = random.randint(0, 1000000)
        self.seedInput.delete(0, tk.END)
        self.seedInput.insert(0, seed)
