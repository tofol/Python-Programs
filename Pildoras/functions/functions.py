import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

__author__ = 'Painkillers'
__email__ = 'author@hotmail.com'
__title__ = 'App BBDD'
__date__ = '4 / 11 / 2018'
__version__ = '1.0.0'
__license__ = 'GNU GPLv3'

root = Tk()

from constants_and_variables.constants_variables import *


def load_icons(image_icon):
    return ImageTk.PhotoImage(file=image_icon)


def connection_bbdd():
    my_connection = sqlite3.connect('Usuarios')
    my_cursor = my_connection.cursor()
    try:
        my_cursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)
            )
        ''')
        messagebox.showinfo('BBDD', 'BBDD done with success.')
    except(RuntimeError, TypeError, NameError, ValueError):
        messagebox.showwarning('Warning!', 'The database already exists.')


def out_application():
    value = messagebox.askquestion('Exit', 'Do you want to go out of the application?')
    if value == 'yes':
        root.destroy()


def clean_fields():
    my_Id.set('')
    my_name.set('')
    my_surname.set('')
    my_password.set('')
    my_address.set('')
    comment_text.delete(1.0, END)


def create():
    my_connection = sqlite3.connect('Usuarios')
    my_cursor = my_connection.cursor()
    data = my_name.get(), my_password.get(), my_surname.get(), my_address.get(), comment_text.get("1.0", END)
    my_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, ?, ?, ?, ?, ?)", data)
    my_connection.commit()
    my_connection.close()
    messagebox.showinfo('BBDD', 'Register inserted with success.')


def read():
    my_connection = sqlite3.connect('Usuarios')
    my_cursor = my_connection.cursor()
    my_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + my_Id.get())
    the_user = my_cursor.fetchall()
    for user in the_user:
        my_Id.set(user[0])
        my_name.set(user[1])
        my_password.set(user[2])
        my_surname.set(user[3])
        my_address.set(user[4])
        comment_text.insert(1.0, user[5])
    my_connection.commit()
    my_connection.close()


def update():
    my_connection = sqlite3.connect('Usuarios')
    my_cursor = my_connection.cursor()
    data = my_name.get(), my_password.get(), my_surname.get(), my_address.get(), comment_text.get('1.0', END)
    my_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, "
                      "COMENTARIOS=?" + "WHERE ID=" + my_Id.get(), data)
    my_connection.commit()
    my_connection.close()
    messagebox.showinfo('BBDD', 'Register updated with success.')


def delete():
    my_connection = sqlite3.connect('Usuarios')
    my_cursor = my_connection.cursor()
    my_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + my_Id.get())
    my_connection.commit()
    my_connection.close()
    messagebox.showinfo('BBDD', 'Register deleted with success.')


create_icon = load_icons(app_icons['create'])
read_icon = load_icons(app_icons['read'])
update_icon = load_icons(app_icons['update'])
delete_icon = load_icons(app_icons['delete'])


def my_toolbar():
    button_configure = {
        'relief': 'sunken',
        'bg': '#272822',
        'activebackground': '#272822'
    }
    button_layout = {
        'side': 'left',
        'padx': 2,
        'pady': 2
    }

    toolbar = Frame(root, border=1, bg='#545a61', relief='sunken')
    create_button = Button(toolbar, image=create_icon, command=create)
    create_button.configure(**button_configure)
    create_button.pack(**button_layout)
    read_button = Button(toolbar, image=read_icon, command=read)
    read_button.configure(**button_configure)
    read_button.pack(**button_layout)
    update_button = Button(toolbar, image=update_icon, command=update)
    update_button.configure(**button_configure)
    update_button.pack(**button_layout)
    delete_button = Button(toolbar, image=delete_icon, command=delete)
    delete_button.configure(**button_configure)
    delete_button.pack(**button_layout)
    toolbar.pack(side='top', fill='x')


def window_license():
    the_license = Toplevel()
    the_license.geometry('250x350+120+120')
    the_license.resizable(width=False, height=False)
    the_license.title('About')
    the_frame = Frame(the_license, padx=10, pady=10, relief='raised')
    the_frame.pack(side='top', fill='both', expand=True)
    label_1 = Label(the_frame, text=__title__ + ' ' + __version__, fg='white')
    label_1.pack(side='top', padx=10)
    label_2 = Label(the_frame, text=__author__)
    label_2.pack(side='top', padx=10)
    label_3 = Label(the_frame, text=__license__)
    label_3.pack(side='top', padx=10)
    label_4 = Label(the_frame, text='Version 3, 29 June 2007\n')
    label_4.pack(side='top', padx=10)
    gpl_v3 = 'Copyright © 2007 Free Software\nFoundation, Inc. <https://fsf.org/>.\n' \
             'Everyone is permitted to copy and\ndistribute verbatim copies of this\n license document, ' \
             'but changing it\nis not allowed.\n\n<https://www.gnu.org/licenses/gpl.html>'
    text_1 = Text(the_frame, width=240, height=10)
    text_1.pack(side='top', padx=10)
    text_1.insert('end', gpl_v3)
    license_button = Button(the_frame, text='Quit', command=the_license.destroy)
    license_button.pack(side='top', padx=15, pady=15)
    the_license.transient(root)
    root.wait_window(the_license)


def window_about():
    about = Toplevel()
    about.geometry('250x160+120+120')
    about.resizable(width=False, height=False)
    about.title('About')
    the_frame = Frame(about, padx=10, pady=10, relief='raised')
    the_frame.pack(side='top', fill='both', expand=True)
    label_1 = Label(the_frame, text=__title__ + ' ' + __version__, fg='white')
    label_1.pack(side='top', padx=10)
    label_2 = Label(the_frame, text=__author__ + ' ' + __date__)
    label_2.pack(side='top', padx=10)
    label_3 = Label(the_frame, text=__email__)
    label_3.pack(side='top', padx=10)
    label_4 = Label(the_frame, text=__license__)
    label_4.pack(side='top', padx=10)
    about_button = Button(the_frame, text='Quit', command=about.destroy)
    about_button.pack(side='top', padx=15, pady=15)
    about.transient(root)
    root.wait_window(about)
