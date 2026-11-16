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

    producer = CSVProducer("transactions.csv", shared_queue, 0.1)
    consumer = Consumer(shared_queue)

    #producer.start()
    #consumer.start()

    t1 = threading.Thread(target=producer.start)
    t2 = threading.Thread(target=consumer.start)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #print(shared_queue.get())
    




if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
