from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root=Tk()
root.title('Codemy.com-Learn To Code')
root.iconbitmap('C:/Users/Praksa/cats/images for GUI/Pacman 4.ico')
root.geometry('400x200')

def graph():
    house_prices=np.random.normal(200000,25000,5000)#200 000-average price; 25000 is the standard deviation,5000 are data points
    plt.polar(house_prices)#50 bins
    plt.show()

my_button=Button(root,text='Graph It',command=graph)
my_button.pack()

root.mainloop()