import pyautogui
from tkinter import *
from main_snapshot import snapShot_handle

# định nghĩa chương trình chính
root = Tk()
root.geometry("300x100")
root.title("Capture Screen")


#frame
Input_frame = Frame(root)
Input_frame.grid(row=0,column=0)

#label
Top = Label(Input_frame,text="Top")
Top.grid(row=0,column=0)
Left= Label(Input_frame,text="Left")
Left.grid(row=0,column=1)
Bottom = Label(Input_frame,text="Bottom")
Bottom.grid(row=0,column=2)
Right = Label(Input_frame,text="Right")
Right.grid(row=0,column=3)

#input
w, s = pyautogui.size()

Top_entry = Entry(Input_frame,  width=10)
Top_entry.insert(0,0)
Top_entry.grid(row=1,column=0)

Left_entry = Entry(Input_frame, width=10)
Left_entry.grid(row=1,column=1)
Left_entry.insert(0,0)

Bottom_entry = Entry(Input_frame, width=10)
Bottom_entry.grid(row=1,column=2)
Bottom_entry.insert(0,w)

Right_entry = Entry(Input_frame, width=10)
Right_entry.grid(row=1,column=3)
Right_entry.insert(0,s)


def printCorr():
    
    Corr_render = {"Top": Top_entry.get(),
                "Left": Left_entry.get(),
                "Bottom": Bottom_entry.get(),
                "Right": Right_entry.get()
                }
    
    print(Corr_render)
    (t,l,b,r) = (float(Corr_render["Top"]), float(Corr_render["Left"]), float(Corr_render["Bottom"]), float(Corr_render["Right"]))
    snapShot_handle(t,l,b,r)
        
    

submitBtn = Button(root, text="Take a shot",
                  activebackground='#78d6ff',
                  activeforeground='#ff0000',
                  command=printCorr)
submitBtn.grid(row=1,column=0)



#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()