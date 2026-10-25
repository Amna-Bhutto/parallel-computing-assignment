# Original: 3 threads each waited 2 seconds and printed
#           their name when starting and exiting.
# Modified: Foodpanda cart example. The cart has 3 items and
#           each item is prepared by its own thread at the
#           same time. Each item takes a different time.

import threading
import time


def prepare_burger():
    """Prepare the burger (takes 3 seconds)."""
    # CHANGED: current_thread().name replaces the outdated getName()
    print(threading.current_thread().name + ' --> preparing')
    time.sleep(3)  # CHANGED: burger takes 3 seconds (original: 2)
    print(threading.current_thread().name + ' --> ready')


def prepare_fries():
    """Prepare the fries (takes 2 seconds)."""
    print(threading.current_thread().name + ' --> preparing')
    time.sleep(2)  # fries take 2 seconds (same as original)
    print(threading.current_thread().name + ' --> ready')


def prepare_drink():
    """Prepare the drink (takes 1 second)."""
    print(threading.current_thread().name + ' --> preparing')
    time.sleep(1)  # CHANGED: drink takes 1 second (original: 2)
    print(threading.current_thread().name + ' --> ready')


if __name__ == "__main__":

    print('Order placed: Burger, Fries, Drink')

    # CHANGED: thread names are now the cart items
    t1 = threading.Thread(name='Burger', target=prepare_burger)
    t2 = threading.Thread(name='Fries', target=prepare_fries)
    t3 = threading.Thread(name='Drink', target=prepare_drink)

    # Start all three threads (all items are prepared at the same time)
    t1.start()
    t2.start()
    t3.start()

    # Wait until every item is ready
    t1.join()
    t2.join()
    t3.join()

    print('Order ready! Rider can pick it up.')