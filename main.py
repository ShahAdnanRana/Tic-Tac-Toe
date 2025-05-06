from tkinter import *
from tkinter import messagebox

root=Tk()

root.geometry("535x660+0+0")
root.title("Game")
root.resizable(False,False)
root.configure(background='powder blue')
button=StringVar()

i=1
def check(button1):
    global i
    if button1['text']=="" and i==1:
        button1['text']='X'
        i=i+1
        winner()

    elif button1['text']=="" and i==2:
        button1['text']='O'
        i=i-1
        winner()

def winner():
    if btn1['text']== 'X' and btn2['text']== 'X' and btn3['text']== 'X':
        btn1.configure(background='powder Blue')
        btn2.configure(background='powder Blue')
        btn3.configure(background='powder Blue')

        messagebox.showinfo("Winner is X" , "O is defeated by X")

    elif btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
        btn4.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn6.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
        btn7.configure(background='powder Blue')
        btn8.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
        btn1.configure(background='powder Blue')
        btn4.configure(background='powder Blue')
        btn7.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
        btn2.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn8.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
        btn3.configure(background='powder Blue')
        btn6.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
        btn1.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")

    elif btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
        btn3.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn7.configure(background='powder Blue')

        messagebox.showinfo("Winner is X", "O is defeated by X")


    elif btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
        btn1.configure(background='powder Blue')
        btn2.configure(background='powder Blue')
        btn3.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
        btn4.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn6.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
        btn7.configure(background='powder Blue')
        btn8.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
        btn1.configure(background='powder Blue')
        btn4.configure(background='powder Blue')
        btn7.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
        btn2.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn8.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
        btn3.configure(background='powder Blue')
        btn6.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
        btn1.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn9.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
        btn3.configure(background='powder Blue')
        btn5.configure(background='powder Blue')
        btn7.configure(background='powder Blue')

        messagebox.showinfo("Winner is O", "X is defeated by O")

    elif all(btn['text'] != "" for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]):
        messagebox.showinfo("TIE", "It's a tie! Try again!")


def reset():
    btn1['text'] = ""
    btn2['text'] = ""
    btn3['text'] = ""
    btn4['text'] = ""
    btn5['text'] = ""
    btn6['text'] = ""
    btn7['text'] = ""
    btn8['text'] = ""
    btn9['text'] = ""

    btn1.configure(background='gainsboro')
    btn2.configure(background='gainsboro')
    btn3.configure(background='gainsboro')
    btn4.configure(background='gainsboro')
    btn5.configure(background='gainsboro')
    btn6.configure(background='gainsboro')
    btn7.configure(background='gainsboro')
    btn8.configure(background='gainsboro')
    btn9.configure(background='gainsboro')

mainframe=Frame(root,height=520,width=600)
mainframe.place(x=0,y=0)

btn1=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn1))
btn1.grid(row=1,column=0,sticky=S+N+E+W)

btn2=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn2))
btn2.grid(row=1,column=1,sticky=S+N+E+W)

btn3=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn3))
btn3.grid(row=1,column=2,sticky=S+N+E+W)

btn4=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn4))
btn4.grid(row=2,column=0,sticky=S+N+E+W)

btn5=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn5))
btn5.grid(row=2,column=1,sticky=S+N+E+W)

btn6=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn6))
btn6.grid(row=2,column=2,sticky=S+N+E+W)

btn7=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn7))
btn7.grid(row=3,column=0,sticky=S+N+E+W)

btn8=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn8))
btn8.grid(row=3,column=1,sticky=S+N+E+W)

btn9=Button(mainframe,text="",font=('comic sans ms',26,'bold'),height=3,width=8,bg='gainsboro',command=lambda:check(btn9))
btn9.grid(row=3,column=2,sticky=S+N+E+W)

btn_reset=Button(mainframe,text="RESET",font=("comic sans ms",26,'bold'),height=1,width=20,bg='gainsboro',command=lambda:reset())
btn_reset.place(x=60,y=560)

root.mainloop()
