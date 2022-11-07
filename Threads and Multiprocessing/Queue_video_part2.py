#FIFO
import queue


q=queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end='  ')

print('\n')

#LIFO
import queue


q=queue.LifoQueue()#last in first out

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end='  ')


