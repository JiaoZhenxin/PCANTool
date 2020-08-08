import threading

from com.nio.lib.PCANBasic import *
from com.nio.msg.CANMsg import *

class CANModel:
    def __init__(self) -> None:
        self.initCANChannel()
        self.createCANSendThread(200)

    # Init PCAN device
    def initCANChannel(self):
        self.objPCAN = PCANBasic()
        result = self.objPCAN.Initialize(PCAN_USBBUS1, PCAN_BAUD_500K)
        if result != PCAN_ERROR_OK:
            result = self.objPCAN.GetErrorText(result)
            print(result)
        else:
            print(result)
            print("PCAN-PIC (Ch-2) was initialized")

    def createCANSendThread(self, cycleTime):
        pass

    def stopCANSendThread(self):
        pass

    def startCANRecThread(self):
        pass

    def stopCANRecThread(self):
        pass

    # Send CAN message
    def sendDataToCAN(self, CANMsg):
        print('CANModel.sendDataToCAN')
        msg = TPCANMsg()
        msg.ID = CANMsg.getMsgId()
        msg.MSGTYPE = PCAN_MESSAGE_STANDARD
        msg.LEN = CANMsg.getMsgLen()
        # msg.DATA = CANMsg.getMsgData()
        print(CANMsg.getMsgId())
        print(CANMsg.getMsgLen())
        msgResult = self.objPCAN.Write(PCAN_USBBUS1, msg)
        if msgResult != PCAN_ERROR_OK:
            msgResult = self.objPCAN.GetErrorText(msgResult)
            print(msgResult)
        else:
            print("Message sent successfully")
        # timer = threading.Timer(0.2, self.send)
        # timer.start()

    def rec(self, CANMsg):
        pass