from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    new_request = {
        'id': random.randint(1, 1000),
        'time': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    queue.put(new_request)
    print(f'Generated request: {new_request["id"]} at {new_request["time"]}')

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Processing request: {request["id"]} generated at {request["time"]}')
    else:
        print('Queue is empty.')


while True:
    generate_request()  
    process_request()  
    
    exit_command = input("Enter 'exit' to stop the program: ")
    if exit_command.lower() == 'exit':
        print("Finished.")
        break

