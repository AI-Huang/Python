#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : Jun-14-19 18:30
# @Author  : Kelly Kan HUANG (kan.huang.hkust@gmail.com)


class Person(object):
    """docstring for Person"""


class Student(Person):
    """Student的生成类
    """
    name = "class student"  # 类变量
    class_var1 = 1
    class_var2 = 2

    def __init__(self, name=None, age=None, title=None):
        super(Student, self).__init__()
        self.name = name
        self.age = age
        self.title = title

    def intro(self):
        print("%s岁, 是学生" % (self.age))


def main():
    mengyan = Student(name="Meng Yan", age="24", title="PhD")
    huangkan = Student(name="Huang Kan", age="25", title="MPhil")
    print(mengyan.__doc__)
    print(mengyan.__dict__)
    print(mengyan.__module__)
    mengyan.intro()
    print(Student.name)
    print(mengyan.__class__)
    print(Student.__base__)

    print(mengyan.class_var1)
    mengyan.class_var1 = 23333
    print(mengyan.class_var1)

    print(f"huangkan.class_var1: {huangkan.class_var1}")  # 还是1
    mengyan = Student(name="Meng Yan", age="24", title="PhD")
    print(f"Student.class_var1: {Student.class_var1}")
    Student.class_var1 = 77777
    print(f"Student.class_var1: {Student.class_var1}")  # 都变了
    print(f"mengyan.class_var1: {mengyan.class_var1}")  # 77777
    print(f"huangkan.class_var1: {huangkan.class_var1}")  # 77777


if __name__ == '__main__':
    main()
