

from com.nio.control.CANControl import *
from com.nio.msg.CANMsg import *

class CANView:
    def __init__(self) -> None:
        self.ctrl = CANControl()
        print("#############")

    def initUI(self):
        pass

    def sendDataToControl(self, msgId, data, len):
        print('CANView.sendDataToControl')
        canMsg = CANMsg(msgId, data, len)
        self.ctrl.sendDataToControl(canMsg)
