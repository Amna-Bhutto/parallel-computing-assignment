# Original: 9 threads used a lock, so only one thread could
#           run at a time. Each waited a random 1-10 seconds.
# Modified: Cashier counter example. 5 customers (threads)
#           want to pay, but there is only ONE cashier (lock).
#           The cashier serves one customer at a time.

import threading
import time
from threading import Thread

# The cashier: only one customer can hold this lock at a time
cashier_lock = threading.Lock()


class Customer(Thread):
    """A customer thread that waits for the cashier and then pays."""

    def __init__(self, name, service_time):
        Thread.__init__(self)
        self.name = name                    # customer name
        self.service_time = service_time    # seconds the cashier needs

    def run(self):
        print(self.name + " is waiting in line")
        cashier_lock.acquire()              # wait until the cashier is free
        print("---> " + self.name + " is being served")
        time.sleep(self.service_time)       # the cashier works on this customer
        print("---> " + self.name + " is done")
        cashier_lock.release()              # cashier becomes free for the next one


def main():
    start_time = time.time()

    # CHANGED: fixed names and times (original used random times)
    customers = [
        Customer("Ali", 2),
        Customer("Sara", 1),
        Customer("Ahmed", 3),
        Customer("Fatima", 2),
        Customer("Hassan", 1),
    ]

    # All customers arrive at the same time
    for c in customers:
        c.start()

    # Wait until every customer has been served
    for c in customers:
        c.join()

    print("All customers served")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()