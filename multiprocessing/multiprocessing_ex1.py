import multiprocessing
import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def all_fib(n):
    fibs = []
    for i in range(n):
        fibs.append(fib(i))
    return fibs

if __name__ == '__main__':
    num_cores = multiprocessing.cpu_count()  # cpu core 개수
    pool = multiprocessing.Pool(processes=num_cores-2) # 현재 시스템에서 사용 할 프로세스 개수

    start_time = time.time()
    num_list = [35, 35, 35, 35]

    rets = pool.map(all_fib, num_list)
    pool.close()
    pool.join()

    print(rets)
    print("--- %s seconds ---" % (time.time() - start_time))
