__author__ = "ハリネズミ"
import threading
import dis


def worker():
    print("im thread")
    t = threading.current_thread()
    print(t.getName())
    return 1

# def test(a,b=0):
#     return a+b
#
# dis.dis(test)

# 現在のスレッドを取得
t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker)
new_t1 = threading.Thread(target=worker)
new_t.start()
new_t1.start()
