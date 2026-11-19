# =========================================================
# Course: Parallel Computing
# File: run_background_processes_no_daemons.py (Chapter 03 - Multiprocessing)
#
# Original: a background process and a normal process ran with
#           daemon = False, so the program waited for both.
#
# Modified: Notes app example.
#   - The AUTO-SAVE process saves the notes 4 times
#     (once every second) in the background.
#   - The main program (the user) closes the app after
#     1 second.
#   - daemon = False, so the program does NOT close until
#     the auto-save has finished all 4 saves.
#
# Main idea: a normal (non-daemon) process keeps running even
# after the main program has finished its own work.
# =========================================================
import multiprocessing   # used to create processes
import time              # used for time.sleep() (delays)


def auto_save():
    """Background helper: saves the notes 4 times."""
    print('Auto-save started')
    for i in range(1, 5):                      # CHANGED: 4 saves
        time.sleep(1)                          # each save takes 1 second
        print('Notes saved (' + str(i) + ' of 4)')
    print('Auto-save finished')                # printed, because it is NOT a daemon


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    saver = multiprocessing.Process(name='auto_save', target=auto_save)
    saver.daemon = False        # NOT a daemon: the program waits for it

    saver.start()               # start the helper in the background

    time.sleep(1)               # CHANGED: the user types for 1 second
    print('Main program: user closed the notes app')

    # No join() here, but Python still waits for the helper,
    # because a non-daemon process must finish before Python exits.