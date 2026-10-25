# Course: Parallel Computing
# Original: a producer made a random item number and a
#           consumer waited for it using a semaphore.
# Modified: Foodpanda example. The kitchen (producer) cooks
#           an order and the rider (consumer) waits until the
#           order is ready before picking it up.

import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-10s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore starts at 0 = no order is ready yet
semaphore = threading.Semaphore(0)

# CHANGED: the shared data is now an order name (original: a number)
order_name = ""

# CHANGED: menu to choose from (original used random numbers 0-1000)
menu = ["Burger", "Pizza", "Biryani", "Pasta", "Shawarma"]


def rider():
    """Rider waits until the kitchen says the order is ready."""
    logging.info('Rider is waiting for the order')
    semaphore.acquire()  # blocks here until the kitchen calls release()
    logging.info('Rider picked up: {}'.format(order_name))


def kitchen():
    """Kitchen cooks a random order, then signals the rider."""
    global order_name
    time.sleep(2)  # CHANGED: cooking takes 2 seconds (original: 3)
    order_name = random.choice(menu)  # pick a random dish from the menu
    logging.info('Kitchen finished: {}'.format(order_name))
    semaphore.release()  # signal: the order is ready


def main():
    # CHANGED: 5 orders (original: 10)
    for i in range(5):
        t1 = threading.Thread(name='Rider', target=rider)
        t2 = threading.Thread(name='Kitchen', target=kitchen)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()

#What you should see: for each of the 5 orders, the Rider prints “waiting”, then 2 seconds later the Kitchen
#prints “finished: (a dish)”,and right after that the Rider prints “picked up: (same dish)”.