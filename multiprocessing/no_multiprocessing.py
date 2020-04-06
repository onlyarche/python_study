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
    start_time = time.time()
    num_list = [35, 35, 35, 35]
    for i, num in enumerate(num_list):
        print(i, all_fib(num))

    print("--- %s seconds ---" % (time.time() - start_time))
