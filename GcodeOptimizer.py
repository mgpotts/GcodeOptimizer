import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as scrolledtext
import GcodeParser

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("G Code Optimizer")
        self.parent.minsize(width=1000, height=600)
        self.initMenu()
        self.initMain()

    def initMain(self):
        # Initialize Main Screen Area

        self.mainPainedWindow = tk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        self.mainPainedWindow.pack(fill=tk.BOTH, expand=1)

        self.textGcode = scrolledtext.ScrolledText(self.mainPainedWindow, width=30)
        self.mainPainedWindow.add(self.textGcode)

        label = tk.Label(self.mainPainedWindow, text="TEST")
        self.mainPainedWindow.add(label)

    def initMenu(self):
        # Initialize application menu bar
        self.menuBar = tk.Menu(self.parent)
        self.parent.config(menu=self.menuBar)

        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="Open", command=self.onOpen)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Save", command=self.onSave)
        self.fileMenu.add_command(label="Save As", command=self.onSaveAs)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

    def onOpen(self):
        # Open Menu
        self.fileName = filedialog.askopenfilename()

        # Read file into text box
        with open(self.fileName, 'r') as f:
            self.textGcode.insert(tk.END, f.read())
        
        # messagebox.showinfo("File Name", self.fileName)


    def onSave(self):
        # Save Menu
        pass

    def onSaveAs(self):
        # Save As Menu
        pass

    def onExit(self):
        # Exit Menu
        self.quit()
     

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()