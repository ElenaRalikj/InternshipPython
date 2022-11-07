import threading
x=0

def thread_task(lock):
    global x
    for i in range(100000):
        lock.acquire()
        x +=1
        lock.release()

#the lock can be blocking or non blocking so this acquire method takes one argument which is true or false
#by default the value of argument is true which means that this acquire is blocking by default
#so lock.acquire actually locks the access of the shared variable, in our case this that is x,
#and at this time only one thread can work on this variable whatever thread has the access to this function at a particular time
#so until and unless one thread execution is completed on this variable after that this lock is released
#that means that the other thread can work on this variable using the lock once again
#so whenever second thread wants to try to access this variable it will just lock the access to this variable first of all and
# then work on this variable whatever we want to do(increment the value or change the value of x and then release the lock and
# releasing means that we once again we want to allow the other thread to work on this shared resource
#so this mechanism will allow only one thread to access this shared resource at a particular time
#so the thread synchronization problem will not occur

def main_task():
    lock=threading.Lock()#the lock class has two methods, one is acquire and the second one is release
    #acquire method is used to lock and the release method is used to release the lock
    t1=threading.Thread(target=thread_task,args=(lock,))
    t2=threading.Thread(target=thread_task,args=(lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=='__main__':
    main_task()
    print('{0}'.format(x))