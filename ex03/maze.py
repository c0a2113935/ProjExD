import tkinter as tk
import maze_maker as mm


def count_up():
    global jid
    global tmr
    label["text"]=tmr
    tmr=tmr+1
    jid=root.after(1000,count_up)




def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, mx, my
    if key == "w": my -= 1
    if key == "s": my += 1
    if key == "a": mx -= 1
    if key == "d": mx += 1
        
    if maze_lst[mx][my] == 1: 
        if key == "w": my += 1
        if key == "s": my -= 1
        if key == "a": mx += 1
        if key == "d": mx -= 1

    if key == "r":
        mx, my = 1, 1

    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    label = tk.Label(root,text="-",font=("",80))
    label.pack()

    tmr = 0
    count_up()

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    tori2= tk.PhotoImage(file="fig/1.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
   
    main_proc()
    root.mainloop()