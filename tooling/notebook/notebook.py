# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Series of tabs to open the text frames"""

from . import textFrame as txf
import tkinter as tk
import tkinter.ttk as ttk

class NoteBook(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.enable_traversal()
    
    def addFrame(self, textFrame, bindings={}):
        """Add a new textFrame, to add the bindings to the correspondign frames provide
        key= the secuence or trigger i.e. '<Control-KeyPress-a>' 
        value= funtion call
        The binding is also added to the text Widget on the frame"""
        for key, value in bindings.items():
            textFrame.bind(key, value)
            textFrame.text.bind(key, value)
        super().add(textFrame, text=textFrame.getName(), underline=0, sticky=tk.NE+tk.SW)
    
    def deleteCurrentTab(self):
        """Remove selected frame"""
        for item in self.winfo_children():
            if str(item)==self.select():
                item.destroy()       
                return
    
    def autosave(self):
        """Save changes done to the file"""
        for item in self.winfo_children():
            if str(item)==self.select():
                item.dumpIntoFile()       
                return

    def fullsave(self, filePath=""):
        """Save changes to new file, absolute path for new location"""
        for item in self.winfo_children():
            if str(item)==self.select():
                item.dumpIntoFile(False, filePath)       
                return
    
    def getSelectedFrame(self):
        """Obtain the selected textFrame on the notebook"""
        for item in self.winfo_children():
            if str(item)==self.select():
                return (True, item)
        return (False,)

"""
Class to test the functionality of the notebook created
"""
class Debugger(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ts = NoteBook(self)
        self.test1 = tk.Button(self, text="Delete", command=self.delition)
        self.test2 = tk.Button(self, text="Add", command=self.do)
        self.test3 = tk.Button(self, text="AddEmpty", command=self.do2)
        self.test4 = tk.Button(self, text="Autosave", command=self.autosv)
        self.test5 = tk.Button(self, text="FullSave", command=self.fullsv)

        self.ts.pack()
        self.test1.pack()
        self.test2.pack()
        self.test3.pack()
        self.test4.pack()
        self.test5.pack()
    
    def do(self):
        """Test the addition of a frame with a given path"""
        self.ts.addFrame(txf.createFrame(self.ts, "textFrame.py")[1])
    
    def do2(self):
        """Test the addtion of new Frame no path"""
        self.ts.addFrame(txf.createFrame(self.ts)[1])

    def delition(self):
        """Test deletion of selected tab"""
        self.ts.deleteCurrentTab()
    
    def autosv(self):
        """Test fot autosaving of files"""
        self.ts.autosave()

    def fullsv(self):
        """Test for full saving of files"""
        self.ts.fullsave("test.txt")

if __name__ == "__main__":
    db = Debugger()
    db.mainloop()
