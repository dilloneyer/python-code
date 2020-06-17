from tkinter import *
import tkinter.messagebox

# ************* Menu Item Initialization *************

class menuItem:

    def __init__(self, masterMenu, str):
        self.createSubMenu = Menu(masterMenu, tearoff=0)
        masterMenu.add_cascade(label=str, menu=self.createSubMenu)

    def addsubItem(self, itemName):
        self.createSubMenu.add_command(label=itemName, command=test)

# ************* Toolbar Initialization *************

class toolbarInit:

    def __init__(self, master):
        self.toolbar = Frame(master, bg="grey")

        self.toolbar.pack(side=TOP, fill=X)

    def addBtn(self, btnName):
        self.toolButton = Button(self.toolbar, text=btnName, command=test)
        self.toolButton.pack(side=LEFT, padx=2, pady=2)

# ************* Status Bar Initialization *************

class statusBar:

    def __init__(self, master):
        self.statusBar = Label(master, text= "Preparing the Test", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

# ************* Message Box Initialization *************

class popoutMessage:

    def __init__(self, message):
        self.msgBox = tkinter.messagebox.showinfo("Window Title", message)

# ************* Canvas Graphic Initialization *************

class canvasCreate:

    def __init__(self, master, w, h):
        self.mainCanvas = Canvas(master, width=w, height=h)

def test():
    print("This is a test, button pressed.")

# *****************************************************************
# ************* Window Initialization (PROGRAM START) *************
# *****************************************************************
window = Tk()

homeScreen = canvasCreate(window,800, 600)

menu1 = Menu(window)
window.config(menu=menu1)

# Add "File" Submenu, with new and open submenu items
file = menuItem(menu1, "File")
newFILE = file.addsubItem("New Log...")
openFILE = file.addsubItem("Open...")

# Add "Edit Submenu, with undo and redo submenu items
edit = menuItem(menu1, "Edit")
undoEDIT = edit.addsubItem("Undo")
redoEDIT = edit.addsubItem("Redo")

# Add Toolbar, with 2 added buttons
tool = toolbarInit(window)
tool.addBtn("Insert Image")
tool.addBtn("Insert File")

# Add a status bar to the bottom west side
status = statusBar(window)

#Add a pop-up message box
#msgBox = popoutMessage("The cat in the hat.")

window.mainloop()
