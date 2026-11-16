"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - Optionally join them so the program runs continuously.

    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """
    shared_queue = Queue()
    producer = CSVProducer.__init__
    consumer = Consumer.__init__
    t1 = threading.Thread
    t2 = threading.Thread

    shared_queue.put(t1)
    shared_queue.put(t2)




if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
