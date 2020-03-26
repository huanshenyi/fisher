__author__ = "ハリネズミ"
from werkzeug.local import LocalStack
import threading
import time

# push,pop,top
# s = LocalStack()
# s.push(1)
# print(s.top)
# print(s.top)
# print(s.pop())
# print(s.pop())
#
# s.push(1)
# s.push(2)
# print(s.top) #2
# print(s.top)#2
# print(s.pop()) #2
# print(s.top) #1

my_stack = LocalStack()
my_stack.push(1)
print("in main thread after push, value is:" + str(my_stack.top))# 1

def work():
    # new スレッド
    print("in new thread before push, value is:" + str(my_stack.top)) # 1
    my_stack.push(2)
    print("in new thread after push, value is:" + str(my_stack.top)) # 2

new_t = threading.Thread(target=work, name="qiyue_thread")
new_t.start()
time.sleep(1)

print("finally, in main thread value is:" + str(my_stack.top)) #1
