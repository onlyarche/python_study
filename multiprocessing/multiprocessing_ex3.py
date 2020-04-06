import multiprocessing as mp
import time
import os
from multiprocessing import Manager

def somefunction(results, inputdata):
    print("process id: ", os.getpid(), "pid: ", inputdata)
    result = 10 - inputdata
    results.append(result)
    print(result)

if __name__ == "__main__":
    start_time = time.time()

    pool = mp.Pool(3)
    results = Manager().list()

    inputdatas = [0, 1, 2]
    pool.starmap(somefunction, [(results, inputdata) for inputdata in inputdatas])

    pool.close()
    pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print(results)