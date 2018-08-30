
from tkinter import *
ret = []
def add():
    
    def input_data(event):
        global ret
        ret =[space1.get(),space2.get(),space3.get(),space4.get(),space5.get(),space6.get()]
        ret = list(map(float,ret))
        
        root.destroy()
        
    root = Tk()
    label = Label(root,text="Wholesale Data Update")
    label1=Label(root,text="Fresh: ")
    label2=Label(root,text="Milk: ")
    label3=Label(root,text="Grocery: ")
    label4=Label(root,text="Frozen: ")
    label5=Label(root,text="Detergents_Paper:")
    label6=Label(root,text="Delicatessen:")
    label.grid(row=0,sticky="E")
    label1.grid(row=1,column=0,sticky="E")
    label2.grid(row=2,column=0,sticky="E")
    label3.grid(row=3,column=0,sticky="E")
    label4.grid(row=4,column=0,sticky="E")
    label5.grid(row=5,column=0,sticky="E")
    label6.grid(row=6,column=0,sticky="E")
    space1=Entry(root)
    space2=Entry(root)
    space3=Entry(root)
    space4=Entry(root)
    space5=Entry(root)
    space6=Entry(root)
    space1.grid(row=1,column=1)
    space2.grid(row=2,column=1)
    space3.grid(row=3,column=1)
    space4.grid(row=4,column=1)
    space5.grid(row=5,column=1)
    space6.grid(row=6,column=1)
    
    sub = Button(text="Submit")
    sub.grid(row=7,column=1,sticky="E")


    sub.bind("<Button-1>",input_data)

    space1.bind("<Button-1>")
    space2.bind("<Button-1>")
    space3.bind("<Button-1>")
    space4.bind("<Button-1>")
    space5.bind("<Button-1>")
    space6.bind("<Button-1>")

    root.mainloop()
    return ret


