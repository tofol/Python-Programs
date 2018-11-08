from functions.functions import *


__author__ = 'Painkillers'
__email__ = 'author@hotmail.com'
__title__ = 'App BBDD'
__date__ = '4 / 11 / 2018'
__version__ = '1.0.0'
__license__ = 'GNU GPLv3'


root.title(__title__ + ' ' + __version__)
root.iconbitmap(default='res/images/idleplus.ico')
root.geometry('300x350+0+0')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)
root.config(menu=bar_menu, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
root.minsize(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
root.option_add('*Font', 'Helvetica 10')  # Default font
root.tk_setPalette(background='#272822')
root.option_add('*tearOff', False)  # No float submenus
connect_icon = load_icons(app_icons['connect'])
quit_icon = load_icons(app_icons['quit'])
delete_fields_icon = load_icons(app_icons['delete_fields'])
bbdd_menu.add_command(label='Connect', underline=0, image=connect_icon, compound='left',
                      command=connection_bbdd, accelerator='Alt+F1')
bbdd_menu.add_command(label='Quit', underline=0, image=quit_icon, compound='left',
                      command=out_application, accelerator='Alt+F4')
delete_menu.add_command(label='Delete Fields', underline=0, image=delete_fields_icon, compound='left',
                        command=clean_fields, accelerator='Alt+F2')
root.bind('<Alt-F1>', lambda event: connection_bbdd())
root.bind('<Alt-F4>', lambda event: out_application())
root.bind('<Alt-F2>', lambda event: delete())

label_crud = ('Create', 'Read', 'Update', 'Delete')
command_crud = (create, read, update, delete)
my_toolbar()
crud_images = (create_icon, read_icon, update_icon, delete_icon)
for i in range(len(label_crud)):
    crud_menu.add_command(label=label_crud[i], underline=0, image=crud_images[i], compound='left',
                          command=command_crud[i])

license_icon = load_icons(app_icons['license'])
about_icon = load_icons(app_icons['about'])
help_menu.add_command(label='License', underline=0, image=license_icon, compound='left', command=window_license)
help_menu.add_command(label='About ...', underline=0, image=about_icon, compound='left', command=window_about)

label_bar_menu = ('BBDD', 'Delete', 'Crud', 'Help')
menu_bar_menu = (bbdd_menu, delete_menu, crud_menu, help_menu)
for i in range(len(label_bar_menu)):
    bar_menu.add_cascade(label=label_bar_menu[i], underline=0, compound='left', menu=menu_bar_menu[i])

# ---------------- STARTING FIELDS ------------------
my_frame.pack()
squares = (square_Id, square_name, square_password, square_surname, square_address, comment_text)
for i in range(len(squares)):
    squares[i].grid(row=i, column=1, padx=10, pady=10)
for i in range(len(squares) - 1):
    squares[i].config(justify='right')
square_password.config(show='*')

vertical_scroll.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')
comment_text.config(yscrollcommand=vertical_scroll.set)

# -----------------------LABELS---------------------------
label_names = (id_label, name_label, password_label, surname_label, address_label, comments_label)
for i in range(len(label_names)):
    label_names[i].grid(row=i, column=0, sticky='e', padx=10, pady=10)

root.mainloop()
