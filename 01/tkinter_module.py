from tkinter import messagebox
import tkinter
pencere = tkinter.Tk()
#rakam1 = tkinter.Button(text="s",bg="red",fg="black")
#rakam1.pack(side="bottom")
#yazi=tkinter.Label(text="LOL")
#yazi.pack()
pencere.geometry("500x250")
#pencere.mainloop()
def hello():
    tkinter.messagebox.showinfo("aaaaaa","b")
B1=tkinter.Button(pencere, text="bba", command=hello)
B1.place(x=250,y=125)
pencere.mainloop()