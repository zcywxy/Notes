[[ReadItLater]] [[Article]]

# [CA (Correspondence Analysis)](https://www.jianshu.com/p/ae96163690dc)

## CA (Correspondence Analysis)

> 笔记内容：
> 
> -   CA(Correspondence Analysis)
> -   CA的R实现、作图及解读
> -   与logistic regression的差别

#### CA(Correspondence Analysis)

如果没有明确的假设，研究目的为探究列联表数据中行列两种变量的关系，那么分析的结果需要给出两个结论：两种变量是否确实存在关联，以及是什么变量与什么变量存在关联，其强度如何。

首先需要进行卡方检验（the test of independence（chi-square test），验证行变量与列变量是相关的。

CA (Correspondence Analysis)为PCA的一种延伸，适用于探究分类变量之间的关系。它同样提供了二维plot, 将变量之间的关系总结并可视化。其input为二维的contingency table(2 \* 2, r \* c)，目的为探究行列的变量是否存在关联。

#### CA的R实现、作图及解读

使用`factoextra`，`fviz_ca_biplot`包可以绘制**symmetric plot(French plot)**, 将行列变量均Plot在同一个图中。用于对行列变量的相关程度有一个宏观的了解：行变量（列变量）两点距离越近，代表其相似程度越高。但是其只能解释行变量（或列变量）之间的相似程度，**不能直接解释行列变量之间的距离**。如下图所示：

![](ReadItLater%20Inbox/assets/5638276-cae253013eb8dc6b.png)

使用`fviz_ca_biplot(arrows= ..)`绘制**Asymmetric biplot**, 将行列各点与原点的连线作为向量。行列两向量之间的夹角越小，代表这两个变量关联程度越大，如下图所示：

![](ReadItLater%20Inbox/assets/5638276-4d1a932759c8f410.png)

详细可见[这个例子](https://link.jianshu.com/?t=http%3A%2F%2Fwww.sthda.com%2Fenglish%2Farticles%2F31-principal-component-methods-in-r-practical-guide%2F113-ca-correspondence-analysis-in-r-essentials)  
以及一些参考资料: [Correspondence analysis (CA)](https://link.jianshu.com/?t=https%3A%2F%2Fmb3is.megx.net%2Fgustame%2Findirect-gradient-analysis%2Fca)

#### 与Logistic regression的关系

处理分类型变量最常用的是logistic regression，但并不意味着不管拿来什么数据都往regression里塞。如下表所示，CA与Logistic regression有适用范围。

![](ReadItLater%20Inbox/assets/5638276-138f906b3b73a978.png)

但是用"independent Variable & dependent Variable" 来形容待分析的变量并不严谨。在一些情况下**有明确的假设**，研究目的为探究自变量对因变量的影响程度，或者预测因变量的变化。也存在一些情况，并**没有明确的假设**，不能把两类变量简单归为自变量与因变量。研究目的为探究两类变量比较宏观的关联程度。可以参考[这篇文献](https://link.jianshu.com/?t=http%3A%2F%2Fjtd.amegroups.com%2Farticle%2Fview%2F4102%2Fhtml)。  

![](ReadItLater%20Inbox/assets/5638276-a00b953df010f09e.png)