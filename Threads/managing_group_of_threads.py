import logging
import time
# importing concurrent.futures for the threadpools
import concurrent.futures


# the code here is similar in places but the intro of concurrent.futures changes it up significantly
def thread_function(name):
    logging.info(f"Thread {name}: starting.")
    time.sleep(2)
    logging.info(f"Thread {name}: finishing.")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    # with, is used as a context manager which is used to create & destroy the pool of threads
    # it also states how many worker threads should be in the working pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # uses .map() to iterate over range 3 and pass a 'thing' to a thread in the pool
        executor.map(thread_function, range(3))
        # notice there is no .join() here - that is because the end of the with block automatically does a .join()

# N.B. - if you call a function that takes no parameters, but you pass it parameters in .map() the thread will error
# the exception will be hidden by ThreadPoolExecutor and the program will just terminate with no output
