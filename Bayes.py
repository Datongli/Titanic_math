"""
构建贝叶斯类的文件
"""
from Passenger import Passenger
import inspect


class Bayes:
    """贝叶斯类"""
    def __init__(self, trainData: list, K: int | float = 2,
                 lammda: int | float = 1):
        """
        初始化贝叶斯类
        :param trainData: 训练数据列表
        :param K: 乘客生还与否的状态
        :param p: 拉普拉斯平滑参数
        :return: 无返回值
        """
        self.trainData = trainData
        self.K = K
        self.lammda = lammda
        self.P_Y = {}  # 不同的生还状态，先验概率
        self.P_X_Y = {}  # 不同生还状态下，各种不同情况（如年龄、性别等）的条件概率
        self.result = []  # 预测结果

    def train(self):
        """
        训练贝叶斯模型
        :return: 无返回值
        """
        """计算生还与否的先验概率P(Y)"""
        self.__calculatePriorProbability()
        # 检查用，可以删除
        print(self.P_Y)
        """计算条件概率P(X|Y)"""
        self.__calculateConditionalProbability()
        # 检查用，可以删除
        for key, value in self.P_X_Y.items():
            print(f"{key} = {value}")

    def test(self, testData: list):
        """
        测试贝叶斯模型
        :return: 打印正确率，无返回值
        """
        """计算后验"""
        self.__calculatePosteriorProbability(testData)
        """计算正确数量"""
        count = 0
        for i in range(len(testData)):
            if testData[i].survived == self.result[i]:
                count += 1
        print("正确率为: {}".format(count / len(testData)))

    def __calculatePriorProbability(self):
        """
        计算幸存与否的先验概率
        私有方法，只建议在类内部调用
        :return: 计算所的的先验概率字典，原地填充self.P_Y，无返回值
        """
        for key, value in Passenger.survived.items():
            self.P_Y['Y=' + str(key)] = (value + self.lammda) / (len(self.trainData) + self.lammda * self.K)

    def __calculateConditionalProbability(self):
        """
        计算各个变量的条件概率P(X|Y)
        私有方法，只建议在类内部调用
        :return: 计算所的的条件概率字典，原地填充self.P_X_Y，无返回值
        """
        # 构建一个列表，用于存储passenger类的各个静态变量名
        static_variable_names = self._getVariableName()
        # 计算条件概率
        for survivedOrNot, _ in Passenger.survived.items():  # 分别对生还与否两种状态计算
            for variableName in static_variable_names:  # 分别对各个变量计算
                variable_dict = getattr(Passenger, variableName)  # 获取每个变量的字典
                for variableValue, _ in variable_dict.items():  # 对于变量的每一种取值，计算条件概率
                    count = self.__calculatePAB(variableValue, survivedOrNot, variableName)
                    # P(X|Y) = P(XY) / P(Y)
                    self.P_X_Y[variableName + '=' + str(variableValue) + '|Y=' + str(survivedOrNot)] = ((count + self.lammda)
                            / (Passenger.survived[survivedOrNot] + self.lammda * len(variable_dict)))

    @staticmethod
    def _getVariableName():
        """
        获取passenger类的各个静态变量名
        静态方法
        :return: 包含Passenger类中各个静态变量名的列表
        """
        static_variable_names = []
        members = inspect.getmembers(Passenger)
        for member in members:
            if not member[0].startswith('__') and not callable(member[1]):
                static_variable_names.append(member[0])
        static_variable_names.remove('survived')  # 移除survived变量名
        return static_variable_names

    def __calculatePAB(self, variableValue, survivedOrNot, variableName):
        """
        计算P(XY)
        私有方法，只建议在类内部调用
        :param variableValue: 变量值
        :param survivedOrNot: 生还与否
        :param variableName: 变量名
        :return: P(XY)
        """
        count = 0
        for passenger in self.trainData:
            if passenger.survived == survivedOrNot and getattr(passenger, variableName) == variableValue:
                count += 1
        return count

    def __calculatePosteriorProbability(self, testData: list):
        """
        计算后验概率
        私有方法，只建议在类内部调用
        :param testData: 测试数据列表
        :return: 预测结果列表
        """
        # 构建一个列表，用于存储passenger类的各个静态变量名
        static_variable_names = self._getVariableName()
        for passenger in testData:
            ans = []  # 承接一个乘客的生还和死亡概率
            # 计算Y=0的概率
            try:
                p = self.P_Y['Y=0']
                for variableName in static_variable_names:
                    p *= self.P_X_Y[variableName + '=' + str(getattr(passenger, variableName)) + '|Y=0']
                ans.append(p)
            except KeyError:
                ans.append(0)
            # 计算Y=1的改概率
            try:
                p = self.P_Y['Y=1']
                for variableName in static_variable_names:
                    p *= self.P_X_Y[variableName + '=' + str(getattr(passenger, variableName)) + '|Y=1']
                ans.append(p)
            except KeyError:
                ans.append(0)
            if ans[0] > ans[1]:
                self.result.append(0)
            else:
                self.result.append(1)


if __name__ == "__main__":
    pass