import tkinter as tk


class RadioApp: # Step 3 - เรียกใช้ class run ทั้ง 2 def
    def __init__(self, root): # Step 4 def ที่ใช้สร้าง หน้าต่างย่อย window2 - สร้าง Radiobutton ทั้งหมด แล้วส่งค่าตัวแปร self ไปที่ def show_selection(self)

        window2 = tk.Toplevel(root) # เปิด window ย่อย
        window2.title("Window2")
        window2.geometry("475x500+300+200")  # กำหนดขนาด window ย่อย

        self.var = tk.StringVar(value=1)  # เก็บสถานะไว้ใน Object
        self.r1 = tk.Radiobutton(window2, text="1. The Kid LAROI, Justin Bieber - STAY", variable=self.var, value=1)            #Radiobutton1
        self.r2 = tk.Radiobutton(window2, text="2. LISA - BORN AGAIN feat. Doja Cat & RAYE)", variable=self.var, value=2)       #Radiobutton2
        self.r3 = tk.Radiobutton(window2, text="3. John Martin - Anywhere For You", variable=self.var,                          #Radiobutton3
                                 value=3)
        self.r1.place(x=20, y=80)       #PositionRadiobutton1
        self.r2.place(x=20, y=120)      #PositionRadiobutton2
        self.r3.place(x=20, y=160)      #PositionRadiobutton3

        ButtonWindow2 = tk.Button(window2, text="Show Selection", command=self.show_selection)  #ButtonWindow2 - command และส่งตัวแปร self ไปที ่def show_selection(self)
        btn.place(x=20, y=200)          #PositionButtonWindow2

    def show_selection(self):   # Step 5 - รับตัวแปร self มาจาก def __init__(self, root)
        print(self.var.get())   #พิมพ์ค่า value ของตัวแปร self



def SM1():    #Step 2 - รับคำสั่งจาก ButtonRoot
    print("SM run")
    app = RadioApp(root) # เรียก class RadioApp


root = tk.Tk()                       #Root window
root.geometry("500x700+800+200")    #ขนาดของ Root window
ButtonRoot = tk.Button(root,text="Select Music", fg="black",command=SM1 , width=15, height=1).place(x=50, y=115) # Step 1 - ปุ่มสำหรับเปิดหน้าต่างย่อยขึ้นมา
root.mainloop()                     #สร้างลูปไม่สิ้นสุด


