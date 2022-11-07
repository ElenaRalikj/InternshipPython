#94 Communication between processes

import multiprocessing

#result=[]

def calc_square(numbers,q):
    #global result
    for n in numbers:
        #result.append(n*n)
        q.put(n*n)#inserting data at the end of the queue

    #print('inside process '+ str(result))

if __name__=='__main__':
    numbers=[2,3,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()

    #print('outside process '+ str(result))

    while q.empty() is False:
        print(q.get())
