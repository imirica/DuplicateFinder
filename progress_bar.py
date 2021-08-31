from tkinter import *
from tkinter import filedialog
from tkinter import ttk
# from duplicateFinderScript import DuplicateFinder
import os
import time
from threading import Thread
import hashlib

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def update_bar(self,percent):
        time.sleep(0.5)
        self.pbar['value']+=percent
        self.percent_label.configure(text=str(int(self.pbar['value'])) + "%")
        root.update_idletasks()

    def create_widgets(self):
        # Labels
        self.title_text="Duplicate Finder"
        self.my_label = Label(self, text=self.title_text, width=60, height=4, fg="blue", bg="white")
        self.my_label.grid(column=1, row=1)
        self.result_label = Label(self, text="Here will be displayed the results", width=60, height=4)
        self.result_label.grid(column=1, row=4)
        self.percent_label = Label(self, textvariable="", width=60, height=4)
        self.percent_label.grid(column=1, row=7)

        #ProgressBarr

        self.pbar=ttk.Progressbar(self, orient=HORIZONTAL, length=300)
        self.pbar.grid(column=1, row=6)

        # Buttons

        self.button_explore = Button(self, text="Select a Path", command=self.browse_files)
        self.button_explore.grid(column=1, row=2)
        self.button_search = Button(self, text="Search for Duplicates", state="disabled", command=self.find_duplicates )#, Thread(target=self.update_bar).start()
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

    #the script

    def get_size(self):
        total_size=0
        count=0
        for dirpath, _, filenames in os.walk(self.start_path):
            for element in filenames:
                count+=1
                file = os.path.join(dirpath, element)
                total_size = total_size + os.path.getsize(file)
        return total_size

    def find_duplicates(self):
        new_dict = {}
        duplicate_files = []
        total_size=self.get_size()
        for dirpath, _, filenames in os.walk(self.start_path):
            for element in filenames:
                file = os.path.join(dirpath, element)
                file_size=os.path.getsize(file)
                percentage=file_size*100/total_size
                self.update_bar(percentage)
                with open(file, 'rb') as f:
                    sha256 = hashlib.sha256(f.read()).hexdigest()
                    if sha256 not in new_dict:
                        new_dict[sha256] = []
                    new_dict[sha256].append(element)
        for values in new_dict.values():
            if len(values) > 1:
                duplicate_files.append(values)
        return "The duplicates files are : ", duplicate_files

root = Tk()
root.title('DuplicateFinder by @mrk')
app = Application(master=root)
app.mainloop()
