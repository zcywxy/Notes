# R code

```
m_p <- glm(f, data=df,family = "poisson")

model <-glm.nb(f,data=df)

model<- glm(f, family = Gamma(link = "log"), data = df)
```

# WTC activity and MoCA/biomarkers analysis example
The MoCA score and all of the other scores are heavily skewed, so OLS isn’t really the best method for modeling the outcome. A better method would be to invert the measures (so the max is now the min) and then model using either poisson or negative-binomial regression.

Poisson regression and negative-binomial regression are both used for **count data analysis**, but they differ in how they model the variability of the counts. Poisson regression assumes that the variance of the counts is equal to the mean, while negative-binomial regression allows for overdispersion, which means the variance is larger than the mean. In general, you should **use Poisson regression when the variance of the counts is similar to the mean**, and there is **no evidence of overdispersion**. On the other hand, you should use *negative-binomial regression* when the variance of the counts is larger than the mean, and there is evidence of overdispersion.

The standard Poisson GLM models the (conditional) mean `E[y]=μE[y]=μ` which is assumed to be equal to the variance `VAR[y]=μVAR[y]=μ`. `dispersiontest` assesses the hypothesis that this assumption holds (equidispersion) against the alternative that the variance is of the form:

`VAR[y]=μ+α⋅trafo(μ).VAR[y]=μ+α⋅trafo(μ).`

Overdispersion corresponds to `α>0α>0` and underdispersion to `α<0α<0`. The coefficient `αα` can be estimated by an auxiliary OLS regression and tested with the corresponding t (or z) statistic which is asymptotically standard normal under the null hypothesis.

Common specifications of the transformation function `trafotrafo` are `trafo(μ)=μ2trafo(μ)=μ2` or `trafo(μ)=μtrafo(μ)=μ`. The former corresponds to a negative binomial (NB) model with quadratic variance function (called NB2 by Cameron and Trivedi, 2005), the latter to a NB model with linear variance function (called NB1 by Cameron and Trivedi, 2005) or quasi-Poisson model with dispersion parameter, i.e.,

`VAR[y]=(1+α)⋅μ=dispersion⋅μ.VAR[y]=(1+α)⋅μ=dispersion⋅μ.`

The quasi-Poisson and negative binomial models are both generalized linear models (GLMs) that are used to analyze count data when the assumptions of a standard Poisson regression model are violated, specifically when there is overdispersion. While both models can handle overdispersed count data, there are some differences between the two models:

1.  Parameterization: The quasi-Poisson model and negative binomial model differ in how they parameterize the relationship between the mean and variance of the response variable. In the quasi-Poisson model, the variance is assumed to be proportional to the mean, with the proportionality constant being estimated from the data. In contrast, the negative binomial model assumes that the variance is a quadratic function of the mean, with an additional parameter, often denoted as alpha, estimated from the data.
    
2.  Interpretation of the dispersion parameter: The dispersion parameter in the quasi-Poisson model is often difficult to interpret, since it is not directly related to any underlying distribution. In contrast, the dispersion parameter in the negative binomial model has a clear interpretation as a measure of the degree of overdispersion.
    
3.  Flexibility: The negative binomial model is more flexible than the quasi-Poisson model in handling overdispersed count data, since it allows for the variance to exceed the mean to a greater degree. The negative binomial model can also handle a wider range of distributions than the quasi-Poisson model, including the Poisson distribution as a special case.
    
4.  Model selection: Choosing between the quasi-Poisson and negative binomial models can be challenging, as there is no definitive test to determine which model is more appropriate for a given data set. Researchers often compare the fit of the two models using information criteria such as the Akaike information criterion (AIC) or Bayesian information criterion (BIC), with lower values indicating better fit.
    

In summary, both the quasi-Poisson and negative binomial models are useful tools for analyzing overdispersed count data, but the choice between the two models depends on the specific characteristics of the data and the goals of the analysis.

## Interpretation of Poisson and negative binomial is same
https://bookdown.org/roback/bookdown-BeyondMLR/ch-poissonreg.html

