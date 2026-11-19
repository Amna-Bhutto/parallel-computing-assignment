# =========================================================
# Course: Parallel Computing
# File: processes_barrier.py (Chapter 03 - Multiprocessing)
#
# Original: 2 processes used a Barrier to wait for each other
#           and 2 processes ran without a barrier. They printed
#           the time they reached each point.
#
# Modified: Cricket match example.
#   - 2 opening batsmen (processes) use a BARRIER. Each one
#     reaches the ground at a different time, but they walk
#     out to bat only when BOTH have arrived.
#   - 2 fans (processes) do NOT use a barrier. They walk
#     into the stadium immediately.
#
# Main idea: a Barrier makes processes wait for each other.
# =========================================================
from multiprocessing import Barrier, Process   # barrier and process tools
import time                                    # used for time.sleep() (delays)


def opener(name, travel_time, gate):
    """A batsman travels to the ground, waits for his partner, then walks out."""
    print(name + ' is on the way to the ground')
    time.sleep(travel_time)                        # CHANGED: travel takes different times
    print(name + ' reached the ground and waits for his partner')
    gate.wait()                                    # wait here until BOTH batsmen arrive
    print(name + ' walks out to bat')              # runs only after both have arrived


def fan(name):
    """A fan enters the stadium without waiting for anyone."""
    print(name + ' entered the stadium (no waiting)')


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':

    gate = Barrier(2)   # the barrier opens only when 2 processes are waiting

    # CHANGED: 2 batsmen with different travel times (original: p1 and p2)
    ali = Process(target=opener, args=('Ali', 1, gate))
    hassan = Process(target=opener, args=('Hassan', 3, gate))

    # CHANGED: 2 fans without a barrier (original: p3 and p4)
    fan1 = Process(target=fan, args=('Fan 1',))
    fan2 = Process(target=fan, args=('Fan 2',))

    # Start all four processes
    ali.start()
    hassan.start()
    fan1.start()
    fan2.start()

    # Wait until all four processes have finished
    ali.join()
    hassan.join()
    fan1.join()
    fan2.join()

    print('Match can start')   # CHANGED: new message