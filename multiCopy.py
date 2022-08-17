
"""
MutiCopy

Copy files N times or create N times folder

Author: g0tie
Github: www.github.com/g0tie
"""

from copy import copy
import tkinter as tk
from tkinter import DISABLED, filedialog as fd

class MultiCopy():
    instructions = "Sélectionner le fichier à copier et entrez le nombre de copies à effectuer"
    selected_filename = "Sélectionnez un fichier..."

    def __init__(self):
        self = tk.Tk()
        self.title = "MultiCopy: Copy mutiple time a file"
        self.createLayout()

    def copy_file(self):
        for i in range(1, int(self.copy_number.get()) ):
            print(self.selected_filename)

    def set_selected_file(self):
        self.selected_filename = fd.askopenfilename(
            title='Sélectionner un fichier',
            initialdir='/',
    )

    def createLayout(self):
        tk.Label(text = self.instructions).grid(row=0, columnspan=3)
        tk.Button(self.root, text= 'Choisir', command = self.set_selected_file).grid(row=1, column=0)

        self.selected_file_label = tk.Label(text = self.selected_filename).grid(row=1, column=1)
        self.copy_number = tk.Entry(self.root).grid(row=1, column=2)
        self.copy_btn =  tk.Button(self.root, text='Copier', command = self.copy_file, state = DISABLED).grid(row=1, column=3)


app = MultiCopy()
app.mainloop()