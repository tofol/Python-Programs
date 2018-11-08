from tkinter import StringVar, Text, Frame, Menu, Entry, Scrollbar, Label
from functions.functions import root


__author__ = 'Painkillers'
__email__ = 'author@hotmail.com'
__title__ = 'App BBDD'
__date__ = '4 / 11 / 2018'
__version__ = '1.0.0'
__license__ = 'GNU GPLv3'


SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

app_icons = {
    'connect': 'res/images/tango/connect.png',
    'quit': 'res/images/tango/quit.png',
    'delete_fields': 'res/images/tango/delete_fields.png',
    'create': 'res/images/tango/create.png',
    'read': 'res/images/tango/read.png',
    'delete': 'res/images/tango/delete.png',
    'update': 'res/images/tango/update.png',
    'license': 'res/images/tango/license.png',
    'about': 'res/images/tango/about.png'
}

my_Id = StringVar()
my_name = StringVar()
my_surname = StringVar()
my_password = StringVar()
my_address = StringVar()


bar_menu = Menu(root)
bbdd_menu = Menu(bar_menu, tearoff=0)
delete_menu = Menu(bar_menu, tearoff=0)
crud_menu = Menu(bar_menu, tearoff=0)
help_menu = Menu(bar_menu, tearoff=0)

my_frame = Frame(root)

square_Id = Entry(my_frame, textvariable=my_Id)
square_name = Entry(my_frame, textvariable=my_name)
square_password = Entry(my_frame, textvariable=my_password)
square_surname = Entry(my_frame, textvariable=my_surname)
square_address = Entry(my_frame, textvariable=my_address)

comment_text = Text(my_frame, width=16, height=5)
vertical_scroll = Scrollbar(my_frame, command=comment_text.yview)

id_label = Label(my_frame, text='Id:')
name_label = Label(my_frame, text='Name:')
password_label = Label(my_frame, text='Password:')
surname_label = Label(my_frame, text='Surname:')
address_label = Label(my_frame, text='Address:')
comments_label = Label(my_frame, text='Comments:')

my_frame_2 = Frame(root)
