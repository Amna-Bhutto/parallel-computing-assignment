# =========================================================
# Course: Parallel Computing
# File: killing_processes.py (Chapter 03 - Multiprocessing)
#
# Original: a process counted from 0 to 9, but the main
#           program terminated it right after starting it.
#
# Modified: Video download example.
#   - The DOWNLOAD process downloads a video in 10 steps
#     (10 percent per second).
#   - After 3 seconds the user presses "Cancel", so the main
#     program terminates the process before it finishes.
#
# Main idea: terminate() stops a running process. is_alive()
# tells us whether it is still running, and exitcode shows
# how it ended.
# =========================================================
import multiprocessing   # used to create processes
import time              # used for time.sleep() (delays)


def download():
    """Downloads a video in 10 steps (1 second per step)."""
    print('Download started')
    for percent in range(10, 101, 10):    # CHANGED: shows 10%, 20% ... 100%
        time.sleep(1)                     # each step takes 1 second
        print('Downloaded ' + str(percent) + '%')
    print('Download finished')            # never printed if cancelled


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    p = multiprocessing.Process(target=download)   # create the process

    print('Before start, running:', p.is_alive())  # False: not started yet
    p.start()                                      # start the download
    print('After start, running:', p.is_alive())   # True: it is running

    time.sleep(3)                                  # CHANGED: wait 3 seconds
    print('User pressed Cancel')                   # CHANGED: new message
    p.terminate()                                  # stop the process immediately

    p.join()                                       # wait until it has really stopped
    print('After cancel, running:', p.is_alive())  # False: it has stopped
    print('Exit code:', p.exitcode)   # negative (e.g. -15) = terminated; 0 = normal finish