import time
import multiprocessing


def calculate_square(n):
    print(f"Start computing square of {n}")
    sum(i*i for i in range(n))

    print(f"End computing square of {n}")
if __name__ == "__main__":
    numbers=[10_000_000, 10_000_001]
    processes=[]
    start_time=time.time()

    for n in numbers:
        p=multiprocessing.Process(target=calculate_square,args=(n,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Parallel processing time is {start_time-time.time():.2f}")