The *Poisson regression model is a type of generalized linear model (GLM)* used to model count data. It assumes that the response variable (count data) follows a Poisson distribution. The model relates the expected value of the response variable to a linear combination of predictor variables *using a logarithmic link function*. The model can be expressed as:
![[Pasted image 20230925132151.png|600]] 

https://quantifyinghealth.com/interpret-poisson-regression-coefficients/
![[Pasted image 20230925174434.png|400]]
## GFAP paper
We, therefore, expected that GFAP would stratify from prior literature into two subclasses, indicating a Normal Class of neurological operations versus a Pathological Class due to the presence of brain trauma or stroke (i.e., cerebrovascular disease.) However, GFAP cutoffs are not well validated and may differ depending on age, gender, race/ethnicity, and even blood volume. ==A multivariable-adjusted finite mixture modeling== (below) determined two classes to the GFAP distribution, with one class represented by a normal distribution of GFAP and another class characterized by the highest-high GFAP levels associated with brain injury or stroke. Finite mixture modeling allows us to model the presence of classes, including, for example, a Pathological Class, while jointly modeling correlates of GFAP distribution within either subclass as necessary. We assumed that GFAP distributions in the *Normal Class* might be related systematically to several variables that *follow a Gaussian distribution*. In the *Pathological Class*, however, we assumed that GFAP distributions would follow a continuous *Log-Gamma distribution* as it is common in indicators that are biased monotonically by a disease. Sensitivity analyses examined whether to use more classes; the two- class model performed the best and is reported here. A quantile-quantile plot upheld the Gaussian distributional assumptions; supporting this decision, we found that the skew and kurtosis were within normal parameters (s = 0.46, k = 2.59). The Pathological Class was non- Gaussian and highly skewed, so we used the Gamma distribution to measure the serologic protein volume. These two classes were derived from the model directly for bivariable comparisons and to describe these classes. For descriptive purposes, class membership was estimated using posterior predicted values; a cutoff value ≥0.10 identifying participants in the Pathological Class. This value appeared to differentiate the highest-high GFAP levels from the low to low-high GFAP levels in distributional analyses. Sensitivity analyses determined whether the highest-high GFAP cutoffs were a primary driver of reported results to address potential bias (see Appendix Table 1.) We further examined symptom-specific predictors of PTSD and depression on the distribution volume of GFAP using OLS regression (Appendix Table 2.)

# Log gamma and negative binomial
在概率统计中，log-gamma函数和负二项分布（negative binomial distribution）是两个不同的概念。下面分别介绍它们的基本概念。

1.  Log-gamma函数： Gamma函数是一个广义阶乘函数，定义为：

Γ(x) = ∫(t^(x-1) * e^(-t) dt)，其中积分区间是从0到正无穷。

对于正整数n，Gamma函数有一个特殊性质：Γ(n) = (n - 1)!。Log-gamma函数是Gamma函数的自然对数，即：

log(Γ(x))。

Log-gamma函数在统计学和概率分布中经常出现，例如多项式分布和Dirichlet分布的共轭先验分布。

2.  负二项分布（Negative binomial distribution）： 负二项分布是一种离散概率分布，描述了在一系列独立的伯努利试验中，成功次数达到预定值（例如r次成功）所需的试验次数。负二项分布的概率质量函数（PMF）为：

P(X = k) = C(k - 1, r - 1) * p^r * (1 - p)^(k - r)，其中k = r, r + 1, r + 2, ...

这里，X表示试验次数，k是总试验次数，r是成功次数，p是每次试验成功的概率，C(n, m)表示组合数，即从n个元素中选取m个元素的组合方式。

如果您想了解log-gamma函数和负二项分布之间的差异，这里有一个简要的总结：

-   Log-gamma函数是一个连续函数，与Gamma函数的自然对数有关。
-   负二项分布是一种离散概率分布，描述了在一系列独立的伯努利试验中达到预定成功次数所需的试验次数。

两者之间没有直接的联系，但它们都在概率统计领域中有各自的应用。
## interpret log gamma
在统计学和数据分析中，对数伽玛（log-gamma）系数通常是指用对数伽玛分布拟合数据时得到的参数估计值。对数伽玛分布是一种连续概率分布，适用于正值数据，特别是那些具有偏态分布的数据。这种分布有两个参数：形状参数（shape parameter）和比例参数（scale parameter）。

