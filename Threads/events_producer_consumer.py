import concurrent.futures
import logging
import random
import threading
import time

import class_events_pipeline


# if you intend to handle more than 1 value in the pipeline at once you need a data structure for that
# in this instance you may be better suited to using a queue
# it would also be wise to ditch the sentinel approach and instead use an Event


def producer(pipe, event):
    """ Simulates getting a message from the network. """
    # for loop has changed to a while loop that checks for the status of event
    while not event.is_set():
        msg = random.randint(1, 101)
        logging.info(f"Producer got {msg}")
        pipe.set_msg(msg, "Producer")

    # log message is displayed to indicate the event status has changed
    logging.info("Producer received EXIT event. Exiting...")


def consumer(pipe, event):
    """ Simulates saving a number in a database. """
    # while condition has changed to check event status and contents of the data structure passed to it
    # it will continue to loop until the pipe is empty and event is set
    # queue must be empty or - 1) you lose the final messages 2) the producer attempts to add message to full queue
    # the producer would never return its value and you would be in a different kind of deadlock
    while not event.is_set() or not pipe.empty():
        msg = pipe.get_msg("Consumer")
        # log message to display the value stored and current size of the queue
        logging.info(f"Consumer storing message: {msg}  (Queue Size: {pipe.qsize()})")

    logging.info("Consumer received EXIT event. Exiting...")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    # below commented code turns on DEBUG logging messages
    # logging.getLogger().setLevel(logging.DEBUG)

    pipe = class_events_pipeline.Pipeline()

    # this object allows 1 thread to signal an event while others wait for that event to happen
    # a key benefit here is that the threads waiting for the event do not necessarily need to halt all activity
    # they just check the status every now and then - similar to a webhook
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # unlike before the executor.submit() needs to also pass event to the producer & consumer functions
        executor.submit(producer, pipe, event)
        executor.submit(consumer, pipe, event)

        # an event can be trigger by many things, but in this instance it will sleep and simply .set() the event
        time.sleep(0.5)
        logging.info("Main: about to set event.")
        event.set()

    # you will see in the output that the threads will be swapped per the OS' decision
    # you will not see blocks as previously when using the SENTINEL approach
    # you should also see that the message 'Main: about to set event' appear as the producer finishes but the consumer
    # still has work to do to clear the queue

    # interestingly as you lower the sleep time to 0.05 you can get the Consumer to finish closer the Main exit
    # as you increase that timer the Main event finishes earlier in comparison to Consumer
