import threading
import time


def print_epoch(nameOfThread,delay):
    count=0
    while count < 5:
        time.sleep(delay)
        count +=1
        print(nameOfThread,'---------',time.time())

class MyThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)#calling the parent init method
        self.name=name
        self.delay=delay

    def run(self):#the run method(it's available inside the thread class in a threading module)
    #this run method is the entry point for the thread
    #this run method is actually called whenever we call start(just like in threading_example)
        print('start thread:',self.name)
        print_epoch(self.name,self.delay)
        print('end thread:',self.name)

if __name__=='__main__':

    t1=MyThread('T-1',1)
    t2=MyThread('T-2',2)

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())
    print(threading.activeCount())#activeCount-no. of threads inside the program
    #it will print the total number of threads which means 2 threads which we already created and plus the one that is the MainThread
    print(threading.currentThread())#printing the currentThread which is active
    print(threading.enumerate())#it will enumerate the number of threads which are active

    t1.join()
    t2.join()

    print('Done')