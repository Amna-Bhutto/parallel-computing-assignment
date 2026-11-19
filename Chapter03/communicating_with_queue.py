# =========================================================
# Course: Parallel Computing
# File: communicating_with_queue.py (Chapter 03 - Multiprocessing)
#
# Original: a producer process put 10 random numbers in a
#           queue and a consumer process took them out.
#
# Modified: Railway ticket counter example.
#   - The PASSENGER process (producer) joins the line with
#     a destination city, one passenger every 1 second.
#   - The CLERK process (consumer) takes the next passenger
#     from the line and issues a ticket (2 seconds each).
#   - A "STOP" message tells the clerk the counter is closing.
#
# Main idea: a multiprocessing Queue is a safe waiting line
# shared between processes. put() adds, get() removes.
# =========================================================
import multiprocessing   # used to create processes and the queue
import time              # used for time.sleep() (delays)


class Passenger(multiprocessing.Process):
    """Producer process: passengers join the line."""

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)   # set up the process
        self.queue = queue                       # the shared line

    def run(self):
        # CHANGED: destinations (original: random numbers 0-256)
        for city in ['Lahore', 'Karachi', 'Multan', 'Quetta']:
            self.queue.put(city)                 # passenger joins the line
            print('Passenger for ' + city + ' joined the line')
            time.sleep(1)                        # next passenger after 1 second
        self.queue.put('STOP')                   # CHANGED: counter closing signal


class Clerk(multiprocessing.Process):
    """Consumer process: issues tickets from the line."""

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)   # set up the process
        self.queue = queue                       # the same shared line

    def run(self):
        while True:
            city = self.queue.get()              # wait for the next passenger
            if city == 'STOP':                   # CHANGED: no more passengers
                print('Clerk: counter closed')
                break
            time.sleep(2)                        # CHANGED: issuing a ticket takes 2 seconds
            print('Clerk: ticket issued for ' + city)


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':
    line = multiprocessing.Queue()               # the shared waiting line

    passenger = Passenger(line)
    clerk = Clerk(line)

    passenger.start()
    clerk.start()

    passenger.join()
    clerk.join()

    print('All tickets issued')                  # CHANGED: new message