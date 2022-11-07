import _thread
import time

def print_epoch(nameofThread,delay):#we want to count the seconds from January 1970 till now
    count=0
    while count<5:
        time.sleep(delay)#we are providing a delay in order to see the thread execution
        count+=1
        print(nameofThread,'---------',time.time())

try:
    _thread.start_new_thread(print_epoch,('thread 1',2))#not provding the third argument, it s optional
    _thread.start_new_thread(print_epoch,('thread 2',4))
except:
    print('this is an error')

#if the function print_epoch returns successfully,
#the thread will silently exit
#but if this function terminate unexpectedly then unhandled exception will be thrown and
#the track trace of that exception will be printed on the terminal
#so, if the function throws then strike trace will be printed and this will be unhandled exception

#In order to avoid the unhandled exception we can provide the try/except block

#First way of waiting

#input()#providing a mechanism to wait for the thread creation
#thread 1 is executed for the second time because the delay time is less than thread 2
#the time printed is the epoch time
#thread 2 is executed twice at the end because in the while loop we have the count limit to be less that 3

#Second way of waiting

while 1:#infinite loop that runs(wait) until the execution of the thread is completed
    pass