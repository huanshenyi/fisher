__author__ = "ハリネズミ"
import time
import threading
from werkzeug.local import Local

class A:
    b=1


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print("in new thread" + str(my_obj.b))


new_t = threading.Thread(target=worker, name="qiyue_thread")
new_t.start()
time.sleep(1)

print("in main thread" + str(my_obj.b))
