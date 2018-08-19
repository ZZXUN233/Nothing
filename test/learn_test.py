class Student():
    name = ""
    age = 0
    score = 0
    count = 0
    __info = ""  # 私有变量

    def __init__(self):
        self.age = 0
        self.name = ""
        self.__class__.count += 1  # 类变量可以用作所有示例类的全局变量

    def print_file(self):
        print("name:" + self.name)
        print("age:" + str(self.age))

    def __update_info(self, info):
        self.__info = info

    def get_score(self, score):
        if score > 90:
            self.__update_info("取得一次A")
        self.score = score

    # 类方法定义
    @classmethod
    def plus_sum(cls):  # cls代表所有该对象的这个类
        cls.count += 1
        print(cls.count)

    # 静态方法,其中不可以访问实例变量，类方法可以替代静态方法
    @staticmethod
    def func1(x, y):
        print(Student.count)
        print(x + y)


if __name__ == '__main__':
    student1 = Student()
    Student.plus_sum()  # 类似类的静态方法
    student2 = Student()
    student2.plus_sum()  # 同时可以被对象调用
    student1.get_score(100)
    student1._Student__info = "假的私有方法"      # 前面的私有变量被更改了
    print(student1.count)
    print(student2.count)
    print(student1.__dict__)
