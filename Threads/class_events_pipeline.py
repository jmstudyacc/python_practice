import logging
import queue


class Pipeline(queue.Queue):
    """
    This class now inherits from the Queue class.
    """

    def __init__(self):
        # inheriting from Queue, and is now a subclass of it, we define the max size of the queue to be 10
        super().__init__(maxsize=10)    # a maxsize prevents the queue from growing 'infinitely' with put() method

    # the lock messages are gone as the Queue class is thread safe - the locks/unlocks are included
    def get_msg(self, name):
        logging.debug(f"{name}: About to get from queue")
        # this assigns value to the next value in the queue
        value = self.get()
        logging.debug(f"{name}: Got {value} from queue ")
        return value

    def set_msg(self, value, name):
        logging.debug(f"{name}: About to add {value} to queue.")
        # this puts the value as the next value in the queue
        self.put(value)
        logging.debug(f"{name}: added {value} to queue.")
