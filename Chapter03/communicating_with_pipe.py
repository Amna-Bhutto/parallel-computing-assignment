# =========================================================
# Course: Parallel Computing
# File: communicating_with_pipe.py (Chapter 03 - Multiprocessing)
#
# Original: process 1 sent the numbers 0 to 9 through a pipe,
#           process 2 squared them and sent them through a
#           second pipe, and the main program printed them.
#
# Modified: Currency exchange example.
#   - Process 1 (cashier) creates dollar amounts.
#   - Process 2 (exchange) converts dollars to rupees.
#   - The main program prints the final amounts.
#   - Pipe 1 connects process 1 -> process 2.
#   - Pipe 2 connects process 2 -> main program.
#
# Main idea: a Pipe is a tunnel. One process sends data in
# with send(), another receives it with recv().
# =========================================================
import multiprocessing   # used to create processes and pipes

RATE = 280               # CHANGED: 1 dollar = 280 rupees (example rate)


def cashier(out_pipe):
    """Process 1: sends dollar amounts into the pipe."""
    # CHANGED: new data (original: numbers 0 to 9)
    for dollars in [10, 20, 30, 40, 50]:
        out_pipe.send(dollars)   # put one amount into the pipe
    out_pipe.send(None)          # CHANGED: None means "no more data"


def exchange(in_pipe, out_pipe):
    """Process 2: receives dollars, converts them, sends rupees."""
    while True:
        dollars = in_pipe.recv()         # wait for the next amount
        if dollars is None:              # stop signal received
            out_pipe.send(None)          # pass the stop signal on
            break
        out_pipe.send(dollars * RATE)    # CHANGED: convert (original: item * item)


# Required on Windows, so new processes do not start more processes
if __name__ == '__main__':

    # Pipe(False) makes a one-way pipe: (receiving end, sending end)
    receive_1, send_1 = multiprocessing.Pipe(False)   # pipe 1
    receive_2, send_2 = multiprocessing.Pipe(False)   # pipe 2

    # Process 1 writes into pipe 1
    p1 = multiprocessing.Process(target=cashier, args=(send_1,))
    # Process 2 reads from pipe 1 and writes into pipe 2
    p2 = multiprocessing.Process(target=exchange, args=(receive_1, send_2))

    p1.start()
    p2.start()

    # The main program reads the results from pipe 2
    while True:
        rupees = receive_2.recv()    # wait for the next result
        if rupees is None:           # stop signal: all data received
            break
        print('Received Rs', rupees)

    p1.join()
    p2.join()
    print('End')