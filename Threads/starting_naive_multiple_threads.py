import logging
import threading
import time


def thread_function(name):
    logging.info(f"Thread {name}: starting.")
    time.sleep(2)
    logging.info(f"Thread {name}: finishing.")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info(f"Main: create and start a thread {index}.")

        # this uses the same mechanism to create a thread object
        x = threading.Thread(target=thread_function, args=(index,))

        # the list of threads is appended with current x value
        threads.append(x)

        # x is then started to begin the thread
        x.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main: before joining thread {index}")
        # as we enumerate over the list threads we join each thread as we enumerate
        thread.join()
        logging.info(f"Main: thread {index} done.")

    # when you run the program you can see that the threads end in a fairly haphazard way
    # the threads will not end in a consistent way when you run the program
