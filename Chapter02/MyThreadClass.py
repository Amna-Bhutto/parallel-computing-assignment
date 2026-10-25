# Original: 9 threads ran at the same time, each sleeping
#           for a random 1-10 seconds. There was no lock.
#
# Modified: Shop example.
#   - 4 customers (threads) are served at 4 different
#     counters at the same time.
#   - Each customer needs a different time (fixed numbers,
#     not random), so the result is easy to check.
#
# Main idea: without a lock, threads do NOT wait for each
# other. The total time is only as long as the slowest one.

import time                      # used for time.sleep() and measuring time
import os                        # used to get the process ID
from threading import Thread     # used to create threads


class Customer(Thread):
    """A customer thread that is served at its own counter."""

    def __init__(self, name, duration):
        Thread.__init__(self)       # set up the thread
        self.name = name            # customer name
        self.duration = duration    # seconds this customer needs

    def run(self):
        # This code runs when the thread starts.
        print("---> " + self.name + " is being served, process ID "
              + str(os.getpid()))
        time.sleep(self.duration)   # the counter works on this customer
        print("---> " + self.name + " is done")


def main():
    start_time = time.time()        # remember the start time

    # CHANGED: 4 customers with fixed times
    # (original: 9 threads with random times)
    ali = Customer("Ali", 2)
    sara = Customer("Sara", 4)
    ahmed = Customer("Ahmed", 1)
    fatima = Customer("Fatima", 3)

    # Start all threads. They run at the same time.
    ali.start()
    sara.start()
    ahmed.start()
    fatima.start()

    # Wait until every customer is done
    ali.join()
    sara.join()
    ahmed.join()
    fatima.join()

    print("All customers served")

    # Total time: about 4 seconds (the slowest customer, Sara),
    # not 10 seconds (2+4+1+3).
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()