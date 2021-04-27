# race conditions occur when two or more threads access a shared resource
# race conditions can be difficult to identify and will cause output that is confusing but not obviously wrong
import concurrent.futures
import logging
import time


class FakeDatabase:
    def __init__(self):
        # database tracks a single value, below, and accessing this will cause the race condition
        self.value = 0

    # this method simulates reading from a database, performing a computation and storing the new value
    def update(self, name):
        logging.info(f"Thread {name}: starting update.")

        # simulation of reading from a database, here it is just copying self.value to local_copy
        local_copy = self.value

        # computation on the found value
        local_copy += 1

        # sleep the process - this causes the race condition as Thread 1 cannot update value before Thread 2 starts
        time.sleep(0.1)

        # save the new value into the 'database'
        self.value = local_copy

        logging.info(f"Thread {name}: finishing update.")


if __name__ == "__main__":
    fmat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info(f"Testing update. Starting value is {database.value}")

    # this ThreadPoolExecutor creates 2 threads and calls .submit() on each of them
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # the .submit() runs database.update()
            executor.submit(database.update,
                            index)  # .submit() allows for args to be passed, here the only arg is index
    logging.info(f"Testing update. Ending value is {database.value}")

# with the number of workers you would expect the value to be 2 - but in reality it is only 1
# if you check there is no error output or exception to suggest the program has suffered a problem
# why is the arithmetic wrong?
