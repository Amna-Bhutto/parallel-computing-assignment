# Original: a Box was shared by an adder thread and a
#           remover thread, protected by an RLock.
#
# Modified: Bank account example.
#   - A DEPOSIT thread adds money to one shared account.
#   - A WITHDRAW thread takes money from the same account.
#   - An RLock protects the balance so both threads never
#     change it at the same moment.
#
# Main idea: an RLock (re-entrant lock) can be taken again
# by the SAME thread that already holds it. A normal Lock
# would freeze (deadlock) in that situation.

import threading   # used to create threads and locks
import time        # used for time.sleep() (delays)


class BankAccount:
    """One shared bank account."""

    def __init__(self):
        self.lock = threading.RLock()   # the re-entrant lock
        self.balance = 1000             # CHANGED: account starts with 1000 (original: 0 items)

    def update_balance(self, amount):
        """Change the balance by 'amount' (positive or negative)."""
        with self.lock:                 # take the lock (2nd time for the same thread)
            self.balance += amount

    def deposit(self, amount):
        """Add money to the account."""
        with self.lock:                 # take the lock (1st time)
            # update_balance() takes the SAME lock again.
            # This works only because it is an RLock.
            self.update_balance(amount)

    def withdraw(self, amount):
        """Take money from the account."""
        with self.lock:                 # take the lock (1st time)
            self.update_balance(-amount)


def depositor(account, times):
    """Thread task: deposit 100, repeated 'times' times."""
    for i in range(times):
        account.deposit(100)            # CHANGED: each deposit is 100
        print('Deposited 100  -> balance:', account.balance)
        time.sleep(1)                   # wait 1 second between deposits


def withdrawer(account, times):
    """Thread task: withdraw 100, repeated 'times' times."""
    for i in range(times):
        account.withdraw(100)           # CHANGED: each withdrawal is 100
        print('Withdrew 100   -> balance:', account.balance)
        time.sleep(1)                   # wait 1 second between withdrawals


def main():
    account = BankAccount()   # create ONE account shared by both threads

    # CHANGED: fixed numbers, 5 deposits and 3 withdrawals
    # (original: random numbers)
    t1 = threading.Thread(target=depositor, args=(account, 5))
    t2 = threading.Thread(target=withdrawer, args=(account, 3))

    # Start both threads. They now run at the same time.
    t1.start()
    t2.start()

    # Wait until both threads have finished
    t1.join()
    t2.join()

    # Expected: 1000 + (5 x 100) - (3 x 100) = 1200
    print('Final balance:', account.balance)


if __name__ == "__main__":
    main()