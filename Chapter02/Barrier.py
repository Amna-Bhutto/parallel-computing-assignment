# Course: Parallel Computing
# Original: 3 runners (Huey, Dewey, Louie) ran a race and
#           waited at a barrier (finish line).
# Modified: Daraz example. A customer ordered 4 items in one
#           parcel. 4 warehouse workers pack one item each.
#           The parcel is sealed only when ALL items are
#           packed (barrier).

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

# CHANGED: 4 items in the order (original: 3 runners)
num_items = 4

# The barrier: nobody continues until all 4 items are packed
parcel_barrier = Barrier(num_items)

# CHANGED: items in the Daraz order (original: Huey, Dewey, Louie)
items = ['Phone Case', 'Headphones', 'T-Shirt', 'Charger']


def packer():
    """A worker packs one item, then waits for the other workers."""
    item = items.pop()  # take one item from the order
    sleep(randrange(1, 5))  # CHANGED: packing takes 1-4 seconds (original: 2-4)
    print('%s packed at: %s' % (item, ctime()))
    parcel_barrier.wait()  # wait here until all items are packed
    print('%s is inside the sealed parcel' % item)  # CHANGED: new line


def main():
    threads = []
    print('Daraz order received: 4 items to pack!')  # CHANGED: new message
    for i in range(num_items):
        threads.append(Thread(target=packer))  # one thread per item
        threads[-1].start()                    # start the thread
    for thread in threads:
        thread.join()  # wait for every worker to finish
    print('Parcel sealed and handed to the rider!')  # CHANGED: new message


if __name__ == "__main__":
    main()