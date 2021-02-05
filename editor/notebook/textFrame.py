# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Frame to store text with support for programming languages"""

import os
import tkinter as tk
import tkinter.ttk as ttk

def createFrame(parent, pathos=""):
    """Return a TextFrame object"""
    if pathos:
        if os.path.isfile(pathos):
            return (True, TextFrame(parent, pathos))
        else:
            return (False,)
    else:
        return (True, TextFrame(parent))


class TextFrame(ttk.Frame):
    count = 1
    def __init__(self, parent, pathos="", width=200, height=300):
        super().__init__(parent, width=width, height=height)
        self.name = "new"+str(TextFrame.count)
        self.path = pathos
        self.text = tk.Text(self)
        self.loadFromFile()
        self.text.pack()
        TextFrame.count+=1
    
    def setPath(self, path):
        """Set the path for the text"""
        self.path = path
        self.setName()
    
    def loadFromFile(self):
        """If a path was provided text is loaded from the given file"""
        if self.path:
            with open(self.path) as fd:
                lines = fd.readlines()
                for line in lines:
                    self.text.insert(tk.END, line)
    
    def dumpIntoFile(self, autosave=True, fullPath=""):
        """Save contents into a file, autosave indicates already given path
        else a new path should be given to fullpath"""
        if autosave:
            with open(self.path, "w") as fw:
                text = self.text.get("1.0",tk.END)
                fw.writelines(text)
        else:
            assert fullPath!=""
            with open(fullPath, "w") as fw:
                text = self.text.get("1.0",tk.END)
                fw.writelines(text)
            self.setPath(fullPath)

    
    def getName(self):
        """See the name of the file"""
        self.setName()
        return self.name

    def setName(self):
        """Declare the name of the file, read from its path. Just name plus extension"""
        if self.path:
            nm = ""
            for char in self.path[::-1]:
                if char != "\\" and char != "/":
                    nm = char+nm
                else:
                    break
            self.name = nm

        