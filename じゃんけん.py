import tkinter as tk
import random
from PIL import Image, ImageTk

def start(button):
    lbl7.place_forget()
    btn4.place_forget()

def dispLabel(button):
    lbl4.configure(text=button.cget("text"))
    hand = ["✊", "✌", "✋"]
    lbl5.configure(text=random.choice(hand))
    judge(button)

win_count = 0
los_count = 0
def judge(button):
    global win_count, los_count
    if (button["text"] == "✊" and lbl5["text"] == "✌") or (button["text"] == "✌" and lbl5["text"] == "✋") or (button["text"] == "✋" and lbl5["text"] == "✊"):
        lbl6.configure(text="HIT!",foreground='yellow', background='black',font=("Times",50,"bold"))
        lbl6.place(x=450, y=260)
        lbl2_text = lbl2.cget("text")
        lbl2_text = lbl2_text[:-1]  
        lbl2.config(text=lbl2_text)
        win_count += 1
        if win_count == 3:
            lbl8.place(x=0, y=0)
            btn5.place(x=450, y=500)
                        
    elif (button["text"] == "✊" and lbl5["text"] == "✋") or (button["text"] == "✌" and lbl5["text"] == "✊") or (button["text"] == "✋" and lbl5["text"] == "✌"):
        lbl6.configure(text="DAMAGE",foreground='red', background='black',font=("Times",50,"bold"))
        lbl6.place(x=370, y=260)
        lbl3_text = lbl3.cget("text")
        lbl3_text = lbl3_text[:-1]  
        lbl3.config(text=lbl3_text)
        los_count += 1
        if los_count == 3:
            lbl9.place(x=0, y=0)
            btn5.place(x=450, y=500)
            
    else:
        lbl6.place_forget()

def reset_game():
    global win_count, los_count
    win_count = 0
    los_count = 0
    lbl2.config(text="CPU ■■■")
    lbl3.config(text="PLAYER ■■■")
    lbl4.config(text=" ")
    lbl5.config(text=" ")
    lbl6.place_forget()
    lbl8.place_forget()
    lbl9.place_forget()
    btn5.place_forget()
       
root = tk.Tk()
root.geometry("1000x600")
image = tk.PhotoImage(file="s.png")
image = image.subsample(4, 4)
image2 = ImageTk.PhotoImage(file="24511746.jpg")
image3 = ImageTk.PhotoImage(file="winbg.jpg")
image4 = ImageTk.PhotoImage(file="losbg.jpg")


lbl4 = tk.Label(text=" ", font=("Times",150,"bold"))
lbl5 = tk.Label(text=" ", font=("Times",150,"bold"))
lbl6 = tk.Label(text=" ")

btn = tk.Button(text="✊", command=lambda: dispLabel(btn), width=10, height=2)
btn2 = tk.Button(text="✌", command=lambda: dispLabel(btn2), width=10, height=2)
btn3 = tk.Button(text="✋", command=lambda: dispLabel(btn3), width=10, height=2)


lbl8 = tk.Label(root, image=image3)
lbl9 = tk.Label(root, image=image4)
lbl1 = tk.Label(root, image=image)
lbl2 = tk.Label(text="CPU ■■■", font=("Segoe UI Black",15))
lbl3 = tk.Label(text="PLAYER ■■■", font=("Segoe UI Black",15))
btn5 = tk.Button(root, text="NEXT", command=reset_game, width=15, height=3)

lbl7 = tk.Label(root, image=image2)
btn4 = tk.Button(text="START", command=lambda: start(btn4), width=10, height=2)

lbl1.place(x=410, y=25)
lbl2.place(x=720, y=50)
lbl3.place(x=170, y=50)
lbl4.place(x=170, y=170)
lbl5.place(x=600, y=170)
lbl7.place(x=0, y=0)

btn.place(x=375, y=450)
btn2.place(x=475, y=450)
btn3.place(x=575, y=450)
btn4.place(x=460, y=450)


root.mainloop()

