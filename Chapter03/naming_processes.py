# =========================================================
# Course: Parallel Computing
# File: naming_processes.py (Chapter 03 - Multiprocessing)
#
# Original: 2 processes ran myFunc(). One had a custom
#           name and the other had the default name.
#
# Modified: Hospital example.
#   - Each PROCESS is a doctor treating a patient.
#   - One doctor has a custom name ("Dr. Ahmed").
#   - The other doctor has the default name (Process-2).
#
# Main idea: every process has a name. You can choose it,
# or Python gives a default one.
# =========================================================
import multiprocessing   # used to create processes
import time              # used for time.sleep() (delays)


def treat_patient():
    """A doctor (process) treats one patient."""
    # current_process().name gives the name of the running process
    name = multiprocessing.current_process().name
    print('Doctor ' + name + ' started treating a patient')
    time.sleep(2)   # CHANGED: treatment takes 2 seconds (original: 3)
    print('Doctor ' + name + ' finished treating the patient')


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':

    # CHANGED: custom name is "Dr. Ahmed" (original: "myFunc process")
    doctor_with_name = multiprocessing.Process(
        name='Dr. Ahmed', target=treat_patient)

    # No name given, so Python uses the default name (Process-2)
    doctor_with_default_name = multiprocessing.Process(
        target=treat_patient)

    # Start both doctors. They work at the same time.
    doctor_with_name.start()
    doctor_with_default_name.start()

    # Wait until both doctors have finished
    doctor_with_name.join()
    doctor_with_default_name.join()

    print('All patients treated')   # CHANGED: new message