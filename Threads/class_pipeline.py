import logging
import threading


class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    # initialises these 3 members and then calls acquire() on .consumer_lock
    # this allows the producer to send a new message without fear of consumer interfering
    def __init__(self):
        # stores the message to be passed between producer & consumer
        self.msg = 0

        # is a threading.Lock object that restricts access to the message by the producer thread
        self.producer_lock = threading.Lock()

        # is a threading.Lock object that restricts access to the message by the consumer thread
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    # get_msg and set_msg are functions that provide opposite functionalities
    # this is because 1 operates to enable consumer and the other enables producer once consumer has been enabled
    def get_msg(self, name):
        logging.debug(f"{name}: About to acquire getlock.")
        self.consumer_lock.acquire()
        logging.debug(f"{name}: Has getlock.")

        # consumer copies the message out
        msg = self.msg
        logging.debug(f"{name}: About to release setlock.")

        # producer lock is released which allows the producer to insert the next message onto the pipeline
        self.producer_lock.release()
        logging.debug(f"{name}: setlock released.")

        # the variable msg is returned not self.msg - this is to eliminate the chance of a race condition for self.msg
        return msg

    # producer calls with this message
    def set_msg(self, msg, name):
        logging.debug(f"{name}: About to acquire setlock.")

        # acquires the producer lock to protect against race conditions
        self.producer_lock.acquire()
        logging.debug(f"{name}: Has setlock.")

        # sets self.msg to the new value of msg
        self.msg = msg
        logging.debug(f"{name}: About to release getlock.")

        # calls release on the consumer lock, allowing it to be read
        self.consumer_lock.release()
        logging.debug(f'{name}: getlock released.')