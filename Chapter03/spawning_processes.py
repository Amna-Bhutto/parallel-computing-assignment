# =========================================================
# Course: Parallel Computing
# File: spawning_processes.py (Chapter 03 - Multiprocessing)
#
# Original: 6 processes, each joined right after start(),
#           so they ran one by one.
# Modified: Daraz example. 3 riders (processes) each deliver
#           one parcel at the same time. Each rider prints
#           its own process ID.
# =========================================================
import multiprocessing   # used to create processes
import os                # used to get the process ID
import time              # used for time.sleep() (delays)


def rider(name):
    """One rider delivers one parcel (takes 2 seconds)."""
    print(name + ' started | process ID: ' + str(os.getpid()))
    time.sleep(2)        # CHANGED: delivery takes 2 seconds
    print(name + ' delivered the parcel')


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    start = time.time()
    print('Main program process ID: ' + str(os.getpid()))

    # CHANGED: 3 riders with names (original: 6 numbered processes)
    names = ['Ali', 'Sara', 'Ahmed']
    processes = []

    for n in names:
        p = multiprocessing.Process(target=rider, args=(n,))
        processes.append(p)
        p.start()        # start the rider (runs in parallel)

    # CHANGED: join after all have started (original joined each
    # one immediately, which made them run one by one)
    for p in processes:
        p.join()         # wait until this rider finishes

    print('All parcels delivered')
    print('--- %s seconds ---' % (time.time() - start))  # about 2 seconds, not 6