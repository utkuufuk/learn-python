import threading

class Messenger(threading.Thread):
    
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

sender = Messenger(name='Message Sender')
receiver = Messenger(name='Message Receiver')

sender.start()
receiver.start()

