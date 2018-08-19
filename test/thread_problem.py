"""
    Created by ZZXUN on 2018/8/6
"""
import threading
import time

from werkzeug.local import Local, LocalStack

__author__ = "ZZXUN"


class A:
    b = 1


my_job = LocalStack()
my_job.push(1)


# 两个线程实例化两个栈，彼此数据不干扰

def worker():
    print("in new thread before push, value is :" + str(my_job.top))
    my_job.push(2)
    print("in new thread after push, value is :" + str(my_job.top))


new_t = threading.Thread(target=worker, name="zzx")
new_t.start()

time.sleep(1)
print("in main thread before push, value is :" + str(my_job.top))
my_job.push(3)
print("in main thread after push, value is :" + str(my_job.top))
