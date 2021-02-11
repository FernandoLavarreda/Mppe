# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Text Editor with commandline and tree view"""

from .notebook import notebook, textFrame
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
from .commandline import shell
from . import tools

class Editor(tk.Tk):
    """Main window tih the notebook, tree view and command line
    For the startOpen it refers to a initial path to open a file if it
    is not provided a new file will be opened"""
    def __init__(self, startOpen=""):
        super().__init__()
        menu = tk.Menu(self)
        filemn = tk.Menu(menu, tearoff=0)
        self.files = notebook.NoteBook(self)
        self.shell = shell.Cmd(self, "D:/Icons/command.png")
        # Bindigns for the notebook and its children
        self.binds = {
             "<Control-KeyPress-n>": self.newFile,
             "<Control-KeyPress-o>": self.openFile,
             "<Control-KeyPress-s>": self.saveFile,
             "<Control-KeyPress-t>": self.saveAs,
             "<Control-KeyPress-w>": self.closeFile,
             "<Control-KeyRelease-Down>": self.focus_shell,
            }

        for binding, callback in self.binds.items():
            self.files.bind(binding, callback)

        self.shell.addComand("compare",(tools.compare_dir,(2,4)))
        self.shell.addComand("transfer",(tools.transfer_files,(2,4)))
        self.shell.addComand("list",(tools.view_files,(1,2)))
        self.shell.addComand("remove",(tools.remove,(1,2)))
        self.shell.addComand("read",(tools.read,(1,1)))
        self.shell.addComand("help",(tools.help_,(0,0)))

        filemn.add_command(label="New File Ctrl-N", command=self.newFile)
        filemn.add_command(label="Open File Ctrl-O", command=self.openFile)
        filemn.add_command(label="Close File Ctrl-W", command=self.closeFile)
        filemn.add_command(labe="Save Ctrl-S", command=self.saveFile)
        filemn.add_command(label="Save as.. Ctrl-T", command=self.saveAs)
        menu.add_cascade(labe="File", menu=filemn)

        # Marks the opening of an existing/new file depending on args sent to constructor
        if startOpen:
            created = textFrame.createFrame(self.files, startOpen)
            if created[0]:
                self.files.addFrame(created[1], self.binds)
        else:
            self.newFile()

        self.shell.shell.bind("<Control-KeyRelease-Up>", self.focus_editor)
        self.files.grid(row=0, column=0)
        self.shell.grid(row=1, column=0, sticky=tk.NE+tk.SW)
        self.config(menu=menu)
        self.focus_editor()
    
    def newFile(self, *args):
        """Add new file to editor"""
        self.files.addFrame(textFrame.createFrame(self.files)[1], self.binds)
        

    def openFile(self, *args):
        """Provide a file Dialog box to open file"""
        filetypes = (("Plain text files", "*"),)
        filename = fd.askopenfilename(title="Open file", initialdir="/", filetypes=filetypes)
        if filename:
            created = textFrame.createFrame(self.files, filename)
            if created[0]:
                self.files.addFrame(created[1], self.binds)


    def saveFile(self, *args):
        """If there is a currently selected tab and the file has a path association
        the changes will be overriden if there is no asociation a call to saveAs will
        be done"""
        found = self.files.getSelectedFrame()
        if found[0]:
            if found[1].getPath():
                self.files.autosave()
            else:
                self.saveAs()


    def saveAs(self, *args):
        """Save as new file the currently selected one"""
        if self.files.winfo_children():
            path = fd.asksaveasfilename(title="New File", defaultextension=".txt", filetypes=(("Text Files", "*"),))
            if path:
                self.files.fullsave(path)
                frame = self.files.getSelectedFrame()[1]
                frame.setPath(path)
                self.files.tab(self.files.select(), text=frame.getName())
        
    
    def closeFile(self, *args):
        """Close current tab, change focus to standing frame
           enable closing only if there are more than 1 window at disposition"""
        if self.files.index("end")>1:
            self.files.deleteCurrentTab()
            self.files.getSelectedFrame()[1].focus_set()
    
    def focus_shell(self, *args):
        """Set the focus on the prompt for commands"""
        self.shell.shell.focus_set()
    
    def focus_editor(self, *args):
        """Set the focus on the text editor"""
        self.files.getSelectedFrame()[1].text.focus_set()

def run(startOpen=""):
    edt = Editor(startOpen=startOpen)
    edt.mainloop()

if __name__ == "__main__":
    edt = Editor()
    edt.mainloop()
