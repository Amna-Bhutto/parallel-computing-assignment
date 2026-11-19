# =========================================================
# Course: Parallel Computing
# File: process_pool.py (Chapter 03 - Multiprocessing)
#
# Original: a pool of 4 processes calculated the square of
#           the numbers 0 to 99.
#
# Modified: School example.
#   - A POOL of 3 teachers (processes) shares a stack of
#     6 exam papers.
#   - Each teacher takes a paper (marks out of 50) and
#     calculates the percentage.
#
# Main idea: a Pool is a fixed group of worker processes.
# pool.map() splits the jobs between them and returns the
# results in the same order as the input.
# =========================================================
import multiprocessing   # used to create the pool of processes
import os                # used to get the process ID
import time              # used for  time.sleep() (delays)

def check_paper(marks):
    """A teacher calculates the percentage for one paper (out of 50)."""
    time.sleep(1)             # CHANGED: checking one paper takes 1 second
    percentage = marks * 2    # CHANGED: marks out of 50 become a percentage
    # Show which teacher (process ID) checked this paper
    print('Teacher (process ' + str(os.getpid()) + ') checked ' + str(marks) + ' marks')
    return percentage         # send the result back to the main program


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':

    # CHANGED: 6 papers with marks out of 50 (original: numbers 0 to 99)
    papers = [45, 30, 50, 22, 38, 41]

    # CHANGED: pool of 3 teachers (original: 4 processes)
    pool = multiprocessing.Pool(processes=3)

    # map() gives each paper to a free teacher and collects the results
    results = pool.map(check_paper, papers, chunksize=1)   # one paper per teacher at a time

    pool.close()   # no more papers will be added
    pool.join()    # wait until all teachers have finished

    print('Marks       :', papers)
    print('Percentages :', results)