当使用对数伽玛模型进行回归分析时，系数的解释与线性回归中的解释类似，但需要注意数据经过了对数变换。在对数伽玛回归模型中，解释变量（自变量）与响应变量（因变量）的对数之间存在线性关系。

假设我们有一个对数伽玛回归模型，如下所示：

`log(y) = β0 + β1 * x1 + β2 * x2 + ... + ε`

其中，y是响应变量，x1和x2是解释变量，β0是截距项，β1和β2是对应的回归系数，ε是误差项。

在这种情况下，回归系数的解释如下：

1.  β0（截距项）：当所有解释变量的值为0时，响应变量的对数值的预测值。
    
2.  β1、β2等（其他系数）：当对应的解释变量（如x1）增加1个单位时，响应变量的对数值预计将发生的变化。例如，如果β1 = 0.5，那么当x1增加1个单位时，响应变量y的对数值预计将增加0.5个单位。
    

需要注意的是，这里的解释是基于响应变量的对数值，而不是原始值。为了得到原始值的解释，可以使用指数函数（exp）将回归系数转换回原始尺度。在这种情况下，系数将表示解释变量的变化与响应变量原始值的相对变化之间的关系。

在解释对数伽玛系数时，请务必考虑模型的整体拟合优度、变量的实际意义和可能的非线性关系。此外，还需要注意潜在的多重共线性、异常值和杠杆点等问题。

Log gamma models are used for predicting continuous and positive outcome variables. They are a type of generalized linear model (GLM) that uses a gamma distribution to model the response variable and a log link function to relate the response variable to the predictors.

To interpret the coefficients in a log gamma model, you need to understand that the log link function takes the natural logarithm (log) of the expected value of the response variable, so the coefficients represent the effect on the log scale. Here's how to interpret the coefficients:

1.  Intercept (β0): The intercept represents the expected value of the natural logarithm of the response variable when all predictor variables are equal to zero. To get the expected value of the response variable in the original scale, you can exponentiate the intercept (i.e., take the exponent of β0).
    
2.  Predictor Coefficients (β1, β2, …, βn): The coefficients of the predictor variables represent the expected change in the natural logarithm of the response variable for a one-unit increase in the corresponding predictor variable, holding all other predictors constant. To interpret the coefficients in terms of the original scale of the response variable, you can use the following steps:
    
    a. **Calculate the percent change: Exponentiate the coefficient, and then subtract 1. Multiply the result by 100 to get the percent change. Mathematically, it is (e^β - 1) * 100**.
    
    b. Interpretation: If the percent change is positive, it indicates an increase in the expected value of the response variable for a one-unit increase in the predictor. If the percent change is negative, it indicates a decrease in the expected value of the response variable for a one-unit increase in the predictor.
    

Remember that, since the model is on a log scale, the relationship between the predictor and the response variable is multiplicative, not additive. This means that for a one-unit change in the predictor variable, the expected value of the response variable will change by a percentage (multiplicative effect) rather than by a fixed amount (additive effect).

Also, be cautious when interpreting coefficients for categorical variables or variables with interactions, as the interpretation can be more complex.

The interpretation of log gamma model coefficients is similar to that of other regression models. In the log gamma model, the coefficients represent the effect of each predictor variable on the logarithm of the response variable.

**Here are some steps to interpret the coefficients of a log gamma model:**

1.  Examine the sign of the coefficients: A *positive* coefficient indicates that an *increase* in the predictor variable is associated with an increase in the response variable, while a *negative* coefficient indicates that an increase in the predictor variable is associated with a *decrease* in the response variable.
    
2.  Look at the magnitude of the coefficients: The magnitude of the coefficient represents the size of the effect of the predictor variable on the response variable. Larger coefficients indicate a stronger effect, while smaller coefficients indicate a weaker effect.
    
3.  Interpret the coefficients in terms of the units of the predictor variable: The coefficients of a log gamma model are on the logarithmic scale, so their interpretation can be a bit more complex than in linear regression models. One way to interpret the coefficients is to exponentiate them, which will give you the multiplicative effect of each predictor variable on the response variable. For example, **if a coefficient is 0.5, this means that a one-unit increase in the predictor variable is associated with a multiplicative increase of exp(0.5) = 1.65 in the response variable**.
    
