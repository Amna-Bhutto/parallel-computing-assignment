# Parallel Computing Assignment - Chapter 03 (Multiprocessing)

## Student Details

- **Course:** Parallel Computing
- **Name:** Amna Maryam Bhutto
- **Roll No:** 24SP-059-CS

---

## About This Chapter

This chapter is based on **Chapter 03 (Process-based parallelism)** of the book
*Python Parallel Programming Cookbook, Second Edition* by Packt Publishing.

In Chapter 02 we used **threads**, which share one process ID and one memory.
In Chapter 03 we use **processes**, and each process has its **own process ID and
its own memory**. Because processes do not share memory, they need a **Pipe** or a
**Queue** to exchange data.

I changed the data and the examples in all 12 files and added clear comments on
every important line. The new examples use real-life situations such as Daraz
riders, a hospital, a restaurant, a school, a cricket match, a currency exchange,
a railway ticket counter, a video download and a notes app.

## Original Source

[Python-Parallel-Programming-Cookbook-Second-Edition](https://github.com/PacktPublishing/Python-Parallel-Programming-Cookbook-Second-Edition)

## Project Structure

```
Chapter03/
├── README.md
├── communicating_with_pipe.py
├── communicating_with_queue.py
├── killing_processes.py
├── myFunc.py
├── naming_processes.py
├── process_in_subclass.py
├── process_pool.py
├── processes_barrier.py
├── run_background_processes.py
├── run_background_processes_no_daemons.py
├── spawning_processes.py
└── spawning_processes_namespace.py
```

## Requirements

- Python 3.x (tested on Python 3.15.1)
- No extra packages needed. Only built-in modules are used: `multiprocessing`, `os` and `time`.
- On Windows, every file uses `if __name__ == '__main__':`. This is required so that new processes do not start more processes.

## How to Run

Open a terminal in the **main project folder** (the one that contains `Chapter02` and `Chapter03`) and run any file with the commands below.

| # | File | Run Command |
|---|------|-------------|
| 1 | `myFunc.py` | `python Chapter03\myFunc.py` |
| 2 | `spawning_processes.py` | `python Chapter03\spawning_processes.py` |
| 3 | `spawning_processes_namespace.py` | `python Chapter03\spawning_processes_namespace.py` |
| 4 | `naming_processes.py` | `python Chapter03\naming_processes.py` |
| 5 | `process_in_subclass.py` | `python Chapter03\process_in_subclass.py` |
| 6 | `process_pool.py` | `python Chapter03\process_pool.py` |
| 7 | `processes_barrier.py` | `python Chapter03\processes_barrier.py` |
| 8 | `communicating_with_pipe.py` | `python Chapter03\communicating_with_pipe.py` |
| 9 | `communicating_with_queue.py` | `python Chapter03\communicating_with_queue.py` |
| 10 | `killing_processes.py` | `python Chapter03\killing_processes.py` |
| 11 | `run_background_processes_no_daemons.py` | `python Chapter03\run_background_processes_no_daemons.py` |
| 12 | `run_background_processes.py` | `python Chapter03\run_background_processes.py` |

**Note:** `spawning_processes_namespace.py` imports the function from `myFunc.py`,
so both files must stay in the same folder.

## Changes Made (File by File)

| # | File | Concept | New Example | What Was Changed |
|---|------|---------|-------------|------------------|
| 1 | `myFunc.py` | Helper function | Daraz rider | Rider number `i` delivers `i` parcels; function name and input kept so other files can import it |
| 2 | `spawning_processes.py` | Creating processes | Daraz riders | 3 riders (processes) each print their own process ID; `join()` moved after all `start()` calls so they run together (about 2 seconds, not 6) |
| 3 | `spawning_processes_namespace.py` | Importing a function | Daraz riders | 4 riders run `myFunc()` imported from `myFunc.py` at the same time |
| 4 | `naming_processes.py` | Process names | Hospital doctors | One doctor has a custom name (`Dr. Ahmed`), the other has Python's default name |
| 5 | `process_in_subclass.py` | Process subclass | Restaurant chefs | A `Chef` class inherits from `Process`; 2 chefs cook at the same time |
| 6 | `process_pool.py` | Process pool | School teachers | A pool of 3 teachers shares 6 exam papers; results stay in input order |
| 7 | `processes_barrier.py` | Barrier | Cricket openers | 2 batsmen wait for each other at a barrier; 2 fans enter without waiting |
| 8 | `communicating_with_pipe.py` | Pipe | Currency exchange | Dollars go through pipe 1 to a converter, then rupees go through pipe 2 to the main program; a `None` message means stop |
| 9 | `communicating_with_queue.py` | Queue | Railway ticket counter | Passengers join a queue and a clerk issues tickets; added a `STOP` message so the program ends |
| 10 | `killing_processes.py` | Terminating a process | Video download | The download is cancelled after 3 seconds with `terminate()`; shows `is_alive()` and `exitcode` |
| 11 | `run_background_processes_no_daemons.py` | Non-daemon process | Notes app | Auto-save is not a daemon, so all 4 saves finish even after the main program ends |
| 12 | `run_background_processes.py` | Daemon process | Notes app | Auto-save is a daemon, so it is stopped when the main program ends (only 2 saves appear) |

## Key Observations

- **Processes have different process IDs.** In Chapter 02 all threads showed one process ID, but each process here shows its own.
- **`start()` all first, then `join()`.** Calling `join()` right after `start()` makes processes run one by one. Joining afterwards lets them run together.
- **A Pool reuses its workers.** 6 papers were checked by only 3 teacher processes.
- **Processes do not share memory.** They exchange data with a Pipe (two ends) or a Queue (shared by many).
- **Daemon vs non-daemon.** A daemon process is stopped when the main program ends, a normal process is waited for.
- **`terminate()` stops a process early.** A negative exit code (for example `-15`) means it was terminated, and `0` means a normal finish.

---

*Author: Amna Maryam Bhutto | Roll No. 24SP-059-CS | Course: Parallel distributed computing*