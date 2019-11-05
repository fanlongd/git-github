
from f4 import Human


class Student(Human):
    # 类变量
    sum = 0

    # 构造函数
    # 初始化对象属性 实例化变量
    def __init__(self, school, name, age):
        self.school = school
        self.__score = 0          # private 变量
        super(Student, self).__init__(name, age)
        # print(self.name, str(self.age))
        # print(self.__class__.sum)

    def marking(self, score):
        if score < 0:
            print('分数不能为负值')
        else:
            self.__score = score
            print(self.name + '同学的成绩为' + str(self.__score))

    # 实例方法 描述对象特征或行为
    def do_homework(self):
        print('chinese homework')
        super(Student, self).get_name()

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级人数：' + str(cls.sum))

    # 静态方法
    @staticmethod
    def add(x, y):
        A = x + y
        print(A)


student1 = Student('人民路小学', '兔八哥', 18)
Student.plus_sum()
student1.marking(59)
student2 = Student('建国路小学', '鸡小萌', 17)
Student.plus_sum()
student2.marking(-1)
student1.do_homework()
# print(student1.__dict__)
# print(student1._Student__score)
# print(student1.name)
# print(student2.age)
# print(Student.sum1)
# print(Student.name)
