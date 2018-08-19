"""
    Created by ZZXUN on 2018/8/6
"""

__author__ = "ZZXUN"


class A:

    def __enter__(self):
        a = 1
        return a

    def __exit__(self):
        b = 2


class MyResouse:
    def __repr__(self):
        return "hello world!"

    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close resourse connection")
        if exc_tb:
            print(str(exc_type))
            print(str(exc_val))
        else:
            print("no error")
        b = 2
        # return True
        return False
        # 如果我们返回False后，在exit的外部还会再次抛出异常

    def query(self):
        print("query data")


# try:
# #     with MyResouse() as resourse:
# #         resourse.query()
# #         print(resourse)
# # except Exception as er:
# #     pass


class Hello:
    def __repr__(self):
        return "hello world!"

    def __enter__(self):
        print("调用__enter__函数")
        return "HELLO WORLD!"

    def __exit__(self, exc_type, exc_value, traceback):
        print("调用__exit__")
        if traceback:
            print(exc_type)
            print(exc_value)
        else:
            pass
        return True


with Hello() as hello:
    print(type(hello))
    print(hello)
    1/0
print(Hello())
