import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("AMAZON FORM")
l1=tk.Label(root,text="First Name",
           font=("Times New Roman",20))
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
l2=tk.Label(root,text="Last Name",
           font=("Times New Roman",20))
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
e2.grid()

l3=tk.Label(root,text="Item Name",
           font=("Times New Roman",20))
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",20),width=25,)
e3.grid()

l5=tk.Label(root,text="Select site of ad ",font=("Times New Roman",15))
l5.grid()

clicked= tk.StringVar()
drop=tk.OptionMenu(root,clicked,"Youtube.com","Instagram.com")
drop.grid()
l4=tk.Label(root,text="",
           font=("Times New Roman",20))
l4.grid()

def submit():

    if(e1.get()=="" and e2.get()==""):
        l4["text"]=" Please Enter Appropriate Data "
    elif(e3.get()==""):
        l4["text"]="* Please Enter Appropriate Data"
    else:
        try:
            f=open("data.txt","+w")
            f.writelines(["First Name="+e1.get()+"\n"])
            f.writelines(["Surname Name="+e2.get()+"\n"])
            f.writelines(["Item Name="+e3.get()+"\n"])
            f.writelines(["Name Of The Site="+clicked.get()])
            f.close()
        except IOError:
            print("Form Data Storage Failed")
        wb.open("https://www.flipkart.com/")
    
b=tk.Button(root,text="SUBMIT",font=("TIMES NEW ROMAN",15),
            command=submit,bg="green",
            activebackground="black")
b.grid()
tk.mainloop()