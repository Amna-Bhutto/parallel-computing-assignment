# =========================================================
# Course: Parallel Computing
# File: myFunc.py (Chapter 03 - Multiprocessing)
#
# Original: a function printed a process number and then
#           printed the numbers from 0 up to that number.
#
# Modified: Daraz delivery example.
#   - Each PROCESS is a delivery rider.
#   - Rider number i has to deliver i parcels.
#   - The function prints every parcel the rider delivers.
#
# =========================================================


def myFunc(i):
    """Rider number i delivers i parcels (i is the rider number)."""

    # CHANGED: message now describes a Daraz rider (original: "calling myFunc")
    print('Daraz rider n°%s is starting deliveries' % i)

    # Repeat once for every parcel this rider must deliver
    for j in range(0, i):
        # CHANGED: prints the parcel number (j + 1 so it starts at 1, not 0)
        print('Rider n°%s delivered parcel %s of %s' % (i, j + 1, i))

    # CHANGED: new message when the rider has finished all parcels
    print('Daraz rider n°%s finished all deliveries' % i)
    return


# This block runs only when you run THIS file directly.
# It does not run when another file imports myFunc.
if __name__ == "__main__":
    myFunc(3)   # test: rider number 3 delivers 3 parcels