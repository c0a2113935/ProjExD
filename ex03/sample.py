import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global jid
    global tmr
    label["text"]=tmr
    tmr=tmr+1
    jid=root.after(1000,count_up)

def key_down(event):
    root.after(1000,count_up)

    key = event.keysym
 
if __name__=="__main__":
    root = tk.Tk()
    label = tk.Label(root,text="-",font=("",80))
    label.pack()
    jid = None
    tmr = 0
    root.bind("<KeyPress>",key_down)
    root.mainloop()
    

