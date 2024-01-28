# Linear Regression
## Assumptions
1. **Linearity** – the relationships between the predictors and the outcome variable should be linear
2. **Normality** – the errors should be normally distributed – technically normality is necessary only for the t-tests to be valid, estimation of the coefficients only requires that the errors be identically and independently distributed
3. **Homogeneity** of variance (homoscedasticity) – the error variance should be constant
	- The assumption of homogeneity of variance means that the level of variance for a particular variable is constant across the sample. If you’ve collected groups of data then this means that the variance of your outcome variable(s) should be the same in each of these groups (i.e. across schools, years, testing groups or predicted values).
	- The assumption of homogeneity of variance is important when conducting between-subjects statistics. The assumption is that the variances (and thus distributions) of independent groups on a continuous variable are similar, "equal," or "equivalent." Levene's Test of Equality of Variances is used to assess this statistical assumption.
	- The assumption of homogeneity is important for ANOVA testing and in regression models. In ANOVA, when homogeneity of variance is violated there is a greater probability of falsely rejecting the null hypothesis. In regression models, the assumption comes in to play with regards to residuals (aka errors). In both cases it useful to test for homogeneity and that’s what this tutorial covers.
4. **Independence** – the errors associated with one observation are not correlated with the errors of any other observation
## Diagnosis
1. Tests for *homoscedasticity* ['hɔməusi,dæs'tisəti]
	- **Violation**: Variance of ε is not constant across observations. Does NOT become less of a problem in larger samples
		- Consequences: 
			1. inefficiency (no longer have minimum standard errors) & biased standard errors, which leads to bias in test statistics and p-values
			2. Coefficient estimates are not biased
	- **Solution**
		1. robust standard errors (doesn’t solve inefficiency but will give you reasonably accurate p-values) or 
		2. weighted least squares=>requires more assumptions 
		3. transform dependent variable=> harder to interpret
	- **Plot**: One of the main assumptions for the ordinary least squares regression is the homogeneity of variance of the residuals. If the model is well-fitted, there should be no pattern to the *residuals* plotted *against* the *fitted values*. If the variance of the residuals is non-constant, then the residual variance is said to be "heteroscedastic." There are graphical and non-graphical methods for detecting heteroscedasticity. A commonly used graphical method is to plot the residuals versus fitted (predicted) values. Below we use a plot statement in the proc reg. The r. and p. tell SAS to calculate the residuals (r.) and predicted values (p.) for use in the plot. We see that the pattern of the data points is getting a little narrower towards the right end, which is an indication of mild heteroscedasticity.
		- ![[Pasted image 20230713011441.png|500]]
2. Test for *linearity*
	- **Violations**: model fails to account for a systematic pattern between Y and X’s. eg, Ceiling effects: Average LDL stops increasing or increases more slowly among women with BMI in the upper reaches of its range
	- **Solution**
		- Add quadratic term
		- Categorize the predictor
		- Take the log 
		- splines曲线
		- Log and square root transformations are useful in situations where regression line increases more slowly with increasing values of the predictor (floor or ceiling effects)
	- **Plot**: scatter plot, partial plot
		```
		proc reg data = qol;
		 model qol = hrqol lifesat / influence vif partial;
		 run; quit;
		```
		- ![[Pasted image 20230713011838.png|500]]
		- Check for departures from linearity using LOWESS (locally weighted scatterplot smoothing). Approximates the regression line under weaker assumption that it is smooth but not necessarily linear. If linear fit were satisfactory, LOWESS curve would be close to the model regression line (nonparametric estimate found under the weaker assumption of smoothness agrees with the estimate found when linearity is assumed). LOWESS only works with one continuous predictor (not multi-predictor models)
3. Test for residual *normality*
	- **Violation**: If ε has a normal distribution, then OLS estimates of the regression coefficients can be shown to have a normal distribution (required for hypothesis tests and CI)
		- 轻微违规 不咋重要， error 分布和 DV 分布相似
		- Consequences of non-normality:
			- Problems for *efficiency* (OLS se no longer the smallest). SE are biased—CI and significance tests may lead to wrong conclusions
			- Non-normality *won’t* affect *parameter estimates*. Just affects SE, t-stats, and CI
		- Especially with larger samples, this requirement is not strictly necessary—regression parameters are “robust” to this assumption, meaning only very large departures substantively affect results
	- **Solution**
		- Transform the dependent variable: can often correct skewness in error distribution
		- Take log
		- Power transformations
		- Find a model with a better fitting distribution. E.g., Poisson, Negative binomial
4. Test for *independence* (Cluster & Longitudinal)
	- **Violation**
		- The statement of this assumption is that the errors associated with one observation are not correlated with the errors of any other observation cover several different situations. Consider the case of collecting data from students in eight *different* elementary *schools*. It is likely that the students within each school will tend to be more like one another that students from different schools, that is, their errors are not independent. 
		- Another way in which the assumption of independence can be broken is when data are collected on the *same variables over time.* Let’s say that we collect truancy data every semester for 12 years. In this situation it is likely that the errors for observation between adjacent semesters will be more highly correlated than for observations more separated in time. This is known as autocorrelation. When you have data that can be considered to be time-series, you should use the dw option that performs a Durbin-Watson test for correlated residuals.
	- **Test**
		```
		proc reg data='c:sasregelemapi2';
		 model api00 = enroll / dw;
		 output out=res3 (keep = snum r) residual=r;
		run;
		quit;
		```
		- ![[Pasted image 20230713033146.png|500]]

## Other 2 issues concerned
1. Influence – individual observations that exert undue influence on the coefficients
2. Collinearity – predictors that are highly collinear, i.e. linearly related, can cause problems in estimating the regression coefficients.
### 2. Collinearity
- **Violation**: Correlation between two variables is too high. “approximate linear relationship among the explanatory variables leads to unreliable regression estimates” (Verbeek)
	- May lead to *unreliable estimates* with *high standard errors* and of unexpected sign or magnitude 
		- If age and experience are highly correlated it is hard for the model to identify the INDIVIDUAL impact of these two variables (which is exactly what regression does)
		- Insufficient information in the sample to identify the effects we would like to identify
	- *Only affects* coefficient estimates for those *variables* that are *collinear* 
	- Sometimes we have to do this—what are the implications? (*don’t* attempt to *interpret* the *lower order coefficients* that are included in higher order coefficients)
- variance inflation factor **VIF**: 1/(1−$r_j^2$) 𝑖𝑠 𝑡ℎ𝑒 𝑣𝑎𝑟𝑖𝑎𝑛𝑐𝑒 𝑖𝑛𝑓𝑙𝑎𝑡𝑖𝑜𝑛 𝑓𝑎𝑐𝑡𝑜𝑟 (𝑉𝐼𝐹)
		- How much correlation with other predictors increases the standard error of 𝑥𝑗
		- $r_j^2$ is the R2 value obtained by regressing the jth predictor on the remaining predictors
			- eg. VIF=5.27, then se for the coefficient is √(5.27) = 2.3 times as large as it would be if covariate was uncorrelated with other xs .
		- Criterion for VIF: 2.5? 5? 10? (no “right” answer but *4 is a common cutoff*)
	-  ![[Pasted image 20230713034004.png|500]]
			- 𝑠𝑦|𝑥2 is the residual variance of the outcome (unexplained variance in the outcome)
			- 𝑟j=√(𝑅2 ) from a multiple regression model in which 𝑥𝑗 is regressed on all other predictors (ie. x1=x2+x3)
			- So we see that regression coefficients are less stable with higher multiple correlations between predictors. More on this later.
				- Variance of 𝛽𝑗 depends on
					1. correlation of xj with other predictors, 
					2. how much additional variation these additional predictors explain
- **Diagnose**
	1. Regress indep var on all other x’s，If R-squared>.60, reason to worry
	2. Run variance inflation factor (VIF)
- **Causes**:
	- Two variables representing same construct (Don’t do this)
	- Use of higher-order coefficients (interactions, quadratic terms)
- **Solutions**:
	1. Delete one or more variables from the model
	2. Combine collinear variables into an index
	3. Estimate a latent variable model (single, unobserved variable representing construct two collinear variables meant to measure)
	4. Joint hypothesis test (instead of looking at individual ts and p-values)
	5. Increase sample size (will reduce inflated se)
	6. Stratified sampling on independent variables

### 1. Influence (DFBETA, Cook'sD)

- “High-leverage” points, potential to exert undue过度的 influence on regression coefficient estimates. Coefficient estimates might change by a large amount if the influential points are omitted from the data set
- Use DFBETA to quantify how much coefficients would change
- If undue influence is identified, run sensitivity analyses with and without points. Check whether conclusions are affected. If so, need to report this

