import concurrent.futures
import logging
import queue
import random
import threading
import time

# instead of making our own class and inheriting from Queue, we can just use Queue directly
# that instance is on show here!

def producer(queue, event):
    """ Simulating information coming from the network. """
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info(f"Producer got message: {message}")
        queue.put(message)

    logging.info("Producer received event. Exiting...")


def consumer(queue, event):
    """ Simulating the saving of value in a database. """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(f"Consumer storing message: {message} (Queue Size: {queue.qsize()})")

    logging.info("Consumer received event. Exiting...")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: About to set event.")
        event.set()