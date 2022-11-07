#Threading module is more powerful and it has more higher level support
#for creating threads in Python

import threading
import time

def print_epoch(nameOfThread,delay):#we want to count the seconds from January 1970 till now
    count=0
    while count<5:
        time.sleep(delay)#we are providing a delay in order to see the thread execution
        count+=1
        print(nameOfThread,'---------',time.time())

def print_cube(num):
    print('Cube={}'.format(num*num*num))

def print_square(num):
    print('Square={}'.format(num*num))

if __name__=='__main__':
    t1=threading.Thread(target=print_cube,args=(2,))#without the coma it gives an error so that's why we are putting it, in order to understand that it s a tuple
    t2=threading.Thread(target=print_square,args=(2,))

    t1.start()
    t2.start()

    t1.join()#the join method waits until the execution is completed
    t2.join()#the join method waits until the execution is completed

    print('Done')