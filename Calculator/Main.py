import tkinter as tk

def text_manage(t):
    global calc
    final = calc["text"] + t

    if final.startswith("/") or final.startswith("*") or final.endswith("++") or final.endswith("--") or final.endswith("**") or final.endswith("//") or calc["text"].endswith("+") or calc["text"].endswith("-") or calc["text"].endswith("*") or calc["text"].endswith("/") or calc["text"].endswith(".") or final.startswith("."):
        
        if t == ".":
            return None
        
        if t == "+" or t == "-" or t == "/" or t == "*":
            return None

    if t == "%":
        reverseds = calc["text"][::-1]
        real = ""
        for i in reverseds:
            if i.isnumeric() or ".":
                real = i + real
            else:
                break
        try:
            percentage = int(real) / 100
            final = calc["text"].replace(real,str(percentage))
        except Exception:
            try:
                percentage = float(real) / 100.0
                final = calc["text"].replace(real,str(percentage))
            except Exception:
                calc.destroy()
                calc = tk.Label(root,text="Error",relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
                calc.grid(row=0,column=0)
                return None
    #     finds = real.find(".")
    #     if finds == -1:
    #         new = int(real)/100
    #         final = str(new)
    #     elif finds == 0:
    #         pass
    #     else: 
    #         real = real.replace(".","")
    #         new = real[0:finds-2] + "." + real[finds-2:]
    #         final = new
    if calc["text"].endswith(")"):
        if t == "+" or t == "-" or t == "*" or t == "/":
            calc.destroy()
            calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
            calc.grid(row=0,column=0)
        else:
            final = calc["text"] + "*" + t
            calc.destroy()
            calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
            calc.grid(row=0,column=0)
    elif calc["text"].isnumeric():
        if t == "(":
            final = calc["text"] + "*" + t
            calc.destroy()
            calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
            calc.grid(row=0,column=0)
        else:
            calc.destroy()
            calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
            calc.grid(row=0,column=0)
    else:
        calc.destroy()
        calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
        calc.grid(row=0,column=0)

    # if calc["text"].startswith("."):
    #     final = "00" + calc["text"] 
    #     calc.destroy()
    #     calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw",wraplength=280,justify="left")
    #     calc.grid(row=0,column=0)

def clear():
    global calc
    calc = tk.Label(root,text="",relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw")
    calc.grid(row=0,column=0)

def clear_one_char():
    global calc
    final = calc["text"][:-1]
    calc = tk.Label(root,text=final,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw")
    calc.grid(row=0,column=0)

def solver():
    global calc
    try:
        fin = str(eval(calc["text"]))
        calc = tk.Label(root,text=fin,relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw")
        calc.grid(row=0,column=0)
    except Exception:
        calc = tk.Label(root,text="Error",relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw")
        calc.grid(row=0,column=0)

root = tk.Tk()

root.iconbitmap("Icon.ico")
root.title("Calculator")
root.geometry("365x450")
root.minsize(365,450)
root.maxsize(365,450)

calc = tk.Label(root,text="",relief="ridge",font="Lucida 13",bd=4,height=4,width=39,anchor="nw")
calc.grid(row=0,column=0)

btn1 = tk.Button(text="1",font="lucida 16",command=lambda : text_manage("1"),height=2,width=5)
btn1.place(x=9,y=100)

btn2 = tk.Button(text="2",font="lucida 16",command=lambda : text_manage("2"),height=2,width=5)
btn2.place(x=80,y=100)

btn3 = tk.Button(text="3",font="lucida 16",command=lambda : text_manage("3"),height=2,width=5)
btn3.place(x=150,y=100)

btn_plus = tk.Button(text="+",font="lucida 16",bg="yellow",command=lambda : text_manage("+"),height=2,width=5)
btn_plus.place(x=220,y=100)

btn4 = tk.Button(text="4",font="lucida 16",command=lambda : text_manage("4"),height=2,width=5)
btn4.place(x=9,y=170)

btn5 = tk.Button(text="5",font="lucida 16",command=lambda : text_manage("5"),height=2,width=5)
btn5.place(x=80,y=170)

btn6 = tk.Button(text="6",font="lucida 16",command=lambda : text_manage("6"),height=2,width=5)
btn6.place(x=150,y=170)

btn_minus = tk.Button(text="-",font="lucida 16",bg="yellow",command=lambda : text_manage("-"),height=2,width=5)
btn_minus.place(x=220,y=170)

btn7 = tk.Button(text="7",font="lucida 16",command=lambda : text_manage("7"),height=2,width=5)
btn7.place(x=9,y=240)

btn8 = tk.Button(text="8",font="lucida 16",command=lambda : text_manage("8"),height=2,width=5)
btn8.place(x=80,y=240)

btn9 = tk.Button(text="9",font="lucida 16",command=lambda : text_manage("9"),height=2,width=5)
btn9.place(x=150,y=240)

btn_multi = tk.Button(text="*",font="lucida 16",bg="yellow",command=lambda : text_manage("*"),height=2,width=5)
btn_multi.place(x=220,y=240)

btn_clear = tk.Button(text="C",font="lucida 16",command=lambda:clear(),height=2,width=5)
btn_clear.place(x=9,y=310)

btn0 = tk.Button(text="0",font="lucida 16",command=lambda : text_manage("0"),height=2,width=5)
btn0.place(x=80,y=310)

btn_dot = tk.Button(text=".",font="lucida 16",command=lambda : text_manage("."),height=2,width=5)
btn_dot.place(x=150,y=310)

btn_div = tk.Button(text="/",font="lucida 16",bg="yellow",command=lambda : text_manage("/"),height=2,width=5)
btn_div.place(x=220,y=310)

btn_equal = tk.Button(text="=",font="lucida 16",bg="orange",command=lambda : solver(),height=2,width=11)
btn_equal.place(x=9,y=380)

btn_del = tk.Button(text="Back",font="lucida 16",bg="orange",command=lambda : clear_one_char(),height=2,width=10,padx=6)
btn_del.place(x=150,y=380)

# Brackets:-

btn_brac1 = tk.Button(text="(",font="Lucida 10",bg="orange",command=lambda : text_manage("("),height=7,width=8,pady=7)
btn_brac1.place(x=290,y=100)

btn_brac2 = tk.Button(text=")",font="Lucida 10",bg="orange",command=lambda : text_manage(")"),height=7,width=8,pady=7)
btn_brac2.place(x=290,y=240)

#Percentage Button:-
btn_percent = tk.Button(text="%",font="lucida 16",bg="yellow",command=lambda:text_manage("%"),height=2,width=5)
btn_percent.place(x=293,y=380)

root.mainloop()