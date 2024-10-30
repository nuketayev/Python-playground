import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def dring_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You studied")


x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=dring_coffee)
y.start()
z = threading.Thread(target=study)
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# dring_coffee()
# study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

