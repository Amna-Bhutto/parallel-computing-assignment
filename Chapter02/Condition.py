# Original: a producer and a consumer shared a list and
#           used a condition to wait for each other.
#
# Modified: inDrive example.
#   - The DRIVER thread waits until a ride is requested.
#   - The PASSENGER thread requests a ride after 3 seconds.
#   - When the request is ready, the passenger wakes up
#     the driver using condition.notify().
#
# Main idea: a Condition lets one thread SLEEP until
# another thread tells it "something has changed".

import threading   # library used to create threads and conditions
import time        # library used for time.sleep() (delays)

# Create the condition object.
# Both threads use this same object to talk to each other.
condition = threading.Condition()

# Shared data (both threads can see this variable).
# False means: no ride has been requested yet.
ride_requested = False


def driver():
    """Driver thread: waits until a ride is requested, then accepts it."""
    print('Driver: waiting for a ride request...')

    # "with condition" locks the condition so only one thread
    # can change the shared data at a time.
    with condition:

        # Check the shared data. While no ride is requested,
        # keep waiting. (A while loop re-checks after waking up.)
        while not ride_requested:
            condition.wait()   # driver goes to sleep here until notify() is called

        # This line runs only AFTER the passenger woke the driver up.
        print('Driver: ride accepted, going to the passenger!')


def passenger():
    """Passenger thread: requests a ride after 3 seconds."""
    # We need "global" because we want to CHANGE the shared variable.
    global ride_requested

    # CHANGED: the passenger takes 3 seconds to book the ride.
    time.sleep(3)

    # Lock the condition before changing the shared data.
    with condition:
        ride_requested = True              # the ride request is now ready
        print('Passenger: ride requested!')

        # Wake up the driver, who is sleeping in condition.wait().
        condition.notify()


# This block runs only when we start this file directly.
if __name__ == "__main__":

    # Create two threads: one for the driver, one for the passenger.
    t1 = threading.Thread(target=driver)
    t2 = threading.Thread(target=passenger)

    # Start both threads. They now run at the same time.
    t1.start()
    t2.start()

    # join() means: wait here until the thread has finished.
    t1.join()
    t2.join()

    # This prints only after both threads are completely done.
    print('Ride started')