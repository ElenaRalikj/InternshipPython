import queue
import threading
import time


#def putting_thread(q):
#    while True:
#        print('starting thread')
#        time.sleep(10)#every 10 seconds we are going to be putting an item
#        q.put(5)#put in 5
#        print('put something')

q=queue.Queue()
#t=threading.Thread(target=putting_thread,args=(q,),daemon=True)
#t.start()

q.put(5)

x=(q.get())
print(x)
#print('first item gotten')

#print(q.get())
#print('finished')

#we have put an integer (5) in the queue, we got it with get and now
#we want to check if the queue is empty

#print(q.empty())

#for i in range(5):
 #   q.put(i)

#while not q.empty():
 #   print(q.get(),end='  ')