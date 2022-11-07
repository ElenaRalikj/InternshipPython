import multiprocessing
import time #just so he can measure how long the script will run
import concurrent.futures

start=time.perf_counter()#start time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#Using the process pool executor(it's best to be used with a context manager
with concurrent.futures.ProcessPoolExecutor() as executor:#this is the contex manager
    if __name__ == '__main__':
        secs=[5,4,3,2,1]
        results=executor.map(do_something,secs)
        # map method basically runs the do_something function
        #with every item of the list secs
        #it just returns the result instead of future objects which are
        #returned when using the submit method
        #the map method is going to run these processes in parallel but instead of
        #returning the results as they re completed, map is going to return
        #the results in the order that they were started

        #In order to loop over the results we do a for loop
        #for result in results:
        #    print(result)
            #it prints out the results in the order that they were started and not
            #in the order that they were finished

            #it our function raised it as an exception it wont actually raise that
            #exception while running the process, the exception will be raised
            #when its value is retrieved from the results iterator
            #so if need to handle any exceptions then we can do that withing the iterator
            #actually the for loop for result in results

        #f1=executor.submit(do_something,1)
        #f2=executor.submit(do_something,1)

        #print(f1.result())
        #print(f2.result())

#processes=[]

#for _ in range(10):
#    if __name__ == '__main__':
#        p=multiprocessing.Process(target=do_something,args=[1.5])#it's going to sleep for 1.5 seconds for 10 different times
#        p.start()
#        processes.append(p)

#serializing sth with pickle means that we are converting Python objects
#into a format that can be deconstructed and reconstructed in another Python script
#after setting seconds in the function do_something and setting args=[1.5]
#we are getting that the process is finished in 1.82 seconds(it should be 1.5 seconds)

# for process in processes:#it will run all the 10 processes in parallel at the same time, so instead of taking it ten seconds it will take 1.36 seconds
#    process.join()


#p1=multiprocessing.Process(target=do_something)
#p2=multiprocessing.Process(target=do_something)

#p1.start()
#p2.start()

#p1.join()
#p2.join()


#do_something()
#do_something()

finish = time.perf_counter()#calculating the finish time

print(f' Finished in {round(finish-start,2)} second(s)')
