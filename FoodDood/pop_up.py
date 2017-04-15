from tkinter import *
from getreqtest import search_calls
from logos import getlogo
import tkinter as tk


class PopUp:

    def __init__(self):
        self.root = Tk()
        self.root.title('Food Analysis Time!')
        self.root.geometry("600x100")
        self.intro = Label(self.root, text='Time to analyze your snack!')
        self.intro.grid()
        self.photo = PhotoImage(file='./Hamp.gif')
        self.label = Label(image=self.photo)
        self.label.grid()
        self.calories = search_calls(getlogo('Hamp.gif'))[1]
        self.sugg_foods = ['beans', 'fruit']

    def run_it(self):
        self.make_menus(self.root)
        self.root.mainloop()

    def make_menus(self, root):
        menu = Menu(root)
        root.config(menu=menu)
        subMenu = Menu(menu)
        subMenu2 = Menu(menu)
        menu.add_cascade(label='Calorie Info', menu=subMenu)
        menu.add_cascade(label='Suggested Foods', menu=subMenu2)
        subMenu.add_command(label = 'Calorie Intake', command = self.get_calories)
        subMenu.add_command(label = 'Calories per Serving', command = self.get_calories)
        subMenu2.add_command(label = 'Suggested Foods', command = self.get_suggested_foods)

    def get_calories(self):
        label = Label(self.root, text = 'There are ' + self.calories + ' of this snack.')
        label.grid()

    def get_suggested_foods(self):
        label = Label(self.root, text = 'Here is a list of some suggested foods: ' + str(self.sugg_foods))
        label.grid()

    def image_set(self):
        photo = PhotoImage(file='./Hamp.gif')
        label = Label(image = photo)
        label.grid()