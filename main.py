import tkinter as tk
import tkinter.ttk as ttk




root = tk.Tk()
#second = tk.Tk()
n = 0
a = tk.StringVar()
a.set(n)

root.title('hello world')
root.geometry('300x150')
#second.title("second window")
#second.geometry("150x150")
photo = tk.PhotoImage(file = r"C:\tkinter_for_asus_program\file.png")
def button_event():
    global n
    n = n+1
    a.set(n)

mylabel = tk.Label(root,textvariable=a,font=('Arial',20)).pack()
mybutton = tk.Button(root, image = photo ,command=button_event,activeforeground='#f00')
mybutton.pack()

combo = ttk.Combobox(root,value=[1,2,3]).pack()

root.mainloop()