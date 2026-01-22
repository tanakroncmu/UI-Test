from tkinter import *

root = Tk() ### สร้าง
root.title("Demo App")

def SM1 (): ### รับ Command มาจากปุ่ม btb11 = Button(root,text="Select Music" จาก หน้า root window
    global SM
    SM = 1
    print("SM1ก็รันนะ") ##
    selectMusic() ## สั่ง selectMusic()

def selectMusic(): ### รับ Command มาจาก def SM1 ():
    global language
    ## ส่วนหน้า UI ของ window ย่อย
    Window2 = Tk()                   # สร้าง window ย่อย
    Window2.title("Window2")            # ชื่อ window ย่อย
    Window2.geometry("475x500+300+200")  # กำหนดขนาด window ย่อย
    ##ส่วนของ Radiobutton ใน window ย่อย
    language = IntVar()     # language - ตั้งเป็นตัวแปรสำหรับใช้ในการรับค่าจาก Radiobutton ทั้ง 3 ตัวเลือกใน  window ย่อย
    language.set(1)         # language ตั้งค่าเริ่มต้นไว้ที่ 1
    Radiobutton(window2,text="1. The Kid LAROI, Justin Bieber - STAY",variable=language, value=1,command=SendVariable).place(x=20, y=80)
    Radiobutton(window2,text="2. LISA - BORN AGAIN feat. Doja Cat & RAYE)",variable=language, value=2,command=SendVariable).place(x=20, y=120)
    Radiobutton(window2,text="3. John Martin - Anywhere For You",variable=language, value=3,command=SendVariable).place(x=20, y=160)

def SendVariable(): ### รับ command จาก Radiobutton ทั้ง 3 ตัวเลือกจาก UI ของ window ย่อย
    global language,languageNum
    ## แสดงผล print ค่า language กับ languageNum ออกมาเพื่อเช็คว่า การเลือก Radiobutton จากใน window ย่อย
    print("Check language = ",language)
    languageNum= language.get()
    print("Check languageNum =",languageNum)

## ส่วนหน้า UI ของ root window
btb11 = Button(root,text="Select Music", fg="black",command=SM1 , width=15, height=1).place(x=50, y=115)

#กำหนดขนาด UI ของ root window
root.geometry("500x700+800+200")
root.mainloop()



