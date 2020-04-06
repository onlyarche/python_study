from multiprocessing import Process
import time
import os



def count(cnt):
    proc = os.getpid()
    for i in range(cnt+1):
        if i>99999 or i<1:
            print("PID: ", proc, " - ", i)

if __name__ == '__main__':
    start_time = time.time()

    num_arr = [100000, 100000, 100000, 100000]
    procs = []
    for index, number in enumerate(num_arr):
        proc = Process(target=count, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print("--- %s seconds ---" % (time.time() - start_time))
