from tkinter import *
import tkinter as tk
from pop_up import PopUp
from tkinter.filedialog import askopenfilename
from getreqtest import search_calls
from logos import getlogo



# the window
root = Tk()

photo = PhotoImage(file='./FDLogo.gif')
label = Label(image = photo)
label.grid()

root.title("Welcome to Food Dood!")
root.geometry("400x700")
app = Frame(root)
app.grid()

# initialize the label
message = "Welcome to Food Dood! \n To nutritionally analyze your item, please click the button below!"
label = Label(app, text=message)
label.grid()

fname=''
d = {
        'Nestle': ['Bonka', 'Caro', 'Herta'],
        'PepsiCo Inc': ['Doritos', "Fritos", "Lays", "Cheetos", "Mountain Dew"],
        'Coca-Cola Company':["Sprite"],
        'Dr Pepper Snapple Group':["Canada Dry"],
        'Nabisco':['Chip\'s Ahoy'],
        'Kellogg':['Pringles']
}

environment={
        'Hershey Co': 80.70,
        'Coca-Cola Company': 76.3,
        'General Mills': 67.10,
        'Nestle': 61.70,
        'Kellogg': 59.80,
        'Nabisco': 59.30,
        'PepsiCo Inc': 49.90,
        'Dr Pepper Snapple Group': 33.80
}

# The next popup
def output(file_name):
    calories = search_calls(getlogo(file_name))
    label = Label(root, text='There are ' + calories[1] + ' of ' + calories[0] + ',' + '\n which is the same as ' + str(int(calories[2]/2.5)) + ' goldfish.')
    label.grid()

    if calories[3] == 'fl oz' or calories[3] == 'can' or calories[3] == 'ml':
        label15 = Label(root, text='If you want a healthier option, try water!')
        label15.grid()
    else:
        label15 = Label(root, text='If you want a healthier option, try beans and fruit!')
        label15.grid()
    for i in d:
        if (calories[0] in d[i]):
            label2 = Label(root, text='Environmentally, ' + i + ' has an green score of: ' + str(environment[i]) + '%.\n')
            label2.grid()
    return

def load_file():
    fname = askopenfilename()
    output(fname)

    # photo = PhotoImage(fname)
    # label2 = Label(image=photo)
    # label2.grid()

# another button
# quit = tk.Button(app, text="EXIT", fg="red", command=root.destroy)
# quit.grid()

button0 = Button(root, text="Browse", fg="blue", command=load_file, width=10)
button0.grid()
# THE FIRST BUTTON OOOOOOO

# button1 = Button(root, text='Load Info', command=lambda: pop_it_up())
# button1.grid()




# run it
root.mainloop()