# =========================================================
# Course: Parallel Computing
# File: run_background_processes.py (Chapter 03 - Multiprocessing)
#
# Original: a background process ran with daemon = True and a
#           normal process ran with daemon = False.
#
# Modified: Notes app example (same as the no_daemons file).
#   - The AUTO-SAVE process saves the notes 4 times
#     (once every second) in the background.
#   - The main program (the user) closes the app after
#     2 seconds.
#   - daemon = True, so when the main program ends, the
#     auto-save is stopped immediately, even if it has not
#     finished all 4 saves.
#
# Main idea: a daemon process is a background helper. It is
# killed automatically when the main program ends.
# =========================================================
import multiprocessing   # used to create processes
import time              # used for time.sleep() (delays)


def auto_save():
    """Background helper: tries to save the notes 4 times."""
    print('Auto-save started')
    for i in range(1, 5):                      # CHANGED: 4 saves
        time.sleep(1)                          # each save takes 1 second
        print('Notes saved (' + str(i) + ' of 4)')
    print('Auto-save finished')                # never printed: the daemon is stopped early


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    saver = multiprocessing.Process(name='auto_save', target=auto_save)
    saver.daemon = True         # DAEMON: stopped when the main program ends

    saver.start()               # start the helper in the background

    time.sleep(2.5)             # CHANGED: the user types for 2.5 seconds
    print('Main program: user closed the notes app')

    # The main program ends here, so the daemon auto-save is stopped.