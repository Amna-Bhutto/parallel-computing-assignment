# Original: 2 threads printed their name. The line that
#           should print the process ID was commented out.
#
# Modified: Hospital example.
#   - The HOSPITAL is the process (one program running).
#   - Each DOCTOR is a thread working inside the hospital.
#   - Every doctor has a different name and thread ID, but
#     all doctors belong to the SAME process ID.
#
# Main idea: threads have their own name, but threads of
# one program share the same process.

from threading import Thread   # used to create threads
import threading               # used to get the thread ID
import time                    # used for time.sleep() (delays)
import os                      # used to get the process ID


class Doctor(Thread):
    """A doctor thread that treats one patient."""

    def __init__(self, name, department):
        Thread.__init__(self)          # set up the thread
        self.name = name               # CHANGED: doctor's name (original: Thread#1)
        self.department = department   # CHANGED: new data, the doctor's department

    def run(self):
        # This code runs when the thread starts.
        # os.getpid() gives the process ID (same for all doctors).
        # threading.get_ident() gives the thread ID (different for each doctor).
        print("{} ({}) started | process ID: {} | thread ID: {}".format(
            self.name, self.department, os.getpid(), threading.get_ident()))

        time.sleep(1)                  # CHANGED: the doctor treats a patient for 1 second

        print("{} ({}) finished treating a patient".format(
            self.name, self.department))


def main():
    # Show the process ID of the hospital (the main program)
    print("Hospital (main process) ID: {}".format(os.getpid()))

    # CHANGED: 3 doctors with names and departments
    # (original: 2 threads named Thread#1 and Thread#2)
    doctor1 = Doctor("Dr. Ahmed", "Cardiology")
    doctor2 = Doctor("Dr. Sara", "Pediatrics")
    doctor3 = Doctor("Dr. Ali", "Surgery")

    # Start all threads. All doctors now work at the same time.
    doctor1.start()
    doctor2.start()
    doctor3.start()

    # Wait until every doctor has finished
    doctor1.join()
    doctor2.join()
    doctor3.join()

    # This prints only after all doctors are done
    print("All patients treated. Hospital closed")


if __name__ == "__main__":
    main()