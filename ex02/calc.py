import tkinter as tk
import tkinter.messagebox as tkm




def button_click(event):
    btn = event.widget
    num = btn["text"]
    ans = 0.0

    if num == "=":
        siki= entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    elif num=="AC":               #Cを押すことにより数字全消去
        entry.delete(0,tk.END)
               

    else:

        entry.insert(tk.END,num)
    #tkm.showinfo("", f"{num}ボタンがクリックされました")



root = tk.Tk()

root.geometry("380x500")
root.configure(bg="black")

entry=tk.Entry(root,justify="right",width=14,font=("",40),bg="gainsboro")
entry.grid(row=0,column=0,columnspan=5)


r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
y,x=1,4
operators =["+","-","*","="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",width=4, height=2, font=("", 30))
    button["bg"]='#F0F8FF'
    button["fg"]='#FF4500'
    button.grid(row=y, column=x)
    button.bind("<1>", button_click)
    y += 1


option=["/","AC"]
for opu in option:
    button = tk.Button(root, text=f"{opu}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button["bg"]='#F0F8FF'
    button["fg"]='#FF4500'
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
    


root.mainloop()