有限混合模型（Finite Mixture Model，简称FMM）是一种概率模型，用于描述观测数据是由多个潜在子群体（或分量）组成的。在这种模型中，每个子群体都有自己的概率分布，而观测数据是这些概率分布的加权和。有限混合模型可以用于解决聚类、分类、模式识别等问题。

有限混合模型的一般形式可以表示为：

p(x) = ∑(π_k * p_k(x))

其中，x表示观测数据，π_k表示第k个子群体的权重（也可以理解为该子群体的先验概率），p_k(x)表示第k个子群体的概率分布。权重π_k需要满足0 <= π_k <= 1且总和为1，即∑(π_k) = 1。

在实际应用中，有限混合模型的分布可以是各种形式，例如高斯混合模型（Gaussian Mixture Model，简称GMM）就是最常见的一种，它使用多个高斯分布来表示不同子群体的概率分布。

为了对有限混合模型进行参数估计，通常使用最大似然估计（Maximum Likelihood Estimation，简称MLE）或贝叶斯方法。而期望最大化（Expectation-Maximization，简称EM）算法是一种常用的求解最大似然估计的迭代方法，它可以有效地处理含有隐变量的概率模型，如有限混合模型。

A finite mixture model (FMM) is a probability model that combines a finite number of probability distributions. It is a statistical model that assumes that the data is a mixture of several subpopulations, each of which is described by a different probability distribution. The FMM is used to model data that cannot be easily modeled by a single probability distribution. The EM algorithm is used to estimate the parameters of the FMM. The EM algorithm is an iterative algorithm that alternates between the E-step and the M-step. In the E-step, the algorithm estimates the probability that each observation belongs to each subpopulation. In the M-step, the algorithm estimates the parameters of each subpopulation. [The EM algorithm continues until convergence is achieved](https://en.wikipedia.org/wiki/Mixture_model)

Populations are often divided into groups or subpopulations—age groups, income brackets, levels of education. Regression models or distributions likely differ across these groups. But sometimes we don't have a variable that identifies the groups. Perhaps the identifying variable is simply missing. Perhaps it is hard to collect—honest reporting of drug use, sex of goldfish, etc. Perhaps it is inherently unobservable—penchant for risky behavior, high propensity to save money, etc. In such cases, we can use finite mixture models (FMMs) to model the probability of belonging to each unobserved group, to estimate distinct parameters of a regression model or distribution in each group, to classify individuals into the groups, and to draw inferences about how each group behaves. 

For instance, we might want to model an individual's annual number of doctor visits based on age and medical conditions. However, the model is likely to differ for individuals who are inclined to schedule an appointment at the first sign of a problem compared with those who wait until conditions are more serious. An automobile insurance company might want to classify drivers into risk categories. Those categories may be high and low risk, or they may be high, medium, and low risk. With FMMs, we can estimate the probability of belonging to a group and fit group-specific models.

“A finite mixture model (FMM) is a statistical model that assumes the presence of unobserved groups, called latent classes, within an overall population. Each latent class can be fit with its own regression model, which may have a linear or generalized linear response function. We can compare models with differing numbers of latent classes and different sets of constraints on parameters to determine the best fitting model. For a given model, we can compare parameter estimates across classes. We can estimate the proportion of the population in each latent class, and we can predict the probabilities that the observations in our sample belong to each latent class.”

A common mistake in statistical modelling is to assume “one size fits all” or to run multiple models on subjectively pre-defined subgroups of consumers, for example. FMM often reveal unexplained heterogeneity that is either ignored or only partially revealed by multiple models for a priori groups. I should note that there are also advanced variations of FMM which are extensions of factor analysis and [structural equation modelling](https://www.linkedin.com/pulse/what-structural-equation-modeling-kevin-gray/) (SEM).