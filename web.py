import tkinter as tk 
import webbrowser as wb 
obj=tk.Tk()

e=tk.Entry(obj,font=("TImes new Roman",30),width=30)
e.grid()
def search():
    query=str(e.get())
    query = query.replace(' ', '+')
    wb.open(f'https://www.w3schools.com/={query}')

    
    
b=tk.Button(obj,text="Close",font=("Times New Roman",30),command=obj.destroy)
b1=tk.Button(obj,text="Search",font=("Times New Roman",30),command=search)
b.grid(row=3)
b1.grid(row=2)

obj.mainloop()

