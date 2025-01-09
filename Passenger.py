"""
用于编写乘客类的文件
"""
import pandas as pd
import numpy as np


class Passenger:
    """
    乘客类
    """
    """用于统计的静态变量"""
    survived, pClass, sex = {}, {}, {}
    age, sibSp, parch, embarked = {}, {}, {}, {}

    def __init__(self, passengerId: int, survived: int, pClass: int,
                 sex: int, age: int | str, sibSp: int, parch: int, embarked: str):
        """
        初始化乘客类
        :param passengerId: 乘客ID
        :param survived: 是否生还 0/1
        :param pClass: 舱位 1/2/3
        :param sex: 性别 male/female
        :param age: 年龄
        :param sibSp: 同行兄弟/配偶数
        :param parch: 同行父母/子女数
        :param embarked: 登船港口 C/Q/S
        """
        self.passengerId = passengerId
        self.survived = survived
        self.pClass = pClass
        self.sex = sex
        self.age = self._changeAge(age)
        self.sibSp = sibSp
        self.parch = parch
        self.embarked = embarked

    def _changeAge(self, age):
        """
        建议只在类内部调用
        将年龄转换为年龄类别
        :param age: 初始化时传入的年龄
        :return: 转换完成之后的年龄类别
        """
        age_class = -1
        if age == "missing":
            return age_class
        if age <= 20:
            age_class = 0
        elif age <= 40:
            age_class = 1
        elif age <= 60:
            age_class = 2
        else:
            age_class = 3
        return age_class
