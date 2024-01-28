[[ReadItLater]] [[Article]]

# [如何判断数据是否可以进行因子分析(Factor analysis)？](https://mp.weixin.qq.com/s/URzgvGgDc7eR6MDvh0X6sQ)

## 可视化 相关矩阵
在因子分析之前，需先观察上述的相关系数。大部分的*相关系数既不能太低，也不能太高*。如果太低，比如小于0.3，就无法找到有效的因子；如果太高，比如大于0.9，提示存在多重共线性问题。  
R 包 "psych", "qgraph", 示例数据 Thurstone.9
将使用R包{psych}中的数据集“Thurstone.9”，此数据集包含710个样本，是一个相关矩阵(Correlation matrix)，查看它的概况：

```
round(Thurstone.9, 2)  # 小数点保留后两位
```
![[Pasted image 20230720021836.png]]

可以将上述相关矩阵画成一个网络图，代码如下：

```
qgraph(Thurstone.9,  
       details = TRUE,   # 显示cutoff值和最大值       
       cut = 0.3,   # cutoff值为0.3，大于此数值，线条更宽颜色更深       
       posCol = "steelblue")
```

![[Pasted image 20230720021945.png|500]] 
我们在代码中将cutoff值设为0.3，所以，如果相关系数低于0.3，线条比较细，颜色较浅；反之，线条更宽颜色更深。同时，图中右下角也标出了最大相关系数为0.77。

## Bartlett检验，判断是否为单位矩阵
观察相关系数可用于初步了解手头上的数据，除此之外，还可以使用Bartlett检验，用于判断相关矩阵是否为一个单位矩阵(Identity matrix)，它指的是对角线为1，其它为0的相关矩阵。换句话说，变量之间不存在相关，是独立的。检验代码如下： 

```
cortest.bartlett(Thurstone.9, n = 710)  # n为相关矩阵的样本量
```

其中，p值为0，因此拒绝H0(它是一个单位矩阵)，提示这个相关矩阵不是单位矩阵，所以上述的结果符合因子分析中的一个前提。  

## 是否多重共线性 计算矩阵行列式 determinant
关于是否存在多重共线性，还可以通过计算矩阵的行列式(determinant)进行判断，代码如下：
```
det(Thurstone.9)
```
如果它的值大于0.00001，提示不存在多重共线性问题。  

## KMO 指数，抽样充分性
最后，另一个用于评估数据是否适用于因子分析的程度的方法为：Kaiser-Meyer-Olkin(KMO)指数。
它可用于判断数据的抽样充分性(Sampling adequacy)，代码如下：
```
KMO(Thurstone.9)
```

KMO值的范围为0到1之间，Kaiser（1974）建议所有变量的KMO值至少都要大于0.5才可以进行因子分析\[1\]。
从上述结果可知，所有变量以及总体(MSA)的值都大于0.5，提示符合抽样充分性这个前提。  

*参考文献*

```
[1]. Kaiser, H. F. (1974). An index of factorial simplicity. Psychometrika, 39(1), 31–36. https://doi.org/10.1007/BF02291575
```

