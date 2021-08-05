import time
from threading import Thread


def minhaThread(msg, t):
    for i in range(10):
        print(msg)
        time.sleep(t)


thread1 = Thread(target=minhaThread, args=("Sou a Thread 1", 2))
thread2 = Thread(target=minhaThread, args=("Sou a Thread 2!!!!", .3))
thread1.start()
thread2.start()
while thread1.is_alive() or thread2.is_alive():
    print('Estou rodando...')
    time.sleep(.5)
