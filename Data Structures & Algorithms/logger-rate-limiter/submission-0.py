class Logger:

    def __init__(self):
        self.last_sent = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_sent:
            if timestamp >= self.last_sent[message]:
                self.last_sent[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.last_sent[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
