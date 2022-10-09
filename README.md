# Iris-classification

*Chinese*

# Python 操作 Excel (使用openpyxl)
# 这是一个分类的练习，使用最小的欧氏距离作为分类的思路。

**示例数据介绍**
Iris 鸾尾花
自然界中，存在3种Iris，为了研究这种花的分类，科学家分别采集了50朵（共150朵），
测量了花瓣长度、花瓣宽度、萼片长度和萼片宽度（cm），这个数据成为了研究者最为熟悉的数据集（Dataset）。
我们将数据存放在一个Excel的两个Sheet中，
80%（三种各40朵）命名为Training，20%（三种各10朵） 命名为Testing

分类器是机器学习中最常见的算法，其核心是通过“已知”解决“未知”。
对Iris，我们已知3种花的各40个测量结果，对于一朵新采集的花，能否通过机器自动判定其所属类别呢？



**思路如下**
计算每种鸢尾花的属性平均值，
计算测试数据与属性平均值之间的欧式距离，找到最小值，
将最小平均属性对应的分类判定为测试数据的分类，
将机器判定的分类与测试集中的标记分类进行对比，计算正确率。

**结果**
30个测试样本中有29个样本是判定正确的，精度约为96.7%。


*English*

# Python operates Excel (using openpyxl)
# This is a classification exercise, using the minimum Euclidean distance as the classification idea

**Introduction to sample data**
Iris Phoenix Tail Flower
In nature, there are three Iris species. To study the classification of these flowers, scientists collected 50 (150 in total),
The petal length, petal width, sepal length and sepal width (cm) were measured, which became the most familiar data set for researchers.
We store the data in two sheets of one Excel,
80% (40 for each of the three) is named Training, and 20% (10 for each of the three) is named Testing

Classifier is the most common algorithm in machine learning. Its core is to solve the "unknown" problem through "known".
For Iris, we have known 40 measurement results of each of the three flowers. For a newly collected flower, can the machine automatically determine its category?



**The ideas are as follows**
Calculate the average attribute value of each iris,
Calculate the Euclidean distance between the test data and the average value of the attribute, and find the minimum value,
The classification corresponding to the minimum average attribute is determined as the classification of test data,
Compare the classification determined by the machine with the mark classification in the test set, and calculate the accuracy.


**Results**
Among the 30 test samples, 29 samples are correct, with an accuracy of 96.7%.
