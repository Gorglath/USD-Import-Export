import multiprocessing as mp
from TestQueue import MultiTest as mt

if __name__ == "__main__":
    #Launch a process to do the test queue.
    process = mp.Process(target=mt.run_test, args=())
    process.start()
