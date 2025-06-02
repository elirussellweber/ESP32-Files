from cam import CameraBoard
from comms import Comms

cam = CameraBoard(os)
comms = Comms()

def get_photo():
    time = cam.get_time()
    buf = cam.take_photo(time)
    return buf
    
def main():
    img = get_photo()
    print(img)
    
main()
