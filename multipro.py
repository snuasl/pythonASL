import time 
import multiprocessing 
import scipy.integrate as integrate

def process_ex(func):
    for _i in range(100000):
        # integrate different equation as input func changes
        _result = integrate.quad(lambda x: func*x**2+func*x, 0, 5)
    print("%d Job Finished!" %(func))

if __name__ == "__main__":
    # check how many cpu available
    numCores = multiprocessing.cpu_count()
    print("Available CPU : ", numCores)

    # to check time (start)
    t1 = time.time()

    # process list 
    process_list = [1, 2, 3, 4, 5, 6, 7, 8]

    pool = multiprocessing.Pool(processes=numCores)
    pool.map(process_ex, process_list)
    pool.close()
    pool.join()

    # to check time (end)
    t2 = time.time()
    print("Elapsed time: ", t2-t1)