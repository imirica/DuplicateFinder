from tkinter import *
from tkinter import filedialog

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Labels
        self.myLabel = Label(self, text="Duplicate Finder", width=60, height=4, fg="blue", bg="white")
        self.myLabel.grid(column=1, row=1)
        self.resultLabel = Label(self, text="Here will be displayed the results", width=60, height=4)
        self.resultLabel.grid(column=1, row=4)
        #Buttons
        self.button_explore = Button(self, text="Select a Path", command=self.browseFiles)
        self.button_explore.grid(column=1, row=2)
        self.button_serch = Button(self, text="Search for Duplicates")
        self.button_serch.grid(column=1, row=3)
        self.button_exit = Button(self, text="Exit", fg="red", command=self.master.destroy)
        self.button_exit.grid(column=1, row=5)

    def browseFiles(self):
        self.filename = filedialog.askdirectory(initialdir="C:/", title="Select a path")
        self.myLabel.configure(text="Duplicate File Search in :  " + self.filename)

root = Tk()
root.title('DuplicateFinder by @mrk')
app = Application(master=root)
app.mainloop()