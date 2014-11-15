# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:37:06 2014

@author: Tobal
"""

import os as os
import tkinter.messagebox
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from PIL import Image, ImageTk


myfonts = {'times': 'times 18 bold', 'verdana': 'Verdana 10'}
fileicons = {
    'new': 'images/file/filenew.png',
    'close': 'images/file/fileclose.png',
    'closeall': 'images/file/filecloseall.png',
    'import': 'images/file/fileimport.png',
    'open': 'images/file/fileopen.png',
    'save': 'images/file/filesave.png',
    'saveas': 'images/file/filesaveas.png',
    'saveall': 'images/file/save_all.png',
    'print': 'images/file/print.png',
    'exit': 'images/file/exit.png'
}
editicons = {
    'copy': 'images/actions/editcopy.png',
    'cut': 'images/actions/editcut.png',
    'paste': 'images/actions/editpaste.png',
    'redo': 'images/actions/redo.png',
    'undo': 'images/actions/undo.png',
    'selectall': 'images/actions/selectall.png'
}
mypatterns = [('Python', '*.py'), ('Python', '*.pyw'), ('All Files', '*.*')]


class IdlePlus(tk.Frame):

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent, class_='IdlePlus')
        parent.iconbitmap(default='images/idleplus.ico')
        self.master = parent
        self.master.title('IDLE Plus')
        # Maximize window
        self.screenWidth = self.master.winfo_screenwidth() - 5
        self.screenHeight = self.master.winfo_screenheight() - 100
        self.master.geometry('%dx%d+%d+%d' % (self.screenWidth,
                                              self.screenHeight, 0, 0))
        self.master.resizable(1, 1)
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.style.configure('TSeparator', bg='white')
        self.style.configure('TFrame', relief='raised', background='#272822')
        self.style.configure('TScrollbar', background='black',
                             activebackground='black', troughcolor='black', highlightbackground='black')
        self.style.configure('TScrollbar.TArrows', background='black')
        self.style.map('TScrollbar', background=[('!focus', 'black')], troughcolor=[
                       ('!focus', 'black')], highlightbackground=[('!focus', 'black')], activebackground=[('!focus', 'black')])
        self.style.configure('TNotebook', background='#272822', padding='0.1i')
        self.style.configure('TNotebook.Tab',
                             background='#272822', foreground='white')
        self.style.map('TNotebook.Tab', background=[
                       ('selected', '#272822')], foreground=[('selected', 'white')])
        self.master.configure(bg='#272822')

        self.master.bind('<Control-q>', self.idleplusQuit)
        self.master.bind('<Control-o>', self.myfileOpen)
        self.master.bind('<Control-n>', self.mynewFile)
        self.master.bind('<Control-s>', self.mysaveFile)
        self.master.bind('<Control-Shift-s>', self.mysaveAs)
        self.master.bind('<Control-x>', self.cut)
        self.master.bind('<Control-c>', self.copy)
        self.master.bind('<Control-v>', self.paste)
        self.master.bind('<Control-a>', self.select_all)
        self.master.bind('<Alt-f>', self.myBarMenu())
        self.master.bind('<Alt-e>', self.myBarMenu())
        self.master.bind('<Alt-h>', self.myBarMenu())

        self.myBarMenu()
        self.myToolBar()
        self.myNoteBook()
        self.statusBar()

    def myfileOpen(self, event=None):
        self.myfile = tk.filedialog.askopenfile(filetypes=mypatterns,
                                                title='Open a Python file', mode='rb+')
        loadedfile = self.myfile.read()
        loadedfile = loadedfile.decode('utf-8')
        base, ext = os.path.splitext(os.path.basename(self.myfile.name))
        self.myfile.close()
        self.textView.insert(index='current linestart', chars=loadedfile)
        self.make_frame_notebook(self.notebook, (base, ext))

    def mynewFile(self, event=None):
        self.filename = 'Untitled.py'
        self.textView.delete(0.0, tk.END)
        self.notebook.tab(0, text=self.filename)

    def mysaveFile(self, event=None):
        self.mysavefile = tk.filedialog.asksaveasfilename(filetypes=mypatterns,
                                                          title='Saving a Python file',
                                                          defaultextension='.py', initialfile=self.myfile.name)
        self.t = self.textView.get(0.0, tk.END)
        loadfile = self.mysavefile.write(self.t)
        loadfile = loadfile.decode('utf-8')
        self.mysavefile.close()

    def mysaveAs(self, event=None):
        self.myfile = tk.filedialog.asksaveasfile(filetypes=mypatterns,
                                                  title='Saving a file with name', mode='wb+',
                                                  defaultextension='.py')
        self.t = self.textView.get(0.0, tk.END)
        try:
            self.myfile.write(self.t.rstrip())
        except:
            tk.messagebox.showerror(title='Error',
                                    message='Unable to save file...')

    def cut(self, event=None):
        self.textView.event_generate('<<Cut>>')
        return 'break'

    def copy(self, event=None):
        if not self.textView.tag_ranges('sel'):
            return
        self.textView.event_generate('<<Copy>>')
        return 'break'

    def paste(self, event=None):
        self.textView.event_generate('<<Paste>>')
        self.textView.see('insert')
        return 'break'

    def select_all(self, event=None):
        self.textView.tag_add('sel', '1.0', 'end-1c')
        self.textView.mark_set('insert', '1.0')
        self.textView.see('insert')
        return 'break'

    def make_frame_notebook(self, widget_notebook=None, mytext=None):
        widget_notebook.add(ttk.Frame(widget_notebook), text=mytext)

    def myNoteBook(self):
        self.notebook = ttk.Notebook(self.master, width=self.screenWidth,
                                     height=self.screenHeight)
        self.notebook.enable_traversal()
        self.framenotebook = ttk.Frame(self.notebook)
        self.notebook.add(self.framenotebook, text='Untitled.py')
        self.notebook.pack(side='top', expand='yes', fill='both')
        self.scrollbarView = ttk.Scrollbar(self.framenotebook,
                                          orient='vertical', takefocus=False)
        self.textView = tk.Text(self.framenotebook, bg='#272822', fg='white',
                                wrap='word', highlightthickness=0,
                                insertbackground='white')
        self.textView.bind('<KeyRelease>', self.get_position)
        self.textView.focus()
        self.scrollbarView.config(command=self.textView.yview)
        self.textView.config(yscrollcommand=self.scrollbarView.set)
        self.scrollbarView.pack(side='right', fill='y')
        self.myseparator = ttk.Separator(self.textView, orient='vertical')
        self.myseparator.place(relx=0.8, height=self.screenHeight, width=0.5)
        self.textView.pack(side='left', expand='yes', fill='both')

    def loadIcons(self, image_icon):
        self.img = Image.open(image_icon)
        self.img = ImageTk.PhotoImage(self.img)
        return self.img

    def myBarMenu(self, event=None):
        self.mymenubar = tk.Menu(self.master)

        self.filemenu = tk.Menu(self.mymenubar, tearoff=0, bg='#272822',
            fg='white', activebackground='orange')
        self.newicon = self.loadIcons(fileicons['new'])
        self.filemenu.add_command(label='New File', underline=0,
                                  compound='left', image=self.newicon, accelerator='CTRL+N',
                                  command=self.mynewFile)
        self.openicon = self.loadIcons(fileicons['open'])
        self.filemenu.add_command(label='Open File', underline=0,
                                  compound='left', image=self.openicon, accelerator='CTRL+O',
                                  command=self.myfileOpen)
        self.filemenu.add_separator()
        self.saveicon = self.loadIcons(fileicons['save'])
        self.filemenu.add_command(label='Save File', underline=0,
                                  compound='left', image=self.saveicon, accelerator='CTRL+S',
                                  command=self.mysaveFile)
        self.saveasicon = self.loadIcons(fileicons['saveas'])
        self.filemenu.add_command(label='Save As...', compound='left',
                                  image=self.saveasicon, accelerator='CTRL+SHIFT+S',
                                  command=self.mysaveAs)
        self.closeicon = self.loadIcons(fileicons['close'])
        self.filemenu.add_command(label='Close File', underline=0,
                                  compound='left', image=self.closeicon, accelerator='ALT+F4')
        self.filemenu.add_separator()
        self.printicon = self.loadIcons(fileicons['print'])
        self.filemenu.add_command(label='Print File', underline=0,
                                  compound='left', image=self.printicon, accelerator='CTRL+P')
        self.filemenu.add_separator()
        self.exiticon = self.loadIcons(fileicons['exit'])
        self.filemenu.add_command(label='Exit', underline=0, compound='left',
                                  image=self.exiticon, accelerator='CTRL+Q', command=self.idleplusQuit)
        self.mymenubar.add_cascade(label='File', menu=self.filemenu,
                                   underline=0)

        self.editmenu = tk.Menu(self.mymenubar, tearoff=0, bg='#272822',
            fg='white', activebackground='orange')
        self.undoicon = self.loadIcons(editicons['undo'])
        self.editmenu.add_command(label='Undo', underline=0, compound='left',
            image=self.undoicon, accelerator='CTRL+Z')
        self.redoicon = self.loadIcons(editicons['redo'])
        self.editmenu.add_command(label='Redo', underline=0, compound='left',
            image=self.redoicon, accelerator='CTRL+SHIFT+Z')
        self.copyicon = self.loadIcons(editicons['copy'])
        self.editmenu.add_command(label='Copy', underline=0, compound='left',
            image=self.copyicon, accelerator='CTRL+C', command=self.copy)
        self.cuticon = self.loadIcons(editicons['cut'])
        self.editmenu.add_command(label='Cut', underline=0, compound='left',
            image=self.cuticon, accelerator='CTRL+X', command=self.cut)
        self.pasteicon = self.loadIcons(editicons['paste'])
        self.editmenu.add_command(label='Paste', underline=0, compound='left',
            image=self.pasteicon, accelerator='CTRL+V', command=self.paste)
        self.selectallicon = self.loadIcons(editicons['selectall'])
        self.editmenu.add_command(label='Select All', underline=0,
            compound='left', image=self.selectallicon, accelerator='CTRL+A',
            command=self.select_all)
        self.mymenubar.add_cascade(label='Edit', underline=0,
            menu=self.editmenu)

        self.aboutmenu = tk.Menu(self.mymenubar, tearoff=0, bg='#272822',
            fg='white', activebackground='orange')
        self.aboutmenu.add_command(label='Help', underline=0, accelerator='F1')
        self.aboutmenu.add_command(label='About IDLE-Plus', underline=0)
        self.mymenubar.add_cascade(label='Help', underline=0,
            menu=self.aboutmenu)

        self.master.configure(menu=self.mymenubar)

    def myToolBar(self, event=None):
        self.toolbar = ttk.Frame(self.master, border=1)
        self.newButton = tk.Button(self.toolbar, image=self.newicon,
            relief='sunken', bg='#272822', activebackground='#272822',
            command=self.mynewFile)
        self.newButton.pack(side='left', padx=2, pady=2)
        self.openButton = tk.Button(self.toolbar, image=self.openicon,
            relief='sunken', bg='#272822', activebackground='#272822',
            command=self.myfileOpen)
        self.openButton.pack(side='left', padx=2, pady=2)
        self.saveButton = tk.Button(self.toolbar, image=self.saveicon,
            relief='sunken', bg='#272822', activebackground='#272822',
            command=self.mysaveFile)
        self.saveButton.pack(side='left', padx=2, pady=2)
        self.saveasButton = tk.Button(self.toolbar, image=self.saveasicon,
            relief='sunken', bg='#272822', activebackground='#272822',
            command=self.mysaveAs)
        self.saveasButton.pack(side='left', padx=2, pady=2)
        self.closeButton = tk.Button(self.toolbar, image=self.closeicon,
            relief='sunken', bg='#272822', activebackground='#272822')
        self.closeButton.pack(side='left', padx=2, pady=2)
        self.toolbarseparator = ttk.Separator(self.toolbar, orient='vertical')
        self.toolbarseparator.place(relx=0.123, width=1.0, height=34)

        self.toolbar.pack(side='top', fill='x')

    def statusBar(self):
        self.frameStatus = tk.Frame(self.master, border=2, bg='#272822',
            relief='sunken')
        self.frameStatus.pack(side='bottom', after=self.toolbar,
            fill='x', padx=5, pady=1)
        numberoflinestxt = str(self.getwindowlines())
        self.labelNumberOfLines = tk.Label(self.frameStatus,
            text='Lines: {0} '.format(numberoflinestxt))
        self.labelNumberOfLines.configure(bg='#272822', fg='white')
        self.labelNumberOfLines.pack(side='right', fill='x', padx=10, pady=2)
        self.labelLinePosition = tk.Label(self.frameStatus,
            text=self.get_position(event=None))
        self.labelLinePosition.configure(bg='#272822', fg='white')
        self.labelLinePosition.pack(side='left', fill='x', padx=10, pady=2)


    def idleplusQuit(self, event=None):
        if tk.messagebox.askokcancel('Quit', 'Do you really want to exit?',
                                     parent=self.master):
            self.master.destroy()

    def get_position(self, event=None):
        """get the line and column number of the text insertion point"""
        self.line, self.column = self.textView.index('insert').split('.')
        self.s = ('Line : {0} - Column : {1}'.format(self.line, self.column))
        print(self.s)
        return self.s

    def getwindowlines(self, event=None):
        self.numberoflines = int(self.textView.index('end-1c').split('.')[0])
        return self.numberoflines


window = tk.Tk()
myapp = IdlePlus(window)
myapp.pack()
window.mainloop()
