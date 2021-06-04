import threading

print("Current thread is:", threading.currentThread().getName())
if threading.currentThread() == threading.main_thread():
    print("Main thread")
else:
    print("other Thread")