import tkinter as tk
# # # Most likely be creating ma
# from tkinter import filedialog, Text
# from os import listdir
# from os.path import isfile, joinny classes for GUI...# # #
# class DirectoryList
# class Framework
# class FileSelection

# Set variables
from tkinter import filedialog

files = []
filepath = ''
root = tk.Tk()
buttonCanvas = tk.Canvas(root, bg="black")
sideCanvas = tk.Canvas(root, bg="#4e5851")
mainCanvas = tk.Canvas(root, bg="#4e5851")
xscrollbar = tk.Scrollbar(sideCanvas, orient='horizontal')
yscrollbar = tk.Scrollbar(sideCanvas, orient='vertical')
dirListBox = tk.Listbox(sideCanvas, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set) #dirListBox = tk.Listbox(sideCanvas, xscrollbarcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
xscrollbar.config(command=dirListBox.xview)
yscrollbar.config(command=dirListBox.yview)

# Add files
def addFiles():
    global files
    # Add file from screen selector
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("text files", ".txt"),("all files","*.*")))
    files.append(filename)

# Set file directory
def addDirectory():
    global filepath
    # Find and set file path
    filepath = filedialog.askdirectory(initialdir="/", title="Select folder with NIRS data")
    # Display the files found in the selected directory
    createDirDisplay()

# Display file content
def displayFile():
    global tk, mainCanvas, files
    # Remove shown duplicates on screen
    for widget in mainCanvas.winfo_children():
        widget.destroy()
    # Display the names of the files selected
    for filename in files:
        tk.Label(mainCanvas, text=filename).pack(side="top",fill="both")

# Create a display box to select files to be evaluated
def createDirDisplay():
    global tk, dirListBox, files, filepath
    # List all files in selected directory "filepath" if filepath isn't null
    if filepath:
        # Remove shown duplicates on screen
        for widget in mainCanvas.winfo_children():
            widget.destroy()
        # Find all files displayed within the
        files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
        # Display selected files in left
        for file in files:
            dirListBox.insert('end', file)

# Add buttons to canvas
def createButtons():
    global tk, buttonCanvas
    # Creating the buttons for set directory path and run files
    tk.Button(buttonCanvas, text="Select Directory", padx=10, pady=5, fg="white", bg="black", command=addDirectory).pack(side="left")
    tk.Button(buttonCanvas, text="Run File", padx=10, pady=5, fg="white", bg="black", command=displayFile).pack(side="left")

# Initialize the canvas and frames for the GUI
def main():
    global root, buttonCanvas, sideCanvas, mainCanvas, dirListBox
    # Set app display size and title
    root.geometry('1500x800')
    root.title("GUI Testing")
    # Create the main canvas on root frame
    # # Buttons canvas (app selectors)
    buttonCanvas.pack(side="top",fill="both")
    # # Side display canvas (files selected)
    sideCanvas.pack(side="left", fill="both")
    # # Main display canvas (file content)
    mainCanvas.pack(side="right", fill="both", expand=True)
    # # File list box (display file content)
    xscrollbar.pack(side='bottom', fill='x')
    yscrollbar.pack(side='right', fill='y')
    dirListBox.pack(fill='both', expand=1)
    dirListBox.insert('end', "Directory Files Found:")

    # Create buttons
    createButtons()
    #Run GUI's root
    root.mainloop()

# Activate app
if __name__ == "__main__":
    main()