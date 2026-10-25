# Course: Parallel Computing
# Original: a producer added items to a list and used an
#           event to tell a consumer to pop them.
# Modified: Daraz Flash Sale example. 4 customers wait on the
#           app. When the seller starts the sale (event is
#           set), all waiting customers rush in together.

import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-10s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# The event: starts "off". Customers wait until it is switched "on".
sale_started = threading.Event()


def customer():
    """A customer waits for the flash sale, then adds an item to the cart."""
    logging.info('Waiting for the flash sale to start')
    sale_started.wait()  # blocks here until the seller calls set()
    logging.info('Sale is live! Item added to cart')


def seller():
    """The seller starts the flash sale after 3 seconds."""
    time.sleep(3)  # CHANGED: sale starts after 3 seconds
    logging.info('FLASH SALE IS NOW LIVE!')
    sale_started.set()  # switch the event on: wakes up ALL waiting customers


def main():
    # CHANGED: 4 customers (original: 1 consumer)
    names = ['Ali', 'Sara', 'Ahmed', 'Fatima']
    threads = []

    for n in names:
        t = threading.Thread(name=n, target=customer)
        threads.append(t)
        t.start()

    # Start the seller who will switch the event on
    s = threading.Thread(name='Seller', target=seller)
    threads.append(s)
    s.start()

    # Wait for everyone to finish
    for t in threads:
        t.join()

    logging.info('Flash sale finished')


if __name__ == "__main__":
    main()

#Difference from Barrier :a Barrier waits until all threads arrive,
# while an Event waits for one thread to give a signal.