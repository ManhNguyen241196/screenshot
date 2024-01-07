from datetime import datetime
from PIL import ImageGrab
import pathlib

def snapShot_handle(t,l,b,r):
    
    ss_region = (t, l, b, r)
    ss_img = ImageGrab.grab(ss_region)
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time.replace(":", ""))
    name_img = 'snapShot' + current_time.replace(":", "")
    link = pathlib.Path(__file__).parent.resolve()
    path_save = pathlib.PurePath(link).joinpath(f'{name_img}.jpg')
    ss_img.save(str(path_save))
