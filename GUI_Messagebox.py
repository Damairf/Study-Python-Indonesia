# Message Box
from tkinter import *
from tkinter import messagebox

window = Tk()

def info_cmd():
    messagebox.showinfo(title="Info Message Box",
                        message="Ini adalah Info box")
    
def warning_cmd():
    messagebox.showwarning(title="Warning Message Box",
                           message="Ini adalah Warning box")

def error_cmd():
    messagebox.showerror(title="Error Message Box",
                           message="Ini adalah Error box")
    
def okcancel_cmd():
    if messagebox.askokcancel(title="Ok Cancel Message Box",
                           message="Ini adalah Ok Cancel box"):
        print("Kamu menekan OK")
    else:
        print("Kamu menekan Cancel")
        
def retry_cmd():
    if messagebox.askretrycancel(title="Retry Message Box",
                                 message="Ini adalah Retry box"):
        print("Kamu menekan Retry")
    else:
        print("Kamu menekan Cancel")
        
def yesorno_cmd():
    if messagebox.askyesno(title="Yes No Message Box",
                           message="Ini adalah Yes No box"):
        print("Kamu menekan Yes")
    else:
        print("Kamu menekan No")
        
def question_cmd():
    jawaban = messagebox.askquestion(title="Question Message Box",
                                     message="Ini adalah Question box")
    if jawaban == "yes":
        print("Kamu menekan Yes")
    else:
        print("Kamu menekan No")
        
def yesnocancel_cmd():
    masukan = messagebox.askyesnocancel(title="Yes No Cancel Message Box",
                                        message="Ini adalah Yes No Cancel box", icon='warning')
    if masukan == True:
        print("Kamu menekan Yes")
    elif masukan == False:
        print("Kamu menekan No")
    else:
        print("Kamu menekan Cancel")
        
info_btn = Button(window,
                command=info_cmd,
                text="INFO")
info_btn.pack()

warning_btn = Button(window,
                command=warning_cmd,
                text="WARNING")
warning_btn.pack()

error_btn = Button(window,
                command=error_cmd,
                text="ERROR")
error_btn.pack()

okcancel_btn = Button(window,
                command=okcancel_cmd,
                text="OK/CANCEL")
okcancel_btn.pack()

retry_btn = Button(window,
                command=retry_cmd,
                text="RETRY")
retry_btn.pack()

yesorno_btn = Button(window,
                command=yesorno_cmd,
                text="YES/NO")
yesorno_btn.pack()

question_btn = Button(window,
                command=question_cmd,
                text="QUESTION")
question_btn.pack()

yesnocancel_btn = Button(window,
                command=yesnocancel_cmd,
                text="YES/NO/CANCEL")
yesnocancel_btn.pack()

window.mainloop()