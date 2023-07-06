import tkinter as tk
import webbrowser as wb
root=tk.Tk()
root.title("Flipcart Form")
l1=tk.Label(root,text="Enter Your Name",
           font=("Times New Roman",20))
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",20),width=25)
e1.grid()
l2=tk.Label(root,text="Phone-No.",
           font=("Times New Roman",20))
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
e2.grid()
l3=tk.Label(root,text="Enter Your USERNAME",
           font=("Times New Roman",20))
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",20),width=25)
e3.grid()
l4=tk.Label(root,text="Enter Your PASSWORD",
           font=("Times New Roman",20))
l4.grid()
e4=tk.Entry(root,font=("Times New Roman",20),width=25,)
e4.grid()
clicked= tk.StringVar()
l5=tk.Label(root,text="",
           font=("Times New Roman",30))
l5.grid()

def submit():

    if(e1.get()=="" and e2.get()==""):
        l5["text"]="* Please Enter The Information"
    elif(e3.get()=="" and e4.get()==""):
        l5["text"]="* Please Enter The Information"
    else:
        try:
            f=open("data.txt","+w")
            f.writelines(["Name="+e1.get()+"\n"])
            f.writelines(["MobileNo="+e2.get()+"\n"])
            f.writelines(["Username="+e3.get()+"\n"])
            f.writelines(["Password="+e4.get()+"\n"])
            f.writelines(["Site Name ="+clicked.get()])
            f.close()
        except IOError:
            print("Form Data Storage Failed")
        wb.open("https://affiliate.flipkart.com/login")
    
b=tk.Button(root,text="Login",font=("TIMES NEW ROMAN",15),
            command=submit,bg="lightgreen",
            activebackground="red")
b.grid()
tk.mainloop()