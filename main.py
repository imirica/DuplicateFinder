from tkinter import *
from tkinter import filedialog
from duplicateFinderScript import DuplicateFinder
import os

class Application(Frame):
    # __slots__ = ["master", "default_path", "create_widgets", "my_label", "result_label", "button_explore",
    #              "button_serch", "button_exit", "start_path"]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def find_files(self):
        x=DuplicateFinder(self.start_path)
        print(x.find_duplicates())

    def create_widgets(self):
        # Labels
        self.title_text="Duplicate Finder"
        self.my_label = Label(self, text=self.title_text, width=60, height=4, fg="blue", bg="white")
        self.my_label.grid(column=1, row=1)
        self.result_label = Label(self, text="Here will be displayed the results", width=60, height=4)
        self.result_label.grid(column=1, row=4)

        # Buttons
        self.button_explore = Button(self, text="Select a Path", command=self.browse_files)
        self.button_explore.grid(column=1, row=2)
        self.button_search = Button(self, text="Search for Duplicates", state="disabled", command=self.find_files)
        self.button_search.grid(column=1, row=3)
        self.button_exit = Button(self, text="Exit", fg="red", command=self.master.destroy)
        self.button_exit.grid(column=1, row=5)

    def browse_files(self):
        self.default_text = "Duplicate File Search in :  "
        self.start_path = filedialog.askdirectory(initialdir="C:/", title="Select a path")

        if self.start_path == "" and self.my_label["text"]!=self.title_text:
            self.button_search["state"] = "active"
        elif self.start_path == "":
            self.button_search["state"] = "disabled"
        else:
            self.button_search["state"] = "active"
            self.my_label.configure(text=self.default_text + self.start_path)


root = Tk()
root.title('DuplicateFinder by @mrk')
app = Application(master=root)
app.mainloop()

#make here a callBack function that finds the size of each file and transmit the information to the progress bar that will be updated