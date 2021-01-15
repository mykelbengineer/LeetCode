class Logger:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_dict = collections.defaultdict()
        
​
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log_dict:
            self.log_dict[message] = timestamp + 10
            return True
        
        else:
            if self.log_dict[message] <= timestamp:
                self.log_dict[message] = timestamp + 10
                return True
            return False
 
                
​
​
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
