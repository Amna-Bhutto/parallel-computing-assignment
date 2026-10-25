# Original: a producer put random numbers in a queue and
#           3 consumers took them out (forever).
#
# Modified: Simple bank example.
#   - 4 customers join one line (the queue).
#   - 2 tellers (threads) take the next customer from the
#     line and serve them for 2 seconds each.
#
# Main idea: a Queue is a safe waiting line shared by threads.

from threading import Thread   # used to create threads
from queue import Queue        # the waiting line
import time                    # used for time.sleep() (delays)

# The shared waiting line. It is empty at the start.
line = Queue()

# CHANGED: our data, the customers in the bank (original: random numbers)
customers = ['Ali', 'Sara', 'Ahmed', 'Fatima']


def teller(name):
    """A teller keeps taking customers from the line and serving them."""
    while True:
        # get() takes the first customer from the line.
        # If the line is empty, the teller waits here.
        customer = line.get()

        # CHANGED: "STOP" is a special message that means the bank is closing.
        if customer == 'STOP':
            print(name + ': closing counter')
            break   # leave the loop, so the thread ends

        print(name + ': serving ' + customer)
        time.sleep(2)   # CHANGED: serving takes 2 seconds
        print(name + ': finished ' + customer)


if __name__ == '__main__':
    # Create 2 tellers. Each one runs the teller() function.
    t1 = Thread(target=teller, args=('Teller 1',))
    t2 = Thread(target=teller, args=('Teller 2',))

    # Start both tellers. They now wait for customers.
    t1.start()
    t2.start()

    # Customers join the line (put() adds them to the queue)
    for c in customers:
        line.put(c)
        print(c + ' joined the line')

    # Send one "STOP" for each teller, so both of them finish
    line.put('STOP')
    line.put('STOP')

    # Wait until both tellers have finished
    t1.join()
    t2.join()

    print('All customers served. Bank closed')