import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from tkinter import filedialog as fd
from tkinter import messagebox
import shutil
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "multiCopy.ui"

class MultiCopy:
    filename = None
   
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        builder.add_from_file(PROJECT_UI)

        self.mainwindow = builder.get_object('toplevel1', master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    
    def select_file(self):
        self.filename = fd.askopenfilename(title='Select a file to copy')
        if self.filename: 
            self.dirpath = os.path.dirname(self.filename)
            self.builder.tkvariables['file_status_msg'].set("OK")
    
    def make_copy(self):
        if self.checkConditions():
            try:
                copy_number = int( self.builder.tkvariables['copy_number'].get() )
                filesname = self.builder.tkvariables['filesname'].get() or 'copy_'
                filename_prefix = self.dirpath + '/' + filesname

                for i in range(copy_number):
                    filename_suffix =  '_{0}{1}'.format(i,os.path.splitext(self.filename)[1])
                    shutil.copy2(self.filename, filename_prefix + filename_suffix)

                messagebox.showinfo("Operation Done","Success !")
            except:
                messagebox.showerror("Error",  'Unexpected error while copying file. Please report')

    def checkConditions(self):
        copy_number = self.builder.tkvariables['copy_number'].get()

        if not copy_number.isnumeric() or int( copy_number ) < 1:
            messagebox.showerror("Error", 'Copy number must be a valid number superior to 0')
            return False

        if not self.filename:
            messagebox.showerror("Error", 'Please select a file')
            return False

        return True
    
if __name__ == '__main__':
    app = MultiCopy()
    app.run()
