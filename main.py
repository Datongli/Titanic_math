"""
该文件是预测泰坦尼克号乘客生还概率的主程序
"""
from Bayes import Bayes
from readData import csv2data


def dataProcess(dataPath: str, dataList: list, trainOrNot: bool = True):
    """
    数据处理
    :param dataPath: 数据路径
    :param dataList: 传入的数据空列表
    :param trainOrNot: 是否为训练集，默认为True
    :return: 就地填充dataList，无返回值
    """
    csv2data(dataPath, dataList, trainOrNot)


if __name__ == "__main__":
    """构建训练/测试数据集"""
    trainPath = r"D:\学习\研究生\研一上\数理统计\大作业\要求\titanic.csv"
    testPath = r"D:\学习\研究生\研一上\数理统计\大作业\要求\test.csv"
    trainData = []  # 用于存储训练数据的列表，内部为Passenger对象
    testData = []  # 用于存储测试数据的列表，内部为Passenger对象
    dataProcess(trainPath, trainData)
    dataProcess(testPath, testData, False)
    """实例化贝叶斯对象"""
    bayes = Bayes(trainData)  # 实例化贝叶斯对象
    bayes.train()  # 训练贝叶斯模型
    bayes.test(testData)  # 测试贝叶斯模型
