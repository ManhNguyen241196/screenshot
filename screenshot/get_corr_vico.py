import pyautogui
import os

check_vico = {"State": False,"Corr": None}

def get_corr_vico(window_title):
    window = pyautogui.getWindowsWithTitle(window_title)[0]  # Assuming only one window with that title
    x, y = window.left, window.top  # Top-left corner coordinates
    width, height = window.width, window.height  # Window dimensions
    return (x,y,width, height)

def check_vico_window():
    os.system('start POWERPNT.EXE') 
    all_windows = pyautogui.getAllWindows()
    # Print the title of each window
    for window_item in all_windows:
        if("PowerPoint" in window_item.title):
            print(window_item.title)
            (x,y,width, height) = get_corr_vico(window_item.title)
            check_vico.update({"State": True,"Corr": (x,y,width, height)})
            print(check_vico)
        else:
            continue

while not check_vico["State"]:
    
    check_vico_window()
    print(check_vico["State"])
    if(check_vico["State"]):
        pyautogui.alert(text='Mở thành công', title='Infor', button='OK')
