

class CANMsg:

    __msgId = 0
    __msgData = 0
    __msgLen = 0

    def __init__(self, msgId, data, len) -> None:
        self.__msgId = msgId
        self.__msgData = data
        self.__msgLen = len

    def getMsgId(self):
        return self.__msgId

    def getMsgData(self):
        return self.__msgData

    def getMsgLen(self):
        return self.__msgLen
