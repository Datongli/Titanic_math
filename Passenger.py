"""
用于编写乘客类的文件
"""


class Passenger:
    """
    乘客类
    """
    """用于统计的静态变量"""
    survived, pClass, sex = {}, {}, {}
    age, sibSp, parch, embarked = {}, {}, {}, {}

    def __init__(self, passengerId: int, survived: int, pClass: int,
                 sex: int, age: int | str, sibSp: int, parch: int, embarked: str, trainOrNot: bool = True):
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
        :param trainOrNot: 是否为训练集，默认为True
        """
        self.passengerId = passengerId
        self.survived = survived
        self.pClass = pClass
        self.sex = sex
        self.age = self._changeAge(age)
        self.sibSp = sibSp
        self.parch = parch
        self.embarked = embarked
        if trainOrNot:
            self.__statisticsInformation()  # 统计乘客信息
        else:
            pass

    @staticmethod
    def _changeAge(age):
        """
        建议只在类内部调用，设置为静态方法
        将年龄转换为年龄类别
        :param age: 初始化时传入的年龄
        :return: 转换完成之后的年龄类别
        """
        if age == "missing":
            return -1
        else:
            return age // 20 if age < 60 else 3

    def __statisticsInformation(self):
        """
        统计乘客信息，填充类的静态变量，利于贝叶斯模型的计算
        私有方法，只建议在类内部调用
        :return: 无返回值
        """
        Passenger.survived[self.survived] = 1 if Passenger.survived.get(self.survived) is None else Passenger.survived[self.survived] + 1
        Passenger.pClass[self.pClass] = 1 if Passenger.pClass.get(self.pClass) is None else Passenger.pClass[self.pClass] + 1
        Passenger.sex[self.sex] = 1 if Passenger.sex.get(self.sex) is None else Passenger.sex[self.sex] + 1
        Passenger.age[self.age] = 1 if Passenger.age.get(self.age) is None else Passenger.age[self.age] + 1
        Passenger.sibSp[self.sibSp] = 1 if Passenger.sibSp.get(self.sibSp) is None else Passenger.sibSp[self.sibSp] + 1
        Passenger.parch[self.parch] = 1 if Passenger.parch.get(self.parch) is None else Passenger.parch[self.parch] + 1
        Passenger.embarked[self.embarked] = 1 if Passenger.embarked.get(self.embarked) is None else Passenger.embarked[self.embarked] + 1


if __name__ == "__main__":
    pass