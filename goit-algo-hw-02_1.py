import queue
import random

queue = queue.Queue()

def generate_request():
    request = random.randint(1, 100)
    queue.put(request)

def process_request():
    if queue.not_empty:
        request = queue.get()
        print(request)
    else:
        print("Queue is empty")

def main():
    while True:
        generate_request()
        process_request()
        user_answer = input("Please type exit to quit ")
        if user_answer == "exit":
            break

if __name__ == "__main__":
    main()