4.  Consider the standard errors and confidence intervals of the coefficients: The standard errors of the coefficients represent the amount of variability in the estimates due to sampling error. Confidence intervals give you a range of plausible values for the coefficients, which can be useful for assessing the precision of the estimates.
    

Overall, interpreting the coefficients of a log gamma model requires a careful consideration of the model and the data being analyzed.

In a log-gamma regression model, the exponentiated coefficients (i.e., the exponential of the regression coefficients) represent the **gamma rate ratio (GRR)**. The GRR is the **ratio of the expected rate** of the dependent variable (which is a continuous, positive variable) for a one-unit change in the independent variable, holding all other variables constant.

The GRR is *similar to the incidence rate ratio (IRR)* in Poisson regression, but while the IRR assumes a Poisson distribution for the dependent variable, the log-gamma regression assumes a gamma distribution.

It is important to note that the gamma distribution is a continuous distribution, while the Poisson distribution is a discrete distribution. This means that the interpretation of the GRR may be slightly different from that of the IRR. While the IRR measures the change in the expected count of the dependent variable for a one-unit change in the independent variable, the GRR measures the change in the expected rate of the dependent variable.

Therefore, in a log-gamma regression model, the exponentiated coefficients represent gamma rate ratios (GRR).
![[Pasted image 20230616190726.png|300]]
## 对于大量零值和严重右偏的数据，

使用log-gamma模型可能不是一个合适的选择。log-gamma函数只适用于正值数据，但对于包含零值的数据集，它并不适用。另外，gamma分布对于零值没有很好的拟合能力。

对于这种类型的数据，可以考虑使用零膨胀模型（zero-inflated model）或者混合模型。零膨胀模型是一种混合模型，它结合了零值生成过程和另一个非零值生成过程。以下是几种可能适用于这种情况的模型：

1.  零膨胀泊松模型（Zero-Inflated Poisson Model，ZIP）：这种模型适用于非负整数值数据，包括两个部分：一个泊松分布模型用于拟合非零值，一个概率模型用于拟合零值。
    
2.  零膨胀负二项模型（Zero-Inflated Negative Binomial Model，ZINB）：与ZIP类似，但使用负二项分布替换泊松分布。负二项分布能够更好地处理过度离散（overdispersion）的数据。
    
3.  零膨胀Gamma模型或其他零膨胀连续分布模型：对于连续的右偏数据，可以考虑使用零膨胀Gamma模型。这个模型结合了零值生成过程和一个适用于正值的连续概率分布（例如Gamma分布）。
    

在选择合适的模型时，需要根据数据的实际情况进行评估。对于具有大量零值和严重右偏的数据，零膨胀模型或混合模型通常能够提供更好的拟合效果。

## 确定数据是否为零膨胀（zero-inflated）
通常涉及对数据进行探索性数据分析（EDA）和统计检验。以下是一些建议：

1.  描述性统计和可视化： 首先，计算数据的描述性统计量，如均值、中位数、方差、峰度和偏度等。然后，通过绘制直方图、箱线图或核密度图等可视化图形来观察数据分布。零膨胀数据通常具有大量的零值和非零值的偏态分布。
    
2.  比较基准模型： 对数据拟合一个基准模型（如泊松分布或负二项分布）并计算拟合优度（如AIC、BIC或似然比等）。然后，拟合一个零膨胀模型（如零膨胀泊松或零膨胀负二项模型），并计算相应的拟合优度。通过比较两个模型的拟合优度，可以评估零膨胀模型是否更适合数据。
    
3.  模型选择检验： 使用模型选择方法，如交叉验证、Akaike信息准则（AIC）、贝叶斯信息准则（BIC）等，来比较零膨胀模型和非零膨胀模型的性能。如果零膨胀模型的拟合优度明显优于非零膨胀模型，那么数据可能是零膨胀的。
    
4.  Vuong检验： Vuong检验是一种用于非嵌套模型比较的统计检验。通过计算似然比统计量的标准化值，Vuong检验可以帮助确定零膨胀模型与非零膨胀模型之间是否存在显著差异。在R中，可以使用`pscl`包的`vuong`函数进行Vuong检验。
    

