# =========================================================
# Course: Parallel Computing
# File: spawning_processes_namespace.py (Chapter 03 - Multiprocessing)
#
# Original: 6 processes ran myFunc() from myFunc.py, but each
#           was joined right after start(), so they ran one by one.
# Modified: Daraz example. 4 riders (processes) run the
#           myFunc() function from myFunc.py (the Daraz rider
#           version) and all work at the same time.
#
# Main idea: a function written in one file can be imported
# and run in separate processes from another file.
# =========================================================
import multiprocessing        # used to create processes
from myFunc import myFunc     # import the Daraz rider function from myFunc.py

# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    processes = []            # list to keep all riders

    # CHANGED: 4 riders, numbered 1 to 4 (original: 6 processes, 0 to 5)
    for i in range(1, 5):
        p = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()             # start the rider (runs in parallel)

    # CHANGED: join after all have started (original joined each
    # one immediately, which made them run one by one)
    for p in processes:
        p.join()              # wait until this rider finishes

    print('All riders finished')   # CHANGED: new message