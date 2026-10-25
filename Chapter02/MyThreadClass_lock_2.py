# Original: 9 threads used a lock only around a print line.
#           The lock was released BEFORE the sleep, so the
#           slow part ran in parallel.
#
# Modified: ATM example.
#   - 4 people use a bank ATM machine.
#   - Entering the PIN needs the ATM, so only ONE person
#     can do it at a time (the lock).
#   - After the PIN, the person waits for their cash.
#     This waiting happens at the same time for everyone
#     because the lock is already released.
#
# Main idea: keep a lock for the shortest time possible.
# Lock only the part that must be one-at-a-time.

import threading                 # used to create threads and locks
import time                      # used for time.sleep() and measuring time
from threading import Thread     # used to create threads

# The ATM: only one person can hold this lock at a time
atm_lock = threading.Lock()


class Person(Thread):
    """A person who uses the ATM to withdraw cash."""

    def __init__(self, name, wait_time):
        Thread.__init__(self)          # set up the thread
        self.name = name               # person's name
        self.wait_time = wait_time     # seconds to wait for the cash

    def run(self):
        # Step 1: use the ATM (one person at a time)
        atm_lock.acquire()             # wait until the ATM is free
        print("---> " + self.name + " is entering the PIN")
        time.sleep(0.5)                # CHANGED: entering the PIN takes 0.5 seconds
        atm_lock.release()             # ATM is free for the next person

        # Step 2: wait for the cash (the lock is already released,
        # so everyone waits at the same time)
        time.sleep(self.wait_time)
        print("---> " + self.name + " received the cash")


def main():
    start_time = time.time()           # remember the start time

    # CHANGED: 4 people with fixed times (original: 9 threads, random times)
    ali = Person("Ali", 2)
    sara = Person("Sara", 3)
    ahmed = Person("Ahmed", 1)
    fatima = Person("Fatima", 2)

    # Start all threads
    ali.start()
    sara.start()
    ahmed.start()
    fatima.start()

    # Wait until everyone has finished
    ali.join()
    sara.join()
    ahmed.join()
    fatima.join()

    print("All people received their cash")
    
    # About 4 seconds: the PINs are entered one by one, but the
    # cash waits overlap. Sara and Fatima finish last, at 4 seconds.
    # Doing everything one by one would take 10 seconds
    # (2+3+1+2 = 8 seconds of waiting, plus 2 seconds of PINs).
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()