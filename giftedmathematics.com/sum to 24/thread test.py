#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     14/01/2013
# Copyright:   (c) CHRISTOPHER_IRWIN 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay, counter):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.counter = counter
        print(name,"created")
        print(self.name,"created")
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.delay, self.counter)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = myThread(1, "a", 1, 5)
thread2 = myThread(2, "b", 2, 3)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print ("Exiting Main Thread")