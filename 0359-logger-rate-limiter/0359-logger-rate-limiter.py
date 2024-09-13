class Logger(object):

    def __init__(self):
        self.hashmap = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        elif message in self.hashmap and self.hashmap[message] <= timestamp - 10:
            self.hashmap[message] = timestamp
            return True
        
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)