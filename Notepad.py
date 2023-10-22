from tkinter import *
from tkinter import filedialog

window = Tk()
default_title = 'Untitled'
default_extension = '.txt'
window.title(default_title + ' - Notepad')
window.geometry('500x500+400+70')
window.iconbitmap(r'D:\ProgramFiles\VS_Code\.vscode\Python\IMT_LABs\Notepad\Notepad.ico')

textbox = Text(window, width=1920, height=1080)
textbox.pack()

# Menus
my_menu = Menu(window, tearoff= False)
window.config(menu= my_menu)

# file functions
def file_new(shortcut = 0):
    window.title(default_title + ' - Notepad')
    textbox.delete(1.0, END)

def file_new_window(shortcut = 0):
    top = Toplevel()
    top.title('Untitled - Notepad')

def file_open(shortcut = 0):
    filename = filedialog.askopenfilename(title= 'Open', filetypes=(("Text Documents", "*.txt"),("All Files", "*.*")))
    with open(filename) as file:
        textbox.delete(1.0, END)
        textbox.insert(1.0, file.read())

def file_save(shortcut = 0):
   text = textbox.get(1.0, END) 
   with open(default_title + default_extension, 'w') as file:
       file.write(text)

def file_save_as(shortcut = 0):
    filename = filedialog.asksaveasfilename(title= 'Open', filetypes=(("Text Documents", "*.txt"), ("All Files", "*.*")))
    print(filename)

def file_page_setup(shortcut = 0):
    pass

def file_print(shortcut = 0):
    pass

# edit functions
def edit_undo(shortcut = 0):
    pass

def edit_cut(shortcut = 0):
    pass

def edit_copy(shortcut = 0):
    pass

def edit_paste(shortcut = 0):
    pass

def edit_delete(shortcut = 0):
    pass

def edit_search(shortcut = 0):
    pass

def edit_find(shortcut = 0):
    pass

def edit_find_next(shortcut = 0):
    pass

def edit_find_previous(shortcut = 0):
    pass

def edit_replace(shortcut = 0):
    pass

def edit_goto(shortcut = 0):
    pass

def edit_select_all(shortcut = 0):
    pass

def edit_time_date(shortcut = 0):
    pass


# Format Functions
def format_font(shortcut = 0):
    pass

def formant_word_wrap(shortcut = 0):
    pass


# View -> Zoom
def zoom_in(shortcut = 0):
    pass

def zoom_out(shortcut = 0):
    pass

def zoom_restore_default_zoom(shortcut = 0):
    pass


# Help
def help_view(shortcut = 0):
    pass

def help_send_feedback(shortcut = 0):
    pass

def help_about_notepad(shortcut = 0):
    pass

def click(shortcut = 0):
    window.title('*' + default_title + ' - Notepad')



# File menu
file = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= 'File', menu= file)
file.add_command(label=r'New                                       Ctrl+N', command= file_new)
file.add_command(label=r'New Window           Ctrl+Shift+N', command= file_new_window)
file.add_command(label=r'Open...                    Ctrl+O', command= file_open)
file.add_command(label=r'Save                       Ctrl+S', command= file_save)
file.add_command(label=r'Save As...           Ctrl+Shift+S', command= file_save_as)
file.add_separator()
file.add_command(label='Exit       ', command= window.quit)

# Edit menu
edit = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= ' Edit ', menu= edit)
edit.add_command(label= 'Undo ', command= edit_undo)
edit.add_separator()
edit.add_command(label= 'Cut ', command= edit_cut)
edit.add_command(label= 'Copy ', command= edit_copy)
edit.add_command(label= 'Paste ', command= edit_paste)
edit.add_command(label= 'Delete ', command= edit_delete)
edit.add_separator()
edit.add_command(label= 'Search with Bing... ', command= edit_search)
edit.add_command(label= 'Find... ', command= edit_find)
edit.add_command(label= 'Find Next ', command= edit_find_next)
edit.add_command(label= 'Find Previous ', command= edit_find_previous)
edit.add_command(label= 'Replace... ', command= edit_replace)
edit.add_command(label= 'Go To... ', command= edit_goto)
edit.add_separator()
edit.add_command(label= 'Select All ', command= edit_select_all)
edit.add_command(label= 'Time/Date ', command= edit_time_date)

# Format menu
format = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= 'Format ', menu= format)
format.add_command(label= 'Word Wrap ', command= formant_word_wrap)
format.add_command(label= 'Font... ', command= format_font)

# View menu
status_bar = BooleanVar()
view = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= 'View', menu= view)
zoom = Menu(view, tearoff= False)
view.add_cascade(label= 'Zoom ', menu= zoom)
zoom.add_command(label= 'Zoom In ', command= zoom_in)
zoom.add_command(label= 'Zoom Out ', command= zoom_out)
zoom.add_command(label= 'Restore Default Zoom ', command= zoom_restore_default_zoom)
view.add_checkbutton(label= 'Status Bar ', offvalue=0, onvalue=1, variable=status_bar)


# Help menu
help = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label= 'Help', menu= help)
help.add_command(label= 'View Help ', command= help_view)
help.add_command(label= 'Send Feedback ', command= help_send_feedback)
help.add_separator()
help.add_command(label= 'About Notepad ', command= help_about_notepad)

# Shortcuts
window.bind('<Control-n>',  file_new)
window.bind('<Control-N>',  file_new)
window.bind('<Control-Shift-N>',  file_new_window)
window.bind('<Control-Shift-n>',  file_new_window)
window.bind('<Control-o>',  file_open)
window.bind('<Control-O>',  file_open)
window.bind('<Control-s>',  file_save)
window.bind('<Control-S>',  file_save)
window.bind('<Control-Shift-S>',  file_save_as)
window.bind('<Control-Shift-s>',  file_save_as)

# Detect any change
window.bind('<Key>', click)


window.mainloop()