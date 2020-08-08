

from com.nio.model.CANModel import *

class CANControl:
    def __init__(self) -> None:
        self.model = CANModel()

    def init(self):
        pass

    def unInit(self):
        pass

    def sendDataToControl(self, CANMsg):
        print('CANControl.sendDataToModel')
        print(CANMsg.getMsgId())
        print(CANMsg.getMsgLen())
        print(CANMsg.getMsgData())
        self.model.sendDataToCAN(CANMsg)


    def rec(self, CANMsg):
        pass