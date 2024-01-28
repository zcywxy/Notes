1. For correlation coefficients, I used a self-defined function to do the correlation. So except for the Cramer’s V comes from { rcompanion } package, all the other functions come from {stats} package. Detailed function copies below:

#1)nominal vs nominal with a bias corrected Cramer's V, from {rcompanion}

#2)numeric vs numeric with Spearman, from {stats}

#3)nominal vs numeric with ANOVA,  {stats}

#4)ordinal vs ordinal/nominal/binary with Kendall rank  {stats}

#5)ordinal vs numeric with Spearman  {stats}

#6)binary vs binary with Phi (pearson)  {stats}

#7)binary vs numeric with point biserial (pearson)  {stats}


2. For p-value, I used the chisq.test for Cramer’s V. chisq.test {stats}. All the other p-value were obtained through the corresponding correlation functions.
## Covariance

A covariance is a [statistical](https://www.analyticsvidhya.com/blog/2021/08/advance-statistics-concepts-for-data-science-enthusiasts/) tool that helps to quantify the total variance of random variables from their expected value(Mean). In simple words, it is a measure of the linear relationship between two random variables. It can take any positive and negative values.

-   **Positive Covariance:** It indicates that two variables tend to move in the same direction, which means that if we increase the value of one variable other variable value will also increase.
-   **Zero Covariance:** It indicates that there is no linear relationship between them.
-   **Negative Covariance:** It indicates that two variables tend to move in the opposite direction, which means that if we increase the value of one variable other variable value will decrease and vice versa.

Covariance between two variables X and Y can be calculated using the following formula:
![[Pasted image 20230203105604.png|200]]

### Limitations of Covariance

1.  Covariance magnitude does not signify the strength of their relationship, so what only matters is the sign, whether it is positive or negative which tells the relationship. 协方差大小并不表示它们关系的强度，所以唯一重要的是符号，无论是正数还是负数，都可以说明关系。
2.  If we convert or scale the measurements of the variable X and Y, then Cov(X’, Y’) ≠ Cov(X, Y) should not happen.
3.  Covariance does not capture the non-linear relationship between two variables.

In order to quantify the strength of their relationship or how strongly they affect each other, we use _Correlation_.

## Correlation Metrics

Correlation also measures the relationship between two variables as well as its magnitude defines the strength between variables. It ranges from -1 to 1 and is usually denoted by _r._

-   **Perfectly Positive Correlation**: When correlation value is exactly 1.
-   **Positive Correlation:** When correlation value falls between 0 to 1.
-   **No Correlation:** When correlation value is 0.
-   **Negative Correlation:** When correlation value falls between -1 to 0.
-   **Perfectly Negative Correlation:** When correlation value is exactly -1.

The following figure illustrates the linear relationship graphically
![[Pasted image 20230203105732.png|500]]

## Types of Correlation Metrics

### 1. Pearson Correlation

Pearson correlation is also known as the Pearson product-moment correlation coefficient and is a normalized measurement of the covariance. It also measures the linear relationship between two variables and fails to capture the non-linear relationship of two variables. Pearson correlation assumes that both variables are normally distributed. It can be used for nominal variables or continuous variables.

There are few pre requisties for the Pearson Correlation to hold valid,

-   Both, _X_ & _Y_ should assume Normal Distribution and must be continuous.
-   There should be no _NaN_ in the data in either of the columns.
-   There should be strong Homoscedascity.
-   There should be no significant outliers present in the data.

t-test

![[Pasted image 20230203105938.png|400]]

Pearson correlation coefficient between two variables X and Y can be calculated by the following formula:

![[Pasted image 20230203110025.png|500]]

#### Limitation of Pearson Correlation

-   It fails to capture the non-linear relationship between two variables.
-   Usually, we do not use the Pearson correlation coefficient for ordinal variables(where sequence matters).

### 2. Spearman’s Rank Correlation

It is a nonparametric(no prior assumptions about distribution) measure for calculating correlation coefficient that is used for ordinal variables or continuous variables. Spearman’s rank correlation can capture both linear or non-linear relationships. Instead of using _X_ & _Y_ raw data in the formulae, Spearman Correlation uses the rank of the data instead.

Since it deals with the rank of the data, this is highly preferred way of measuring association for Ordinal data.

Spearman Correlation will be able to capture non-monotonic relationships in the data as well. Also Spearman Correlation, is not that sensitive to outliers

![[Pasted image 20230203110149.png|300]]

Spearman’s rank correlation coefficient between two variables X and Y can be calculated using the following formula:

![[Pasted image 20230203110308.png|300]]

### 3. Kendall Rank Correlation

Kendell rank correlation, sometimes called Kendall tau coefficient, is a nonparametric measure for calculating the rank correlation of ordinals variables. It can also capture both linear or non-linear relationships between two variables. There are three different flavours of Kendall tau namely **tau-a, tau-b, tau-c**.

Generalized Kendall rank correlation coefficient between two variables X and Y can be calculated using the following formula:

![[Pasted image 20230203110348.png|500]]

**Concordant Pair:** A pair is concordant if the observed rank is higher on one variable and is also higher on another variable.

**Discordant Pair:** A pair is discordant if the observed rank is higher on one variable and is lower on the other variable.

![[Pasted image 20230203110501.png|500]]
### 4. Point Biserial Correlation

Point Biserial Correlation is used when one variable is dichotomous(binary) and another variable is continuous. It can also capture both linear or non-linear relationships between two variables. It is denoted by rpb.

**Dichotomous Variable:** If a variable can have only binary values like head or tail, male or female then such variable is called a dichotomous variable.

Point Biserial correlation coefficient between two variables X and Y can be calculated using the following formula:

![[Pasted image 20230203110530.png|500]]

### 5. ANOVA

the closest analogue to a “correlation” between a nominal explanatory variable and continuous response would be η, the square-root of η2, which is the equivalent of the multiple correlation coefficient **R** for regression

This is type of association measure is highly advisable when the features are non-dichotomous i.e more than two categories present in the feature. 

### 6. Phi **coefficient**

In [statistics](https://en.wikipedia.org/wiki/Statistics), the **phi coefficient** (or **mean square contingency coefficient** and denoted by **φ** or **r****φ**) is a measure of association for two binary variables. it is known as the Matthews correlation coefficient (MCC) and used as a measure of the quality of binary (two-class) classifications, introduced by biochemist Brian W. Matthews in 1975. Introduced by Karl Pearson, and also known as the Yule phi coefficient from its introduction by Udny Yule in 1912 this measure is similar to the Pearson correlation coefficient in its interpretation. In fact, a Pearson correlation coefficient estimated for two binary variables will return the phi coefficient. Two binary variables are considered positively associated if most of the data falls along the diagonal cells. In contrast, two binary variables are considered negatively associated if most of the data falls off the diagonal. If we have a 2×2 table for two random variables x and y. simply a Pearson correlation computed on dichotomous variables.

### 7. Cramér's V

Cramér’s V is an effect size measurement for the chi-square test of independence. It measures how strongly two categorical fields are associated.

The effect size is calculated in the following manner:

1.  Determine which field has the fewest number of categories.
2.  Subtract 1 from the number of categories in this field.
3.  Multiply the result by the total number of records.
4.  Divide the chi-square value by the previous result. The chi-square value is obtained from the chi-square test of independence
5.  Take the square root.

![[Pasted image 20230203110622.png]]For two ordinal variables, a Spearman correlation or Kendall’s tau are preferable over Cramér’s V

### Other related concepts

#### Categorical variables: 

also known as discrete or qualitative variables. Categorical variables can be further categorised as either nominal, dichotomous or ordinal.

-   **Nominal** variables are variables that have two or more categories, but which do not have an intrinsic order. For example, type of property (house, unit and apartment), company names, religion, colour preference and postal code.
-   **Dichotomous** variables are nominal variables but only have two categories or levels. For example, gender(male and female), yes/no questions, and telecom churn data (churn or stay).
-   **Ordinal** variables are variables that have two or more categories just like nominal variables, but they can also be ordered or ranked. For example, car size(subcompact, compact, midsize, luxury), economic status (lower, middle, or upper class), rank 5 types of beer, and degree of satisfaction (very dissatisfied, somewhat dissatisfied, somewhat dissatisfied, and dissatisfied).

#### Continuous variables: 

also known as quantitative variables. This type of data possesses the properties of order and equal intervals between adjacent units. Continuous variables can be further categorised as either interval or ratiovariables.

-   **Interval variables:** data that can be measured along a continuum and have numerical values. For example, temperature, birth years, degree of satisfaction (point scale units, 1–10) and shoe size.
-   **Ratio variables**: they are interval variables, but with a clear definition of 0, indicating there is none of that variable. For example, income, price, distance, number of children in a family, hours of driving, dose amount, and many more.

The name “ratio” reflects the fact that multiplication and division operations can be performed on the values of a ratio variable. Thus, we can say that a 15 dollar price is three times more expensive than a 5 dollar price. However, a temperature of 10°C should not be considered twice as hot as 5°C. It is only 5°C higher (i.e. only addition and subtraction operations can be applied to values of an interval variable).

Here is a diagram (Figure 1) adopted from [GraphPad](https://www.graphpad.com/) that may help you to understand these different variables

![](https://cdn.nlark.com/yuque/0/2022/png/22065462/1653180568428-5eda819a-c359-4591-b2fd-9a836a3968be.png)

![](https://cdn.nlark.com/yuque/0/2022/png/22065462/1653180665368-958ffff9-8ce9-458b-9929-dc7b5d5961cb.png)

  

  

  

![](https://cdn.nlark.com/yuque/0/2022/png/22065462/1653178601639-77adb8a2-513b-4dd0-a1ca-b4db7e634e92.png)

  

## References:

[https://www.analyticsvidhya.com/blog/2021/09/different-type-of-correlation-metrics-used-by-data-scientist/](https://www.analyticsvidhya.com/blog/2021/09/different-type-of-correlation-metrics-used-by-data-scientist/)