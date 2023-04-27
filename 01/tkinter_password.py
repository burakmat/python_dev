from tkinter import *
pencere=Tk()
def girisyapma():
    global durum
    alinanPw= pwGiris.get()
    alinanNick= nickGiris.get()
    if alinanNick == "Burak" and alinanPw == "160601":
        durum.config(text="Correct",bg="green")
    else:
        durum.config(text="Incorrect",bg="red")
alinanPw = Label(pencere, text="Password")
alinanPw.grid(row=1,column=0)
pwGiris=Entry(pencere,width="8",show="*")
pwGiris.grid(row=1,column=1)
alinanNick=Label(pencere,text="Nickname")
alinanNick.grid(row=0,column=0)
nickGiris=Entry(pencere,width="8")
nickGiris.grid(row=0,column=1)
rememberPw=Checkbutton(pencere,text="Remember my password.")
rememberPw.grid(row=2,columnspan=2)
enter=Button(pencere,text="Enter", command=girisyapma)
enter.grid(row=3,column=0)
durum=Label(pencere)
durum.grid(row=3,column=1)
pencere.geometry("250x100")
pencere.mainloop()