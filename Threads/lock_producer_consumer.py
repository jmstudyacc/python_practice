import concurrent.futures
import logging
import random
import class_pipeline

SENTINEL = object()

# general premise - a producer that reads from a simulated network and places a message into the pipeline
# this is not an ideal solution - it only allows for 1 value in the pipeline
# no good for when you are dealing with a burst of traffic!


def producer(pipe):
    """ Simulates getting a message from the network. """
    for index in range(10):
        # to generate a fake message a random number is generated
        msg = random.randint(1, 101)
        logging.info(f"Producer got {msg}")
        # producer calls pipeline.set_message() to send the message to the consumer
        pipe.set_msg(msg, "Producer")

    # a SENTINEL value is also sent to the consumer to announce that the producer is done
    pipe.set_msg(SENTINEL, "Producer")


def consumer(pipe):
    """ Simulates saving a number in a database. """
    msg = 0
    while msg is not SENTINEL:
        # the consumer reads the message from the pipeline
        msg = pipe.get_msg("Consumer")
        # if the message received is SENTINEL value consumer returns from the function - terminating the thread
        if msg is not SENTINEL:
            logging.info(f"Consumer storing message: {msg}")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    # below commented code turns on DEBUG logging messages
    # logging.getLogger().setLevel(logging.DEBUG)

    pipe = class_pipeline.Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # like before calls submit() on appropriate functions with the pipeline as the single positional arg
        executor.submit(producer, pipe)
        executor.submit(consumer, pipe)