请注意，确定数据是否为零膨胀通常需要对数据和模型进行综合评估。单一的方法或指标可能无法提供确凿的证据。结合多种方法和指标可以帮助更准确地判断数据是否为零膨胀。

## what differences between gmma log and only log transformed outcome OLS
When analyzing non-normally distributed data, two common approaches include using a generalized linear model (GLM) with an appropriate distribution and link function (e.g., gamma with a log link) or transforming the outcome variable (e.g., log transformation) and using ordinary least squares (OLS) regression. Here are the key differences between these two approaches:

1.  Model assumptions and estimation:
    
    Gamma GLM with a log link:
    
    -   Assumes that the outcome variable follows a gamma distribution.
    -   The model relates the expected value of the response variable to the predictor variables using a logarithmic link function.
    -   Estimates parameters using maximum likelihood estimation (MLE).
    
    Log-transformed outcome OLS:
    
    -   Assumes that the log-transformed outcome variable follows a normal distribution.
    -   The model relates the expected value of the log-transformed response variable to the predictor variables using an identity link function.
    -   Estimates parameters using ordinary least squares.
2.  Interpretation:
    
    Gamma GLM with a log link:
    
    -   The model estimates the multiplicative effects of the predictor variables on the original (untransformed) outcome variable, while accounting for the gamma distribution.
    -   Coefficients are interpreted as the multiplicative change in the expected outcome for a one-unit increase in the predictor variable, holding other predictor variables constant.
    
    Log-transformed outcome OLS:
    
    -   The model estimates the additive effects of the predictor variables on the log-transformed outcome variable.
    -   Coefficients are interpreted as the additive change in the expected log-transformed outcome for a one-unit increase in the predictor variable, holding other predictor variables constant. To interpret the coefficients in terms of the original (untransformed) outcome, you can exponentiate the coefficients to obtain the multiplicative change in the expected outcome.
3.  Prediction:
    
    Gamma GLM with a log link:
    
    -   Predictions are generated on the original scale of the outcome variable directly.
    
    Log-transformed outcome OLS:
    
    -   Predictions are generated on the log scale of the outcome variable, and then back-transformed to the original scale using exponentiation.

Both methods are valid when dealing with non-normally distributed data. The choice between the two approaches depends on the research question, the distribution of the outcome variable, and the assumptions that best fit the data. It is essential to validate the model assumptions and assess the goodness of fit when choosing a modeling approach.

# Why Central limit theorem cannot make count data suit for linear regression
The Central Limit Theorem (CLT) states that the distribution of the sum or average of a large number of independent, identically distributed random variables approaches a normal distribution, regardless of the original distribution. While CLT can help with concerns related to the normality of the sampling distribution of the estimators, it does not address other issues specific to count data.

Count data is characterized by the following properties:

1.  Discrete: Count data consists of non-negative integers (0, 1, 2, 3, ...), while linear regression assumes a continuous outcome. Applying linear regression to count data can lead to biased estimates and incorrect inferences because it does not account for the discrete nature of the data.
2.  Non-negative: Count data is always non-negative, as it represents the number of occurrences of an event. Linear regression, on the other hand, can produce negative predictions, which are not meaningful for count data.
3.  Variance structure: Linear regression assumes constant variance (homoscedasticity) across the range of predicted values, while count data often exhibits a variance that depends on the mean. For example, in a Poisson distribution, the variance is equal to the mean, while in a negative binomial distribution, the variance is greater than the mean.
4.  Link function: In linear regression, the relationship between the predictors and the outcome is modeled directly. In contrast, generalized linear models (GLMs) for count data, such as Poisson or negative binomial regression, use a link function to relate the predictors to the outcome, such as the natural logarithm of the expected count in the case of Poisson regression.  

Although the Central Limit Theorem helps to ensure that the sampling distribution of the estimators in linear regression will be approximately normal for large sample sizes, it does not address these specific issues related to count data. Therefore, using linear regression for count data may lead to biased and inefficient estimates, even with a large sample size. Instead, it is more appropriate to use models specifically designed for count data, such as Poisson regression or negative binomial regression, which account for the unique characteristics of count data.
