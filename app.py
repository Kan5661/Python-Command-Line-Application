import seed as db
import tkinter as tk
from tkinter import ttk

Note = db.Note

TK_SILENCE_DEPRECATION=1 

# root/pages
root = tk.Tk()
root.title('Notes')
root.resizable(False, False)

# screen size/positioning
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# button functions
def find():
    edit_heading_input.delete(0, 'end')
    edit_heading_input.insert(0, Note.get(Note.heading == find_notes_input.get()).heading)

    edit_note_input.delete('1.0', 'end')
    edit_note_input.insert(tk.END, Note.get(Note.heading == find_notes_input.get()).note)
    

def edit():
    current_note = Note.get(Note.heading == find_notes_input.get())
    current_note.heading = edit_heading_input.get()
    current_note.note = edit_note_input.get("1.0", "end-1c")
    current_note.save()
    print('note saved')

def delete():
    Note.get(Note.heading == find_notes_input.get()).delete_instance()
    edit_heading_input.delete(0, 'end')
    edit_heading_input.insert(0, '')

    edit_note_input.delete('1.0', 'end')
    edit_note_input.insert(tk.END, '')

    print('note deleted')

def create():
    Note(heading=new_heading_input.get(), note=new_note_input.get("1.0", "end-1c")).save()
    print('new note created')

# widgets
find_note = ttk.Label(root)
find_note.place(x= 500, y = 20)

find_notes_button = ttk.Button(root, text='Find notes', width=8, command=find)
find_notes_button.place(x=20, y=20)
find_notes_input = ttk.Entry(root, width=32)
find_notes_input.place(x=155, y=20)
edit_heading_input = tk.Entry(root, width=32)
edit_heading_input.place(x=20, y=65)
edit_note_input = tk.Text(root)
edit_note_input.place(x=20, y=100, width=300, height=350)
edit_button = ttk.Button(root, text='Save', command=edit)
edit_button.place(x=175, y=450)
delete_button = ttk.Button(root, text='Delete', command=delete)
delete_button.place(x=65, y=450)


new_heading_input = tk.Entry(root, width=32)
new_heading_input.place(x=370, y=65)
new_note_input = tk.Text(root)
new_note_input.place(x=370, y=100, width=300, height=350)
create_button = ttk.Button(root, text='new note', command=create)
create_button.place(x=475, y=450)


root.mainloop()