Outliers: In linear regression, an outlier is an observation with large residual. In other words, it is an observation whose dependent-variable value is unusual given its values on the predictor variables. An outlier may indicate a sample peculiarity or may indicate a data entry error or other problem.
异常值：在线性回归中，异常值是具有大残差的观测值。换句话说，它是一个观察，其因变量值在预测变量上的值是不寻常的。异常值可能表示样本特性或可能表示数据输入错误或其他问题。

Leverage: An observation with an extreme value on a predictor variable is called a point with high leverage. Leverage is a measure of how far an observation deviates from the mean of that variable. These leverage points can have an effect on the estimate of regression coefficients.
杠杆：在预测变量上具有极值的观察称为具有高杠杆的点。杠杆是衡量观察值偏离该变量均值的程度。这些杠杆点会对回归系数的估计产生影响。

Influence: An observation is said to be influential if removing the observation substantially changes the estimate of coefficients. Influence can be thought of as the product of leverage and outlierness.
影响：如果移除观察显着改变了系数的估计，则称该观察具有影响。影响可以被认为是杠杆和异常值的产物。

How can we identify these three types of observations? Let’s look at an example dataset called crime. 

Let’s say that we want to predict crime by pctmetro, poverty, and single. That is to say, we want to build a linear regression model between the response variable crime and the independent variables pctmetro, poverty and single. We will first look at the scatter plots of crime against each of the predictor variables before the regression analysis so we will have some ideas about potential problems. We can create a scatterplot matrix of these variables as shown below.

proc insight data="c:sasregcrime";
  scatter crime pctmetro poverty single*
          crime pctmetro poverty single;
run;
quit;

![[Pasted image 20230713040529.png|500]]

  

The graphs of crime with other variables show some potential problems. In every plot, we see a data point that is far away from the rest of the data points. Let’s make individual graphs of crime with pctmetro and poverty and single so we can get a better view of these scatterplots. We will add the pointlabel = ("#state") option in the symbol statement to plot the state name instead of a point.

goptions reset=all;
axis1 label=(r=0 a=90);
symbol1 pointlabel = ("#state") font=simplex value=none;

proc gplot data="c:sasregcrime";
  plot crime* pctmetro=1 / vaxis=axis1;
run;
quit;

![[Pasted image 20230713040627.png|500]]

Now let’s try the regression command predicting crime from pctmetro, poverty and single. We will go step-by-step to identify all the potentially unusual or influential points afterwards. 

We will output several statistics that we will need for the next few analyses to a dataset called crime1res, and we will explain each statistic in turn.  These statistics include the studentized residual (called r), leverage (called lev), Cook’s D (called cd) and DFFITS (called dffit). We are requesting all of these statistics now so that they can be placed in a single dataset that we will use for the next several examples. Otherwise, we could have to rerun the proc reg each time we wanted a new statistic and save that statistic to another output data file.

proc reg data="c:sasregcrime";
  model crime=pctmetro poverty single;
  output out=crime1res(keep=sid state crime pctmetro poverty single 
                       r lev cd dffit)
                       rstudent=r h=lev cookd=cd dffits=dffit;
run;
quit;

The following table summarizes the general rules of thumb we use for these measures to identify observations worthy of further investigation (where k is the number of predictors and n is the number of observations).

|   |   |
|---|---|
|Measure|Value|
|leverage|>(2k+2)/n|
|abs(rstu)|> 2|
|Cook’s D|> 4/n|
|abs(DFITS)|> 2* sqrt(k/n)|
|abs(DFBETA)|> 2/sqrt(n)|

  

The lowest value that Cook’s D can assume is zero, and the higher the Cook’s D is, the more influential the point is. The conventional cut-off point is 4/n. We can list any observation above the cut-off point by doing the following. We do see that the Cook’s D for DC is by far the largest. 

proc print data=crime1res;

  where cd > (4/51);

  var crime pctmetro poverty single state cd;

run;

Now let’s take a look at DFITS. The conventional cut-off point for DFITS is 2* sqrt(k/n). DFITS can be either positive or negative, with numbers close to zero corresponding to the points with small or zero influence. As we see, DFITS also indicates that DC is, by far, the most influential observation.

proc print data=crime1res;

  where abs(dffit)> (2* sqrt(3/51));

  var crime pctmetro poverty single state dffit;

run;

The above measures are general measures of influence. You can also consider more specific measures of influence that assess how each coefficient is changed by deleting the observation. This measure is called DFBETA and is created for each of the predictors. Apparently this is more computationally intensive than summary statistics such as Cook’s D because the more predictors a model has, the more computation it may involve. We can restrict our attention to only those predictors that we are most concerned with and to see how well behaved those predictors are. In SAS, we need to use the ods output OutStatistics statement to produce the DFBETAs for each of the predictors. The names for the new variables created are chosen by SAS automatically and begin with DFB_. 

proc reg data="c:sasregcrime";

  model crime=pctmetro poverty single / influence;

  ods output OutputStatistics=crimedfbetas;

  id state;

run;

quit;

This created three variables, DFB_pctmetro, DFB_poverty and DFB_single. Let’s look at the first 5 values. 

proc print data=crimedfbetas (obs=5);

  var state DFB_pctmetro DFB_poverty DFB_single;

run;

  

- Detecting Unusual and Influential Data
    

scatterplots of the dependent variables versus the independent variable

looking at the largest values of the studentized residuals, leverage, Cook’s D, DFFITS and DFBETAs

- Tests for Normality of Residuals Tests for Heteroscedasity
    

kernel density plot

quantile-quantile plots

standardized normal probability plots

Shapiro-Wilk W test

scatterplot of residuals versus predicted (fitted) values

White test

- Tests for Multicollinearity
    

looking at VIF

looking at tolerance

- Tests for Non-Linearity
    

scatterplot of independent variable versus dependent variable

- Tests for Model Specification
    

time series

Durbin-Watson test

  

## Equations
![[Pasted image 20230714230603.png|500]] ![[Pasted image 20230714230816.png|500]] ![[Pasted image 20230714232729.png|500]] 
## Interpretation

- Overall model significance
    
- Model fit (R square, or when more than 3 or 4 predictors, modified R square)
    
- Magnitude and direction of significant predictors in the model, along with their significance level
    
- In multiple regression, we usually describe an effect and then note that this effect was observed “after controlling for <covariates” or similar language.
    

## SAS Lab

### 1. Create new categorical var

