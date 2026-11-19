# =========================================================
# Course: Parallel Computing
# File: process_in_subclass.py (Chapter 03 - Multiprocessing)
#
# Original: a class MyProcess inherited from Process and
#           printed a message in run(). 10 processes ran
#           one by one.
# Modified: Restaurant example. Each chef is a process (a
#           class inheriting from Process). 2 chefs cook a
#           dish at the same time.
#
# Main idea: to make your own process, write a class that
# inherits from Process and put the work in run().
# =========================================================
import multiprocessing   # used to create processes
import time              # used for time.sleep() (delays)


class Chef(multiprocessing.Process):
    """A chef is a process that cooks one dish."""

    def __init__(self, dish):
        multiprocessing.Process.__init__(self)   # set up the process
        self.dish = dish                         # CHANGED: the dish to cook

    def run(self):
        # run() is called automatically when start() is used
        print(self.name + ' is cooking ' + self.dish)
        time.sleep(2)                            # CHANGED: cooking takes 2 seconds
        print(self.name + ' finished ' + self.dish)


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    # CHANGED: 2 chefs with dishes (original: 10 processes, no data)
    chef1 = Chef('Biryani')
    chef2 = Chef('Pizza')

    # Start both chefs. They cook at the same time.
    chef1.start()
    chef2.start()

    # Wait until both chefs have finished
    chef1.join()
    chef2.join()

    print('All dishes are ready')