
from tkinter import *

window = Tk()
window.title('My Profile Card')
window.geometry('400x380')

title = Label(window, text='My Profile Card', fg='white', bg='purple', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text='Name : ', fg='grey', bg='black')
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg='grey', bg='black', width=30)
name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(window, text='Hobby : ', fg='grey', bg='black')
hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg='grey', bg='black', width=30)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)  

about_frame= Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me : ")
about_label.pack()

submit_button = Button(window, text='submit', fg='grey', bg='black', width=40)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()