![](https://lh3.googleusercontent.com/6X5IplLNTF7UOur_WKd-Q6jfoV_8dBb7V13HoQVJg9-1b7qZKYnBBDLl7NGfIBiY-R2yT3q8o6uCS8716QHp4uY1jEVesmRR78fmKsTWsnPXl8KGJJ96O8VEOPrMMCP3e0T7U6jwpAbmGZ4PHOcdSg)

  

### 2. Simple Linear Regression

![](https://lh5.googleusercontent.com/CMXR5ySUSJUcF2mOJQVOAhJnYFvHDR793pYWCvCPuXsy7uxjG319A7TZMMsbVa7zdAyYQQHsKCS9XUkQnqgDgibAk5NcvibsY5hn1hB5rCKgTFerNMppKV04LunGOhAnflM1VBsj3Kr4IMBy2Kh2OA)

  

### 3.Multivariate Linear Regression and  R-square

![](https://lh6.googleusercontent.com/tvU_fYEp1xBxdqFpMSkOQh84HBR0z9G8EaI0KcdbArt1cAvNtAJev3HdWQNcrgWTOuNTwCIwWdsjVcrcJwNcNTFRY7ov9mzbIyCOrIcyvO172SEEOEZqUJM-byVu0zhraorkuH8gPYZ5-JyUhYj04g)

  

![](https://lh6.googleusercontent.com/TXdbQCrm8RvQgSJipTZPqJFYufbt7hoCN1RFnT_p3jZaZqXHGx2RVNeiWe6Oar7Awc1Jp6ixOE6U13QFtsyElqPcbgzKBktTQjilPZp_bt3ia1beseM0dexy4IGhzr8U1zeKt5XmV_rVWHmUajGTAQ)![](https://lh4.googleusercontent.com/OgGVPB4hEX2t7WN0JbXUJqHr3yb0gDhLt5rknbusUnZV4jHdmYs6S_mW90I90Hau4qJ6ugKeNc3gfFsFPS081Z2LYad7jORfXn_8in-n3_GylqcjgAUtmAkiFCRuUqizefcIuN9XDDJcJSqeyDbwvg)

  

### 4. Three-Way Interaction and Simple Effect

![](https://lh6.googleusercontent.com/oFipDuUiH1_mgJwE4Avh8UC9633Gq-xwMgwwQwdFb2Ya10lCstllZEd-ApbO2G-oXzPG-EO5ui29jYT8fkchgT9lQOuddbN44Saxy8NVYaf5EnjojYiipJlRxjmqGH05JoCVdaui9tNhiZRK3-UxXg)

![](https://lh5.googleusercontent.com/DhCIMw77UrzyArRsSKVxYYYNBkVK5lWMbiUMQFSnf58Topt1_bqaqwW-z0TWBEQWozYz5HIejFzfIECpFaHyVRZj3RtPpzefCPH8sC9XDpWtotlXcq2TQD9Q7p4dnhQnukU3yvT_ZcaCD43yt1ukAg)

![](https://lh3.googleusercontent.com/SVCaLqU2HXJDDTxfyHrKTGSTQLIQUmjz9GY60a5XARbBLbhCxEqcFQubcBle-NsbHC0RUWASZxsyRsG1ssddZuB5rdw1DddJ9xhijT13Uyc10b2337z3GZEVnK7qKH4VgQ_DAtqlV74u7N-feU686A)

Order=1 result

![](https://lh6.googleusercontent.com/7rEhEc705E8G2U-Y4iDuURja6NadO9rqqyv_lqtYZRmLRgtGbPgwS-DknWjfKaPh2W6VL0nS15iFA4ir2irQZlLoH7y4g_QlZHkOWSEwEl3MBWRHiiI9WK5FvuXXiOcfbCCnIZFFcmyeyFYu-NtGLg)

Order=2 result

![](https://lh5.googleusercontent.com/wanxioUgc9y8LKSCEMgz71P2Z1rBb6EZ_GhEj6iA6BFSLPC1I0Hq2Gt8Efceq4DfqlePx3HM_uxSYCxzN-n3T-Io6VU6iguMfYZfdYIvrcBpJ1bSsWN0460UfgUGDeMVjJIw52BPzxZqz_WHZ6wAmw)

![](https://lh3.googleusercontent.com/wvb-OCIkM9606pTNTFh5iNUM4tYOLPmPcNi1YuXBDkKjZoQxuXiKc8loCktKik34_WbnwZCsoZxjdj_ZPiALQbMQk2llWgxVw1x94HzUZn1WgJetjgD7LVC3Q3BGc8783-z3EIeGbQkKvKexKrKZUQ)

### 5. Diagnostic

![](https://lh4.googleusercontent.com/Nhizo8gmZiBDAa7iYYP9waSkuWl-XVubIe31MP8sLwdhNi2hTVZ5TmUM4VGBZgMKJomVFc3uiHc3dP_gODe3F-Lf-E9pUwtWBFVtfTzhpm_8_BSBTbb6oqBXW6Sm0o5zrv52nNZOBxycPgRQEn4OvA)

![](https://lh5.googleusercontent.com/TUFE3xQiFQYoKw7KJSHcB4J0hJQ-cvUCppA7QMLiHQ-XtbPhOVz30ZVZI3bQ4UN30jAH5SpxwuXnYVgz7gwdlfV9_magt7j-W1w-Bo-WE89VDaRBzNatcMQ6yGpkemsFdDlK4RRE5vOtyCb7EheHCw)

influence option gives a long useless table, look at default Cook's D for outliers. In Cook's original study he says that a cut-off rate of 1 should be comparable to identify influencers. However, various other studies use 4/n or 4/(n−k−1) as a cut-off, where n is the sample number.

  

VIF cutoff = 10, for more info [https://support.sas.com/resources/papers/proceedings17/1404-2017.pdf](https://support.sas.com/resources/papers/proceedings17/1404-2017.pdf)

  

![](https://lh3.googleusercontent.com/Il1Ccnf5FTg-x1hhu1HHM2KjFPSvJrJhBp5mzWGWt6s2bKBUCQxJovOQPgeqycyku-dsQZQ6aohjyoQ-UVOgYAYMZhzQ-7QDxHU3nxKj3Vt8ROiGszRqFHgdLqrd-qNM4juVURjCxj_Kk1LgBvBD5g)

SAS default results only have residual against each predictor, partial option gives results of dependent residual (after controlling other covariates) against each predictor.

![](https://lh5.googleusercontent.com/JCch7UIQXKdDVNPBCbDXady_-G-XPRwsrQknYbhD68Ibhhdb1ffmCf_Fip77M2aAwcGBncsRTDFxlqsD5lnd8vwzPaCouEH_nD641lWJvElsUDdeS6PWTsvdUJ71aQ0gjcyGn32Z4sl4TtMQ_N2NSQ)![](https://lh4.googleusercontent.com/5HIE8Vc9qsLSmiq4K0-nUyq4GwSgNd2xZFxdsE53uDwMrXVSaNlEkq_SyS-qpEiPST0g7j5PqCLulrmGzJ8CQZFWyuEZ9GQnXOM0Unz52EcZB4VjuEAJG0ogDCFF8Yet-InR5w9_l1a0o9HoWe3hkA)

  
  
  

# Logistic Regression

## Categorical Outcomes

- Binary events 
    
- Model health care utilization
    
- Binary models for decision-making 
    

  

Binomial Distribution

- Predict number of events when a random event has two outcomes (A and B)
    
- If X is a random variable with a binomial distribution, the probability density function: ![](https://lh5.googleusercontent.com/TLAlawM9GnMLvK1EMf222HmWvLbeJ2DcqKyd9qR2oilibN0UAfjxktv-rfZXFKnWS3xfs-A1PnXlpnd-CPlPi2tvn8DX0-hZyKt9cmXUnr4y-1N4jYuf98j0cKPZpCoSGQd7OAzGe_Pcd23-Dh7YYg)
    

## Parameters of Interest

- Marginal effect (ME)
    

- ME=P1-P0
    
- MEs are directly behaviorally interpretable and in the metric of interest (prob of B occurring)
    

- Risk Ratio (RR or relative risk)
    

- RR=P1/P0
    
- RRs carry a clear behavioral interpretation but are not in the metric of the probability of interest
    
- Risk ratio is the ratio of the probability of an outcome in an exposed group to the probability of an outcome in an unexposed group.
    
- Ranges from 0 to infinity
    

- Odds
    

- Odds=P/(1-P)
    
- Oddsexposed=0.1084/(1-0.1084)=0.1216
    
- Oddsunexposed=0.0692/(1-0.0692)=0.074
    
- ![](https://lh4.googleusercontent.com/bHusJ297ixwjIC5HVuuPEkD_dotw2sZFP5aJb5A98h0SC_KS_PSPv623NkBiiqPD8bHOc-oVnCBHVaHOlcb_cuojGxAM9MIzwTrQevAx8mHbojNH28oYXn1hpnIxoO_CsbVrtddsexUbEGuH8LzwVA)
    

- Odds Ratio (OR)
    

- OR=[P1/(1-P1)/P0/(1-P0)]=Oddsexposed/Oddsunexposed
    
- ![](https://lh5.googleusercontent.com/OFgQR-kfVRTcYIvnR3fK5sb2spLz2jFof2_tdKRXrrihRq5Tflf0rToivZJz810zmOfGj4_4qmqo47TUtdOfKlMsnePFek2RyOPeKIs2QiLl5Kp-V-s54MYC40SpgxtL1Y8v4-4ISIUKUgr4e4cGXw)
    
- Ratio of the odds associated with 2 values of x is given by the factor exp(𝜷₁)
    
- ORs are neither behaviorally interpretable or in the metric of immediate interest
    
- Ranges from 0 to infinity, alway > 0
    
- Problem with ORs and case-control approach
    

- By effectively over-sampling cases relative to what a true probability sample might have yielded, it undermines ability to estimate average risk level for the outcome of interest, which is driven by B0
    

- Risk Differences (excess risk) 
    

- Risk difference = Riskexposed - Riskunexposed
    
- Risk difference is the difference in incidence proportion or risk between the exposed and the unexposed groups. In other words, it is the difference between the estimated risk in the groups defined by the predictor
    
- Ranges from -1 to 1
    

- OR vs. RR
    

- When p~0.10, OR is relatively close to RR (even closer when p<0.10)
    
- However, if we interpret OR as a RR, we are OVERESTIMATING the effect of exposure
    
- Value of OR is always more extreme than RR when OR>1
    
- Only equal when OR=RR=1
    
- OR<RR when OR<1
    
- Example:RR=1.57, OR=1.64
    

  

Logit Function 

- The logit model controls for covariates and constrains the predicted probabilities to be between zero and one
    
- ![](https://lh5.googleusercontent.com/0SToGg1dLap9vmNVVKzRngcGprk_h-zlBs3IYWuU1SvyVD6g1Tcy1Oe6ar4M2cyZ-Y7n0kX7iSFA5pPUEbynuS5wEEJtzDoOx8806Cknqgk4Ts6_-xxDu8zrfIzz_ug3ZtHAJPHgMLWiZUjI2cfk8Q) Or ![](https://lh3.googleusercontent.com/cHIypT5_hV9fCgz8kh0S108ma8vQI7zMXsiuLYfFbpxatc0IgiQov45J3yn2TU_J3FH7h9WhxbWTb_zk3J_-9nJVf2OhCKcA5MjZDBSbX9dzhGixJ8U6qJh2PKmC86YqiNMZCV05tRe7HKg9JRNApQ)
    

Logistic Model

- Allows for a smooth change in risk throughout the range of x (S-shape)
    
- Risk increases slowly up to a threshold range of x, followed by a more rapid increase  and a subsequent leveling off of risk
    
- ![](https://lh4.googleusercontent.com/xb7JJpMnOms66UYJbyxeFgAWqyAuOp9bi0lKvYOE8XJHjDFuxOO7xRvVta_w2ZTY_HLqumnPDWS-H8n_wmsddmBtkYW-cG8OEyoZLwC2dPdWbZJvVuUwRuJtcJiV0vTF9szo4KiPdPTIK5ExI5Me3Q)
    
- S-shape bounded by 0 and 1; Approaches 0 when x approaches –infinity; Approaches 1 when x approaches +infinity
    

  

Multi-predictor Model

- Based on the same assumptions underlying single predictor version
    
- Assumes that multiple predictors are related to the outcome in an additive fashion on the log odds scale
    
- For a given predictor, the coefficient gives the change in the log odds of the outcome associated with a unit increase in the predictor, for arbitrary fixed values for the remaining predictors
    

  
Assumptions

Since this is categorical outcomes, there is no variance and no 1) residual normality; 2) homoscedasticity assumptions.

  

1. Outcomes. binary logistic regression requires the dependent variable to be binary and ordinal logistic regression requires the dependent variable to be ordinal.
    

  

2. Independence. logistic regression requires the observations to be independent of each other.  In other words, the observations should not come from repeated measurements or matched data.
    

  

3. Linearity. logistic regression assumes linearity of independent variables and log odds.  although this analysis does not require the dependent and independent variables to be related linearly, it requires that the independent variables are linearly related to the log odds.
    

  

4. Sample Size. logistic regression typically requires a large sample size.  A general guideline is that you need at least 10 cases with the least frequent outcome for each independent variable in your model. For example, if you have 5 independent variables and the expected probability of your least frequent outcome is .10, then you would need a minimum sample size of 500 (10*5 / .10).
    
5. Collinearity. logistic regression requires there to be little or no multicollinearity among the independent variables.  This means that the independent variables should not be too highly correlated with each other.
    

## Diagnosis

Ref: [https://towardsdatascience.com/assumptions-of-logistic-regression-clearly-explained-44d85a22b290](https://towardsdatascience.com/assumptions-of-logistic-regression-clearly-explained-44d85a22b290)

  

- Multi-collinearity (check correlation matrix of predictors—concern grows with any r > .7 or multiple r’s > .5; drop or combine predictor variables)
    
- Influential outliers (rerun models without outliers. If model is substantively unaffected, leave them in the final analysis. If model changes, consider presenting both results noting the differences (perhaps one set of results would be relegated to a footnote).
    
- Non-linear associations (test for quadratic and sometimes cubic effects—leave in model if significant, drop if not).
    

## Interpretation

- Overall model significance
    
- Type III tests for variables with more than 1 df 
    
- Categorical variable with more than 2 values 
    
- Model fit (c is common, others provide similar info)
    
- OR’s and CI’s of significant predictors in the model, sometimes along with their significance level
    

- Regression coefficients are interpreted as log odds ratios, which can be expressed as odds ratios via exponentiation. 
    
- ​​![](https://lh4.googleusercontent.com/lELdPtbApGWMUbvqP4_N5qrjnQPCC9_4KNZuKwBBBrQMiLsO01XsXhBOaqPQ2Qegipz7foP9AdHvMwApLYi07QfXoIXZzGTTrgfJN9tA73PGli2jIuAeSe5GmXT86unhBBSwpryzdRjgO5oQbYWlyw)
    
- When outputting coefficients: If CI does not contain zero, reject the null
    
- When outputting OR: If CI does not contain 1, reject the null
    

- As in multiple linear regression, we usually describe an effect and then note that this effect was observed “after controlling for <covariates” or similar language.
    

Comparison of Methods

- Logit
    

![](https://lh3.googleusercontent.com/qjZLSCLyPP_1yUp_m68IvRvZ-PshSOeVMg7hPYPG65rYiNB7OorXwquIry5yZcwFp2JGDXHf7JjEVVootsFyDJe5Z3MORuQu6oMl7aaXuahLOW-VeP2ycIi5m8AXhYUHuaEV-i0UieqJwAczPCR8mA) 

- Probit
    

![](https://lh5.googleusercontent.com/u2EGDh5FyNEmGUoEBbj6ysBlIily8RrqY85VxhEwcbkr-n9qTq-uuWvZ-pDG-bH6iriGUdN80v3MrK5xT-SFtMF_BdDT9HUBPM4gqci_-hRYuuDopxJaAHFLG9UcxSJupvnWlCPuqFUkg-8iv_oIVg)

- LPM
    

![](https://lh3.googleusercontent.com/OTGhPQSbwTNdq-YgDvdmnh-vARvQS43bM6npl3ggi0rsh3GrR3k12BIBRmXmmoxcaca1PGQlq-lzcZVhLP3cODe5fXSt2cO_neUjkbLsnWkpGmRywGoViviJJAkoudhD-bwD-8t1PhMp7xN9tlV8Kg)

## SAS Lab

1. ### Create new variable
    

![](https://lh4.googleusercontent.com/bUPhGRMPUWaV5FanO3LPBuMQKj-hu4ht4T_twA0xHE7_tY743cnK1uN7tTDwz5_UhipOx8g7jrC_UuVVM0EHZqHYnt5x0wsJLlb6scBC2oruo7sW_m0IY8Utpb_5Lh5fwBCtiMOJUia483Li9INs3Q)

2. ### Logistic regression model
    

![](https://lh3.googleusercontent.com/JPMt5wS49uPLsysX3itYpvjO5yyt5UBDBg0aYyrR4D7xMMlRRbhQxnE_jrO8E2BKcanzluzrOsKLPIAfydaG6UTubT7ql9Fl0bhQDi1e0MDfdWKoOELp416A7DDgIA-nVWoJ61nzH8SJUgEyhOiFRA)

![](https://lh4.googleusercontent.com/N2jLRXVNvu9ZMx4XGGVd0TmkTN57weKA5yxhBZpWFWwqvfmcI4D69f53D-sfd7fq-v2RpNTfHtpfpBe8gcjKnZbk8aKtc70c_H7Ex9c7UnHTlvNAII1CL2NENdz_GKw_kBTqg1uBABFdzeXCH0yNyg)

3. ### Ordered logit
    

![](https://lh5.googleusercontent.com/nSH2GaIWK7oiOcOGl0q_arSHryJWwoPkHOIoPKztRsKKcb9Asri-nU3JG3l1MfwgOhy6aaliZNFO4-X_A_IkESXWAv1ffH7GB-C1Vlda2qNyAeaZg5u89FtKGZ5fdRHWI8jU4tLF3y7jq0Txl7hhMw)

  

4. ### Diagnosis
    

- #### Interaction
    

![](https://lh3.googleusercontent.com/OOI_TfflWr7uEuPrwmb1hIsAUrFF0o5JciF0vfcdvmo9QIG7nqo6YTpVQqxbU8u3LK16sRr3b0MPgPQmE_dAaudl9SADt_iuP6ZbE6HZc10N4cJ_J-gFhBFKsmghUZdjiOBQQINk236Vch8qvlrljQ)![](https://lh4.googleusercontent.com/lqx58bGna61cdBq2VSIKvhOXTxsFrqiJRUEy7Cw_TIxokCALAZRiuJdRbJ9ecNcfKLYzR0nF4PF4ZGYzGBLu1pOQY5mWaZAMpVYnpalQx1RLfa6lOZi0LaHnnPh8-Liv5UZ3y7gcmeiW50skMmGr7A)![](https://lh3.googleusercontent.com/GFlKCJKdU2_HN_2ki5PJTDvBndZ9faV-0gjPkuTCmcrod5Hc0vLskX75Xggo0xMmXfFG4I0IzlgR1i5RgqrN_thjHBj7xH_6n2-fM61G-3isBvjYYKJgaGgkfpe8HC_NiJKctxoyb9-OCtM8hBEcyA)

- #### Influential outliers and ROC curve
    

![](https://lh4.googleusercontent.com/g9SIusmxdRjhSiFtTuIB6hZWXEurgtMMb9afsqh4bNFuXwBTLzAl1DWnlEkp2WZh69355fFi-Oq6nLziJVJ0i8Du_vaA-Nj0rPhmfGL9dUU_nNQb9tIVW-wkWZhaQ6DglRnCTywRdoreJge4h7UqNw)![](https://lh5.googleusercontent.com/8wTXjLpAKuKWeJHZamM2zVpiHDQmn72gZlwy9zRugToGKF9RL8Chg96XUNvjLaKuklc_D005yzZAanEyHQSRV58Yve1isokFgt29rJb8PyOqaZuitfhWFjXQICysnH1BnMJBXCKkPQL9GG_9ZHVMtA)![](https://lh6.googleusercontent.com/t2faGdB1o7yYYML32LQh7Keq_Qm-Y7J8kCO-sdG29aGZFyQHSEqEobGwutWFr5csA6EFjzLBdJGkFh6bx3oGBHGXEJBqeqs3lghxGkPJj-01_MXciydfr83xKS0DIQRm4-qp9kTO1qxEWbjnhuDaMw)

- #### linearity assumption and “pseudo” r square 
    

![](https://lh5.googleusercontent.com/ZDMiqWiKd2Ewt3z3s1Dw_0xLU67iphjF9tE4YyeQvf-0NBM_h99JKNURAPrynbD7f6XCZQM19Rsdpvm3hyAx1iHzGf_bUOe41AULar61XWvxdRw9PU7k6qCEPoUlCVy1eHFOLm96wSCtILkSa-euTA)![](https://lh5.googleusercontent.com/0ZgD4J1cqCQGgrYcGMiJOk5QUzXlFeSlAotli9KUpAZ_wE5HAksnfcsWnerCAxPlUKUf0oQOmMrI6w5Hf46_B3WQas-ooLOW9gMXhT-p2tGA5Wbtgz6ebAYODPmZhmVsbhGR5m8EqSeGd4S-zRq3yQ)

5. ### Calculate RR from OR 
    

# ![](https://lh4.googleusercontent.com/pUgHg9mwOmheGhr_rkM41C9YhxEmj1aCWr91HbhM_ma_gUYQc3JBLLjr8UBqCg4EQhtKwlBcXyXp2tdicvuzbVopYdiccbzfuXlEQ1NzIM_W98OSnuquqEI9NvZv8h3fZAEbg08-dInNKiaqWnQh-w)

# Survival Test 

## Assumptions

- the survival probability is the same for censored and uncensored subjects; 
    
- the likelihood of the occurrence of the event is the same for the participants enrolled early and late; 
    
- the probability of censoring is the same for different groups
    

## Diagnosis

- Multi-collinearity (check correlation matrix of predictors—concern grows with any r > .7 or multiple r’s > .5; drop or combine predictor variables)
    
- Influential outliers (rerun models without outliers. If model is substantively unaffected, leave them in the final analysis. If model changes, consider presenting both results noting the differences (perhaps one set of results would be relegated to a footnote).
    
- Proportional hazards assumption (add time covarying term--interaction with time variable) allow the hazard to change overtime
    
- Functional form (add quadratic, cubic terms if needed)
    

## Interpretation

- Overall model significance
    
- Type III tests for variables with more than 1 df : having a categorical variable that has more than 3 categories, we are interested to see whether every categories are significant
    
- HR’s and CI’s of significant predictors in the model, sometimes along with their significance level
    
- As in multiple linear regression, we usually describe an effect and then note that this effect was observed “after controlling for <covariates” or similar language.
    

  

## SAS Lab

1. ### proc univariate
    

![](https://lh6.googleusercontent.com/U-WhvQMh84byzbSAIpbKWs97eFqKEJIfdfi1PIS9ZOvdMZ7XYKlea3Xtw2XgGF0F1RwdQAlXSowwIT0R8J82RN-6JrUmyjb5W8bEBiQ6y8HwUm6Yulhy7UJk6o7X7b3JI_HsFZ_oQpeOPz_UjFtfJA)Highly skewed distribution: The risk of death is high at the early on, then the risk decreases as time goes 

![](https://lh6.googleusercontent.com/x8kTDZU9LAzdC4bpAxNuEpax2eebvpnYmYSXg3Qdv7AObXF7Tv3igsR2RqxwV4ZlsFhXy_kQD4dWzLbmXqQmXdwaCOeWS9TUBUk0JtPdp2LRYMOm60v1GyA4rXU8YRz_0Tjp0qP6jZm4m43JCVOqsQ)

2. ### lifetest to calculate the survival curve with confidence bands
    

![](https://lh6.googleusercontent.com/ui3jsk6-ojFKmXMyiJ54qmXVjKgk-nWnqWzX1Aj0RWRKLyMIdf6sFEmSKkUQdYwIbyoPcDZ61sJr2UIjOvTBEC2U5wZF3OME18sPPOz9y5owuIzs9K3FstZqpD_fbdjUWR-Awth2eD94KRaAv6wFJA)

![](https://lh3.googleusercontent.com/4kwwzk-n0yQhGKTJff-AaSN9swgzoi_jMoL3mjs9N8pk-r_TZwJY5etENVOQEklFHBe_fzva809aBUvv0nEsEKnOueKK8WTY84lw1bKLA0MafI36Ii0UzmGSvZk86xYe7ouIlrA9cvLByAaH3nEWLw)

3. ### Hazard plot
    

![](https://lh3.googleusercontent.com/CZboz4pNx549aUwKZ8uGeOgfL2aIUTeBZfsjohRNwVywqvO1SOdp3bumpP0NqayAchXimv3Mj4FJ-INsPR4Jg3NW6et_W-5pkS88eLre6AxMcwN9pNwjouOO2LtCTiWXnwG7tOUcjq7ojX9fPKHRRw)![](https://lh6.googleusercontent.com/PQ7nkMi4mSXdI_ybNXZV571NrtuSddseJtB5abEsK6t1iLrUQxES1qvKavgb7cm0VHlyfZJXzsdTSHbdGQiqYNAPg-mZwTJm-C3Q63ZQ7GO1Xo1R5LUyDh4s7P_LGP_OYdg6BiMZQ63WPls1gU_Vug)

A little bump followed by the sudden risk of the rise of the risk 

4. ### Stratify by gender and compare the survival curve
    

![](https://lh5.googleusercontent.com/H2jtqcAt2Px8YBy11KZToXRKQfaQ6yEl-harO5kEB2WjGLKmNpxrpJPVnGTvgfp0Xv1ujSyYVQXohkNSawx_wz8ywE2q9jOfUAaqJqniUf_3gGzmB0ZjE4sk5dfp20Ulj8Q2HM5Ba3McpHdwryArDA)

  

![](https://lh4.googleusercontent.com/wJXrvBgz1KlcA9IMHB0Z1Vzt5PSHPfN8Wg3d8IMDSUdq7G1iXkgxmMoXwTcYegCndtmlOipArpWcE-KDn68w9a2NQo2RJ5tIrBUTFlDzNzCgZMtsS6wxTh_pqqC5t6UoPSs2__p-RaWKskLkcXvwIA)

5. ### Hazard ratio 
    

  

![](https://lh5.googleusercontent.com/V5WMpZkR0m5CGmwzEBXgJNRtbP8T0iW8LhaSrJRl65U8MZTkaAlQ4hkCJx3aUepZK5VaI5gbgILh36D_159i0EAYZQp9dAqppvJaMuABoWazrls71JzWTNiHdn2AbsS1nJ1Xm3qZprT4WQWqe6dIqw)

  

6. ### Cox hazard model
    

![](https://lh5.googleusercontent.com/gZQiEyTgeB7BJwLrNoV_3_g9McKrcDNGsvJPZyAbRo1MLLxYAkV3p8JFuXkAhsscFHyxJEgu4T7qNF7QQYb7bvQYzXQvD18oPpOdd3XjBL7IMy_pwk-v_b8dvUfm1rTGkSo9x1UIViUZ9GO8zIpgTw)

![](https://lh5.googleusercontent.com/3fvl1LHJ1VMRUm5Lz4Mg_gkhnvzfN-LKuHaY9n7YQ15E5P4PftpAGweQuPRQA6FubSvpVUDAvdH95L0V9E5c4pIF3GEgWVvbbxaQTbO4LCLhUogQwSm4QQh5fLyppuytjxS0OEA5KtZCC1OAnoax4w)![](https://lh3.googleusercontent.com/B-bp3rIwg0qE4rkTxk2y8w12hxRl6myuQ3nkbNP0egdKO2REpvDYXDfHsFConuaHnCsiKPlAGLMgcMsEe_tOVN2WI4uuCYNr-tChn4Zu0d3a8Xp42PMIo2BRRGeK5FWF7XlO3XbXCz62WtY63nRY9g)

7. ### leverage plots
    

![](https://lh3.googleusercontent.com/LD2M-BpZ2jqkbsGhGqabA8JeC82KbTanz8Riw-VVfmgRIsV43d2kEWNFTvaE51dxU2ZPnQ0BMw2Yi_Ae50Pxx6xkx4USlVszPh6PeNn5g5zNI3YChtWSSHiQkhCYF9kqotgwghX3AADKrx-ZZ_jLwA)

![](https://lh6.googleusercontent.com/WJ0UqHOTueNpnNfVoY21P90JiThmDoezIOQ8TXJa6D5XHFmln-dUoqBllEZo-kEtOVi-Uya5NXm_CJTzvNLsPJyQK-AAMe9DJuZMBS6iHqPEItfYFfodjo25Z3Ie64tcy07MGjkyXm6HsIxNj5SAJA)

  
  
  
  
  

## Survival Theory

ref

[https://bioconnector.github.io/workshops/r-survival.html](https://bioconnector.github.io/workshops/r-survival.html)

[https://epirhandbook.com/survival-analysis.html](https://epirhandbook.com/survival-analysis.html)

[https://www.openintro.org/book/surv_in_r/](https://www.openintro.org/book/surv_in_r/)

[https://rviews.rstudio.com/2017/09/25/survival-analysis-with-r/](https://rviews.rstudio.com/2017/09/25/survival-analysis-with-r/)

[http://www.drizopoulos.com/courses/emc/survival%20analysis%20in%20r%20companion](http://www.drizopoulos.com/courses/emc/survival%20analysis%20in%20r%20companion)

### Concept

Survival analysis lets you analyze the rates of occurrence of events over time, without assuming the rates are constant. Generally, survival analysis lets you model the time until an event occurs, or compare the time-to-event between different groups, or how time-to-event correlates with quantitative variables.

The hazard is the instantaneous event (death) rate at a particular time point t. Survival analysis doesn’t assume the hazard is constant over time. The cumulative hazard is the total hazard experienced up to time t.

The survival function, is the probability an individual survives (or, the probability that the event of interest does not occur) up to and including time t. It’s the probability that the event (e.g., death) hasn’t occured yet. It looks like this, where T is the time of death, and Pr(T>t) is the probability that the time of death is greater than some time t. S is a probability, so 0≤S(t)≤1, since survival times are always positive (T≥0).

S(t)=Pr(T>t)

The Kaplan-Meier curve illustrates the survival function. It’s a step function illustrating the cumulative survival probability over time. The curve is horizontal over periods where no event occurs, then drops vertically corresponding to a change in the survival function at each time an event occurs.

Censoring is a type of missing data problem unique to survival analysis. This happens when you track the sample/subject through the end of the study and the event never occurs. This could also happen due to the sample/subject dropping out of the study for reasons other than death, or some other loss to followup. The sample is censored in that you only know that the individual survived up to the loss to followup, but you don’t know anything about survival after that.

Proportional hazards assumption: The main goal of survival analysis is to compare the survival functions in different groups, e.g., leukemia patients as compared to cancer-free controls. If you followed both groups until everyone died, both survival curves would end at 0%, but one group might have survived on average a lot longer than the other group. Survival analysis does this by comparing the hazard at different times over the observation period. Survival analysis doesn’t assume that the hazard is constant, but does assume that the ratio of hazards between groups is constant over time. This class does not cover methods to deal with non-proportional hazards, or interactions of covariates with the time to event.

Proportional hazards regression a.k.a. Cox regression is the most common approach to assess the effect of different variables on survival.

  

### Cox PH Model

Kaplan-Meier curves are good for visualizing differences in survival between two categorical groups, but they don’t work well for assessing the effect of quantitative variables like age, gene expression, leukocyte count, etc. Cox PH regression can assess the effect of both categorical and continuous variables, and can model the effect of multiple variables at once.

Cox PH regression models the natural log of the hazard at time t, denoted h(t), as a function of the baseline hazard (h0(t)) (the hazard for an individual where all exposure variables are 0) and multiple exposure variables x1, x1, ..., xp. The form of the Cox PH model is:

log(h(t))=log(h0(t))+β1x1+β2x2+...+βpxp

If you exponentiate both sides of the equation, and limit the right hand side to just a single categorical exposure variable (x1) with two groups (x1=1 for exposed and x1=0 for unexposed), the equation becomes:

h1(t)=h0(t)×eβ1x1

Rearranging that equation lets you estimate the hazard ratio, comparing the exposed to the unexposed individuals at timet:

HR(t)=h1(t)/h0(t)=eβ1

This model shows that the hazard ratio is eβ1, and remains constant over time t (hence the name proportional hazards regression). The β values are the regression coefficients that are estimated from the model, and represent the log(HazardRatio) for each unit increase in the corresponding predictor variable. The interpretation of the hazards ratio depends on the measurement scale of the predictor variable, but in simple terms, a positive coefficient indicates worse survival and a negative coefficient indicates better survival for the variable in question.

  

# Generalized Linear Model

## Assumptions

- The data  are independently distributed, i.e., cases are independent.
    
- The dependent variable  does NOT need to be normally distributed, but it typically assumes a distribution from an exponential family (e.g. binomial, Poisson, multinomial, normal,...)
    
- GLM does NOT assume a linear relationship between the dependent variable and the independent variables, but it does assume linear relationship between the transformed response in terms of the link function and the explanatory variables; e.g., for binary logistic regression .
    
- Independent (explanatory) variables can be even the power terms or some other nonlinear transformations of the original independent variables.
    
- The homogeneity of variance does NOT need to be satisfied. In fact, it is not even possible in many cases given the model structure, and overdispersion (when the observed variance is larger than what the model assumes) maybe present.
    
- Errors need to be independent but NOT normally distributed.
    
- It uses maximum likelihood estimation (MLE) rather than ordinary least squares (OLS) to estimate the parameters, and thus relies on large-sample approximations.
    
- Goodness-of-fit measures rely on sufficiently large samples, where a heuristic rule is that not more than 20% of the expected cells counts are less than 5.
    

## Diagnosis

- For Poisson models, check for overdispersion
    
- Influential outliers (rerun models without outliers. If model is substantively unaffected, leave them in the final analysis. If model changes, consider presenting both results noting the differences (perhaps one set of results would be relegated to a footnote).
    
- Non-linear associations (test for quadratic and sometimes cubic effects—leave in model if significant, drop if not).
    

## Interpretation

- Type III tests for variables with more than 1 df 
    
- OR’s and CI’s of significant predictors in the model, sometimes along with their significance level—use ESTIMATE to get exponentiated coefficients for count data
    
- As in multiple linear regression, we usually describe an effect and then note that this effect was observed “after controlling for <covariates” or similar language.
    

  

## Book Chapter 8

### 1. Counts Data

Q: Can the new treatment reduce the number of needed visits to the emergency room?

#### Issue with count data: 

one-third of the observations are 0 (did not return to the emergency room within the year) and over half are either 0 or 1. This is highly nonnormal and cannot be transformed to be approximately normal—any transformation by an increasing function will merely move the one-third of the observations that are exactly 0 to another numerical value, but there will still be a “lump” of observations at that point consisting of one-third of the data.

The mean number of visits must be a positive number and a linear model, especially with continuous predictors, may, for extreme values of the covariates, predict negative values. 

hard-to-follow, some subjects are only under observation (and hence eligible for showing up for emergency room visits) for part of the year.

Since the mean value is not likely to be exactly zero (otherwise, there is nothing to model), using the log function is mathematically acceptable (as opposed to trying to log transform the original counts, many of which are zero). exponential in (8.2) keeps the mean value positive.

leads us to consider a model for the log of the mean response. Note that this is different from the mean of the log-transformed responses

![](https://lh4.googleusercontent.com/plpbewj1QLenc9IU2bcM7OYLyhTKhK8L_qSfctCHeYy09QpPqgSoRxLuFMiakRYiJb-S9CJG4e5Aef5wdfpbArgQNeyvNnIs6RDLXrjrPnhrre7RCS9KfPVwkB6nNevpwyT0epUUbkhUdp7_xMgpOA)

What if the subject is only followed for half a year? A simple way around this problem is to model the mean count per unit time instead of the mean count, irrespective of the observation time.

![](https://lh6.googleusercontent.com/wg2IAc-bqBfdaE0uY4xFX0CVu1JSH6GHbEtdwzHi56_62Q_H1PkN5e_aqc-16-A1V0IIzYLc45CYZANm9hbkdFBi9nzTdGaUrn_2szJmqrxlTP8K2TBtHdEANADxTCFIyOgvrv6yFSWmIOyihaXpVQ)

#### Possoin Distribution

![](https://lh3.googleusercontent.com/1hPRlDyIVGOooHbnUlUdQVqxkLNPVQE4DRUnkWSvAOFeEyV_YNCTI3AnTzpTjDhw0v7jNJ1PAQ1kN6UpvKCvWpuWSxdw5DLnA3YRj9RrCZK1kAiAv4mlBLENm0tnSy_SoYNUTW1o_viRRq89U6OsSg)

![](https://lh4.googleusercontent.com/_7uDS3nRXFsuMkP6JNbPrTyJoGW4lhUb1HnnAl9KQ-7pYIawi4K7GSzLr8t4nZ--ni4oOhn0rXQpYRo4yVqbYwtx8wn1Iyazt9dGCG9ElOjsu3LbbClgM2AZI3JSAfq9HQkQiBNMEl8NRJpcgFPOcw)

RACEi is 1 for nonwhites and 0 for whites and suppose the race coefficient is estimated to be 𝛽1=-0.5. ![](https://lh5.googleusercontent.com/okMRRDnHKj1F8opZv2f9ZdjvApZaILJd-REPXQFKkCng1auBrhUmT3frUOgDsuU0K_zFRTsNBPrxV-bBKZqQ4ZbD1DvVCcaPPl7BbqbjD-W4155Z8zmL43QYH0-x9GIPYrho2r6IUhS3hICg8dNKQA)

#### interpretation

After adjustment for treatment group and alcohol and drug usage, whites tend to use the emergency room at a rate 1.65 that of the nonwhites. Said another way, the average rate of usage for whites is 65% higher than that for non-whites. 

#### issue with poissson

A feature of the Poisson distribution is that the mean and variance are required to be the same. Ironically, the Poisson distribution often fails to hold in practice since the variability in the data often exceeds that of the mean.

  

A common solution (where appropriate) is to assume that the variance is proportional to the mean, not exactly equal to it, and estimate the proportionality factor, which is called the scale parameter, from the data. a scale parameter of 2.5 would mean that the variance was 2.5 times larger than the mean 

#### Negative binomial

[https://stats.idre.ucla.edu/stata/output/negative-binomial-regression/](https://stats.idre.ucla.edu/stata/output/negative-binomial-regression/)

negative binomial (a different count data distribution) regression routine, in which the variance is modeled as a quadratic function of the mean

#### IRR Incidence Rate Ratio Interpretation

The following is the interpretation of the negative binomial regression in terms of incidence rate ratios, which can be obtained by nbreg, irr after running the negative binomial model or by specifying the irr option when the full model is specified. This part of the interpretation applies to the output below.

Before we interpret the coefficients in terms of incidence rate ratios, we must address how we can go from interpreting the regression coefficients as a difference between the logs of expected counts to incidence rate ratios. In the discussion above, regression coefficients were interpreted as the difference between the log of expected counts, where formally, this can be written as β = log( μx0+1) – log( μx0 ), where β is the regression coefficient, μ is the expected count and the subscripts represent where the predictor variable, say x, is evaluated at x0 and x0+1 (implying a one unit change in the predictor variable x). Recall that the difference of two logs is equal to the log of their quotient, log( μx0+1) – log( μx0 ) = log( μx0+1 / μx0 ), and therefore, we could have also interpreted the parameter estimate as the log of the ratio of expected counts: This explains the "ratio" in incidence rate ratios. In addition, what we referred to as a count is technically a rate. Our response variable is the number of days absent over the school year, which by definition, is a rate. A rate is defined as the number of events per time (or space). Hence, we could also interpret the regression coefficients as the log of the rate ratio: This explains the "rate" in incidence rate ratio. Finally, the rate at which events occur is called the incidence rate; thus we arrive at being able to interpret the coefficients in terms of incidence rate ratios from our interpretation above. 

Also, each subject in our sample was followed for one school year. If this was not the case (i.e., some subjects were followed for half a year, some for a year and the rest for two years) and we were to neglect the exposure time, our regression estimates would be biased, since our model assumes all subjects had the same follow up time. If this was an issue, we would use the exposure option, exposure(varname), where varname corresponds to the length of time an individual was followed to adjust the poisson regression estimates.

![](https://lh6.googleusercontent.com/AfZFm57fUVpvHsmh4Udde7Qec2Tg069oydaqVA7CoQis3JCevNO6yVexDQPxCmujoYtksAPmzpf9AuX_UafF2vyEnkfZefsUxt5GYQ6Gm0-sU7eAg5mKg0ayx6tj1gCpzWdE8MALiaIYlENOIHQqjQ)

### 2. Right skewed continuous outcome (health care cost)

#### Gamma Distribution

gamma distribution, a flexible distribution for positive, continuous variables that incorporates the assumption that the standard deviation is proportional to the mean.

![](https://lh3.googleusercontent.com/ltU8JE5SCiZRVqq_RzREW7PHKrmZP1SyyMgNrJ5UwpQZI6xvPAPoxVusKrngNJg_ZyB7Si7ryoCF_41nIce4Ggu2wVgiKLrGCo-FHFLtWJgrTXSBsdWsX5cAkGnZFPAGAqMwJOnE5Bli_4yhHD7heg)

if 𝛽2 = 0.5, adjusting for race, gestational age, and birthweight, the cost associated with babies receiving phototherapy was exp(0.5)≈1.65 as high as those not receiving it.

  
  

### 3. Inflated zero value

#### build separate models for the zeros and the nonzero values. 

For the analysis of hospitalization costs, we could use a logistic regression for the probability of the cost being zero. And for the nonzero costs, we could fit a GLM assuming a gamma distribution.

For the syringe sharing data, we could use a logistic regression to model the chance of sharing zero syringes with the predictor of being homeless. Stata can accommodate either a Poisson or negative binomial distribution which has been truncated to only allow nonzero values through its ztp (zero-truncated Poisson) or ztnb (zero-truncated negative binomial) regression commands.

![](https://lh5.googleusercontent.com/j4DlnkSJqP5JMgAHC-JUmInj7-MYK_vjRv4q2Ux1Rv42lEWQu197FNystASIEyQ5MWxen1xBfBLqvsSEwhWh11PaKJqNFefw9RfDXDnfI3MzR26F4XmPzj2zTID0tRPLZrhFg30SGPDOQLUnRLN7Pw)![](https://lh3.googleusercontent.com/45WJSpDVJZqp85OMLKEjBB_LKZUhlTvx4fc2Jm5oo0BEg9Pw1hVYAwCe5FFzfW3nOwgH3W_yhTXR6Ek4Xs6xYy9_baiPNDJew0haGqyvVziHLrulcU9rdl9CFuB0etdu3aOuthAUWkiuOLh3hT_LzQ)

The logistic model estimates the odds ratio of not sharing a needle. the homeless have odds of sharing a needle which are a little over two times higher than the nonhomeless (2.1385=1/.4676).

The zero-truncated regression estimate indicates that, among those that do share needles, the homeless share syringes at a rate a little over two times more often than the nonhomeless. 

exp{-0.7708} = 0.4626

#### use zero-inflated models

uses an underlying model in which two processes are operating: first a process that generates the zeros (like the logistic regression above) and then a count data model, such as the Poisson. This is slightly different from the two-part model since a zero in the data could have arisen either from the zero- generation process or from the count data process, which just happens to a zero. These models are more natural for some situations.

For example, consider modeling the number of open nurse anesthetist positions per hospital, similar to the study of Merwin et al. (2009), with predictors being the log of the number of surgeries, log of the average daily number of patients, log of the number of operating rooms and the state in which it is located. The number of open positions could be zero because the hospital does not hire nurse anesthetists or because they do, but they have no open positions. Zero-inflated models can be used in situations in which we can justify the underlying two processes or in situations in which we merely need to accommodate the large percentage of zero outcome values.

Table 8.5 shows the results from fitting a zero-inflated negative binomial model, where the inflate option gives the predictors for the underlying process that generates the zeros and again we have set the level to 97.5% to accommodate the two tests. The estimates and interpretations are very similar to the two-part fit above, with the effect of being homeless on the count data model being identical and the effect of being homeless on the zero model being very similar. Table 8.5 reports the log odds of not sharing a syringe as -0.7708, which corresponds to an odds ratio of exp{-0.7708} = 0.4626, similar to Table 8.4.

### 4. GLM

A number of statistical packages, including Stata, have what are called gener- alized linear model commands that are capable of fitting linear, logistic, Poisson regression and other models. The basic idea is to let the data analyst tailor the analysis to the data rather than having to transform or otherwise manipulate the data to fit an analysis. This has significant advantages in situations like the phototherapy cost example where we want to model the outcome without transformation.

Fitting a GLM involves making a number of decisions:

(1) What is the distribution of the data (for a fixed pattern of covariates)? 

(Poisson and gamma distributions)

  

(2) What function will be used to link the mean of the data to the predictors? 

a log function of the mean to give us a linear model in the predictors

(3) Which predictor sshould be included in the model?

our choice of predictors was motivated by the subject matter. 

In linear regression, we modeled the mean directly and assumed a normal distribution. This is using an identity link function, i.e., we modeled the mean identically, without transforming it. 

In logistic regression, we modeled the log of the odds, i.e., log(p/[1-p]) and assumed a binomial or binary outcome. In that case, we used a logit link to link the mean, p, to the predictors.

For example, current capabilities in Stata are to handle six distributions (normal, binomial, Poisson, gamma, negative binomial, and inverse gaussian), and ten link functions (including identity, log, logit, probit, power functions).

#### Robust Variance estimate

![](https://lh6.googleusercontent.com/dRp2t46PNqPekRsxqkMzfNFByNONmNPqskLU039SrgGqWBqddP8Z3EfkX6cQ8WbafxThfbD4SP6wQTXs6-HSLuE_11WTW3sxnDLgfz3ZkwHIiS0vzB_7dsWP_PUh0Dp3MTbXoWj0Y31gCb7vxgCfqA)

![](https://lh4.googleusercontent.com/qx-HGc6_z3AdWsWaM_DRhmnfhFjkfIamlk61ka8lzCDD1UOGs2GvN-WOxHIEdldSf5EQYu6WJSyMLf5VkcjcRMcnYBtFoSlFAKD0TjC0IX5dVqLhpWRJ81dCuR2pUe7-P47nnsfZ0XC85kXVbNUF6w)

  

In rate models the offset usually represent the log of exposure, and Stata lets us specify it directly using the offset() option with the name of the variable representing the offset, or using the exposure() option with the name of the variable representing exposure, in which case Stata takes the log.

#### Clinical Trial Example

![](https://lh3.googleusercontent.com/Ewqe4r50w1w1a1aZDwFRAaQLp6-lU_BYVp8-9rg0-gHfQEFJoWwUf0gaermt4JfbW2XM5jZYLmTG7AyFMFx48rQmwTHDu3fgiFt_TleX6C2bQV_eannEzzaoVw1k9z1h7Gyu1Q6XFVVq-OyRtlQjlg)

![](https://lh3.googleusercontent.com/kDI0aBmUSAqpOtsTkHpZh79ukNsTtNNB_wzt4sagxRFXY6B0M_jFJv1O5ZT7pCBMHiWI2fma6uCuvaZd8gBga9Vol-hz5gyq_BvI1iw9bfXgUrstKw5xHpIHXK8LmW_zeNjN5fXLEWiFJJdQAcg1lA)

In the low risk of falling groups, the yearly rates of fracture are much less (0.042 for the placebo group and 0.034 for the alendronate groups). These correspond to about 4.2 and 3.4 fractures per 100 women over a year. 

In the high risk of falling groups, the rates are higher and about the same as one another (about 5.1 and 5.2 fractures per 100 woman years).

![](https://lh6.googleusercontent.com/-PmahZ5wmrKRU9yY36hThdPm2ymCPpkDtHwuxf5RsgtvwXn7jWHcSazQ_mXI4ONgOTODaUowERi_KxmtcnWBFPy4rFRtc9dl3kkTfxhBzzpHxfmm-dVwknP6XS2SHEd-3qSXvBvOH3NucsfsTKcxJg)

![](https://lh6.googleusercontent.com/HezOITReL-kH-DaRqGkZDm5XkcICgKKA1lyIukOW7wNw9JKd6HqMF6bFr1968nmVEnzl5icQjM5VQ8X2qxhYIDAuxxl_SQrY4boVbFsH9UsPdGns0tpbGMqv5Ad40ESsgkwVk3hViqAD2HB4iSu7jw)

  

#### Mean Varaince Relationship

![](https://lh3.googleusercontent.com/xQaLIy1MhKSwUBpdV7tQWwqEWqs2D6YsTnazjJLplsv8cU5syrOMSPnD8MsA0u0pGRUsIf84tTimzv_xUICPEkFUs4KrI6wPpH7XkoiRFwvFN6dIC8PNrQSk4ylOC8Jtps4JgB1R4lkv-rm4VMKqJQ)

  

## SAS Lab

#### 1. Look at dependent count variable distribution

![](https://lh4.googleusercontent.com/FkVNqNdMWWLllmOJ_BlECXSgUf3R1IKtH2IGJap4-MhPvjB4iKPcZHjahzUUi7zLHcKZycg_e2lHkHfUegcrfWRyUPy5FUaDbFMs7af0oDX8e6iOng7fBl1NJ-8AJgAFIni8wMyx45u8m-dVNsDUrg)

![](https://lh3.googleusercontent.com/3ZNx6GSk31yMaUWjcyxFPUk6U2aYkFKBuTiYJcC1lDzXi4ke11mtVwgyGmBekeGpbi7r-A7R6-BpOD24YJ61yjstuQdxpD2w5V8UZULlr6kzlMbufMnh3WkJXBkWkip0yutD1tfWrE6VK8l3riCQdQ)

#### 2. Fit a poisson distribution

![](https://lh6.googleusercontent.com/MBerCR7xmgR69M3RBRUi54WHXSwNt_1nwXQZ95haDHLBAmmD-9nb2AivlTgwyySbEFt6ODAV4UCsHKQRiXyTbqLA4Cro2utkEfD_vNmlIFmu65sY2z-NHqwwxCUSCKirAsqOjwfrrCjCelN6aBa-1A)

this "sort by descending camper" is useless since we don't use "order = data", we use class statement option "param=ref ref = first"

![](https://lh3.googleusercontent.com/fbvkIqaLEPr45KnYvrHY8CyGTpUey_wd8nfGdC20kSVOpU458vu-DzI3jyfJOhO-JrsTvb3FRZTtDhqML3cF7cVjWdTTnKiRzSQOUnWAlLMO-bJwgPpFX-lWiPNbnitX4hvSr_5M8UtH2kJZID2tMw)

#### 3. Genmod do logistic job

![](https://lh6.googleusercontent.com/Y74lpfcXxwrB2z7hj51bo_YxDwhliBcxVCnt_6bayufPzou0Gubs6GbRSnWCdLe_2yZhy73vThSMEu6SA5Q_k7b9pvDNuKz0kM-uBu5t4qbm7J2iKhz_0scyvbzDeKGe9rVlAvv2-U8DrpqoQQPuaw)

  

#### 4. Fit Negative Binomial 

![](https://lh5.googleusercontent.com/wxlbFof_pGWd3TxHm-FdJul2cXSigazQWsc_0K7LWXIlS5nTckJmkn6jcI17C4Hh1Fssh0W8YFvgVkJp-j_hII1nrd_xlor2iDAZKWGilQV_EX2J77FTUBcXSvp9vxh8G1tIsmdZWQHOLHGMKLUKZQ)

  

![](https://lh4.googleusercontent.com/nOb0NzGwyMljSv6xqVNp4KgxkJ3tGMkLjhp7PCQq5Llkk3DIXZK2UK4zcYLe2-Brru5Qmsvnp-wctiqOZKR7How5B8Ma_Cm9KR3QZtH0H1Sl5fU_C3JfQlWJg49seHvoYzob2U-a0S6-GwLLQjwpDg)

  

#### 5. Check Linearity

![](https://lh3.googleusercontent.com/knvStQXQkhHUkl9fzlycbshahvDf7n6GzPrrJ41cAspUpOxPRJlsyeegwOpFXUel7HAufLjohmKQkFyqfI2l-pzS0m04H2lOFQYVW_bwnmeOLDHz_n7otT3p3gsF68hc0xIwdNQnufPWX1X-t17-kA)

  

#### 6. Zero Inflated Model

![](https://lh4.googleusercontent.com/Rs7-wwjm_grOXaILai5gH4QaA3cuIIglqMN5UJMmrgT7EathkmF5zb8h7a54ucRf95eoEyU9Jav_mi8KvuanXz_UEjmkNAVj-aqgXcuc-HCvDtALHO8PAcsFHx6OnrXh1wgtzOXV9xdKexQTU6LGgA)

  

#### 7. Plot observation ID * cook's D plot to check for outliers

![](https://lh5.googleusercontent.com/6eyA5XPJaXys0JVaRACy3yWYWzJgdcQClxsSfk8ATAspa7KyWkEoHe1b2h06tQKDGTdLD_vuD04hn3xTIA41_2Kbl_J67I6pewIYq45V4qiTJDEHwrXtjIZNQN-lgV4rclybioU3dwH746OLrKnBVg)

![](https://lh3.googleusercontent.com/WoBBHX4MGvspzVU6slg9iXJ2-hcnQTRWlgp4m91mMLF4KPGFj-nl-SIb4EjKGkCOFyHuNoy9zrra-f9JJV6hre8C0y-t_H1n81FoeXlW18Zj4_M0bHGiLwDILpGqCuoCM9rx-TS0ZcojDEpuMuI5yA)

  
  
  
  
  
**