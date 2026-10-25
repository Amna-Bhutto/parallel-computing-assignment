# Original: 10 threads each printed a message.
# Modified: 5 threads each calculate the square of a number.

import threading
import time

# CHANGED: our data, one number for each thread
numbers = [2, 4, 6, 8, 10]


def my_func(thread_number, value):
    """Calculate the square of one number and print the result."""
    time.sleep(1)  # CHANGED: pretend the work takes 1 second
    result = value * value  # the work done by this thread
    print('Thread N°{} calculated {} x {} = {}'.format(
        thread_number, value, value, result))


def main():
    """Create one thread for each number and run them in parallel."""
    threads = []
    for i in range(len(numbers)):
        # Each thread gets its own number to work on
        t = threading.Thread(target=my_func, args=(i, numbers[i]))
        threads.append(t)
        t.start()  # start the thread

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print('All threads finished')


if __name__ == "__main__":
    main()