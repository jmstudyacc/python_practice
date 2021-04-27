import logging
import threading
import time


# really only just logs messages, DOES NOT CREATE THE THREAD(S)
def thread_function(name):
    # function sends the below message to log
    logging.info(f"Thread {name}: starting.")

    # function sleeps for 2 seconds
    time.sleep(2)

    # obvious
    logging.info(f"Thread {name}: finishing.")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: before creating a thread.")

    # creation of a thread instance, with an arg passed to the function that names the thread
    x = threading.Thread(target=thread_function, args=("Blue",))

    # threads that are daemons will be killed when the program ends - Blue will continue, but Red will be killed
    # x = threading.Thread(target=thread_function, args=("Blue",), daemon=True)

    logging.info("Main: before running a thread.")

    # starting a thread instance
    x.start()
    logging.info("Main: wait for the thread to finish.")

    # by including x.join() we tell the program to wait for for the threads to finish before closing
    # here you will see that BLUE thread must finish before main closes
    x.join()

    logging.info("Main: all done.")
