# Parallel Computing Assignment - Chapter 02 

## Student Details

- **Course:** Parallel Computing
- **Name:** Amna Maryam Bhutto
- **Roll No:** 24SP-059-CS

---

## About This Project

This project is based on **Chapter 02 (Thread-based parallelism)** of the book
*Python Parallel Programming Cookbook, Second Edition* by Packt Publishing.

I changed the data and the examples in all 12 files and added clear comments
on every important line. The new examples use real-life situations such as
Foodpanda, Daraz, inDrive, a bank, an ATM and a hospital.

## Original Source

[Python-Parallel-Programming-Cookbook-Second-Edition](https://github.com/PacktPublishing/Python-Parallel-Programming-Cookbook-Second-Edition)

## Project Structure

```
parallel-computing-assignment/
├── README.md
└── Chapter02/
    ├── Barrier.py
    ├── Condition.py
    ├── Event.py
    ├── MyThreadClass.py
    ├── MyThreadClass_lock.py
    ├── MyThreadClass_lock_2.py
    ├── Rlock.py
    ├── Semaphore.py
    ├── Thread_definition.py
    ├── Thread_determine.py
    ├── Thread_name_and_processes.py
    └── Threading_with_queue.py
```

## Requirements

- Python 3.x (tested on Python 3.15.1)
- No extra packages needed. Only built-in modules are used: `threading`, `queue`, `time`, `os`, `logging` and `random`.

## How to Run

Open a terminal in the main folder and run any file, for example:

```powershell
python Chapter02\Thread_definition.py
```

## Changes Made (File by File)

| # | File | Concept | New Example | What Was Changed |
|---|------|---------|-------------|------------------|
| 1 | `Thread_definition.py` | Creating threads | Squaring numbers | 5 threads each square one number; added a 1-second delay to show parallel work |
| 2 | `Thread_determine.py` | Thread names | Foodpanda cart | 3 threads prepare Burger, Fries and Drink at the same time; replaced the outdated `getName()` |
| 3 | `MyThreadClass.py` | Threads without a lock | Shop with 4 counters | 4 customers with fixed times instead of 9 random threads; total time about 4 seconds |
| 4 | `MyThreadClass_lock.py` | Lock | Single cashier | 5 customers share one cashier; total time 9 seconds |
| 5 | `MyThreadClass_lock_2.py` | Lock on a short part only | ATM machine | Lock covers only the PIN entry; total time about 4 seconds |
| 6 | `Semaphore.py` | Semaphore | Kitchen and rider | Rider waits until the kitchen finishes each order (5 orders) |
| 7 | `Barrier.py` | Barrier | Daraz parcel | 4 items are packed; the parcel is sealed only when all are packed |
| 8 | `Event.py` | Event | Daraz flash sale | 4 customers wait; one signal starts the sale for all of them |
| 9 | `Condition.py` | Condition | inDrive ride | Driver waits until the passenger requests a ride |
| 10 | `Rlock.py` | RLock | Bank account | Deposit and withdraw threads share one account; final balance 1200 |
| 11 | `Threading_with_queue.py` | Queue | Bank tellers | 2 tellers serve 4 customers from one line; added a STOP message so the program ends |
| 12 | `Thread_name_and_processes.py` | Threads and processes | Hospital doctors | 3 doctors (threads) share one process ID; added thread ID |

## Key Observations

- **No lock:** threads run together, so the total time equals the slowest thread.
- **Lock around everything:** threads take turns, so the total time is the sum of all of them.
- **Lock around a short part:** a good balance between safety and speed.
- **Threads share one process ID**, but each thread has its own thread ID.

---

*Author: Amna Maryam Bhutto | Roll No. 24SP-059-CS | Course: Parallel Computing*