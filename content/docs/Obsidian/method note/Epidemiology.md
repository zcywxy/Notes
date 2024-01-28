# Measurements

The outcomes of epidemiologic research have been traditionally defined in terms of disease, although the growing application of epidemiology to public health and preventive medicine increasingly requires the use of outcomes measuring health in general (e.g., outcome measures of functional status in epidemiologic studies related to aging). Outcomes can be expressed as either discrete (e.g., disease occurrence or severity) or continuous variables. Continuous variables, such as blood pressure and glucose levels, are commonly used as outcomes in epidemiology. The main statistical tools used to analyze correlates or predictors of these types of outcomes are the correlation coefficients, analysis of variance, and linear regression analysis, which are discussed in numerous statistical textbooks. Linear regression is briefly reviewed in Chapter 7 (Section 7.4.1) as a background for the introduction to multivariate regression analysis techniques in epidemiology. Other methodological issues regarding the analysis of continuous variables in epidemiology, specifically as they relate to quality control and reliability measures, are covered in Chapter 8. Most of the present chapter deals with categorical dichotomous outcome variables, which are the most often used in epidemiologic studies. The frequency of this type of outcome can be generically defined as the number of individuals with the outcome (the numerator) divided by the number of individuals at risk for that outcome (the denominator). There are two types of absolute measures of outcome frequency: incidence and prevalence (Table 2-1). Although the term incidence has been traditionally used to indicate a proportion of newly developed (incident) cases of a disease, in fact, it encompasses the frequency of any new health- or disease-related event, including death, recurrent disease among patients, disease remission, menopause, and so forth. Incidence is a particularly important measure for analytical epidemiologic research, as it allows the estimation of risk necessary to assess causal associations (Chapter 10, Section 10.2.4). Prevalence, on the other hand, measures the frequency of an existing outcome either at one point in time—point prevalence, or during a given period—period prevalence. A special type of period prevalence is the lifetime prevalence, which measures the cumulative lifetime frequency of an outcome up to the present time (i.e., the proportion of people who have had the event at any time in the past).

流行病学研究的结果传统上是根据疾病来定义的，尽管流行病学在公共卫生和预防医学中的应用越来越多，越来越需要使用总体上衡量健康的结果（例如，与衰老相关的流行病学研究中功能状态的结果测量）。结果可以表示为离散变量（例如，疾病发生或严重程度）或连续变量。连续变量，例如血压和血糖水平，通常用作流行病学的结果。用于分析这些类型结果的相关性或预测因素的主要统计工具是相关系数、方差分析和线性回归分析，许多统计教科书都讨论了这些工具。第 7 章（第 7.4.1 节）简要回顾了线性回归，作为介绍流行病学中多元回归分析技术的背景。有关流行病学中连续变量分析的其他方法论问题，特别是与质量控制和可靠性措施有关的问题，将在第 8 章中介绍。本章的大部分内容涉及分类二分类结果变量，这是流行病学研究中最常用的。此类结果的频率通常可以定义为具有该结果的个体数量（分子）除以该结果存在风险的个体数量（分母）。结果频率的绝对测量有两种类型：发生率和流行率（表 2-1）。尽管术语“发生率”传统上用于表示某种疾病新发展（事件）病例的比例，但实际上，它包含任何新的健康或疾病相关事件的频率，包括死亡、患者中的复发性疾病、疾病缓解、更年期等。发病率是分析流行病学研究的一个特别重要的衡量标准，因为它允许估计必要的风险以评估因果关系（第 10 章，第 10.2.4 节）。另一方面，患病率衡量现有结果在某个时间点（点患病率）或给定期间（期间患病率）的频率。一种特殊类型的期间患病率是终生患病率，它衡量截至当前时间的结果的累积终生频率（即，在过去任何时间发生过该事件的人的比例）。

For both prevalence and incidence, it is necessary to have a clear definition of the outcome as an event (a “noteworthy happening,” as defined in an English dictionary1). In epidemiology, an event is typically defined as the occurrence of any phenomenon of disease or health that can be discretely characterized. For incidence (see Section 2.2), this characterization needs to include a precise definition of the time of occurrence of the event in question. Some events are easily defined and time of occurrence easily located in time, such as “birth,” “death,” “surgery,” and “trauma.” Others are not easily defined and require some more or less arbitrary operational definition for study, such as “menopause,” “recovery,” “dementia,” or cytomegalovirus (CMV) disease (Table 2-2). An example of the complexity of defining certain clinical events is given by the widely adopted definition of a case of AIDS, which uses a number of clinical and laboratory criteria. The next two sections of this chapter describe the different alternatives for the calculation of incidence and prevalence. The last section describes the odds, another measure of disease frequency that is the basis for a measure of association often used in epidemiology, particularly in case-based case-control studies (Chapter 1, Section 1.4.2)—namely, the

odds ratio (Chapter 3, Section 3.4.1).

对于流行率和发病率，有必要将结果明确定义为事件（英语词典中定义的“值得注意的事件”1）。在流行病学中，事件通常被定义为可以离散表征的任何疾病或健康现象的发生。对于发生率（参见第 2.2 节），该特征需要包括所讨论事件发生时间的精确定义。有些事件很容易定义，发生的时间也很容易在时间上定位，例如“出生”、“死亡”、“手术”和“创伤”。其他的定义并不容易，需要一些或多或少的任意操作定义来研究，例如“更年期”、“恢复”、“痴呆症”或巨细胞病毒 (CMV) 疾病（表 2-2）。广泛采用的艾滋病病例定义给出了定义某些临床事件的复杂性的一个例子，该定义使用了许多临床和实验室标准。 2本章接下来的两节描述了计算发病率和流行率的不同选择。最后一部分描述了几率，这是另一种疾病频率的度量，它是流行病学中常用的关联度量的基础，特别是在基于病例的病例对照研究中（第 1 章，第 1.4.2 节）——即优势比（第 3 章，第 3.4.1 节）。

## Incidence

Incidence is best understood in the context of prospective (cohort) studies (Chapter 1, Section 1.4.1). The basic structure of any incidence indicator is represented by the number of events occurring in a defined population over a specified period of time (numerator), divided by the population at risk for that event over that time (denominator). There are two types of measures of incidence defined by the type of denominator: (1) incidence based on persons at riskand (2) incidence based on person-time units at risk.

在前瞻性（队列）研究（第 1 章，第 1.4.1 节）的背景下，可以最好地理解发生率。 任何发生率指标的基本结构都由特定时间段内特定人群中发生的事件数量（分子）除以该时间段内该事件的风险人群（分母）来表示。 分母类型定义了两种类型的发生率度量：(1) 基于处于危险中的人的发生率和 (2) 基于处于危险中的人-时间单位的发生率。

![[Pasted image 20230410122747.png|600]] ![[Pasted image 20230410122925.png|600]] 

## Risk, rate, odds

ratio 就是个比率，俩数相除就是 比率。可以有单位，也可以无单位。

probability 就是事件发生的可能性，发生次数/总观察数。

rate 是 事件发生的概率 局限在一个 时间单位。

*Risk, another term for probability*

Absolute (arithmetic) change = rate2–rate1

Relative change = rate2/rate1

Proportional (percent) change = (rate2–rate1)/rate1  

