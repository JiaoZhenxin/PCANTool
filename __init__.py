import time

from com.nio.view.CANView import *

if __name__ == '__main__':

    view = CANView()
    view.sendDataToControl(111,222,333)
    time.sleep(10)