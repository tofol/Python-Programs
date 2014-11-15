from tkinter import *
from PIL import Image, ImageTk

root    = Tk()
img = Image.open('images/file/filenew.png')
eimg = ImageTk.PhotoImage(img)
mbutton = Menubutton(root, text='Food', compound='left', image=eimg)
picks   = Menu(mbutton)               
mbutton.config(menu=picks)           
picks.add_command(label='A',  command=root.quit, compound='left', image=eimg)
picks.add_command(label='B',  command=root.quit)
picks.add_command(label='C', command=root.quit)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop()
