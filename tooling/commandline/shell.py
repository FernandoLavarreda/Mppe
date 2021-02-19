# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image


"""
Class to represent a commandline generated for tk Apps
"""
class Cmd(ttk.Frame):
    def __init__(self, parent, img=""):
        super().__init__(master=parent)
        self.output = tk.StringVar()
        self.input = tk.StringVar()
        self.commands = {}
        self.stack_of_calls = []
        self.cursor = -1
        self.shell = ttk.Entry(self, textvariable=self.input)

        # Frame for output
        frame = tk.Canvas(self, scrollregion=(0, 0, 1000, 1000))
        subframe = ttk.Frame(frame)
        self.stdout = ttk.Label(subframe, textvariable=self.output)
        self.stdout.pack()
        frame.create_window(0,0, window=subframe, anchor=tk.NE)
        subframe.pack()
        self.yview = tk.Scrollbar(self)
        self.yview.config(command=frame.yview)
        frame.config(yscrollcommand=self.yview.set)      
        

        if img:
            try:
                image = ImageTk.PhotoImage(Image.open(img).resize((15, 15), Image.ANTIALIAS))
            except Exception:
                pass
            else:
                lb = ttk.Label(self, image=image)
                lb.image = image
                lb.grid(row=0, column=0)
        
        self.shell.bind("<KeyRelease-Return>", self.exceute)
        self.shell.bind("<KeyRelease-Up>", self.historyUp)
        self.shell.bind("<KeyRelease-Down>", self.historyDown)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.shell.grid(row=0, column=1, columnspan=1, sticky=tk.NE+tk.SW)
        self.yview.grid(row=1, column=0)
        frame.grid(row=1, column=1, columnspan=1)
        
    
    def addComand(self, alias, command):
        """Add a funtion to be executed on the commandline
        the alias is the name to acces the funtion a str
        command should be a tuple of the form (funtion, (min, max))
        where min corresponds to minimum amounto of parameters for the funtion
        and max to its maximum amount"""
        self.commands[alias] = command
    
    def exceute(self, *args):
        """Parse entry from shell and run the corrsepondig command"""
        reading = parse(self.input.get())
        self.stack_of_calls.append(self.input.get())
        self.cursor = -1
        if reading:
            if reading[0] in self.commands.keys():
                if self.commands[reading[0]][1][0]<= len(reading)-1 and  len(reading)-1 <= self.commands[reading[0]][1][1]:
                    self.output.set(self.commands[reading[0]][0](*reading[1:]))
                    
                else:
                    self.output.set("Incorrect amount of arguments")
            else:
                self.output.set("Command not recognized")
        else:
            self.output.set("")
        if len(self.stack_of_calls)>125:
            del self.stack_of_calls[:60]
        self.input.set("")
    
    def historyUp(self, *args):
        """Access previous shell actions"""
        if len(self.stack_of_calls)>=abs(self.cursor):
            self.input.set(self.stack_of_calls[self.cursor])
            if len(self.stack_of_calls) == abs(self.cursor):
                pass
            else:
                self.cursor-=1
    
    def historyDown(self, *args):
        """Access previous calls moving downward"""
        if self.cursor<=-1:
            self.input.set(self.stack_of_calls[self.cursor])
            if self.cursor<-1:
                self.cursor+=1


def parse(values):
    """Return entry values into a parsed format"""
    buffer = ""
    tokens = []
    start = False
    for char in values:
        if char == " ":
            if start:
                buffer+=char
            else:
                tokens.append(buffer)
                buffer = ""
        elif char == "\"":
            if start:
                start = False
                tokens.append(buffer)
                buffer = ""
            else:
                tokens.append(buffer)
                buffer = ""
                start = True
        else:
            buffer+=char
    if buffer:
        tokens.append(buffer)
    return tokens


#Debugging
if __name__ == "__main__":
    main = tk.Tk()
    loas = Cmd(main, "D:\\Icons\\command.png")
    loas.addComand("parse", (parse, (1, 1)))
    loas.shell.bind("<KeyRelease-Return>", loas.exceute)
    loas.pack()
    main.mainloop()
