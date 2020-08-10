
from apscheduler.schedulers.background import BackgroundScheduler

from com.nio.lib.PCANBasic import *
from com.nio.msg.CANMsg import *

class CANModel:

    __CHANEL_NAME = PCAN_USBBUS1
    __MSG_TYPE = PCAN_MESSAGE_STANDARD
    __txQueue = {1: CANMsg(0, 1, 2), 2: CANMsg(3, 4, 5)}
    __tx_scheduler = None
    __objPCAN = None

    def __init__(self) -> None:
        # self.__initCANChannel()
        self.__tx_scheduler = BackgroundScheduler()
        self.__initCANSendThread()

    # Init PCAN device
    def __initCANChannel(self):
        self.__objPCAN = PCANBasic()
        result = self.__objPCAN.Initialize(self.__CHANEL_NAME, PCAN_BAUD_500K)
        if result != PCAN_ERROR_OK:
            result = self.__objPCAN.GetErrorText(result)
            print(result)
        else:
            print("PCAN-PIC (Ch-2) was initialized")

    def __initCANSendThread(self):
        self.__tx_scheduler.add_job(self.__canQueue1, 'interval', seconds=1, id='Queue1')
        self.__tx_scheduler.start()

    def addCANMsg(self, CANMsg):
        self.__txQueue[CANMsg.getMsgId()] = CANMsg

    def deleteCANMsg(self, CANMsg):
        self.__txQueue.pop(CANMsg.getMsgId())

    def stopCANSendThread(self):
        pass

    def startCANRecThread(self):
        pass

    def stopCANRecThread(self):
        pass

    # Send CAN message
    def sendDataToCAN(self, CANMsg):
        print('CANModel.sendDataToCAN')
        # self.__txQueue.update({CANMsg.getMsgId(), CANMsg})
        self.__txQueue.update({11: CANMsg(10, 11, 12)})

    def rec(self, CANMsg):
        pass

    ######################################### Queue function #########################################
    # Msg Queue base on cycle time
    def __canQueue1(self):
        for key in self.__txQueue:
            print(self.__txQueue[key].getMsgId())
            print(self.__txQueue[key].getMsgLen())
            if self.__objPCAN is None:
                print('Message can not be sent, it cause by PCAN obj is None')
                return
            msg = TPCANMsg()
            msg.ID = self.__txQueue[key].getMsgId()
            msg.MSGTYPE = self.__MSG_TYPE
            msg.LEN = self.__txQueue[key].getMsgLen()
            # msg.DATA = self.__txQueue[key].getMsgData()
            msgResult = self.__objPCAN.Write(self.__CHANEL_NAME, msg)
            if msgResult != PCAN_ERROR_OK:
                msgResult = self.__objPCAN.GetErrorText(msgResult)
                print(msgResult)
            else:
                print("Message2 sent successfully")