-   **Probability**: _(# events that occured in a period)/(number of entities eligible)_.  Probability is the proportion (ie, percentage) of times an event would occur if an observation were repeated many times. This number ranges between 0 and 1. For instance, if I want to know the probability or risk that I get a cold this winter, I will want to count the number of people who lived in my city over that winter and got a cold during the winter and divide that by the total number of people living in my city that winter.

-   **Rate**. _(# events that occurred in a period)/(total time period experience by all subjects)_. Now consider the case where different people live in my cite different amounts of time. I could measure the total number of flu cases divided by the total number of days the eligilbe people lived in my city. Another example would be a health plan that measures the rate at which people are hospitalized. People often enroll and disenroll in health plans so for a given year, the health plan would count up all the hospitalizations in the year and divide by the total months enrolled of all these people.
-   **Relative risk**. _(probability of outcome in the exposed)/(probability of the outcome in the unexposed)._  ratio of probabilities. Let’s go back to my flu example. Let’s say that kids spread the flu easily. Assume one did a study where 40% of adults with young children got the flu, but only 20% of adults without young children got the flu. In this case, the relative risk is 2 (i.e., 40%/20% =2). A relative risk number can vary between 0 and infinity.
-   **Odds**: _(probability of an outcome)/(1-probability of an outcome)_. Odds are simply a different expression of the probability: the probability of an event divided by the probability of the event not happening.
-   **Odds ratio**.  _(Odds of exposed group)/(odds in unexposed group)_. An odds ratio is the odds of the event in one group, for example, those exposed to a drug, divided by the odds in another group not exposed. 

A **ratio** can be written as one number divided by another (a fraction) of the form a/b

-   Both a and b refer to the frequency of some event or occurrence

A **proportion** is a ratio in which the numerator is a subset (or part) of the denominator and can be written as a/(a+b)

-   A relative frequency
-   A proportion is always a ratio

A **rate** is a ratio of the form a*/ (a+b)

-   a* = the frequency of events during a certain time period
-   a+b = the number at risk of the event during that time period
-   The calendar time period is the same in both the numerator and denominator of a rate
-   A rate may or may not be a proportion
-   A rate is always a ratio
-   A rate expresses the relative frequency of an event per unit time (“risk”)
![[Pasted image 20230410123128.png|400]] ![[Pasted image 20230410123049.png|600]]

Odds ratios always exaggerate the true relative risk to some degree. When the probability of the disease is low (for example, less than 10%), the odds ratio approximates the true relative risk. As the event becomes more common, the exag- geration grows, and the odds ratio no longer is a useful proxy for the relative risk.

Although the odds ratio is always a valid measure of association, it is not always a good substitute for the relative risk. Because of the difficulty in understanding odds ratios, their use should probably be limited to case-control studies and logistic regression, for which odds ratios are the proper measures of association.

If the odds ratio is greater than 1.0, it is larger than the relative risk. Conversely, if the odds ratio is less than 1.0, it is smaller than the relative risk. This discrepancy becomes clinically important only when the baseline probabilities of the out- come exceed 0.10 to 0.20.

in case-control studies, researchers have a numerator (cases) but no denominator, so rates and relative risks cannot be determined.

For logistic regression ![[Pasted image 20230410123245.png|200]] 

An odds ratio of 1.5 means the odds of the outcome in group A happening are one and a half times the odds of the outcome happening in group B.

Approximate the relative risk from an adjusted odds ratio. ![[Pasted image 20230410123304.png|200]] 

P0 is the proportion of those unexposed who develop the outcome, OR is the odds ratio, and RR is the relative risk estimated from the odds ratio. As the background rate of the outcome gets low (ie, P0 approaches zero in the “rare disease assumption”), the denominator in brackets approaches 1.0, and the relative risk approaches the odds ratio.



-   **Risk difference.** _Risk in exposed group – risk in unexposed group_. 

### Converting Probability and Odds

Probability to Odds

The formula for converting from probability to odds is `probability/(1–probability)=odds`

With a probability of 0.30, the odds would be calculated as
0.30/(1– 0.30)=0.30/0.70=0.43

Odds to Probability

In the reverse direction, the formula for converting odds to probability is`odds/(odds+1)=probabilit`

With an odds of 4, the probabil- ity would be calculated as
4/(4+1)=4/5=0.80

ref:[https://www.healthcare-economist.com/2018/11/16/what-is-the-difference-between-rate-risk-and-odds/](https://www.healthcare-economist.com/2018/11/16/what-is-the-difference-between-rate-risk-and-odds/)

[https://www.cureus.com/articles/39455-whats-the-risk-differentiating-risk-ratios-odds-ratios-and-hazard-ratios](https://www.cureus.com/articles/39455-whats-the-risk-differentiating-risk-ratios-odds-ratios-and-hazard-ratios)

[http://ocw.jhsph.edu/courses/fundepi/pdfs/Lecture5.pdf](http://ocw.jhsph.edu/courses/fundepi/pdfs/Lecture5.pdf)

# Confounder Definition

to study whether A causes disease B, we say a third factor X is a confounder if

-   Factor X is a known risk factor for disease B
-   Factor X is associated with A, but is not a result of factor A.

![[Pasted image 20230410123329.png|500]] 

# Bias

related to study design and procedures

###  Selection/Information Bias

![[Pasted image 20230410123430.png|500]] ![[Pasted image 20230410123356.png|500]] 

## Bias vs Confounders

-   bias is the error of the study design
-   confounding is the true phenomenon, needs to be explained. if not explain, it is a bias error.
-   the modifier does not have to be associated with exposure, exposure has different effects on the subgroup

# Mediator: Mediation Analysis

Before we start, please keep in mind that, as any other regression analysis, mediation analysis does not imply causal relationships unless it is based on experimental design.

To analyze mediation:  
1. Follow Baron & Kenny’s steps  
2. Use either the Sobel test or bootstrapping for significance testing.

The following shows the basic steps for mediation analysis suggested by Baron & Kenny (1986). A mediation analysis is comprised of three sets of regression: X → Y, X → M, and X + M → Y. This post will show examples using R, but you can use any statistical software. They are just three regression analyses!

Download data online. This is a simulated dataset for this post. myData <- read.csv('http://static.lib.virginia.edu/statlab/materials/data/mediationData.csv') 

![[Pasted image 20230410121620.png|500]] ![[Pasted image 20230410121651.png|600]] ![[Pasted image 20230410121739.png|500]] 

If the effect of X on Y completely disappears, M fully mediates between X and Y (_full mediation_). If the effect of X on Y still exists, but in a smaller magnitude, M partially mediates between X and Y (_partial mediation_). The example shows a full mediation, yet a full mediation rarely happens in practice.

Once we find these relationships, we want to see if this mediation effect is statistically significant (different from zero or not). To do so, there are two main approaches: the Sobel test (Sobel, 1982) and bootstrapping (Preacher & Hayes, 2004). In R, you can use sobel() in ‘multilevel’ package for the Sobel test and mediate() in ‘mediation’package for bootstrapping. Because bootstrapping is strongly recommended in recent years (although Sobel test was widely used before), I’ll show only the bootstrapping method in this example.

`mediate()` takes two model objects as input (X → M and X + M → Y) and we need to specify which variable is an IV (treatment) and a mediator (mediator). For bootstrapping, set boot = TRUE and sims to at least 500. After running it, look for ACME (Average Causal Mediation Effects) in the results and see if it’s different from zero. For details of mediate(), please refer to Tingley, Yamamoto, Hirose, Keele, & Imai (2014).

```
library(mediation)
results <- mediate(model.M, model.Y, treat='X', mediator='M',
                   boot=TRUE, sims=500)
summary(results)
#                Estimate 95% CI Lower 95% CI Upper p-value
# ACME             0.3565       0.2155       0.5291    0.00
# ADE              0.0396      -0.1761       0.2598    0.66
# Total Effect     0.3961       0.1563       0.5794    0.00
# Prop. Mediated   0.9000       0.5254       1.8820    0.00

### ACME = 0.3565, 95% CI [0.2155, 0.5291]  # significant!
### ACME stands for Average Causal Mediation Effects
### ADE stands for Average Direct Effects
### Total Effect is a sum of a mediation (indirect) effect and a direct effect
```

Note that the Total Effect in the summary (0.3961) is b1 in the first step: a total effect of X on Y (without M). The direct effect(ADE, 0.0396) is b4 in the third step: a direct effect of X on Y after taking into account a mediation (indirect) effect of M. Finally, the mediation effect (ACME) is the total effect minus the direct effect (b1–b4, or 0.3961 - 0.0396 = 0.3565), which equals to a product of a coefficient of X in the second step and a coefficient of M in the last step (b2×b3, or 0.56102 * 0.6355 = 0.3565). The goal of mediation analysis is to obtain this indirect effect and see if it’s statistically significant.

By the way, we don’t have to follow all three steps as Baron and Kenny suggested. We could simply run two regressions (X → M and X + M → Y) and test its significance using the two models. However, the suggested steps help you understand how it works!

```
model.M <- lm(M ~ X, myData)
model.Y <- lm(Y ~ X + M, myData)
results <- mediate(model.M, model.Y, treat='X', mediator='M',
                   boot=TRUE, sims=100)
summary(results)
```

Mediation analysis is not limited to linear regression; we can use logistic regression or polynomial regression and more. Also, we can add more variables and relationships, for example, moderated mediation or mediated moderation. However, if your model is very complex and cannot be expressed as a small set of regressions, you might want to consider structural equation modeling instead.

To sum up, here’s a flowchart for mediation analysis!
![[Pasted image 20230410121908.png]]

ref: [https://data.library.virginia.edu/introduction-to-mediation-analysis/](https://data.library.virginia.edu/introduction-to-mediation-analysis/)

# Moderator: Interaction Analysis

## Paper: Visualizing interaction effects: a proposal for presentation and interpretation
[link](file:///Users/yuan/Dropbox/papers/EducationCog/Visualizing%20interaction%20effects-%20a%20proposal%20for%20presentation%20and%20interpretation.pdf)
Y=A+B+A* B
The main effect of A is : unit increase in A is associated with unit increase in Y, given the second interacting variable is equal to a specific value. Those are **conditional effects**. The *P-values* of the conditional effects are given: test whether the slope of one variable is significantly *different from zero*, if the *other constituting variable is zero*. 

==Question==: Does all regression models test coefficient like this?

![[Pasted image 20230822142118.png|400]] ![[Pasted image 20230822142214.png|400]] ![[Pasted image 20230822142548.png|400]]  

- **The P-values and β1 is for A when B=0**, if want to test the effect of x1 for a specific x2
	- ![[Pasted image 20230822142423.png|400]] 

## Plot Interaction effect
![[Pasted image 20230822143743.png]]
![[Pasted image 20230410123536.png|500]] ![[Pasted image 20230410124351.png|500]] ![[Pasted image 20230410124413.png|500]] ![[Pasted image 20230410124538.png|500]] ![[Pasted image 20230410124559.png|420]] ![[Pasted image 20230410124643.png|500]] ![[Pasted image 20230410124702.png|500]] ![[Pasted image 20230410124730.png|540]] ![[Pasted image 20230410124812.png|540]] 


## Summary

取决于结果的单位，absolute/relative，分为additive/multiplicative 两种interaction

两种测试方法：分层看结果，或者看joint effect 在 observation & expectation 里是否一样

The term interaction is used in epidemiology to describe a situation in which two or more risk factors modify the effect of each other with regard to the occurrence or level of a given outcome. This phenomenon is also known as effect modification and needs to be distinguished from the phenomenon of confounding. As discussed in detail in Chapter 5, confounding refers to a situation in which a variable that is associated with both the exposure and the outcome of interest is responsible for the entirety or part of the statistical association between the exposure and the outcome. Interaction between a given variable (effect modifier) and a given exposure is a different phenomenon, as detailed in the following sections. The clear distinction between confounding and interaction notwithstanding, it is important to recognize that, as discussed later in this chapter, under certain circumstances, interaction might cause confounding (see Section 6.8) and the presence of confounding might cause the appearance of an interaction effect (Section 6.10.2).

术语相互作用在流行病学中用于描述两个或多个风险因素在给定结果的发生或水平方面改变彼此影响的情况。这种现象也称为效应修正，需要与混杂现象区分开来。正如第 5 章详细讨论的，混杂是指与暴露和感兴趣的结果相关的变量对暴露和结果之间的全部或部分统计关联负责的情况。给定变量（效果修饰符）和给定曝光之间的相互作用是一种不同的现象，如以下部分所述。尽管混淆和交互之间有明确的区别，但重要的是要认识到，正如本章后面所讨论的，在某些情况下，交互可能会导致混淆（参见第 6.8 节），而混淆的存在可能会导致交互的出现效果（第 6.10.2 节）。

For dichotomous variables, interaction means that the effect of the exposure on the outcome differs depending on whether or not another variable (the effect modifier) is present. If interaction exists and the presence of the effect modifier strengthens (accentuates) the effect of the exposure of interest, this variable and the exposure are said to be synergistic [ˌsɪnərˈdʒɪstɪk] (positive interaction); if the presence of the effect modifier diminishes or eliminates the effect of the exposure of interest, it can be said that the effect modifier and the exposure are antagonistic [ænˌtæɡəˈnɪstɪk] (negative interaction). Likewise, in the case of continuous variables, interaction means that the effect of exposure on outcome (e.g., expressed by the regression coefficient; see Chapter 7, Section 7.4.1) depends on the level of another variable (rather than on its presence/absence).

对于二分变量，交互作用意味着暴露对结果的影响取决于是否存在另一个变量（效应修饰符）。如果相互作用存在并且效应修饰符的存在加强（强调）感兴趣的暴露的影响，则该变量和暴露被称为协同作用（正相互作用）；如果效应调节剂的存在减弱或消除了感兴趣的暴露的影响，则可以说效应调节剂和暴露是对立的（负相互作用）。同样，在连续变量的情况下，交互作用意味着暴露对结果的影响（例如，由回归系数表示；见第 7 章第 7.4.1 节）取决于另一个变量的水平（而不是其存在/缺席）。

A minimum of three factors is needed for the phenomenon of interaction to occur. For this chapter, the main putative risk factor is designated as factor A, the outcome variable as Y, and the third factor (potential effect modifier) as Z. In addition, although it is recognized that there are differences between absolute or relative differences in risk, rate, and odds, the generic terms risk, attributable risk, and relative risk are mostly used. In this chapter, the term homogeneity indicates that the effects of a risk factor A are homogeneous or similar in strata formed by factor Z. Heterogeneity of effects, therefore, implies that these effects are dissimilar. The discussion that follows is largely based on the simplest situation involving interaction between two independent variables with two categories each and a discrete outcome (e.g., disease present or absent). Other types of interaction, which can be assessed but are not discussed in detail in this textbook, include those based on more than two “independent” variables, or on continuous variables. Interaction can be defined in two different yet compatible ways. Each definition leads to a specific strategy for the evaluation of interaction, both of which are discussed in detail in the following section.

相互作用现象的发生至少需要三个因素。在本章中，主要假定的风险因素被指定为因素 A，结果变量被指定为 Y，第三个因素（潜在影响修饰符）被指定为 Z。此外，尽管认识到在绝对或相对差异之间存在差异风险、比率和几率，主要使用通用术语风险、归因风险和相对风险。在本章中，术语同质性表示风险因素 A 的影响在由因素 Z 形成的层中是同质的或相似的。因此，影响的异质性意味着这些影响是不同的。接下来的讨论主要基于最简单的情况，涉及两个独立变量之间的相互作用，每个变量有两个类别和一个离散结果（例如，存在或不存在疾病）。可以评估但在本教科书中未详细讨论的其他类型的交互包括基于两个以上“独立”变量或连续变量的交互。

交互可以用两种不同但兼容的方式定义。每个定义都会导致一个特定的交互评估策略，这两种策略都将在下一节中详细讨论。

As discussed by Petitti,1 the term “effect” needs to be used with caution when inferring etiologic relationships from observational studies. A more appropriate term to define interaction would be perhaps “association modification,” but as the expression “effect modification” is widely used in the literature regardless of the soundness of the causal inference, we use it in a somewhat nonspecific sense, i.e., expressing both causal and noncausal interactions. An important issue in the evaluation of interaction is how to measure “effect.” Effect can be measured either by the attributable risk (additive model) or by a relative difference—for example, the relative risk (multiplicative model). The conceptual basis for the evaluation of interaction is the same for both models.

正如 Petitti 所讨论的，1 在从观察性研究推断病因关系时，需要谨慎使用“效应”一词。 定义交互作用的更合适的术语可能是“关联修饰”，但由于“效果修饰”一词在文献中被广泛使用，而不管因果推断的合理性如何，我们以某种非特定的意义使用它，即表达 因果和非因果相互作用。交互评价中的一个重要问题是如何衡量“效果”。 效果可以通过归因风险（加法模型）或相对差异来衡量——例如，相对风险（乘法模型）。 两种模型的交互评估的概念基础是相同的。

## Definition

1. Definition based on homogeneity or heterogeneity of effects: Interaction occurs when the effect of a risk factor A on the risk of an outcome Y is not homogeneous in strata formed by a third variable Z. When this definition is used, variable Z is often referred to as an effect modifier.

2. Definition based on the comparison between observed and expected joint effects of risk factor A and third variable Z: Interaction occurs when the observed joint effect of A and Z differs from that expected on the basis of their independent effects.

1. 基于效应的同质性或异质性的定义：当风险因素 A 对结果 Y 风险的影响在由第三个变量 Z 形成的分层中不均匀时，就会发生相互作用。当使用这个定义时，变量 Z 通常是 称为效果修饰符。

2. 基于风险因素 A 和第三个变量 Z 的观察和预期联合效应之间比较的定义：当观察到的 A 和 Z 的联合效应不同于基于它们的独立效应的预期联合效应时，就会发生相互作用。

As discussed by Petitti,1 the term “effect” needs to be used with caution when inferring etiologic relationships from observational studies. A more appropriate term to define interaction would be perhaps “association modification,” but as the expression “effect modification” is widely used in the literature regardless of the soundness of the causal inference, we use it in a somewhat nonspecific sense, i.e., expressing both causal and noncausal interactions. An important issue in the evaluation of interaction is how to measure “effect.” Effect can be measured either by the attributable risk (additive model) or by a relative difference—for example, the relative risk (multiplicative model). The conceptual basis for the evaluation of interaction is the same for both models.

正如 Petitti 所讨论的，1 在从观察性研究推断病因关系时，需要谨慎使用“效应”一词。 定义交互作用的更合适的术语可能是“关联修饰”，但由于“效果修饰”一词在文献中被广泛使用，而不管因果推断的合理性如何，我们以某种非特定的意义使用它，即表达 因果和非因果相互作用。交互评价中的一个重要问题是如何衡量“效果”。 效果可以通过归因风险（加法模型）或相对差异来衡量——例如，相对风险（乘法模型）。 两种模型的交互评估的概念基础是相同的。

A **moderator** influences the level, direction, or presence of a relationship between variables. It shows you for whom, when, or under what circumstances a relationship will hold.

Moderators usually help you judge the [external validity](https://www.scribbr.com/methodology/external-validity/) of your study by identifying the limitations of when the relationship between variables holds. For example, while social media use can predict levels of loneliness, this relationship may be stronger for adolescents than for older adults. Age is a moderator here.

Moderators can be:

-   **Categorical variables** such as ethnicity, race, religion, favorite colors, health status, or stimulus type,
-   **Quantitative variables** such as age, weight, height, income, or visual stimulus size.
-   A **mediating variable** (or **mediator**) explains the process through which two [variables](https://www.scribbr.com/methodology/types-of-variables/) are related, while a**moderating variable** (or **moderator**) affects the strength and direction of that relationship.

## Evaluate Interaction

### Homogeneity Effect

Variability in susceptibility to an outcome given exposure to a risk factor is reflected by the between-individual heterogeneity of the effect of the risk factor. This is virtually a universal phenomenon for both infectious and noninfectious diseases. For example, even for a strong association, such as that between smoking and lung cancer, not every exposed person develops the disease. Assuming that chance does not play a role in determining which smokers develop lung cancer, this suggests that smoking by itself is not a sufficient cause. Thus, smokers who develop lung cancer are likely to differ from smokers who do not, in that another component cause2 must be present in smokers who develop lung cancer. This component risk factor may act by either completing the multicausal constellation needed to cause lung cancer or by increasing susceptibility to smoking- induced lung cancer (see also Chapter 10, section 10.2.1). In the latter situation, this component cause can be thought of generically as a susceptibility factor, which could be either genetically or environmentally determined.

风险因素影响的个体间异质性反映了在暴露于风险因素的情况下对结果的易感性的可变性。这实际上是传染病和非传染病的普遍现象。例如，即使吸烟与肺癌之间存在很强的关联，也不是每个暴露的人都会患上这种疾病。假设偶然性在决定哪些吸烟者患肺癌方面没有作用，这表明吸烟本身并不是一个充分的原因。因此，患肺癌的吸烟者可能与未患肺癌的吸烟者不同，因为患肺癌的吸烟者必须存在另一种原因2。该风险因素可能通过完成导致肺癌所需的多因组合或通过增加对吸烟诱发的肺癌的易感性而起作用（另见第 10 章第 10.2.1 节）。在后一种情况下，这个组成部分的原因通常可以被认为是一个易感因素，它可以是由遗传或环境决定的。

![[Pasted image 20230410122103.png|500]] ![[Pasted image 20230410122157.png|500]] ![[Pasted image 20230410122226.png|500]] 
![[Pasted image 20230410122356.png|500]]

A simplistic representation of the conceptual framework for interaction defined as heterogeneity of effects is shown in Figure 6-1. After it is observed that a statistical association exists between a risk factor A and a disease outcome Y, and it is reasonably certain that the association is not due to confounding, bias, or chance, the key question in evaluating interaction is this: Does the magnitude or direction of the effect of A on Y vary according to the occurrence of some other variable Z in the study population? A positive answer suggests the presence of interaction. For example, because diabetes is a stronger risk factor for coronary heart disease (CHD) in women than in men, it can be concluded that there is interaction (i.e., that gender modifies the effect of diabetes on CHD risk).

图 6-1 显示了定义为效应异质性的交互概念框架的简单表示。在观察到风险因素 A 和疾病结果 Y 之间存在统计关联，并且可以合理地确定关联不是由于混杂、偏倚或偶然导致之后，评估交互作用的关键问题是： A 对 Y 的影响的大小或方向根据研究人群中某些其他变量 Z 的出现而变化？肯定的回答表明存在交互作用。例如，由于糖尿病是女性比男性更严重的冠心病 (CHD) 危险因素，因此可以得出结论，存在交互作用（即，性别会改变糖尿病对 CHD 风险的影响）。

The conceptualization of interaction as the occurrence of heterogeneous effects of A (e.g., asbestos exposure) according to the presence or absence of Z (e.g., smoking) explains why the expression “effect modification” is used as a synonym for interaction. For example, appropriate language when describing the interaction between smoking and asbestos in regard to the risk of respiratory cancer is that “the effect of asbestos exposure on respiratory cancer risk is modified by cigarette smoking in that it is stronger in smokers than in nonsmokers.” The expression effect modifier suggests that the investigator has decided to consider A as the “main” variable of interest, and Z as the effect modifier. From the preventive standpoint, the variable not amenable to intervention (e.g., a gene) is usually regarded as the effect modifier, in contrast to an exposure that can be prevented or eliminated. Thus, for example, in a prospective study conducted in Eastern Finland, apolipoprotein e4 was shown to modify the effect of frequent drinking on dementia, in that a strong positive association was only present for carriers of the e4 allele.4 Another example is that recessive mutant alleles can be said to modify the effect of dietary phenyl- alanine on risk of clinical hyperphenylalaninemias, as diet-induced disease will only occur if these alleles are present. In both these examples, the choice of which variables are the effect modifiers (apolipoprotein e4 allele, recessive mutant alleles for hyperphenyl- alaninemia), although somewhat arbitrary, underscores the fact that these modifiers are immutable, whereas, on the other hand, both frequent drinking and diet can be altered. Another common strategy is to choose a variable with a known effect on the outcome as effect modifier and a novel potential risk factor as the independent variable of interest.

根据 Z 的存在或不存在（例如，吸烟），将相互作用概念化为 A 的异质效应（例如，石棉暴露）的发生，这解释了为什么“效果改变”一词被用作相互作用的同义词。例如，在描述吸烟和石棉之间关于呼吸道癌症风险的相互作用时，适当的语言是“石棉暴露对呼吸道癌症风险的影响会因吸烟而改变，因为吸烟者比不吸烟者更强。”表达式效果修饰符表明研究人员已决定将 A 视为感兴趣的“主要”变量，将 Z 作为效果修饰符。从预防的角度来看，与可以预防或消除的暴露相反，不适合干预的变量（例如，基因）通常被视为效应调节剂。因此，例如，在芬兰东部进行的一项前瞻性研究中，载脂蛋白 e4 被证明可以改变频繁饮酒对痴呆症的影响，因为只有 e4 等位基因的携带者才存在强烈的正相关。 4 另一个例子是隐性可以说突变等位基因改变了饮食苯丙氨酸对临床高苯丙氨酸血症风险的影响，因为只有存在这些等位基因时才会发生饮食诱导的疾病。在这两个例子中，选择哪些变量是效应修饰符（载脂蛋白 e4 等位基因，高苯丙氨酸血症的隐性突变等位基因），虽然有些武断，但强调了这些修饰符是不可变的，而另一方面，两者都频繁饮酒和饮食可以改变。另一种常见的策略是选择一个对结果有已知影响的变量作为效应修饰符，并选择一个新的潜在风险因素作为感兴趣的自变量。

As mentioned previously, a key issue in the evaluation of interaction is that it involves at least three variables: the main factor of interest A (e.g., diabetes), the potential effect modifier Z (e.g., gender), and a given outcome Y (e.g., coronary heart disease). There may, however, be more than two interacting independent variables—e.g., if diabetes were a more important risk factor for women than for men only among older subjects. In this hypothetical example, the simultaneous presence of two variables would be needed to modify the effect of diabetes: gender and age.

如前所述，相互作用评估中的一个关键问题是它至少涉及三个变量：感兴趣的主要因素 A（例如，糖尿病）、潜在影响修饰符 Z（例如，性别）和给定的结果 Y（例如，冠心病）。然而，可能存在两个以上相互作用的自变量——例如，如果糖尿病是女性比男性更重要的风险因素，则仅在老年受试者中。在这个假设的例子中，需要同时存在两个变量来改变糖尿病的影响：性别和年龄。

#### Detection of Additive Interaction: The Absolute Difference or Attributable Risk Model

Additive interaction is considered to be present when the attributable risk in those exposed to factor A varies (is heterogeneous) as a function of a third variable Z. The easiest way to evaluate interaction in this instance is to calculate the attributable risks for those exposed to risk factor A for each stratum defined by levels of the potential effect modifier Z. Hypothetical examples of this strategy to evaluate additive interaction are shown in Tables 6-1 and 6-2. 

In Table 6-1, the absolute excess risks of Y attributable to A do not differ according to exposure to Z. In Table 6-2, the attributable risk for A is larger for those exposed than for those not exposed to Z, denoting heterogeneity of the absolute effects of A. 
In these tables, there are two different reference categories for the attributable risks associated with A: for the stratum in which Z is absent, the reference category is Z absent, A absent; for the stratum in which Z is present, the reference category is Z present, A absent. The patterns shown in Tables 6-1 and 6-2 can be examined graphically (Figure 6-2A). A graph using an arithmetic scale to plot risks is used to assess additive interaction. The risks or rates for each category of the risk factor A are plotted separately for individuals exposed and those not exposed to the third variable Z. In this type of graph (with an arithmetic scale in the ordinate), the steepness of the slopes is a function of the absolute differences. Thus, when the absolute difference in risk of the outcome according to A (attributable risk in those exposed to A) is the same regardless of exposure to Z, the two lines are parallel. When the absolute differences differ, denoting additive interaction, the lines are not parallel.

当暴露于因子 A 的人的归因风险（ARexp，即暴露于 A 的人和未暴露于 A 的人之间的风险绝对差异；参见第 3 章，公式 3.4）变化（异质性）时，认为存在加性相互作用第三个变量 Z 的函数。 在这种情况下，评估交互作用的最简单方法是计算暴露于风险因子 A 的人的归因风险，这些分层由潜在影响修饰符 Z 的水平定义。表 6- 显示了该策略的假设示例。 1 和 6-2。表6-1中，归因于A的绝对超额风险不因暴露于Z而异。 表6-2中，暴露于A的归因风险大于未暴露于Z的A的归因风险，表示异质性A 的绝对影响。在这些表中，与 A 相关的归因风险有两个不同的参考类别：对于没有 Z 的层，参考类别是 Z 不存在，A 不存在；对于存在 Z 的层，参考类别为 Z 存在，A 不存在。 表 6-1 和 6-2 中显示的模式可以通过图形进行检查（图 6-2A）。使用算术标度绘制风险的图表用于评估加性相互作用。对于暴露于第三变量 Z 的个体和未暴露于第三变量 Z 的个体，风险因子 A 的每个类别的风险或比率分别绘制。在这种类型的图表中（纵坐标为算术刻度），斜率的陡度为绝对差的函数。因此，当根据 A 的结果风险的绝对差异（暴露于 A 的风险）相同时，无论暴露于 Z，两条线是平行的。当绝对差异不同时，表示加性相互作用，线不平行。

#### Detection of Multiplicative Interaction: The Relative Difference or Ratio Model

Multiplicative interaction is considered to be present when the relative difference (ratio) in the risk of an outcome Y between subjects exposed and those not exposed to a putative risk factor A differs (is heterogeneous) as a function of a third variable Z. Hypothetical examples of the evaluation of multiplicative interaction are shown in Tables 6-3 and 6-4. (Consistent with Tables 6-1 and 6-2, there are two different reference categories for the relative risks associated with A: for the stratum in which Z is absent, the reference category is Z absent, A absent; for the stratum in which Z is present, the reference category is Z present, A absent.) In Table 6-3, the relative risk for A is the same for those exposed and those not exposed to Z. In Table 6-4, the relative risk for A is larger for those exposed than for those not exposed to Z, indicating that the effects of A measured by the relative risk are heterogeneous according to Z. 

As for additive interaction, multiplicative interaction can be evaluated graphically by plotting the rates for each category of A according to the strata defined by Z (Figure 6-2B). For multiplicative interaction assessment, however, a log scale is used in the ordinate. Thus, the steepness of the slopes is a function of the relative differences: when the risk ratios for A are the same in those exposed and in those not exposed to Z, the Z-specific curves are parallel, indicating absence of multiplicative interaction. Nonparallel lines suggest the presence of multiplicative interaction.

当暴露于推定风险因子 A 的受试者与未暴露于推定风险因子 A 的受试者之间的结果 Y 风险的相对差异（比率）不同（异质性）作为第三变量 Z 的函数时，认为存在乘性相互作用。 假设示例表6-3和表6-4显示了乘法相互作用的评价。 （与表 6-1 和 6-2 一致，与 A 相关的相对风险有两个不同的参考类别：对于不存在 Z 的层，参考类别不存在 Z，不存在 A；对于Z 存在，参考类别为 Z 存在，A 不存在。）在表 6-3 中，A 的相对风险对于暴露于 Z 的人和未暴露于 Z 的人是相同的。在表 6-4 中，A 的相对风险暴露于 Z 的人大于那些未暴露于 Z 的人，表明根据 Z，以相对风险衡量的 A 的影响是异质的。至于加性相互作用，可以通过根据 Z 定义的层（图 6-2B）绘制 A 的每个类别的比率来以图形方式评估乘性相互作用。然而，对于乘法相互作用评估，在纵坐标中使用对数标度。因此，斜率的陡度是相对差异的函数：当暴露于 Z 的人和未暴露于 Z 的人中 A 的风险比相同时，Z 特定曲线是平行的，表明不存在乘法相互作用。非平行线表明存在乘法相互作用。 



# Endogeneity

[https://en.wikipedia.org/wiki/Endogeneity_(econometrics)](https://en.wikipedia.org/wiki/Endogeneity_(econometrics))

In econometrics, endogeneity broadly refers to situations in which an explanatory variable is correlated with the error term. The distinction between endogenous and exogenous variables originated in simultaneous equations models, where one separates variables whose values are determined by the model from variables which are predetermined; ignoring simultaneity in the estimation leads to biased estimates as it violates the exogeneity assumption of the Gauss–Markov theorem. The problem of endogeneity is often, unfortunately, ignored by researchers conducting non-experimental research and doing so precludes making policy recommendations. Instrumental variable techniques are commonly used to address this problem.

Besides simultaneity, correlation between explanatory variables and the error term can arise when an unobserved or omitted variable is confounding both independent and dependent variables, or when independent variables are measured with error.

在计量经济学中，内生性泛指解释变量与误差项相关的情况。 内生变量和外生变量的区别起源于联立方程模型，其中将值由模型确定的变量与预先确定的变量分开； 忽略估计中的同时性会导致估计有偏差，因为它违反了高斯-马尔可夫定理的外生性假设。 不幸的是，进行非实验性研究的研究人员常常忽视内生性问题，这样做会妨碍提出政策建议。 工具变量技术通常用于解决这个问题。

除了同时性之外，当未观察或遗漏的变量混淆自变量和因变量时，或者当自变量测量有误差时，解释变量与误差项之间的相关性也会出现。

## Endogenous variable

Two variables that can occur in regression models are:

**1. Endogenous variables:** Variables that are explained by other variables within a model.

**2. Exogenous variables:** Variables that are _not_ explained by other variables within a model.

When using regression models, researchers are often interested in understanding the relationship between one or more explanatory variables and a[response variable](https://www.statology.org/explanatory-response-variables/).

And in general:

-   It’s possible to manipulate endogenous variables to produce some effect in the response variable.
-   It’s not possible to manipulate exogenous variables.

The following examples illustrate how to identify endogenous vs. exogenous variables in different regression models.

### **Example 1: Crop Yield**

Suppose a farmer is interested in understanding the factors that affect total crop yield. He collects data and builds the following [regression model](https://www.statology.org/multiple-linear-regression/):

Crop Yield = B0 + B1(Fertilizer) + B2(Type of Soil Used) + B3(Rainfall)

Here is how to identify each variable in the model:

-   Crop Yield: This variable is **endogenous** because it can be explained by fertilizer, type of soil used, and rainfall.
-   Fertilizer: This variable is **endogenous** because its effectiveness is influenced by the type of soil used.
-   Type of Soil Used: This variable is **endogenous** because it is influenced by the type of soil used.
-   Rainfall: This variable is **exogenous** because it is not influenced by the other variables in the model. In other words, the amount of fertilizer used or the type of soil used cannot effect the amount of rainfall in any way.

### **Example 2: Consumer Spending**

Suppose an economist is interested in understanding the factors that affect consumer spending. She collects data and builds the following[regression model](https://www.statology.org/multiple-linear-regression/):

Consumer Spending = B0 + B1(Income) + B2(Investment Returns) + B3(Government Tax Rates)

Here is how to identify each variable in the model:

-   Consumer Spending: This variable is **endogenous** because it can be explained by income, investment returns, and government spending.
-   Income: This variable is **endogenous** because it is affected by government tax rates.
-   Investment Returns: This variable is **endogenous** because it is influenced government tax rates.
-   Government tax rates: This variable is **exogenous** because it is not influenced by the other variables in the model. In other words, the amount that an individual earns in income or earns in investment returns cannot effect the tax rates set by the government in any way.

# Causality

[https://www.youtube.com/watch?v=5x_pPemAVxs&ab_channel=BradyNeal-CausalInference](https://www.youtube.com/watch?v=5x_pPemAVxs&ab_channel=BradyNeal-CausalInference)

## Counterfactural missing problem

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637155798194-296c37c0-48fd-4b1e-8bed-7c7466555a99.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637155887391-7b1e9ff7-42eb-4b03-a479-8de6bce26775.png)

Fundamental Problem of Causal Inference: Missing Counterfactural data

## Average treatment effect (ATE) V.S Associational Difference

  
![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637156214466-5ba6b7ff-7e1d-4e0c-a92f-c1082eafe7cf.png)

conditional expectations, associational difference

difference between causal quantity and association quantity

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637156612882-3e902f7a-e44d-4193-8074-e8ee83bf081e.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637156670534-c1e2dbec-21a0-4d6a-8769-32ee230cb516.png)

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637156745843-389095b8-0741-4c6a-9714-934aa286b20c.png)

Assumptions would make the ATE = associational difference. Ignorability = Exchangability, treatment independent with outcome

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157051277-63a031ec-0740-48ab-9b0a-a7b04ce50942.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157090391-cfe38842-055f-4e85-8dd8-e0edf70c4e6d.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157360312-1b7dbed4-3e31-4ccc-a261-5269a05148d7.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157359480-979b158c-217f-4d39-aa0b-893619f236ea.png)  ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157451866-2a64f827-7aff-4c50-afb3-aa17066a27ed.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157501032-62809015-67cc-4dcd-a4c1-db047a217957.png)

### Positivity

feel like propensity score

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157713089-15ca2c05-7a23-432d-80cd-c68f9630f4d4.png)

positivity assumption make sure those two terms do not equal to 0

overlap is another way to look at positivity assumption

![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637158891136-4fdd8f15-d02b-48df-8f5b-92787612314c.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637157924275-3fe619e0-bb6b-4522-a375-1f54a1f4d5c7.png) ![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637158050616-2914146d-5cdb-4b18-8174-f64498fd910f.png)
![|500](https://cdn.nlark.com/yuque/0/2021/png/22065462/1637158147360-7be4c9ec-4b9d-4596-afc8-f5584b72e84d.png)  
  

## paper 

[https://serval.unil.ch/resource/serval:BIB_5E5CC6C39143.P001/REF.pdf](https://serval.unil.ch/resource/serval:BIB_5E5CC6C39143.P001/REF.pdf)

Most leadership and management researchers ignore one key design and estimation problem rendering parameter estimates uninterpretable: Endogeneity. We discuss the problem of endogeneity in depth and explain conditions that engender it using examples grounded in the leadership literature. We show how consistent causal estimates can be derived from the randomized experiment, where endogeneity is eliminated by experimental design. We then review the reasons why estimates may become biased (i.e., inconsistent) in non-experimental designs and present a number of useful remedies for examining causal relations with non- experimental data. We write in intuitive terms using nontechnical language to make this chapter accessible to a large audience.

大多数领导力和管理研究人员忽略了一个关键的设计和估计问题，使参数估计无法解释：内生性。 我们深入讨论了内生性问题，并使用以领导力文献为基础的例子解释了产生内生性的条件。 我们展示了如何从随机实验中得出一致的因果估计，其中通过实验设计消除了内生性。 然后，我们回顾了估计在非实验设计中可能出现偏差（即不一致）的原因，并提出了许多有用的补救措施来检查与非实验数据的因果关系。 我们使用非技术语言以直观的方式编写，以使大量读者可以访问本章。

Theory is the ultimate aim of science (Kerlinger & Lee, 2000). Contrary to the lay

individuals described in Aldous Huxley’s opening quote, scientists put their theories to the empirical test in order to determine whether or not the theories are plausible. As stated by Murphy (1997, p. 4), “the methods chosen should be appropriate to the research question and the inferences drawn should be consistent with what was actually attempted in [the] study”. Given the importance of theory testing for understanding and predicting how the world works, the choice of research design and analysis method is of the utmost importance, particularly because research findings influence policy and practice.

理论是科学的最终目标（Kerlinger & Lee，2000）。与外行相反，在 Aldous Huxley 的开场白中描述的个体，科学家们将他们的理论进行了实证检验，以确定这些理论是否合理。正如 Murphy (1997, p. 4) 所说，“所选择的方法应该适合研究问题，得出的推论应该与 [the] 研究中实际尝试的一致”。鉴于理论测试对于理解和预测世界如何运作的重要性，研究设计和分析方法的选择至关重要，特别是因为研究结果会影响政策和实践。

As we will explain in detail, the randomized experiment is the gold standard to identify and test causal relationships. However, be it for practical or ethical considerations, it may not always be possible to conduct randomized experiments (see Cook, Shadish, & Wong, 2008; Rubin, 2008). Although most researchers undoubtedly know that the randomized experiment is the method of choice to infer causality, many researchers ignore two key issues:

正如我们将详细解释的那样，随机实验是识别和测试因果关系的黄金标准。然而，无论是出于实践还是伦理考虑，进行随机实验可能并不总是可行（参见 Cook、Shadish 和 Wong，2008 年；Rubin，2008 年）。尽管大多数研究人员无疑都知道随机实验是推断因果关系的首选方法，但许多研究人员忽略了两个关键问题：

1.  experimental design is not the only method available to make valid causal inferences; that is, there are other designs available to make valid causal claims, which do not require manipulation of the exogenous variables on the part of the researcher.
2.  nonexperimental designs that do not address problems of endogeneity are pretty much useless for understanding phenomena; that is, finding a relationship between an endogenous regressor x—that has not been purged from endogeneity somehow—and y does not help leadership theory one bit!

1. 实验设计并不是做出有效因果推断的唯一方法； 也就是说，还有其他设计可用于提出有效的因果声明，这些设计不需要研究人员操纵外生变量。

2. 不解决内生性问题的非实验设计对于理解现象几乎没有用处； 也就是说，找到内生回归变量 x（尚未以某种方式从内生性中清除）与 y 之间的关系对领导力理论没有一点帮助！

The way in which we state the above two points, particularly the second is, admittedly

rather harsh and blunt; however, going through the chapter will make readers realize that what we have said is actually an understatement. To help research advance in leadership (and other social sciences) more researchers must join the effort to stomp-out endogeneity; this problem is far bigger than we dared to imagine.

我们陈述上述两点的方式，尤其是第二点，无可否认相当严厉和生硬；然而，阅读本章会让读者意识到我们所说的实际上是轻描淡写。为了帮助领导力（和其他社会科学）的研究取得进展，更多的研究人员必须加入到消除内生性的努力中；这个问题远远超出我们的想象。

We recently conducted a review of leadership studies suggesting that the conditions and designs that allow to uncover causal relationship with non-experimental data are not well understood by the majority of leadership researchers (Antonakis, Bendahan, Jacquart, & Lalive, 2010). This problem is not isolated to the field of leadership. In fact, aside from the field of economics, which starting addressing this problem a couple of decades ago, many social-sciences disciplines face a similar situation (Bascle, 2008; Duncan, Magnusson, & Ludwig, 2004; Foster & McLanahan, 1996; Gennetian, Magnuson, & Morris, 2008; Halaby, 2004; Larcker & Rusticus, 2010; Shaver, 1998).

我们最近对领导力研究进行了审查，表明大多数领导力研究人员并没有很好地理解允许揭示与非实验数据因果关系的条件和设计（Antonakis、Bendahan、Jacquart 和 Lalive，2010 年）。这个问题并非孤立于领导力领域。事实上，除了几十年前开始解决这个问题的经济学领域外，许多社会科学学科也面临着类似的情况（Bascle，2008；Duncan, Magnusson, & Ludwig，2004；Foster & McLanahan，1996； Gennetian、Magnuson 和 Morris，2008 年；Halaby，2004 年；Larcker 和 Rusticus，2010 年；Shaver，1998 年）。

For example, a recent review has found that less than 10% of the papers published in the top strategy journal (i.e., Strategic Management Journal) properly analyzed the non-experimental data they presented (Hamilton & Nickerson, 2003). In our review, where we examined a random sample of 110 leadership papers published in top scientific journals, we found that researchers failed to correct between 66 % to 90 % of design and estimation conditions that threaten estimate validity (refer to Table 1 for a summary of the threats). We also found that 109 of the articles had at least one threat to validity and that 100 articles had three or more validity threats (which we discuss in more detail later). This sad state of affairs has to be changed because policy implications that stem from research that is incorrectly undertaken will be wrong.

例如，最近的一项评论发现，在顶级战略期刊（即战略管理期刊）上发表的论文中，只有不到 10% 正确分析了他们提供的非实验数据（Hamilton & Nickerson，2003）。在我们的审查中，我们检查了在顶级科学期刊上发表的 110 篇领导力论文的随机样本，我们发现研究人员未能纠正威胁估计有效性的 66% 到 90% 的设计和估计条件（请参阅表 1 的摘要的威胁）。我们还发现，109 篇文章至少有一个有效性威胁，100 篇文章有 3 个或更多有效性威胁（我们稍后会详细讨论）。这种可悲的状况必须改变，因为错误开展的研究所产生的政策含义将是错误的。

When we refer to causal analysis of nonexperimental data, we are referring to designs that will produce coefficients that capture the magnitude of the true (causal) relationship rather than just an association or a correlation (which could be spurious). True estimates are called consistent. To say that an estimate is consistent suggests that it will converge to the true population parameter as sample size converges to infinity (i.e., asymptotically).

当我们提到非实验数据的因果分析时，我们指的是将产生能够捕捉真实（因果）关系大小的系数的设计，而不仅仅是关联或相关（可能是虚假的）。真正的估计称为一致。说一个估计是一致的表明它会随着样本大小收敛到无穷大（即渐近地）收敛到真实的总体参数。

The main threat to consistency is endogeneity; much of what we will discuss in this chapter focuses on explaining what it is and how to deal with it. If an estimate is inconsistent, it is purely and simply uninterpretable. A coefficient may appear to adequately reflect the hypothesized relationship—for example, it is the right direction and the effect is highly significant—but in presence of endogeneity it will be inconsistent and will not reflect the true population parameter. Reporting it is pretty much useless to help understand a phenomenon because the observed correlation may be far off from the true relation; that is, the true relation could be higher, lower, zero, or of a different sign from the observed association (correlation). This is why understanding the nature of causal designs is crucial.

一致性的主要威胁是内生性；我们将在本章中讨论的大部分内容都集中在解释它是什么以及如何处理它。如果估计值不一致，则纯粹是无法解释的。一个系数可能看起来充分反映了假设的关系——例如，它是正确的方向，效果非常显着——但在存在内生性的情况下，它会不一致，不会反映真实的人口参数。报告帮助理解现象几乎没有用，因为观察到的相关性可能与真实的关系相去甚远；也就是说，真正的关系可以是更高、更低、零或与观察到的关联（相关性）不同的符号。这就是为什么了解因果设计的本质至关重要。

Our goal in this chapter is to present some of the methods available to researchers for testing theory correctly. We begin this chapter by discussing what theories are and why causality is important to theory testing; we then present a simple example of endogeneity with simulated data and extend the problem to leadership research to show that models with endogenous regressors are simply not very useful (these data will prove to be very useful as a teaching aid for those teaching methods courses). Next, we present the randomized experiment as a failsafe way to make causal claims; an understanding of what, precisely, random assignment does is essential for understanding how endogeneity is engendered, why it renders estimates biased. We then present some methods that can be used to causally analyze nonexperimental data. We close this chapter by discussing future directions in leadership research.

我们在本章中的目标是介绍一些可供研究人员正确检验理论的方法。我们通过讨论什么是理论以及为什么因果关系对理论检验很重要来开始本章；然后，我们用模拟数据展示了一个简单的内生性示例，并将问题扩展到领导力研究，以表明具有内生回归量的模型并不是很有用（这些数据将被证明作为那些教学方法课程的教学辅助工具非常有用）。接下来，我们将随机实验作为提出因果声明的故障安全方式；准确地理解随机分配的作用对于理解内生性是如何产生的，为什么它会使估计有偏差至关重要。然后，我们提出了一些可用于对非实验数据进行因果分析的方法。我们通过讨论领导力研究的未来方向来结束本章。

### What is causality?

A theory consists in a set of interrelated constructs and data connecting these constructs with the empirical world—within certain boundaries and under certain constraints (Antonakis et al., 2004); a theory is constructed so as to answers a number of questions: What elements are being studied and how do they relate? Why would this be so? When (whereand to whom) does the theory apply? In order to be acceptable, a theory should be devoid of contradictions and be consistent with the empirical world—that is, it should have internal and external consistency; moreover, a theory should be testable, have both generality and parsimony (for in-depth treatment see Bacharach, 1989; Dubin, 1976; Kerlinger & Lee, 2000). More importantly, a theory should present a causally valid explanation of a phenomenon.

一个理论由一组相互关联的结构和数据组成，这些结构和数据将这些结构与经验世界联系起来——在某些边界内和某些约束下（Antonakis 等，2004）；构建一个理论是为了回答许多问题：正在研究哪些元素以及它们之间的关系？为什么会这样？该理论何时（何地以及对谁）适用？为了被接受，一个理论应该没有矛盾并与经验世界相一致——即它应该具有内在和外在的一致性；此外，一个理论应该是可检验的，具有普遍性和简约性（深入研究参见 Bacharach, 1989; Dubin, 1976; Kerlinger & Lee, 2000）。更重要的是，一个理论应该对现象提出一个因果上有效的解释。

What causality is and how it should be tested has important implications for understanding natural phenomena (and the theories that explain them); it also has important implications regarding how scientific research should be conducted. Causality is a fascinating topic that has been examined in-depth by many philosophers and scientists (cf. Mulaik, 2009; Pearl, 2009). In this chapter, we steer clear from philosophical considerations and adopt a pragmatic and broadly accepted view on causality. Here, we focus on understanding how one can assess and quantify a causal effect. Classically, x is said to have an effect on y if the following three conditions are met (Holland, 1986; Kenny, 1979):

因果关系是什么以及如何检验它对于理解自然现象（以及解释它们的理论）具有重要意义；它还对如何开展科学研究具有重要意义。因果关系是一个引人入胜的话题，许多哲学家和科学家对其进行了深入研究（参见穆莱克，2009 年；珀尔，2009 年）。在本章中，我们避开哲学考虑，对因果关系采取务实和广泛接受的观点。在这里，我们专注于了解如何评估和量化因果效应。传统上，如果满足以下三个条件，则 x 对 y 有影响（Holland，1986；Kenny，1979）：

(a) y follows x temporally  
(b) y changes as x changes (and this relationship is statistically significant)  
(c) no other causes should eliminate the relation between x and y.  
The first two conditions are quite straight forward; regarding first condition, caution is warranted in the case where x and y simultaneously affect each other; also, that y follows x by no mean suggests that x caused y. This latter point will become clear in the first simulation we present. 

(a) y 在时间上跟随 x

(b) y 随着 x 的变化而变化（这种关系在统计上是显着的）

(c) 没有其他原因可以消除 x 和 y 之间的关系。

前两个条件非常简单；关于第一个条件，在x和y同时相互影响的情况下，必须谨慎；此外，y 跟在 x 之后绝不意味着 x 导致了 y。后一点将在我们呈现的第一个模拟中变得清晰。

Also, we should note that from the second condition it follows that the constructs being studied should be operationalized (measured) and statistically analyzed. Although necessary, it is clear that these two first conditions are not sufficient to establish causality. They are however sufficient for one to fall prey to the _post hoc, ergo propter hoc fallacy_, which consists in wrongly interpreting causality by inferring that x is the cause of y precisely because it occurred before y(Kerlinger & Lee, 2000). The third condition has more to do with design and analysis issues than it has with theoretical arguments, though theory is important too (see also James, Mulaik, & Brett, 1982; Mulaik & James, 1995). It is also the more troublesome condition and the one with which much of our chapter will be concerned.

此外，我们应该注意到，根据第二个条件，所研究的构念应该被操作化（测量）和统计分析。虽然必要，但很明显，这两个首要条件不足以建立因果关系。然而，它们足以让人们陷入事后的、ergo propter hoc 谬误，即错误地解释因果关系，推断 x 正是 y 的原因，因为它发生在 y 之前（Kerlinger & Lee，2000）。第三个条件更多地与设计和分析问题有关，而不是与理论论证有关，尽管理论也很重要（另见 James、Mulaik 和 Brett，1982 年；Mulaik 和 James，1995 年）。这也是更麻烦的情况，也是我们本章的大部分内容将涉及的情况。

This third condition can be restated by simply saying that changes in x produce changes in y holding all other things equal. This is clearly the case if x varies randomly and independently from the system of variables under study; if x depended on some unmodeled causes that also drive other variables in the model then x would be said to be endogenous—hence the problem of endogeneity. As we alluded to in the introduction, the consequences of endogeneity are dire. If the necessary precautions are not taken to purge the endogenous variable of endogeneity then estimated coefficients are devoid of any meaning and cannot be interpreted.  
这第三个条件可以通过简单地说 x 的变化引起 y 的变化来重申，保持所有其他条件不变。 如果 x 随机变化且独立于所研究的变量系统，则情况显然如此； 如果 x 依赖于一些未建模的原因，这些原因也驱动模型中的其他变量，那么 x 将被认为是内生的——因此存在内生性问题。 正如我们在引言中提到的，内生性的后果是可怕的。 如果没有采取必要的预防措施来清除内生性的内生变量，那么估计的系数就没有任何意义并且无法解释。