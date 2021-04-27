# there are a number of options to fix race conditions, but here will be focusing on Lock
# solving this problem requires only 1 thread into the read-modify-write section of the code
# in python this is a lock, in some other languages it might be a mutex - MUTual EXclusion
# a lock is like a single pass that must be given up for another to use - only 1 thread can have the lock
# the basic functions for this are .acquire() and .release() - if the lock is not released it cannot be acquired
import concurrent.futures
import logging
import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        # an instance variable called self._lock has been added which runs the threading.Lock() method
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info(f"Thread {name}: starting update.")

        # threads can run the next line of code, but will not be able to take the lock until it is released
        logging.info(f"Thread {name}: about to lock.")
        # Python's 'Lock' will operate as a context manager and will be released automatically if the with block ends
        # here it is initialised and released by the 'with' statement
        with self._lock:
            logging.debug(f"Thread {name}: lock acquired.")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug(f"Thread {name}: computation complete.")
            logging.debug(f"Thread {name}: about to release lock.")
            # once the above line is finished the lock is released, .release(), and the next thread could take the lock
        logging.debug(f"Thread {name}: lock released.")
        logging.info(f"Thread {name}: finishing update.")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.DEBUG, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info(f"Testing locked update: Starting value is {database.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info(f"Testing locked update: Ending value is {database.value}")

# as you can see here Lock() is a crucial component of threading to avoid race conditions
# this alongside RLock can be used to mitigate race conditions and deadlocks!
