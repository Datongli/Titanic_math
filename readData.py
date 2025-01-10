"""
用于读取数据的文件
"""
import pandas as pd
from Passenger import Passenger


def csv2data(dataPath: str, dataList: list, trainOrNot: bool = True):
    """
    读取csv文件中的数据
    :param dataPath: 数据路径
    :param dataList: 存放数据的列表
    :param trainOrNot: 是否为训练集，默认为True
    :return: 就地填充dataList，无返回值
    """
    data = pd.read_csv(dataPath)  # 将csv中的数据读取成为DataFrame
    for index, row in data.iterrows():  # 遍历DataFrame中的每一行
        # 实例化每一个乘客对象
        age = "missing" if pd.isnull(row['Age']) else row['Age']  # 判断年龄是否为空，为空则赋值为"missing"
        passenger = Passenger(row['PassengerId'], row['Survived'], row['Pclass'],
                              row['Sex'], age, row['SibSp'], row['Parch'], row['Embarked'], trainOrNot)
        dataList.append(passenger)


if __name__ == "__main__":
    pass