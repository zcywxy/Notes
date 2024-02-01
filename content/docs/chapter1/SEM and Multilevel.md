---
title: SEM
linktitle: SEM
type: book
date: '2019-05-05T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
tags: ["method","SEM","CFA"]
---

[The Pod Cast](https://www.buzzsprout.com/639103)
# Some Definition
- R Square vs. **adjusted R Square**
	- adjusted r square *doesn't exist* in the *SEM* 
	- In factor analysis, it is called community, but it's essentially just an r square.
	- The more predictors you throw at this model, the more you're going to explain, just by chance, it's it's a kind of a penalized estimator. Adjust for this chance variability that you might be explaining that even if there's nothing going on, you're not gonna get an r square of exactly zero. It *penalizes* for the *number of predictors*, and it is also *based* on your *sample size*. 
	- If you have a small sample, it's gonna have a greater penalty for having a lot of predictors in model. let's say you had a data set with six people in it. If you put five predictors in your model, you will have an r square of one in your sample, even if there's really in the population no relationship between those predictors and the outcome And it's because you've exhausted your degrees of freedom. There's nothing left to explain. You've triangulate every data perfectly. In a small sample, there's a greater penalty and a big sample, there's less of a penalty. And that's part of why adjusted r squared doesn't exist in the SEM. SEM is a large sample statistical model. We typically assume the sample is big enough that you don't need to make that adjustment.
- Stepwise Regression
	- I will never in my life recommend step wise regression. There's been a lot of research to show that it invariably doesn't put you in the right place. If you do forward, you end up in a different place than if you do backward. So it's kind of arbitrary. So there are better tools out there. If you have a large number of predictors and you wanna run a regression model and figure out what is the optimal subset, there are better tools out there for doing that. 
	 - So there's a whole area known as **regularization**, which is an approach to fitting complicated models where you're looking for sparsity. Right? So you've got 100 predictors, and you wanna throw 100 predictors at your sample of 1,000 and figure out which ten really matter. **Lasso** is a very popular approach to that, but that's **a machine learning approach**.
	 -  It depends on your sampling. It depends on the quality of your measures. It depends on the complexity of your model. It depends on the adequacy of the model. It depends the extent to which you're meeting assumptions. 
All of these are hydraulic kind of forces, where if you have poor measurements of someone reliability, then you may need a larger sample size and things offset. And they're just simply aren't good rules of thumb, the thing with regression. And this is kind of cool to know. 
# 1. SEM
### 0. Global Overview
- What we do with the SEM is to try to reproduce the covariance matrix and mean vector that we observed in our sample
- Structural Equation Model (SEM) is a general analytic framework that include t-test, ANOVA, MANOVA, multiple regression, path analysis, factor analysis, growth trajectories.
- But allows for many critical important **extensions**:
	1. estimating models with multiple dependent variables
	2. testing complex mediating mechanisms
	3. estimating latent variables to account for measurement error
	4. testing invariance of models across groups
	5. estimating latent factors with binary or ordinal indicators (look at the probability of endorsing a symptom or reaching a diagnosis or buying a product. What is the probability that you would enroll in another class?)
	6. modeling growth trajectories with repeated
- **Advantages**
	1. Highly flexible in allowing various parameter structures and tests
	2. Allows for simultaneous test that otherwise must be done in a step-wise fashion (mediator test)
	3. Offers alternative for continuous, non-normally distributed, or binary, ordinal, count data
	4. Provides powerful and rigorous tests of individual stability and change in longitudinal data
- **Disadvantages**
	1. Models can be complicated and wander *away from theory*
	2. Challenging to decide if a *model* adequately *"fits"* the data
	3. Radically *different models* can *fit* data precisely the *same*
		- ![[Pasted image 20230712102419.png]]
	4. Philosophical blind spot in that the SEM takes the absence of evidence as support for the hypothesized model
		-  Normally, the null is your hypothesis is not correct, you need evidence to prove you are right. But the null hypothesis in the SEM is your model is correct. Then we have to bring empirical data to say that it's not correct 
	5. Large N is needed for stable model estimation, but how large is large enough is hard to know
	6. Likely any modeling framework, the SEM *cannot "fix" poor sampling* or *weak measurement*

### 1. Regression & SEM
[[Regressions_To be finished]]
- The *dependent* variable is almost always going to be a *continuous* and assumed to be *normally distributed* variable. It's *really the residuals* that are soon to be *normally distributed*. And we make similar assumptions in the traditional SEM that the dependent variables are continuous, and that they are *conditionally normally distributed after accounting* for the predictor variables. There are versions of SEM that exist for binary and ordinal outcomes and for count outcomes and other kinds of things.
- *Maximum likelihood* is *predicated on defining the distribution for your variables*. We will use the normal theory, maximum likelihood. But again, there are variations for other kinds of outcome variables. 
- We look at our multiple *R square* that tells us how much variance is explained by the set of predictors. Then we do an *overall F test* on the model. We see *whether* that's *significantly greater than* chance, a blind to guess, as to what the outcome might. We can also use *F tests* to look at *subsets of predictors*. And that's very common in hierarchical regression models, or kind of build models by adding predictors and sets. 
- We usually use *unique tests*. Each individual predictor is going to get its own regression coefficient, the *raw regression coefficients*, and we can interpret that as the effect of that predictor while *holding* all *else* *constant* or over and above the effects the effects of any other predictors. We'll also be able to calculate *standardized effect estimates*, like standardized regression coefficients.
- Multiple *regression* model is *saturated* 饱和的, which means we estimate *as many parameters* in the model *as* things that *we observed* in the sample. What we observe in the sample and what we reproduce by the model are always exactly equal. One of the limitations of the regression is we *don't* get an *overall measure of model fit*. We get an F test in the regression, but that's actually assessing a null hypothesis about the r squared. We are accounting for a significant amount of variability in the dependent variable, but it's not until tomorrow morning where we start to impose restrictions on our model that what we observed and what we reproduce are different. And then we're gonna play a children's game of how different is. Okay before we say, no, that's not right. 
- **Advantages**
	- provides individual tests of the unique contribution of each predictor net all other predictors
	- provides joint tests of sets of predictors and estimates proportion of explained variance via R square
	- can include continuous or categorical predictors
	- can include interactions and power terms
- **Disadvantages** & Assumptions
	- A single outcome variable y
	- Only direct effects from x to y
	- All variables measured without error
		- SEM allows for latent variables to account for measurement error
	- All effects of x on y are linear
	- Residuals have constant variance $\Psi$ (homoscedasticity)
		- SEM can allow for differences in mean and variance structures across groups (heteroscedasticity)
	- Residuals are normally distributed
	- Residuals are independent
		- SEM can model dependent observations
- Regression in SEM structure
	1. Dataset variables
		**peer** adolescent report on peer substance use and peer tolerance of use
		**coa** parent report of alcoholism diagnosis where 0=non-alcoholic and 1=alcoholic
		**gen** gender 0=girl 1=boy
		**age** age measured in years at assessment
		**stress** self report measure of uncontrollable negative life stressful events
		**emotion** self report measure of temperamental emotional expressiveness
		**negaff** self report measure of depression and anxiety
	2. One predictor regression = two samples t-test
		- ![[Pasted image 20230714234002.png|300]] peer = α + γ coa + ζ
		- ![[Pasted image 20230716011248.png|300]] we often omit the variance of predictor and put intercept above the predictor
		- R code
			- ![[Pasted image 20230715203416.png|600]] 
				- First, we need to create what’s called a **model syntax object**. 
				- Then fit the model using the **sem function**, placing the results into the data object fit. 
				- **meanstructure** argument will obtain an estimate of the regression intercept.
				- we are using ML (maximum likelihood) estimation with the **nlminb optimizer** (this is a built-in optimizer in R for finding the minimum of a function).
		- Results
			- ![[Pasted image 20230715202238.png|400]]
		- Interpretation
			- *Lavaan* & slides *difference*
				- It is worth pausing here to note that **lavaan counts parameters differently** than we described in lecture. For this model, we would normally count five parameters, the mean and variance of COA, the intercept and slope of the regression of Peer on COA, and the residual variance of Peer. But lavaan **does not count the mean or variance of the predictor**, COA, as parameters of the model. Nor does it count **covariances among predictors** (though there are no such covariances in the current model) as free parameters. Fortunately, lavaan also does not count these parameters when determining the number of observed moments, so the degrees of freedom for the test statistic work out regardless (e.g., here it neither counts the mean and variance of COA as observed moments nor does it count them as estimated moments, leaving a net difference of zero when calculating the degrees of freedom).
			- *Multiple regression feature*
				- This output also provides some information about model fit. **Multiple regression models are just identified** (i.e., every piece of information provided by the sample is ‘used up’ to estimate model parameters so that no degrees of freedom remain). Therefore, the model fits the data perfectly and it is not worthwhile to interpret the test statistic (this and other fit indices will be discussed in later sections).
			- Three parts results
				- The output is subdivided into **three parts, regressions, intercepts, and variances**. In the Regressions section, the peer ~ coa coefficient is the slope parameter estimate γ . In the ˆ Intercepts section, the coefficient listed for .peer is the intercept α . Finally, in the Variances section, the coefficient listed for .peer is the represents represents ψ , the estimated variance of ζ i (i.e., residual variance). The Estimate column lists is the ML point estimate of each parameter. The Std.Err column gives the standard error for each estimate (where these are computed using the expected information matrix, as noted above). Next, the z-value column reports the Wald z-statistic for the null hypothesis test that the parameter is significantly different from zero in the population, and the P(>|z|) column reports the p-value associated with this z-statistic.
				- Here, we see that the average **non-COA has a score of .298** on peer and the average **COA** has a score that is .176 units higher than non-COAs on peer (**.298 + .176 = .474**). Both the intercept and slope are significantly different from zero. Finally, the **variance** in deviant peer association that is **not explained by COA status is .280**. This indicates that, although COA status is a significant predictor of peer, COA status does not fully account for affiliation with peers.
			- *Standardization*
				- Because peer is not on an intrinsically meaningful scale, we cannot easily interpret the differences among the regression parameters or residual variances. To better interpret these results, we can request **standardized estimates**. Within lavaan, several methods of standardization are available within the summary function. The first type, obtained by including **standardized=TRUE**, is the typical fully standardized solution. In this case, **both the independent and dependent variables are standardized to have a variance of 1** (note that lavaan does **not**, however, also **make the means 0**, as one might expect). 
				- The **Std.lv** column refers to a solution in which **only the latent variables are standardized and not the observed variables**. Since the current model contains no latent variables, this is of little use here. The **Std.all** column contains the fully standardized estimates of interest, in which all variables (observed and latent) are standardized to have a variance of one. Thus, we say that a one standard deviation increase in COA status is associated with a .164 standard deviation increase in deviant peer associations.
				- It may be more useful to retain the original scaling of COA while standardizing peer. If we include **std.nox=TRUE** in the summary function, as shown below, we will obtain estimates in which the latent variables and endogenous observed variables are standardized but the exogenous observed variables are left in their raw scale. These are commonly known as partially standardized estimates.
			- R Square
				- Finally, we can also calculate how much variance is explained in peer by coa by requesting that lavaan output the r-squared statistic. **R-Square** is the estimated **proportion of variance** in peer that **is accounted for by the models** (i.e., COA, the only predictor included in this model). We have explained less than 3% of the total variance in peer with the COA predictor. Note, however, that measured variable regression models assume that no measurement error is present. If measurement error is present, the estimated relationship among the variables in the model may be attenuated and the R 2 value will also be underestimated.
	3. Multiple Regression
		- ![[Pasted image 20230715203139.png|300]]  peer = α + γ1coa + γ 2gen + γ 3age + ζ 
		- R code
			- ![[Pasted image 20230715204117.png|700]] 
			- we have specified that peer is regression on coa, gen, and age. Note that, again, we use the **regression operator ~** to indicate the regression. Now that our model includes multiple predictors, we use the + operator in between each predictor.
		- Results
			- ![[Pasted image 20230715204221.png|400]] ![[Pasted image 20230715205803.png|500]] 
		- Interpretation
			- We see that gen is not a significant predictor of peer when COA and age are also included in the model (p = .381). However, age is significantly related with peer such that older adolescents are more likely to associate with deviant peers. We estimate that a one-year increase in age is associated with a .151-increase in deviant peer association ratings. COA remains a significant predictor of peer, and the regression parameter **estimate (i.e., it has increased from .18 to .21) has not changed much** from the single-predictor model to the multiple-predictor model **relative to its standard error (0.06)**. The **stability** of this coefficient **reflects** the fact that **COA is not highly correlated with gen or age**.
			- To better interpret these results, and to get a sense for the relative contribution of each predictor, we requested the **partially standardized solution**. We prefer this method of standardization for this example because **all three predictors have natural scales**. As can be seen in the Std.nox column of output, after controlling for age and gender, COAs affiliate with deviant peers about .391 standard deviation units more than non-COAs. Each additional year of age is associated with a .281 standard deviation increase in self-reported affiliation with deviant peers.
			- From the R-square output, we can see that the multiple predictor regression model explains more of the variance in peer than the single predictor model. Age and gender account for an additional 17% of the variance in peer, over and above COA status. Still, approximately **80% of the variance in peer remains unexplained by the variables in our model**.
			- how much was each of these contributing to r square? Coa is contributing 3 % of that explained variance. Age is contributing, 16 % of that explained variance, and gender is contributing virtually nothing. sum those unique values up, not equal, to overall R squared, because the *overall R* squared is also going to *pick up joint effects*. Right? Remember, these are the unique effects. 

### 2. Path Analysis
#### 2.0 Six Steps
1. **Specification**: What is the model? Predictors? Outcomes? Mediators? Factors?
	- Use **Path Diagrams** for specification
2. **Identification**: possible to obtain all model parameter estimates?
	- *Over-identified*: there is *more observed* information *than* the number of parameters *to be estimated*. If we observed 20 variances and covariance and means we're only estimating 15parameters that is an over identified model because *we're imposing restrictions* on the model. 
	- *Just-identified*: there is the same amount of observed information as the number of parameters to be estimated. this is always the case for the multiple regression model. all predictors predicted the dependent variable and all predictors are correlated. You are imposing no restrictions. 
	- *degree of freedom* is going to *represent* a *restriction*. Regression have no degrees of freedom. our covariance matrix we observed is always equal to the covariance matrix that's implied by the model
	- *Under-identified*: there is less observed information than the number of parameters to be estimated.
	- Rules
		- necessary rules: they have to be satisfied to establish that your model is identified, but they don't on their own established identification
			- the **t-rule**: k=(p+q)(p+q+1)2+(p+q), p-endogenous and q-exogenous variables. for t estimated parameters in theta, the value of t must be less than or equal to k. the differences between t and k is the degree of freedom.
		- Sufficient rules:  if you meet them, your model is for sure identified
			- the **Null B rule**: yi=α+Byi+Γxi+ζi, when **B**=0, there is no relations among the DVs. Sufficient
			- the **recursive rule**: no feedback or bi-directional effects, no correlated residuals. Sufficient but not necessary.
		- the **common sense rule**
			- Example: ![[Pasted image 20230718034811.png|300]]
			- This model implies three forms of relation between the endogenous variables, yet only one covariance is observed
3. **Estimation**: How to obtain best estimates. 
	- **Properties** for estimator
		- *unbiased*: if we were to repeat our study an infinite number of times, the mean of the sample estimates would equal the population value
		- *consistent*: as the sample size approaches infinity, the sample estimate approaches the population values. Is it a consistent estimator where the answer gets better at as the sample size gets bigger
		- *efficient*: no other estimator has a smaller sampling error for the estimate. you're gonna have the most precise estimates you can possibly have given your sample size at hand
	- **OLS** ordinary least square is an unbiased, consistent and efficient estimator under the usual assumptions. But it doesn't extend well to a lot of more complicated models.
		- The idea was we *define this loss function* in terms of the *observed and the predicted values* of y and we want to get those as closest possible to one another so that our residuals are really tiny. Our predicted values are as close as they can be to the observer values. 
		- OLS do *t tests* for parameter test. We're dealing with degrees of freedom, maximum likelihood throw degrees of freedom out the window
	- **ML** is asymptotically unbiased, consistent, and maximally efficient: mixture model and logistic regression use ML ^ML-intro
		- Maximum likelihood is based on a little bit different conceptualization of fit is we *define what is the distribution* of our data that gives us the likelihood. Then we try to find the parameters for that distribution. Think of a normal distribution. It's got means it's got variances, it's got covariance as we try to find the parameters. They're gonna *make that distribution produce* that data *as closely as possible*. We want a distribution. We want a likelihood that's gonna be as high as it can be for the that we choose the parameter estimates. It's the most common estimator used to fit structural equation models. It's a flexible estimate. It's using a variety of other contexts. *Logistic regression*, all kinds of models are fit using maximum likelihood because it is a very general approach to estimation. a *combination of maximum likelihood* estimates *is* itself a *maximum* likelihood estimate
		- ![[Pasted image 20230716094738.png|300]] 
		- If you use maximum likelihood to fit the regression model, you get the exact *same* estimates for the *regression coefficients*, *not* so much the *residual variance*. It's a very different approach to model estimation, but it gives you the same answer. However, it allows you to extend to more complex models. 
		- how likely you would observe the data at hand if those were the true parameter values in the population. 
		- **Two general approaches**
			- Sufficient-statistic ML (SSML): estimation is based on the observed covariance matrix and mean vector
				- assume *complete*-case data and *normally* distributed *dependent* variables
					- note that the assumption of continuous and normal distributions applies only to the dependent variables in the model, not the independent (or predictor) variables. For various reasons, some historical and others practical, the SEM was first formulated assuming using joint multivariate normality for all IVs and DVs. However, under broad conditions, this joint assumption of normality yields the same maximum likelihood estimates as the assumption of normality applied to just the DVs, even when the IVs are not normally distributed
			- Full-information ML (FIML): estimation is based on whatever data are observed for each individual case
				- allow for partially missing data and alternative methods for addressing non-normal distributions and nested data structures. For complete and normal data, SSML and FIML are identical
		- **Advantages** of ML
			- can be used to fit a wide variety of models
			- ML is asymptotically unbiased, consistent, and maximally efficient
			- estimates are asymptotically normal distributed, providing basis for inference tests
			- combinations of ML estimates can be compared using likelihood ratio tests (chi-square difference tests)
			- FIML can accommodate *partially missing* and non-normal data
				- ![[Pasted image 20230716192740.png|200]] 
				- we've got that sigma theta hat, we're trying to figure out what parameter estimates for theta are gonna make this covariance matrix optimal for producing data that looks like this. 
				- this person is *missing a data point*. What we do is we say, what does this sigma theta hat look like? It's gonna be a 4 by 4 covariance matrix. when I calculate the *likelihood* for *this individual* is i'm just gonna *knock out that second row and second column* where that missing data is. i'm only gonna *evaluate* this data against the *3 by 3 matrix* for y one, x one, and x two. It's taking whatever data is there and making the most of the available data in terms of trying to identify what values of theta hat are gonna be optimal for that data.
		- **Steps** of ML
			- *start values*: initial values for parameter estimates selected
			- *iteration*: the likelihood computed and estimates updated
			- *converge*: the likelihood computed again, and this continues until difference between two successive likelihood values is sufficiently small
			- Fit statistics, parameter estimates, and standard errors retained from final step
			- *Z test* in ML
				- Z test on our model parameters. Z distribution is a standard normal curve, that standard normal curve comes out of maximum likelihood theory's usual assumptions. Our parameter estimates will have normal sampling distributions. 
	- all of *statistics* is essentially taking a *sample* and generating *estimates* with which to make inferences *to the population*
4. **Evaluation**: How well does the model fit the data 
	- How well does the **model fit** the data
		- To evaluate fit, we first define our null hypothesis
			- ![[Pasted image 20230716195318.png|250]] 
			- this is a *different* notion of *“fit”* *than* what is captured by *R2* (which measures strength of prediction). Here we are solely concerned with reproducing the values of the means, variances, and covariances of y and x, regardless of the strength of prediction. Of course, both aspects of fit are important and should be considered when evaluating the model.
			- In linear regression model, this it is always true that S=𝛴($\hat{\theta}$)  m=𝞵($\hat\theta$). **Regressions are just-identified**, uses the same number of parameters to exactly reproduce the observed moments. So the model necessarily fits perfectly and is said to be **saturated**. Most SEMs, are over-identified, resulting testable restrictions on model-implied moments.
	- Which **estimates** are **significant** 
		- Tests of individual parameters: z=$\hat\theta \over SE_{\hat\theta}$
			- ![[Pasted image 20230716201639.png|80]]
			- This z-test is the large sample equivalent of the t-test that is commonly implemented when fitting regression models via OLS. The t-distribution converges to the z-distribution as N increases and become functionally indistinguishable at about 25 degrees of freedom. Likewise, the z-type confidence interval is the large sample equivalent of the t-type confidence interval.
		- Joint parameter tests
			- ![[Pasted image 20230716201559.png|100]] two tests could be used
			1. *multivariate walled test*. Sometimes it's referred to as a contrast, and that would give us the kind of *large sample equivalent* to the *F test* were used to in ordinary least squares. It's  a *chi square* as opposed to an a F test, just like we have a z instead of a t.
			2. *likelihood ratio test*, *also* yields a *chi square*. But just to keep you confused is the multivariate walled chi square and the likelihood ratio test chi square *aren't identical*. They're usually really close to one another, but they're not exactly the same numbers. And each one is a legitimate way to test this null hypothesis. *Either* of those, you *could construe* as equivalent to the test of multiple *R square*. If both of these are simultaneously zero, then your r square is zero. Right? Nothing to see here.
	- How well can I predict the outcome
	- Some **index** ^evaluation-index
		- There is *not one clear* and *universally accepted* strategy for assessing the adequacy of fit of SEMs. Further, no "golden rules" about cut-offs for fit indices that will show a good fitting model.
		- The model part is, by definition, it is a simplified representation of a more complicated entity. By definition, all models are wrong. What that means is is your model is wrong, my model is wrong, all our models are wrong, which means that even if we have a tiny miss specification, we're gonna identify that and reject the null hypothesis if we have a sufficiently large sample. If you have a small sample size, you're not able to detect differences. In the observed in the reproduce covariance, you actually have an advantage for having low power, because you don't have the ability to reject the null.  just keep an eye on it. What we do is we always report the chi square. So in your work, please always report the chi square of the degrees of freedom and the p value, because that's the foundation of everything that's going to come from here. 
		- **R square**: variance explained by the model
		- **Likelihood Ration Test (LRT)**: Also called Chi-Square Test. Compare with the saturated model which impose no restrictions on means or covariances. non-significant means the tested model is good. Poorly fitting model can be accepted because there is insufficient power to detect the misspecification. **Used for nested model comparison**.
			- The *likelihood ratio* (or "chi-square") test statistic, in a *sample statistic*, is denoted as *T* that reflects fit of ==hypothesized== model relative ==to saturated== model. T is distributed as a *central chi-square* (*expected value* of a central chi square is *equal to* the *degrees of freedom*) with df=k-t. k is total number of moments and t is number of estimated parameters. This is often called the "model chi-square". Follow a non-central chi-square under alternative model. As the *model* becomes *miss-specified*, the T gets larger and larger with respect to the degrees of freedom, and that numerator gets bigger and bigger, that is called the non centrality parameter. 
			- The chi-square value less than 2-times of degrees of freedom means good fit
			- significant T-statistic indicates it is improbable that test statistic of this value or larger would be found if null true, we reject the null, and thus reject the hypothesized model
			- non-significant T-statistics indicates fail to reject the hypothesized model
		- **Chi-Square Test and LRT**
			- Yes, both the Chi-square statistic in a Chi-square test and the test statistic in a Likelihood Ratio Test (LRT) can follow a Chi-square distribution, but they are used in different contexts and derived from different types of data and hypotheses.
			1. **Chi-square Statistic in a Chi-square Test**:
				- **Context**: Used primarily for categorical data.
				- **Purpose**: Applied to test for independence in contingency tables or for goodness-of-fit to see how well an observed distribution matches an expected distribution.
				- **Calculation**: The Chi-square statistic is calculated as $\chi^2 = \sum \frac{(O - E)^2}{E}$, where O is the observed frequency and E is the expected frequency.
				- **Distribution**: This statistic follows a Chi-square distribution. The degrees of freedom are usually determined by the number of categories in the data minus one (or more, depending on the specific test and its setup).
			2. **Test Statistic in a Likelihood Ratio Test (LRT)**:
				  - **Context**: Used in comparing nested statistical models.
				  - **Purpose**: To compare the goodness of fit between a simpler (null) model and a more complex (alternative) model.
				  - **Calculation**: The test statistic for LRT is calculated as $D = -2 \ln(\frac{\text{Likelihood of simpler model}}{\text{Likelihood of more complex model}})$.
				  - **Distribution**: Under certain conditions, the test statistic D follows a Chi-square distribution. The degrees of freedom for this distribution are typically the difference in the number of parameters between the two models.
			- **Both Follow Chi-square Distribution**: In both cases, the test statistic can be chi-square distributed, but they are used for different types of hypotheses and analyses. The Chi-square test is more direct in its application to categorical data, while the LRT involves a comparison of model likelihoods and is often used in more complex statistical modeling scenarios.
			- **Different Contexts and Calculations**: The way these statistics are calculated and the types of questions they are used to answer are quite different, reflecting the diverse applications of the Chi-square distribution in statistical testing.
		- **Relative Goodness of Fit Indices**: improvement in hypothesized model *compared to baseline model*  
			- The *baseline* model includes a mean and variance for all measured variables, but assumes *all covariances* to be *zero*. The baseline model is *highly restricted*.
			- No formal statistical tests of these. We *can't* derive a sampling *distribution* for the difference of these distributions, can't derive about sampling distribution of the goodness of fit indices. 
			- T-statistic and df for hypothesized model as $T_h$ and $df_h$, for baseline model is $T_b$ and $df_b$ 
				- ![[Pasted image 20230719042041.png|400]]
			- *TLI,CFI, IFI >0.95 is good*. 
		- **Absolute** Goodness of Fit Indices: 
			- **RMSEA** root mean squared error of approximation, model misfit in a metric of per degree of freedom in the likelihood itself. (*≤ 0.05* is excellent; ≤ 0.08 moderate fit; *>1.0* is poor). 
				- ![[Pasted image 20230719043503.png|150]] 
				- the non centrality parameter that's adjusted for degrees of freedom.
				- Although its *distribution* can be *constructed*, the *cut-points* are *no better* informed than those used for the relative fit indices. in some models, . 11 indicates good fit. In other models, . 02 indicates bad fit. It depends on model complexity degrees of freedom, sample size.
			- **SRMR** Standardized Root Mean Square Residual : difference between the observed and model-implied covariance matrices in a standardized metric (≤ *.08 is good*, not penalized for the number of model parameters, so tends to be better for less restricted models).
		- any reasonable sample size with any reasonable model. Your chi square is almost always gonna be significant unless you are not imposing restrictions
5. **Potential re-specification**: Can the model be improved? How are modifications identified
	- *First* consider modifications with respect to *theory*, *then* describe methods for letting sample *data guide* our decisions
	- *Nested model*: can be derived from restrict or relax. Models are not nested if the simpler model has both restrictions and additions relative to the comparison model
		- ![[Pasted image 20230719075641.png|500]] 
		- the non-significant LRT means the additional parameters of Model B do not significantly improve the fit of the model and we should retain Model A
		- Likelihood ratio test for nested models
	- *Non-nested* model
		- Information criteria takes the model -2 log-likelihood and impose a penalty related to number of model parameters to *reward parsimony*.
			- Akaike information criterion AIC
			- Bayes information criterion BIC
			- usually scaled so that the best model is the one with the lowest value for the information criterion
	- **Modification Indices (MIs)**: expected change (based on model derivatives not actual likelihood ratio tests. but very close estimates). Calculated for every parameter that is restricted. Take one at a time, entirely data driven
		- a given misspecification in model might appear in multiple places via MIs, but not known where "true" misspecification resides
		- parameters should only be freed based on an MI if it is reasonable and fully justified by theory. Modifications based on MIs should be fully described to a reader
6. **Interpretation**: Which effects are significant? Which are substantively meaningful?
	- Raw parameter estimates
	- Standardized parameter estimates
	- R square, explained variance in outcomes
#### 2.1 Moments Structure
- **θ**
	- ![](https://github.com/crystalbell98/Notes/blob/main/content/docs/figure/Pasted%20image%2020230113174234.png)
	- all theta does is holds our model. Again, imagine a bookshelf. One book is your intercept. The next book is your first regression coefficient, the next book is your second regression coefficient. Theta is gonna be a storage system for our model. We're gonna put whatever our model is in the theta. The variance of zeta there is psi.
	- When we start to build *more complicated* models, none of what we're gonna talk about is gonna change. It's *just theta gets longer*. In the path analysis model, we're gonna have more psi and more alpha. 
- **Moments** in multivariate model and SEM
	- A multivariate distribution can be defined by the first four moments of the distribution. The **first moment** or is the *mean*. The **second moment** is the *variance*, the **third moment** is *skewness*, and the **4th moment** is *kurtosis*. In SEM, we use first two moments. 
	- **Population moments** are *𝛴 and 𝞵*, 
	- **sample moments** are *S and m*, 
	- population **model-implied moments** are *Σ(θ) and μ(θ)*
		- Model-Implied Moments: Model is a **set of parameters**. Population Moments include **means and covariance**. Model-Implied Moments is moment matrix implied by the model, which is similar to y and ŷ. can each parameter be uniquely expressed using observed information? Extent to which there is sufficient known information to infer unknown values.
#### 2.2 Path Tracing
- **Rules**
	- Leave from and return to a variable to reconstruct the variance
	- Leave one variable and travel to another to reconstruct the covariance
	- Rule 1: When you *begin* a trace *backward* from a variable using a single headed arrow, you can *proceed backward any number* of times; upon reaching a variable, you can do two things
		- Span a double-headed arrow and stop
		- Span a double-headed arrow and proceed the trace forward
	- Rule 2: Once you *start forward* you may move *forward any number* of times but, after moving forward you may *not move backwards* or span *a double-headed arrow*.
	- Rule 3: For any given trace you can only pass through a variable once: thus *no loops* are allowed
	- For means: begin at the triangle, can only move forward, and cannot span a double-headed arrow
- Example
	- **One predictor regression**
		- ![[Pasted image 20230716073328.png|300]]
			- ![[Pasted image 20230716073351.png|100]] we start at x and cross the span back to x
			- ![[Pasted image 20230716073408.png|130]] we start at y. trace backwards, and span the double-headed arrow of x
			- ![[Pasted image 20230716073437.png|300]] we start at y, trace backwards and span the double-headed arrow of x and return whence we came; to this we add the residual trace. This first term is the explained variance, the second is the residual variance, and the sum is the total variance.
			- ![[Pasted image 20230716074442.png|100]] ![[Pasted image 20230716074457.png|150]] 
			- Remember what I promised you is for all predictors. The model implied moments just take on their values variances. Covariance is means because we're not imposing anything on it. 
	- **Two predictors regression**
		- ![[Pasted image 20230716081128.png|300]]
			- ![[Pasted image 20230716081217.png|150]] from x1 to x2
			- ![[Pasted image 20230716081312.png|200]] 
			- ![[Pasted image 20230716081403.png|300]] 
				- ![[Pasted image 20230716081423.png|300]]
- complex for advanced SEM. Fortunately, the matrix gives these all-in-one expression. The advantage of tracing rules is to *help establish model identification*
#### 2.3 Path Analysis Models
- **Definition**
	- Typically, path models are not gonna be saturated. That means they are not going to fit the sample data perfectly, which means we're gonna have to say how much misfit are we gonna be comfortable with? Path analysis model is a generalization of multiple regression
	- *Other Name*: Simultaneous equation models, SEMs with observed measures
	- *Exogenous* variable: a variable that is not expressed as a function of other variable; its causes are "outside" of the system
	- *Endogenous* variable: a variable that is expressed as a function of one or more other variables; its causes are "within" the system
	- *Disturbance*: the *residual*. unexplained variance of an endogenous variable. the part that is unrelated to the predictors.
	- *Recursive* model: no correlated residuals and only unidirectional effects
		- ![[Pasted image 20230717070534.png|300]]
	- *non-recursive* model: correlated residuals and/or feedback loops (eg. bi-directional effects)
		- ![[Pasted image 20230717070720.png|400]] 
		- ![[Pasted image 20230717070741.png|400]]
		- ![[Pasted image 20230717070802.png|400]] 
		- 
##### 2.3.1 General model
![[Pasted image 20230718002406.png|800]] ![[Pasted image 20230718003454.png|50]]
##### 2.3.2 Simple Mediator model
Mediator explains *why and how* one variable exerts an *effect on another*
1. Example for formula and variance covariance
	- ![[Pasted image 20230718003904.png|400]]
	- we're imposing *restriction* on *x2 to y2*
	- four-by-four model-implied covariance matrix
		- ![[Pasted image 20230718004531.png|300]] 
			- Through path tracing we can know
				- ![[Pasted image 20230718004730.png|300]] 
			- matrix value function
				- ![[Pasted image 20230718005335.png|300]] 
2. Example of model improvement
	- ![[Pasted image 20230718045014.png]] ![[Pasted image 20230721200657.png|400]] 
	- **Poor Model Fit**
		- ![[Pasted image 20230721053008.png|300]]
		- ![[Pasted image 20230721195737.png|400]] 
			- As a **default**, lavaan allows all exogenous variables to covary but it fixes the residual **covariances among endogenous variables to zero**. The residual terms of stress and emotion are freed to covary within the section of the code marked covariances. To designate a covariance (or variance) we use the ~~ operator. Thus, **stress ~~ emotion** tells lavaan to include a residual covariance for stress and emotion.
		- `summary(fit.1, fit.measures=TRUE)`
		- ![[Pasted image 20230721201004.png|400]] 
			- this LRT reject the null hypothesis, means that the model not fits the data.
		- ![[Pasted image 20230721202434.png|400]] 
			- the CFI and the TLI are far lower than .9, the standard lower bound for a good-fitting model. Finally, the 90% confidence interval for the RMSEA does not even include .10 at the lower bound, indicating terrible fit. As such, we cannot interpret the obtained parameter estimates with any confidence given the severe misfit of the model.
	- Do we say our ideological mechanisms have been *verified* by this model *?* *No*, not at all. 
		1. First, *not* yet *established* this *is* a *good* model. This could be an atrocious model for the data, in which case we really wouldn't put much stock in whether these effects are significant or not. 
		2. Any given *set of links* in the chain is significant is *not the sam*e thing as establishing that the *entire chain* is significant. we can test that entire chain of effects by computing and testing the full indirect effect, as opposed to each little part of that chain along the way. 
	- Evaluate the model
		- *Raw metric of covariates*, will be influence by the measurement scaler
			- ![[Pasted image 20230718063054.png|400]]
		- *Standardized* between model implied covariance and observed
			- The normalized residuals are rescaled to follow a standard normal distribution. Values exceeding ±2 indicate a large discrepancy
			- ![[Pasted image 20230718063311.png|400]]
			- *zero* in here. there are *no restrictions* on what those covariance is could look like in our model. Right? There's nothing testable about those associations in our model. 
			- ![[Pasted image 20230721204347.png|400]] 
				- request the **model-implied covariance matrix (fitted(fit))** and the **raw and standardized residual matrices** (resid(fit, type=“raw”) and resid(fit, type=“normalized”), respectively). These residuals represent the differences between the observed covariance matrix and the matrix that is implied by the structure of the model.
		- **Modification Indices**
			- ![[Pasted image 20230721053055.png|300]] 
				- x on y means regressions; x with y means covariance
				- Most reasonable *first* step is to free regression of *peer on age*. Then re-estimate the model. Here we *don't consider* the *covariance* because. correlating *coa with the residual of peer*, is that's a highly *atypical parameter*. but one of the assumptions is our residual terms are independent of our predictors. And this would be, in this particular model, a nonsensical parameter. Is that's why is we would be *correlating* an *exogenous* variable with a *disturbance* that is an atypical and very *difficult to defend* parameter, because our restrictions were focused on the regression coefficients. That's what we're going to add from the modification indices. 
			- ![[Pasted image 20230721202726.png|400]]
			- ![[Pasted image 20230721202748.png|400]]
				- Note the overlap in suggested modification indices. This tells us that our original model does not allow for a significant relation between **age** and **negaff** or between **age** and **peer**. These suggestions are not independent from one another; allowing **negaff** to relate directly with **age** would imply an increased correlation between **negaff** and **peer**.
			- ![[Pasted image 20230721053230.png|150]] 
				- MI predicted model LRT would be 81.17-42.54=38.63 and the actual value was 34.37. *MI* was a *good* but *not exact*, estimate of the LRT.
				- ![[Pasted image 20230721203128.png|200]] 
					- ![[Pasted image 20230721203222.png|300]] 
					- ![[Pasted image 20230721203240.png|200]] 
					- including age as a predictor of deviant peer affiliation has significantly improved the fit of the model. However, the relative model fit is still poor. We can again examine the modification indices to determine whether a justifiable model modification would lead to further improvements in model fit.
			- ![[Pasted image 20230721053550.png|250]]  
				- free restriction: regression of peer on coa
			- ![[Pasted image 20230721053734.png|300]]
				- free restriction: age on negaff
	- Final Model
		- ![[Pasted image 20230721105054.png|400]] 
3. Mediation test with final verified model
	- **type of effects**
		- *total effects*: sum of all possible paths
		- *total indirect effects*: sum of all possible indirect paths leading from predictor to outcome
		- *specific indirect effects*: any single indirect path leading from predictor to outcome
	- **point estimate**
		- ![[Pasted image 20230721105921.png|200]]
		- The direct effect is simply e
		- the first specific indirect effect is the *product of a and b*
		- the second specific indirect effect is the product of c and d
		- the total indirect effect is the sum of the two specific indirect effects
		- the total effect is the sum of the total indirect effect & the direct effect
	- **confidence interval**
		- *Delta method shortages*
			- only a first order taylor series *approximation* to get the standard error and SEs can be *inexact*
			- we make this into a z statistic, *assumes* indirect effects have *normal sampling distributions* but this is typically not the case
			- basing inferential test on traditional critical ratio *assumes symmetric sampling distribution* that is also typically not the case
		- **Bootstrap method**
			- *advantages*
				- not assume normality of sampling distribution and allows for asymmetric CIs, and can be applied in many different circumstances
				- bootstrap CIs are considered the gold standard for testing indirect effects and should be used in practice when possible
			- *disadvantages*
				- computationally intensive fitting hundreds or thousands of individual models
				- each individually fitted model can encounter its own estimation problems
				- in many cases, virtually no difference between bootstrap and delta tests
			- treat my original sample as the population and i'm gonna *re-sample data* from it *with replacement*. We'll do that *1,000 times* and fit the model to those redrawn samples. Each time we fit the model, we're gonna retain the indirect effect estimate. and then we're gonna arrange the distribution of those indirect effect estimates. We could just calculate a histogram. What does this histogram look for? Those indirect effect estimates? That's gonna give us an *empirical sampling distribution*. We're not gonna have to draw on any analytic theory to say the sampling distribution looks like a chi square. The sampling distribution looks like an f for t or z or whatever. Instead, we just say that's what it looks like. That's the sampling distribution. 
			- *percentile method*
				- And we identify the particular estimate that falls at the, let's say, the 2.5th percentile, and the 97.5th percentile. 
				- why a 1000? Because then 25 and 975 are whole numbers. And so we can just sort our data and pick out the 25th and the nine hundred and seventy fifth estimate in that sort of distribution. And those will be our 2.5th and 97.5 percentiles. 
				- values could vary based on software and random number seed
			- *standard error method*
				- could take the standard deviation of that empirical distribution to serve as your standard error, and calculate a critical ratio and reference that to a z test.
				- Don't use this, use the percentile method because the confidence intervals are asymmetric. Whereas the z test assumes a nice, normal curve. 
	- final model example
		- ![[Pasted image 20230721105054.png|400]]
		- pathway for mediator effect
			- ![[Pasted image 20230721112507.png|400]] 
			- ![[Pasted image 20230721112530.png|400]]
			- ![[Pasted image 20230721112606.png|400]] 
			- ![[Pasted image 20230721112635.png|400]] 
		- R code
			- ![[Pasted image 20230721225809.png|400]] 
				- What’s new here is that we’ve **added parameter labels** for the paths involved in the *direct and indirect effects* of **coa** on **peer**. For instance, in the line stress ~ c_s* coa + gen + age, we have supplied the label c_s for the effect of **coa** on **stress**. Likewise, the other paths involved in computing the effects of interest have also been labeled. To help keep track of things, our labels consist of the first letter of the predictor, an underscore, and first letter of outcome, but any labels are fine. We can now refer to these labels when defining direct, indirect, and total effects.
				- Following the core model specification, we have new lines to define the direct, specific indirect, total indirect, and total effects. This is done using the *“define” operator* **:=**. For instance, ind_s := c_s* s_n* n_p requests that lavvan compute the quantity ind_s as the product of the three paths previously labeled c_s, s_n, and n_p.
				- If we were to fit this model using the **default** options, lavaan would generate point estimates for all of the newly defined effects as well as *delta-method* standard errors. As we noted in lecture, however, the current best practices is to conduct inferential tests of indirect effects using bootstrapped confidence intervals. Fortunately, it is straightforward to compute these using lavaan.
			- ![[Pasted image 20230721230154.png|400]] 
				- Then, in the sem function, we specified se="bootstrap", bootstrap=1000 to request that lavaan compute bootstrapped standard errors with 1000 bootstrapped samples. We actually don’t care much about the standard errors. What we really *want* are *bootstrapped confidence intervals*, which are generated in the *parameterEstimates function* with the *boot.ci.type argument*. The parameterEstimates function produces a simple list of the parameter estimates from the model. By including the boot.ci.type argument, we request that this output include 95% boostrapped confidence intervals.
				- Note that there exist multiple methods for calculating bootrapped CIs. The **percentile method** is probably easiest to understand – the 1000 boostrapped estimates are ordered by magnitude and the 25 thestimate (2.5 thpercentile) and 975 thestimate (97.5 thpercentile) are taken as the confidence limits, yielding a 95% confidence interval. This method, which is widely available in many software programs, is obtained via *boot.ci.type = "perc"*. That is the method we used in the lecture notes. A slightly *preferable approach*, however, is to use **bias-corrected bootstrapped confidence** intervals, and these are readily available in lavaan. To obtain the bias- corrected confidence intervals, we simply use *boot.ci.type = "bca.simple"*. The bias- corrected intervals are shown in the output below. In terms of null hypothesis testing, the same conclusions are generated with the bias-corrected CIs as with the percentile CIs presented in lecture, but there are some slight differences in the specific values of the confidence limits.
			- ![[Pasted image 20230721230748.png|500]] 
				- The total effect of **coa** on **peer** is equal to .209 and represents a combination of the direct effect (.185) and the total indirect effect (.024). The 95% CI is equal to .094 and .306; because this does not contain zero, the total effect is deemed to be significant.
				- Examining the mediational pathways, we see that the specific indirect effect **coa**→**stress**→**negaff**→**peer**, labeled ind_s to indicate it is the indirect effect through **stress**, is equal to .015 (95% CI=.005, .036) and is significant (does not include zero). The biological pathway from **coa**→**emotion**→**negaff**→**peer**, labeled ind_e to indicate it is the indirect effect through **emotion**, is equal to .009 (95% CI=0, .022) and thus does not reach statistical significance (because the lower CI is equal to zero).
#### 2.4 Assumptions
##### 2.4.1 Assumptions of maximum likelihood estimation
1. Sufficiently **large sample size**
	1. ML is derived under *asymptotic* conditions and *assumes infinite* sample *sizes*
		1. we need large sample size *to* obtain a properly *converged* solution and stable sample estimates. small sample size can lead to problems in optimization, non-positive definite matrices
		2. we need a large sample size *to* ensure that the test statistic *follows* the *assumed* probability *distribution*. Small sample size can result in inflated test statistics and increased Type 1 error
	2. how large is large enough is inherently unknowable, so we strive to obtain as large a sample as is reasonably possible. Sufficient sample size can depend on things such as quality of measurement and complexity of the model.
2. **Independence of residuals**
	1. No two residuals any more or less similar than any other two. Hierarchical nesting of multiple children within a classroom or multiple time points nested within an individual
	2. when violated, both test statistics and standard errors can be biased. It is difficult to disaggregate between- and within-group effects
	3. need multilevel analysis or growth models
3. **Multivariate normality of residuals**
	1. In regression: *conditional normality*: residuals assumed normally distributed and it is the distribution of the dependent variable conditioned on the predictors, but no distribution assumptions made about exogenous variables
	2. In *path model*, it is *multivariate* because there are *multiple endogenous variables*
	3. ML likelihood is derived under multivariate normality
		1. It only considers the first two distributional moments: the mean vector and the covariance matrix
	4. Often *difficult* to unambiguously determine *when* data are *sufficiently non-normal* to be of *concern*
	5. One challenge is that *univariate* normality is necessary but *not* sufficient to *infer multivariate* normality
	6. Another challenge is that, although there are numerical *tests* for univariate and multivariate normality, these are often *over-powered* and almost always identify non-normality
	7. Often, though not definitive, careful *graphical analysis* can be most useful when examining distributions of dependent variables
	8. two issues
		1. *not* make distributional *assumptions* about *exogenous* variables
		2. *if* the *residuals* are continuous but *non-normal*, two problems
			1. the likelihood ratio test statistic is too large, thus increasing the likelihood of *falsely rejecting a correct null*. conclude the *model* is incorrect when the model is correct.
			2. the standard errors of the *parameters* are too small, thus increasing the likelihood of *falsely rejecting a correct null*. conclude there is an effect when there is no effect.
4. Missing data are missing at random
	1. Missing completely at random MCAR: any missing case is strictly random and unrelated to any other variables in or out of the model
	2. Missing at random MAR: any missing case can be related to variables in the model, but not to variables omitted from the model
	3. Missing not at random MNAR: any missing case is related to variables that are omitted from the model
	4. Raw-data ML assumes MAR which subsumes MCAR
	5. much more complex approaches are needed for MNAR. It is likely that most data structures in the behavioral sciences are MAR, so this is not an unreasonable assumption to invoke
##### 2.4.2 Assumptions of the path analysis model itself
5. two additional key assumptions underlying the path model itself
	1. **Linearity** among the observed measures
		1. we assume that all relations among observed measures are linear in form
		2. non-linear relationship could be multiplicative interactions or quadratic effects
		3. violation of this assumption leads to a misspecified model
		4. for discrete observed variables (binary or ordinal), whose relationships are intrinsically nonlinear. We must consider alternative approaches for specifying and estimating nonlinear SEMs
	2. **Perfect reliability**
		1. assume all observed variables measured without error. all observed variance is true variance to be modeled
		2. within behavioral, health, social sciences, this assumption is absurd. most constructs assessed with some degree of measurement error
		3. both regression and path analysis models assume all observed variance to be true variability of the construct
		4. two rather insidious problems
			1. an estimated regression *coefficient is* bounded as *function of reliability* of predictor
				1. $y_i=\hat\alpha + \hat\gamma_1 x_i+\hat\varsigma_i$ 
				2. population reliability of the exogenous variable as $\rho$.
					1. reliability=${true\space score\space variance} \over {the \space total \space variance}$
					2. Thus, reliability can only equal one when there is no error variance
				3. $E(\hat\gamma_1)=\gamma_1\rho$ 
					1. On average, sample estimate is limited to the product of the population coefficient and the reliability of the exogenous predictor
					2. Sometimes called *attenuation due to unreliability*
				4. ways to avoid attenuation
					1. use perfectly reliable predictors, but this is unrealistic
					2. correct for unreliability by *fixing residual variance to some estimate* in path model, but tends to perform poorly and is *not recommended*
					3. construct multiple indicator *latent factors* to empirically estimate and remove error variance and thus disattenuate the coefficients.
			2. We also assume perfect reliability in the endogenous or dependent variables
				1. unreliability in the endogenous variables does not bias parameter estimates, but does increase the standard errors and thus reduces statistical power


### 3. Factor Analysis
- **General Path Diagram and Equations**
	- ![[Pasted image 20231110122604.png|500]]  ![[Pasted image 20231110122629.png|700]]  ![[Pasted image 20231110122708.png|600]] ![[Pasted image 20231110122805.png|500]] ![[Pasted image 20231110122842.png|600]] ![[Pasted image 20231110123238.png|600]]   ![[Pasted image 20231110122931.png|600]] ![[Pasted image 20231110123403.png|600]]  ![[Pasted image 20231110123846.png|600]] 
- Covariance Structure Analysis
	- ![[Pasted image 20231110123652.png|700]]  
# 2. LSEM
- [Test Measurement Invariance](file:///Users/yuan/Documents/PSY_505/Logitudinal_Study/R_SEM_Example/SEM_analysis.nb.html)
## Different Types of Longitudinal Designs
Longitudinal Definition: 
- "The one sine qua non of longitudinal research is that the entity under investigation is observed repeatedly as it exists and evolves over time" 
- at least a subset of entities under investigation are observed repeatedly. And allows for missing data and single observation data   
- Development of thing or an entity that exist naturally or develop over the time. 
- Even if there is one variable that is measured repeatedly should be retained 

Cohort-by-age table (helpful to organize different designs)
- Three dimensions: Birth Year, Calendar Year, and Age. Given two you can get the third. **Cross-sectional design** is more between the subject design 
	- ![[Pasted image 20230608000113.png|320]] ![[Pasted image 20230608000138.png|400]] ![[Pasted image 20230608000221.png|350]]
		- Cross-Sectional Design confounds within- & between-person change 
			- ![[Pasted image 20230608001018.png|500]]
- Repeated Cross-Sectional Design
	- ![[Pasted image 20230623033718.png|400]]
- Single Cohort Longitudinal Design
	- ![[Pasted image 20230623033826.png|400]]
- Monitoring time trends but confounds individual and cohort development. 
	- ![[Pasted image 20230608002225.png|480]]  ![[Pasted image 20230608002337.png|600]]

## Bivariate Autoregressive Cross-Lagged Panel Models

The mean of the *outcome* ate time 2 *differs* for treatment vs. control *above-and-beyond* the effect of the *outcome measured at time 1*.

We observed the bivariate correlations and want to build a model to explain it.
![[Pasted image 20230628020607.png|500]] ![[Pasted image 20230628020631.png|500]] ![[Pasted image 20230629002354.png|500]] ![[Pasted image 20230629004138.png|500]] **Evaluation**
- **R square**: variance explained by the model
- **Chi-Square Test Statistics**: compare with the saturated model which impose no restrictions on means or covariances. non-significant means the tested model is good. Poorly fitting model can be accepted because there is insufficient power to detect the misspecification. **Used for nested model comparison**.
- Relative Goodness of Fit Indices:**TLI,CFI, IFI** **>0.95 is good**. baseline model, all mean and variance and no covariance. hypothesized model is the tested model.
- Absolute Goodness of Fit Indices: **RMSEA** (≤ **0.05 is excellent**; ≤ 0.08 moderate fit; >1.0 is poor). Standardized Root Mean Square Residual **SRMR** (≤ **.08 is good**, not penalized for the number of model parameters, so tends to be better for less restricted models).
![[Pasted image 20230629005021.png|500]] 


## The Unconditional Linear Latent Curve Model
- **Latent Factor for Intercept and Slope**
	- ![[Pasted image 20231110120940.png|400]] ![[Pasted image 20231110121245.png|400]]  ![[Pasted image 20231110121314.png|400]] ![[Pasted image 20231110121153.png|400]] 
- Latent Curve is a special type of Confirmatory Factor Analysis
	- ![[Pasted image 20231110121631.png|400]] ![[Pasted image 20231110121707.png|400]] 
		- k to indicate the number of latent factors
# 3. Applied Measurement Modeling
#### Measurement
- **Definition**
	- measurement, in the broadest sense, is defined as the assignment of numerals to objects or events according to rules
- **Motivation** for measurement modeling
	1. Developing a scale to *measure* a theoretical *construct*
	2. Understanding psychometric *properties of a scale* across person, place, or time
	3. Obtaining reliable and valid scores for *subsequent analysis*
	4. Ranking and selecting subjects on scale scores
- Construct **validity**
	- the degree to which a test measures what it claims to be measuring
	- four steps for enhancing construct validity
		1. explicate the person, setting, treatment, and outcomes of interest
		2. carefully select instances that appear to match those constructs
		3. assess the match between instances and constructs
		4. revise construct descriptions accordingly
	- We weave this into everything that we discuss about factor analysis
		- what do we believe to *exist*?
		- how do we *measure* this in a principle有原则的 *way*
		- how do we know the *measures hold* over person, place, and time?
	- establishing construct validity is a *dynamic* and *never-ending* process
- **Different scales** of measurement
	1. *Nominal*
		1. nominal denotes name, any numerical values indicate neither quantity nor order
		2. example: sex, treatment condition, race, country
		3. there are advantages to denoting groups using numbers when fitting statistical models, but these are only used as labels
	2. *Ordinal*
		1. reflect order
		2. example: 1=strongly disagree, 2=disagree, 3=agree, 4=strongly agree
		3. this poses a challenge, we know 4 is greater than 3, but we don't know how much greater
		4. Ordinal only means that the *distances between equal points* along the scale *represent unequal amounts of things*.
	3. *Interval*
		1. allowing for assessment of the distance between values
		2. assume that adjacent values are separated by equal intervals
		3. example: 32 to 33 degrees is the same amount of change as moving from 89 to 90 degree
		4. limitation: *zero does not represent the absence of construct*: zero Celsius do not represent absence of heat
	4. *Ratio*
		1. it subsumes the interval level but also *has a true zero*
		2. example: weight, height, velocity
			1. 50 degrees F=10 degrees C, and 100 degrees F=37.8 C. 100/50=2 but 37.8/10=3.78 so ratios are different because no shared absolute zero
			2. 50 lbs= 22.68kg and 100 lbs=45.36kg, so 100/50=2 and 45.36/22.68=2. thus weight is a ratio level of measurement because it has an absolute zero
- **Classical test theory** CTT (re-visit in chapter 4)
	- **reliability**: what is the extent to which an item or *score* is *consistent* across person, place, or time
		- think of standing on a scale, stepping off, and standing back on: do you obtain the same weight each time? Or is there some random error that leads to discrepancies across measurements?
	1. add up a set of items to represent the underlying construct of interest
	2. compute Coefficient Alpha to evaluate reliability of the scale score
	3. compute item-total correlations to identify "bad" items
	4. correlate the scale scores with other measures to assess validity
- **Mean** (assess central tendency) and **Variance** (assesses variability)
	- Population
		- ![[Pasted image 20230726071344.png|400]] ![[Pasted image 20230726071833.png|200]] 
	- a variance is actually the covariance of a variable with itself
	- Sample mean and variance
		- ![[Pasted image 20230726071633.png|300]] ![[Pasted image 20230726072031.png|200]] 
- **Correlation**: standardized covariance, covariance divided by the product of the standard deviations
	- ![[Pasted image 20230726072454.png|100]] ![[Pasted image 20230726072506.png|100]] 
	- ![[Pasted image 20230726072837.png|400]] ![[Pasted image 20230726072903.png|400]] 
- Great sentence
	- **_It_** **_is_** **_the_** **_faith_** **_of_** **_all_** **_science_** **_that_** **_an_** **_unlimited_** **_number_** **_of_** **_phenomena_** **_can_** **_be_** **_comprehended_** **_in_** **_terms_** **_of_** **_a_** **_limited_** **_number_** **_of_** **_concepts_** **_or_** **_ideal_** **_constructs._** **_Without_** **_this_** **_faith_** **_no_** **_science_** **_could_** **_ever_** **_have_** **_any_** **_motivation_**
- **Latent Variable**, is some *continuum*, unobserved and vary in magnitude form unit-to-unit
- Core **Steps** in the EFA
	1. Method of extraction: *how* do we *estimate* out factors
		1. principal components
		2. principal axis factoring
		3. alpha factoring
		4. image analysis
		5. unweighted least squares
		6. maximum likelihood
	2. Factor Enumeration: *how many* factors are there?
	3. Factor rotation: can we *rescale* our *loadings* to be *interpretable*
	4. Substantive interpretation: what the heck does it *mean*
	5. Scoring: can be obtain scale *scores* for use elsewhere
#### Principal Components Analysis
- PCA is **not** a "true" factor model
	- PCA uses *weighted combinations of observed* items to estimate components
	- a "true" factor model uses observed items to infer unobserved latent factors
	- PCA establish a number of core principles that apply to all factor analytic approaches
	- Here, we treat PCA as a type of EFA
	- If we extract as many _factors_ as there are observed _items_, then we perfectly reproduce **R** such that **R** =**R** ($\hat\theta$)
	- a common _factor_ _analysis_ will account for correlations _among_ _measured_ _variables_ _better_ _than_ _a_ _PCA,_ _whereas_ _a_ _PCA_ _will_ _account_ _for_ _more_ _of_ _the_ _observed_ _variance_ _in_ _the_ _measured_ _variables_
- Goal of PCA
	- The goal of PCA is to extract **_fewer_** than all possible eigenvalues to explain not all, but **_most_** of the **variance**
- **Eigenvalues**
	- An _eigenvalue_ represents a component of *variance* among a set of items that is associated with a weighted composite of the items where the _eigenvectors_ serve as the corresponding weights
	- There are as many eigenvalues as observed items and extracting all possible eigenvalues will explain 100% of the observed variance
	- variance of a weighted component among a set of items. If you use those as weights for your eight items and compute a weighted composite，the variance of that composite is the eigenvalue
	- If you compute as many eigenvalues as items，all you did was bring car into the garage，repainted and pull it out and it's exactly the same car. You've just *repackage* that *information*
- **Components**
	- The primary motivation of PCA is to form one or a small number of weighted combinations of the observed variables called _components_
	- The first component represents the weighted combination of variables that results in the maximum variance possible
	- The second component represents a weighted combination of variables that remains _net_ _the_ _removal_ of the first component
- **Equation** of **PCA**
	- ![[Pasted image 20230726093235.png|400]]
	- ![[Pasted image 20230726093311.png|100]] 
- **Equation** of **correlation matrix**
	- Population
		- ![[Pasted image 20230726093606.png|100]] 
		- ![[Pasted image 20230726093642.png|300]] 
			- ![[Pasted image 20230726093723.png|300]] 
	- Sample
		- ![[Pasted image 20230726093757.png|100]]
- Determine the **Number of Factors**
	- The *Kaiser-Guttman rule*: there be no more components than eigenvalues that exceed 1.0
	- *Scree Plot*: We can plot the eigenvalues in sequence so the eigenvalues are on the vertical axis and the associated components are on the horizontal axis. The goal is to identify the "bend" in the plot and the number of eigenvalues above this bend are the suggested number of components
		- ![[Pasted image 20240102111514.png|200]] 
	- Parallel Analysis: second line reflects the eigenvalues computed for randomly sampled and uncorrelated data with the same number of variables and sample size as the given study. the number of components to be extracted should be greater than the number generated by random data.
		- ![[Pasted image 20240102111707.png|300]] 
- **Rotation**: *orthogonal* (that result in uncorrelated factors) and *oblique* (that result in correlated) factors
	- Particular orientation is an optimized orientation with regard to explaining variance individually. no matter what orientation I put them at，they explain the *same amount of variance overall* (is this true for oblique?)
	- **Varimax Rotation** (Orthogonal): Maximize the variance in the loadings. It's going to rotate until you get for any one factor high loadings and low loadings. results in each variable's loadings being high on one factor and low on all other factors
	- **Oblique Rotation**
		- ![[Pasted image 20240102154523.png|300]] 
		- The *factor structure matrix* contains the estimated correlations between each item and the underlying factor ignoring all other factors
			- so these are akin to bivariate correlations between two variables
		- The *factor pattern matrix* contains the estimated standardized coefficients (or factor loadings) obtained by regressing the observed items on the latent factors
			- these are computed for each factor net all other factors. β estimates in the multiple regression
		- In an orthogonal solution (where the factors do not correlate) the factor pattern and factor structure matrices are numerically the same
		- Use factor pattern matrix for oblique rotation
		- for fa function in r
			- ![[Pasted image 20240107222034.png]]
- **Communality**
	- each item has a communality: this is simply an R2 value as is commonly encountered in regression
	- the proportion of total variance explained by the set of predictors, but in the EFA the "predictors" are the latent factors
	- For historical reasons, we refer to the communality as $h^2$ 
	- e.g., $h^2_p$=.48 indicates the extracted factors account for 48% of the total observed variance in measured variable p
- **Interpretation** and Naming the Factor
	- high loading .4, low loading .2
	- It is desired that any given factor be defined by at least 3 items
- **Assumptions**
	1. variables are measured on a *continuous* scale
		-  interval or ratio scales, but possibly ordinal if sufficient number of categories 
	2. variables are *linearly* related to one another
		-  unit of analysis is correlation matrix that captures bivariate linear relations
	3. the correlation matrix represents *sufficient* statistics
	    -  "sufficient" means it contains all that is needed to understand the data
	    -  there are **no** *missing* data, *non-normal* data, *non-independent* observations
	4. critically, the items are assessed with *no measurement error*
		-  all observed variance is true score variance available for factoring
#### Common Factor Model
- **Differences with PCA & Estimation**
	- Instead of maximizing the variance associated with each factor, the CFM prioritizes reproducing the observed correlation matrix
	- Always remember *PCA* is not a true factor model but instead forms *weighted composites of the indicators assuming no measurement error*
	- There are two primary approaches used to accomplish this: 
		- **unweighted least squares (ULS)**
			- *minimize the sums* of the squared discrepancies between our observed matrix R and our model-implied matrix $R(\hat{\theta})$ 
			- ![[Pasted image 20240102165813.png|400]] 
			- here tr is the trace which is the sum pf the matrix diagonal
		- **maximum likelihood (ML)** [[SEM and Multilevel#^ML-intro]] [[SEM and Multilevel#^FIML-REML]]
			- Neither PCA nor ULS makes any assumptions about the shape of distributions of the items. In contrast, ML *assumes* that the items follow a *multivariate normal distribution* in the population.
			- the goal of ML is to obtain parameter estimates that *maximize the likelihood* of the observed sample data. what parameters would make our observed data most likely?
			- ![[Pasted image 20240102170302.png|400]] ![[Pasted image 20240102170406.png|400]] 
			1. Sufficient-statistic ML (SSML) estimation is based solely on the observed correlation matrix
				- assumes complete-case data and normally distributed DVs
			2. Full-information ML (FIML) estimation is based on whatever data are observed for each individual case
				- allows for partially missing data, methods for addressing non-normal distributions, and nested data structures
			- **LRT for Single Model**: [[SEM and Multilevel#^evaluation-index]]  Through remarkable derivations we don't present here, the minimum of the ML fit function multiplied by the sample size minus one is a test statistic that follows a central $\chi^2$  distribution. ![[Pasted image 20240103105225.png|300]] where *p* is the number of variables and *m* the number of factors. We then use this probability to make an inference about our null and alternative hypotheses. A significant T-statistic (e.g., p<.05) indicates it is improbable that a test statistic of this value or larger would be found if the null is true (reject the Null)
				- ![[Pasted image 20240103105410.png|300]] 
			- **LRT for Nested Model**: In general, two models are nested if one model can be defined by placing (or removing) restrictions on another model
				- ![[Pasted image 20240103110210.png|400]] 
- **Sample Model-Implied Correlation Matrix**
	- ![[Pasted image 20240102165229.png|300]] ![[Pasted image 20240103093011.png|330]] 
- **Factor Score Estimation**
	- "components" can be directly computed in PCA but "factors" can only be indirectly estimated in the common factor model
	- *Regression Methods* Factor Scores
		- Z is the standardized observed score
		- ![[Pasted image 20240105120931.png|400]] ![[Pasted image 20240105155337.png|500]]
		- We can choose to achieve different goals we might have in scoring
- Advantages:
	- items can differentially contribute to the underlying factor
	- items are allowed to contain measurement error
	- items can be defined by more than one underlying factor
- Disadvantages:
	- they are entirely based on the final sample estimates from the model
	- Under conditions of small sample size, non-normality, non-linearity, model misspecification, etc., the parameter estimates may be biased, variable, or both. this is in turn "baked in" to the factor scores
	- Thus the scores are as stable as are these parameter estimates. There are situations where factor scores can perform much worse than unweighted means because the EFA is itself is in some way unstable
- 
##### Example



# 4. Multilevel Models
## Classic Multilevel Model
- Limitation of the traditional linear regression
	- ![[Pasted image 20231117105732.png|500]] ![[Pasted image 20231117105914.png|500]] 
	- When assuming independence of nested data there is the potential for making **incorrect inferences** about misleading effect estimates.
- Eldest children have the higher IQ, Birth order effects on math scores. In data sets with one sibling per family, *birth order effects (within-family)* may be **contaminated** by *between-family differences*. (e.g., birth order confounded with family disadvantage if later born children tend to be from larger, less advantaged families)
		- ![[Pasted image 20231117110600.png|400]] 
- **Traditional Model** ANOVA
	- ![[Pasted image 20231117110904.png|500]] ![[Pasted image 20231117111021.png|400]]
- We can, however, use alternative methods for **computing SEs** that incorporate information about the **nested data structure**. Most common is Huber-White sandwich estimator for cluster-correlated data
	- Corrected standard errors approach provides accurate *estimate of total effect* with proper standard errors
	- This approach is useful if you are interested in overall effects (*pooling individuals over groups*) and you want unbiased SEs and test statistics.
	- **Cannot** be used to evaluate *within*- versus *between*-group effects.
	- **Cannot** be used to evaluate whether effects vary *across groups*
	- Correcting standard errors can be useful, but the estimates of the model still pool over individuals from all groups and hence do not provide information on within-group versus between-group differences, or whether effects might differ in magnitude over groups. This approach is at its best when the dependence in the data is mild. When observations are highly correlated, such as with longitudinal data, even the corrected standard errors may not yield fully accurate inferences. A similar but better approach is then to use *Generalized Estimating Equations (GEE)*. In GEE, *data within clusters are weighted by a working correlation matrix* that helps to account for the dependence among observations. The analyst must choose the specific structure for the working correlation matrix (e.g., unstructured, compound symmetric, autoregressive). GEE estimates are consistent regardless of which structure is chosen (accurate when there is a large number of clusters) but choosing a structure that represents the dependence in the data well results in more efficient estimates (estimates with smaller standard errors and hence greater power). Standard errors are calculated using the sandwich estimator, which helps to ensure that inferences will be robust to the choice of working correlation structure (i.e., still accurate even if the working correlation structure was poorly chosen). Choosing an independence structure would reduce the GEE to the approach just described, a standard OLS regression with adjusted standard errors. In contrast, all other structures allow for some form of cluster correlation. Because GEE is predominantly used with longitudinal data, and then primarily with discrete outcomes, we defer further discussion of this approach to Chapter 10
- **Fixed Effect Model** = **group-mean centered outcome**
	- ![[Pasted image 20231117111920.png|400]] 
	- The overall intercept of the model has been omitted here, permitting dummy variables for all 20 levels of the Peer Group variable to be included in the model. In this specification of the model there is no reference group and the coefficients β1 through β20 can be interpreted as peer-group-specific intercepts. These *group-specific intercepts* serve to absorb any mean differences in alcohol use across peer groups that remain after controlling for family conflict. It is worth noting that there are a few different ways to conduct the fixed-effects approach. 
	- **Another variation** is to group-mean center the outcome variable. For instance, we could calculate the average alcohol use within each peer group and then subtract those group means from each individual’s score. This subtracts out the differences across groups, removing the dependence. Analyzing the *group-mean- centered outcome* produces equivalent results to the regression approach described above. When there are just *two observations per cluster* another variation of the fixed effects approach is to *take difference scores*. For instance, we could take the difference in math IQ scores between first and second born children within each family. In taking the difference, any family level characteristics that are shared across siblings cancel each other out. The difference scores then become the object of analysis. 
	- **Advantages**
		- It is the most appropriate method if the groups are truly fixed and not representative of a population of groups.
			- e.g., treatment groups, ethnic groups, religions, etc. 
		- Useful when there are a small number of groups. 
			- e.g., data collected from only 3 schools.
		- Adjusts model for all unmeasured group-level covariates.
			- Main effect of group controls for all between-group differences
			- Estimates of individual-level predictors *unambiguously reflect within-group effects*, as all between-group variance has been removed.
		- A standard GLM.
	- **Disadvantages**
		- Difficult to evaluate effects of group-level variables (can be done with contrasts, but becomes cumbersome).
			- e.g., is alcohol use related to the popularity of the peer group?
		- Many nuisance parameters to estimate (not parsimonious). 
			- Problem with small groups (e.g., dyadic data)  
			- Problem with “singletons” (e.g., “only children” in family data)
		- Grouping variable assumed to be a fixed predictor, so inferences must be restricted to these particular groups (not a broader population of groups).
- **Random Intercept Model vs. Fixed Intercept Model** 
	- (random means average estimate and variance estimate, the value can be changed based on the variance)
	- *Group differences* are assumed to follow a particular *distribution* in the population. We sample from this distribution when we sample groups.
	- Our concern is with the *parameters of the population distribution*, not with differences among the sampled groups.
	- ![[Pasted image 20231117113225.png|400]]
	- ![[Pasted image 20231117113438.png|600]] ![[Pasted image 20231117113555.png|600]] 
	- **Advantages**
		- Parsimonious
		- Permits inferences to the population of groups.
		- Conforms to the sampling design, with the random selection of groups followed by the random selection of individuals within groups.
		- Enables us to examine the effects of individual-level and group-level influences simultaneously
	- **Disadvantages**
		- Requires a sufficient number of groups to enable inferences to population
		- Requires that we assume a specific distribution for group effects (e.g., *group differences are normally distributed*)
		- *Omitted group-level variables* can be problematic (e.g., when correlated with individual-level variables that are included in the model)
		- Requires more complex methods of estimation (i.e., maximum likelihood)
	- Prefer Random Effect
		- Do not want our inferences to be limited to groups in the sample by using a model that fails to conform to sampling design.
		- Can check assumptions for the distributions of the random effects.
		- Can mitigate omitted variable bias problem through careful model specification and centering.
		- **Simplifies to GLM if no evidence of dependence due to nesting**.
- How many groups are enough to do mixed model
	- Early methodological literature recommended at least 30 groups, but largely arbitrary
	- More recent research suggests can go as low as 10 clusters
		- Requires use of small-sample adjustments to estimation and inference tests, but these are readily available in off-the-shelf software
- **The Random-Effects ANOVA Model**
	- ![[Pasted image 20231117131858.png|500]] ![[Pasted image 20231117132040.png|400]] 
	- ![[Pasted image 20231117132135.png|400]] ![[Pasted image 20231117132215.png|600]] 
	- ![[Pasted image 20231117184954.png|500]] ![[Pasted image 20231117185119.png|500]] 
	- The ICC shows a high level of dependence and a relatively *large* contribution of *between-family factors* to Math IQ. The p-values shown here for the z-tests are one-tailed probabilities. A one-tailed p-value is used here because variances cannot be negative. Some software programs (e.g., SAS) report one-tailed p-values for variances and two-tailed p-values for covariances, whereas other software programs (e.g., SPSS) report two-tailed p-values for all variance and covariance estimates. Stata reports only confidence limits (although a p-value could be computed easily based on the reported estimate and standard error). “Lower” and “Upper” in the table above refer to 95% confidence limits. Importantly, the z-tests and confidence limits shown here are based on alternative assumptions about the sampling distributions of the variance parameters. In accordance with the asymptotic properties of maximum likelihood estimates, the z-tests (or Wald tests) assume a normal distribution. Given the impossibility of negative variances, however, the sampling distributions of variances tend to be skewed in finite samples. The asymmetric confidence limits shown here are computed by SAS based on assuming a skewed sampling distribution (obtained via a Satterthwaite approximation). Similar in spirit, Stata computes z-type confidence limits for the log of the standard deviation, then transforms these values to obtain asymmetric limits for the variance. Although the confidence limits are generally more accurate, they are not useful for null hypothesis tests because they will never include zero. (If the lower bound is close to zero, however, that is suggestive that the variance component is superfluous).
- **Intraclass Correlation**: Standardizing within-group variance
	- If ICC = 0 then there are no between-group differences to produce dependence. The nesting of the data is irrelevant. If ICC = 1 then all differences are between-groups differences and individuals within a group have identical scores.
	- ![[Pasted image 20231117134347.png|500]] ![[Pasted image 20231117134442.png|400]] 
	- ![[Pasted image 20231117134640.png|500]] 
- **Including lower level predictors**- random intercept regression model
	- ![[Pasted image 20231117190000.png|500]] ![[Pasted image 20231117190303.png|500]] 
	- ![[Pasted image 20231117190545.png|500]] ![[Pasted image 20231117191107.png|1000]] 
	- ![[Pasted image 20231117194747.png|500]] 
- **Incorporating Upper-Level Predictors**: Means as Outcomes
	- Values of *Level 2 predictors are constant within any given group*, so Level 2 predictors *cannot explain within-group variance*.
	- ![[Pasted image 20231117194628.png|500]] ![[Pasted image 20231117194824.png|500]] 
	- ![[Pasted image 20231117195852.png|500]] 
- **Including Predictors at Both Levels**: Intercepts as Outcomes
	-  ![[Pasted image 20231118122857.png|500]] ![[Pasted image 20231118123612.png|500]] 
- **Decomposing Between- and Within-Group Effects**
	- Total effect: The relation between x and y pooling over all individuals ignoring group membership (sometimes called the marginal effect)
	- Within-group effect: The relation between x and y for all individuals within a given group (sometimes called the conditional effect)
	- Between-group effect: The relation between the means of x and y aggregating over all individuals within each group (sometimes called the ecological or contextual effect)
	- *Plot* example of between & within group effect
		- ![[Pasted image 20231118124637.png|500]] ![[Pasted image 20231118124656.png|500]] ![[Pasted image 20231118124739.png|500]] ![[Pasted image 20231118124818.png|500]] ![[Pasted image 20231118124936.png|500]] 
	- In standard OLS regression, we sometimes “center” predictors by subtracting the mean from each score on a variable. improve interpretability given that the regression intercept is the overall sample mean of y. improve estimation of interaction effects due to decreased collinearity.
	- For Level 2 predictors, centering done solely for interpretation.
		- ![[Pasted image 20231118131018.png|500]] 
	- Level 1 predictors can explain both within- and between-groups variance in outcome
		- ![[Pasted image 20231118131129.png|500]] 
	- Defining meaning of intercept
		- ![[Pasted image 20231118132039.png|500]] 
		- ![[Pasted image 20231118132153.png|500]]  ![[Pasted image 20231119004814.png|400]]
		- ![[Pasted image 20231119004406.png|500]] ![[Pasted image 20231119004833.png|400]]
		- ![[Pasted image 20231119004917.png|500]] ![[Pasted image 20231119005001.png|400]] 
	- *Within*- and *between*-group effects are *confounded* when **Level 1 predictors** are *raw* scale or *grand-mean centered*.
		- ![[Pasted image 20231119101443.png|500]]
		- ![[Pasted image 20231119101624.png|500]]  ![[Pasted image 20231119005554.png|600]]  
	- Grand-Mean Centering & *Including* the *group mean* as a predictor partials the between-group effect from the within-group effect.
		- ![[Pasted image 20231119100906.png|500]] ![[Pasted image 20231119102402.png|500]] 
	- *Group-mean centered Level 1 predictors* have no between-groups variation left, hence coefficients reflect within-group effects only
		- ![[Pasted image 20231119102909.png|500]]  
	- When using *group-mean centering*, no special procedures need be applied to generate a ‘clean’ estimate of W. This is a significant advantage of group-mean centering, but it comes at the cost of *discarding the between-groups variation* on the predictor. *Fortunately*, we can **add this information back** into the model to obtain an estimate of B, similar to the way we did this with grand-mean centering. **add group-mean as level 2 predictor**.
		- ![[Pasted image 20231119103034.png|500]] ![[Pasted image 20231119103500.png|500]] 
- **Ecological Fallacy**: Drawing conclusions about individuals nested within groups based on between-group differences
	- Communities with more eating and drinking establishments have higher crime rates; but choosing to eat out does not necessarily increase an individual’s chance of being victimized
	- States with higher average wealth tend to vote democratic; but voters with higher incomes tend to vote republican
- **Simpson’s Paradox**: within-group relations are opposite in direction from the total relations
	- Berkeley sex bias case: on average, women rejected at higher rate for graduate school; on individual case, women accepted at higher rate because tended to apply to more competitive academic programs
	- The *median US wage rose about 1%* between 2000-2013, yet *median wages dropped for each education group* (e.g., HS dropouts, HS graduates, some college, college degree); due to increase in number of people pursuing higher education
	- ![[Pasted image 20231118125646.png|500]]
- **Reliability of the group means**
	- When we include the group means in the model we are treating these as if they were error free. But *sampling error* creeps in if we are sampling *a small fraction of the total number* of individuals per cluster.
	- Unreliability of the group means causes the *between-group effect to be biased*.
		- More bias with smaller clusters
		- *More bias* when a predictor has *less between-group variability*
		- Between-group effect is biased toward within-group effect
	- Interestingly, within-group effects are not affected by unreliability of the group means.
	- If unreliability of the group means is a concern, two primary options:
		- Transition to a latent variable modeling approach
		- Post-hoc correction for attenuation
		- ![[Pasted image 20231119194707.png|500]] 
	- Using *aggregated* data on *a larger number of observations* when small subset are drawn from the group
		- Sometimes aggregate statistics are available on a larger number of observations than those included in the sample. For instance, suppose sampled 5 students from each of many universities. 
		- Might be able to obtain average family income of all students attending each university.
		- Better to use those averages as group means than to compute group means using just the subset of students who were sampled.
- Including **Random Slopes** for **Level-1 Predictors**
	- ![[Pasted image 20231119201301.png|500]] ![[Pasted image 20231119201321.png|500]] ![[Pasted image 20231119201816.png|500]] 
	- The covariance matrix of random effects is called *tau or T*. The diagonal elements are variances and the off-diagonal elements are covariances. The covariances can be standardized into correlations by dividing the covariance by the product of the standard deviations. 
		- But interpretation of u0j depends on scaling of xij (Group- versus grand-mean centering, or raw scale)
		- ![[Pasted image 20231119202038.png|500]] ![[Pasted image 20231119202822.png|600]]  
		- *Correlation* between *random intercepts & slope* interpreted like any other
			- Positive correlation means higher values of u0j associated with higher values of u1j
			- Negative correlation means higher values of u0 j associated with lower values of u1j
			- ![[Pasted image 20231119203026.png|500]] ![[Pasted image 20231119203045.png|500]] 
		- Include p level-1 predictors: The greatest *challenge* in model building at level-1 is the *rapid expansion of the tau matrix*.
			- ![[Pasted image 20231119203303.png|500]] ![[Pasted image 20231119203327.png|500]]  
	- ![[Pasted image 20231119203712.png|500]] ![[Pasted image 20231119203742.png|700]] 
- Modeling Cross-Level Interactions: Explain **slope variation** across groups with the inclusion of one or more **level-2 predictors**
	- When we include the level-2 predictor in both the intercept and the slope equations, then this predictor is manifested as both a main effect and a cross-level interaction with the level-1 predictor. Given this, we can draw on techniques for probing interactions that are commonly used in the standard regression model.
	- The inclusion of a *Level 2* predictor as a *main effect in the slope* equation results in a multiplicative interaction in reduced-form.
	- the regression of y on x depends in part on w
	- Given the symmetry of the interaction, the regression of y on w also depends in part on x
	- ![[Pasted image 20231119210052.png|500]] ![[Pasted image 20231119211142.png|600]]  
	- ![[Pasted image 20231119211819.png|500]] 
		- These are compound parameters and provide the intercept and slope of the regression of y on x *at a particular value of w*
		- ![[Pasted image 20231119212036.png|500]] 
- Key Multilevel Model Assumptions
	- Level 1 residuals (r) are independent, homoscedastic, and normally distributed with mean 0 and variance 𝛔2
	- Level 2 random effects (u) are independent over Level 2 units, homoscedastic, and multivariate normally distributed with **mean 0** and **covariance matrix T**
		- The random effect is independent across groups, but within group, they can correlated, and is evaluated by the above covariance matrix T
	- Level 1 residuals are uncorrelated with Level 2 random effects, and vice versa.
- Model Assessment
	- Create histogram and QQ plots of *residuals* and *random effects* to examine normality assumption.
		- ![[Pasted image 20231121135359.png|500]]
		- ![[Pasted image 20231121134554.png|500]] ![[Pasted image 20231121134611.png|500]] 
	- Create bivariate plots of *residuals* by each *predictor* to examine homoscedasticity and influential observations.
		- Example plots
			- ![[Pasted image 20231121134708.png|500]] 
				- for multilevel models trend may result from “*residual confounding*”. Random effects and Level-1 residuals assumed uncorrelated in population. The way they are estimated, however, produces a correlation. Use of random effects in predicted values leads to spurious trend with residuals. One solution is to *use predicted values* based solely on *fixed effects*
				- ![[Pasted image 20231121135020.png|500]] 
			- ![[Pasted image 20231121135043.png|500]] 
			- ![[Pasted image 20231121135112.png|500]] 
		- Models with random effects can produce two types of Level 1 residuals
			- subject-specific residuals：calculated using information from both fixed and random effects
			- population-averaged residuals： calculated using information from *just the fixed effects*
			- Generally, the subject-specific residuals are a good first choice for evaluating model assumptions and outliers because these are direct estimates of rˆij
	- Create bivariate plots of each *random effect* by all other *random effects* to examine homoscedasticity, bivariate normality, and influential observations.
		- ![[Pasted image 20231121135310.png|500]] 
		- ![[Pasted image 20231121135658.png|500]]
	- Assumptions that **cannot be** empirically *evaluated*:
		- Mean of Level 1 residuals and Level 2 random effects is equal to zero.
		- Level 1 *residuals* are uncorrelated with Level 2 *random* effects, and vice versa.
		- Level 1 and Level 2 *predictors* are *uncorrelated* with Level 1 *residuals* and Level 2 *random* effects.
	- Violation of homoscedasticity: use robust standard errors or model heteroscedasticity by predictor variables
	- Violation of independence of errors or random effects: 
		- Level 1 : consider alternative error structures
		- Level 2: consider a three-level model
- Model Evaluation ^FIML-REML
	- Full Information Maximum Likelihood (FIML) & Restricted Maximum Likelihood (REML)
		- FIML estimate divides sum of squared deviations by N implying that *population mean is known*. FIML treats fixed effects as known
			- ![[Pasted image 20231121141930.png|200]]
		- REML divides by N -1 to reflect loss of 1 degree-of-freedom due to the estimation of the sample mean. REML incorporates uncertainty in the estimation of the fixed effects. The degree of freedom is N-1 because of the estimate of y bar.
			- ![[Pasted image 20231121142004.png|200]] 
		- At large sample sizes, FIML and REML will provide identical or nearly identical results for all effects.
		- At smaller sample sizes, FIML and REML will provide identical or nearly identical results for fixed effects. But will provide *different* results for *random effects*. *FIML* tends to produce *smaller variance components* compared to REML
		- Because FIML is a full-information ML estimator, *FIML* will be more *efficient* (i.e., smaller standard errors)
		- Because REML treats fixed effects as sample-based estimates, *REML* provides *less biased* estimates of variance components and standard errors at smaller N
	- Testing Nested Models: Likelihood Ratio Test
		- Define deviance to be -2 times the log of the likelihood: D= -2LL
		- if two models are nested, the difference between each model D is (usually) distributed as a chi-square
		- Two models are nested if the parameters in one model are a direct subset of those of a second model.

## Repeated Measurements Multilevel Model
- Model
	- ![[Pasted image 20231121144836.png|500]]
- Metrics of Time
	- ![[Pasted image 20231121145006.png|500]] 
	- ![[Pasted image 20231121145038.png|500]] 
- Wave
	- ![[Pasted image 20231121144928.png|500]] 
- Error Structure at Level 1
	- Standard assumption is that the Level 1 residuals are homoscedastic -- i.e., equal variance at each time point
	- In many repeated measures applications, this may not hold -- e.g., , diverging or converging trajectories
	- An alternative is a diagonal Level-1 residual matrix with heteroscedastic (i.e., unequal) residuals over time
	- Homoscedastic Error Structure
		- ![[Pasted image 20231121145559.png|400]] 
	- Heteroscedastic Error Structure
		- ![[Pasted image 20231121145629.png|500]]
- Exchangeability
	- In hierarchically structured data, individual children nested in a class are arbitrarily ordered -- they are exchangeable
	- In longitudinally structured data, individual observations nested in an individual are temporally ordered -- they are not exchangeable.
- Example of Growth Model without Predictor
	- ![[Pasted image 20231121150322.png|500]] ![[Pasted image 20231121150538.png|500]] ![[Pasted image 20231121150908.png|500]] 
	- Can use LRT to compare random intercept-only model with random intercept & random slope model
	- ![[Pasted image 20231121151505.png|500]] 
- Quadratic Multilevel Growth Model
	- ![[Pasted image 20231121151321.png|500]] 
	- LRT for Linear vs. Quadratic
- Time-Invariant Covariates= Level 2 predictor
	- ![[Pasted image 20231121151743.png|500]] 
	- Model-implied Trajectories
		- ![[Pasted image 20231121151922.png|400]] ![[Pasted image 20231121151945.png|400]] 
	- allow heterogeneity over groups in the random effects covariance parameters
		- ![[Pasted image 20231121152208.png|500]] ![[Pasted image 20231121152232.png|500]] 
- Time-Varying Covariates= Level 1 predictor
	- We accord the time variable special conceptual status through the notion of a growth trajectory. The effect of other time-varying covariates may be viewed as perturbing an individual from their underlying trajectory.
		- ![[Pasted image 20231121152329.png|500]] ![[Pasted image 20231121152357.png|500]] 
	- Adding Time-varying with fixed slope
		- ![[Pasted image 20231121152558.png|500]] ![[Pasted image 20231121152638.png|500]] 
	- Adding Time-varying as random slope
		- ![[Pasted image 20231121153040.png|500]] 
	- Adding Time-varying as fixed slope but interact with time
		- ![[Pasted image 20231121153206.png|500]] 
	- Lagged Effects of TVC
		- ![[Pasted image 20231121153529.png|500]]
		- 
## Multivariate Multilevel Models
- Application: 
	- Relationships between dependent variables at Level 1
		- Residual correlation  
- Relationships between dependent variables at Level 2
	- Correlations among random effects  
- Joint effects of predictors on multiple dependent variables
	- Simultaneous tests of predictor effects across set of outcomes
- Limitations of the Time Varying Covariates Model
	- concerns the decomposition of within- and between-person effects
		- ![[Pasted image 20231110111955.png|400]] 
			- Dashes indicate the between-person differences, captured by the person means, whereas the dots are the actual observations. Person-mean centering captures the within-person variability.
		- ![[Pasted image 20231110113527.png|300]] 
		- In *hierarchical* data, the *ordering* of observations is often *arbitrary* (i.e., observations are exchangeable), but with *over-time data there is a natural temporal ordering* to the observations that must be considered. We can plot the TVC as a function of time to see whether this ordering matters.
			- ![[Pasted image 20231110113617.png|400]] 
		- Here we see a *strong linear increase in the upper left* plot, and more modest time trends for the other plots. The person means are reflected in the plots by the horizontal reference lines; person mean centering would capture the distance between the dots and horizontal reference. Clearly, however some of what is captured by the *person-mean centered* TVC is actually the *time trend*.
			- ![[Pasted image 20231110113831.png|500]] ![[Pasted image 20231116152003.png|500]]
- Steps to do
	- Begin by fitting univariate growth models to each outcome   
	- Rearrange the data to *create a single synthetic dependent variable (z)* to represent both outcomes, with indicator variables to indicate which outcome is which
	- Determine the reduced form expression for z
	- Specify an appropriate variance-covariance structure for the random effects and residuals
	- If specified correctly, a multivariate growth model will reproduce all of the results of dual univariate growth models almost exactly (this is good to check), but provide additional results on how growth processes are related
- Equation Structure
	- ![[Pasted image 20231121161645.png|500]] ![[Pasted image 20231121161739.png|500]] 


# 5 SEM and MLM Book
- ==From this book, I want to know==
	1. Whether AR can existed simultaneously with random slope
	2. how to test whether random component is different from 0
	3. what are different model assumptions and how to test them

- ==Next time==
	1. Read the following notes, if forgot, re-read the book. Make sure know the previous knowledge
	2. begin with page 33, continue for 3 hours

- Five reason to do longitudinal analysis: 
	- summarized within-change pattern and how this pattern (rationale 1) different between groups (rationale 2), 
	- how "change" different in different behavior class, predict between group differences (rationale 3).  
	- causes of within-change differences (rationale 4)
	- how between-differences contribute to within-change differences, identify the time-invariant variables that are related to specific aspects of within-person change (rationale 5)
- History of growth model
	- 1938: identify a mathematical function that would provide the best representation of each pig’s growth trajectory: quadratic polynomial. And then use analysis of variance to study trajectory differences
		- a linear change component interpreted as “average growth rate in pounds per week,” and a quadratic change component interpreted as “half the rate of change in the growth rate in pounds per week” (i.e., a scaling of acceleration)
			- The derivative of a function at a point is the rate at which the function's value changes at that point. linear means the change (1) is constant. quadratic means the change (1) is change (2). by 2a for ax^2, so a is the half the rate of change
	- Tucker 1958: **Principle Component** Way
		- sums of squares and cross-products matrix obtained from repeated measures data were subjected to a principal components analysis.
		- The principal components model *decomposed the repeated measures* data *into* a set of *generalized learning curves*, component **loadings** representing distinct **patterns of change**, and individual component weights (*component scores*). The generalized learning curves were interpreted as the fundamental aspects of change that all individuals shared (Rationale 1)
		- Individual component weights (*component scores*) indicating the *degree to which* an individual’s observed trajectory was *saturated* by each of the generalized learning curves (components). indicated how individual trajectories were different from one another (Rationale 2)
		- Examine the component score between groups
		- 1966 Tucker: rotation
	- 1977 Harville: introduce **linear mixed effects models** 
		- Laird and Ware (1982) developed estimation techniques for those models. 
		- Level 1 and Level 2 notation.
		- handle incomplete and highly unbalanced data
		- 1987 Brky refined the model assumptions
	- 1979 Sorbom: **Structural Equation Model**
		- Tisak 1990: *Latent curve model*, as a restricted confirmatory factor model
		- Extensions to multiple-group growth models, higher-order polynomial models, spline models, and a variety of models with *nonlinear* change patterns
		- McArdle (1986) combined additive *genetic* models and latent growth models in the analysis of longitudinal data from twins to assess the additive genetic (heritability), common environmental, and unique environmental components of initial test performance, change in performance over time, and unique (individual) variability.
	- 2003 Magnusson: **Qualitative differences** in within-person change
		- group individuals based on their change patterns (e.g., early learners, late learn- ers) introduced semiparametric group-based models, that represented between-person differences in change as a collection of latent classes
	- 2000s model *individual change* and time-dependent *lead-lag associations* **simultaneously**
		- Curran and Bollen (2001) highlighted how autoregressive and cross-lagged effects could be included directly in growth models specified in the *structural equation modeling* framework.
- **Multilevel and SEM** can fit the same model and obtain identical results
	- Multilevel is easier in individually varying time scales and nonlinear trajectories
	- SEM is easier in residual structures and fitting multivariate change models
	- The majority of growth models can be specified in both frameworks (see Curran, 2003; Ghisletta & Lindenberger, 2003; Willett & Sayer, 1994); however, certain models *can only be specified in one framework* or the other because of *program limitations*. For example, inherently (fully) nonlinear models can only be directly fit within the (nonlinear) multilevel modeling framework, and second-order growth models can only be fit within the structural equation modeling framework.
	- experience working in both the multilevel and structural equation modeling frameworks is beneficial.
- Plot longitudinal data before fitting the model
	- ![[Pasted image 20231206103034.png|500]]
	- ![[Pasted image 20231206103058.png|500]] 
- Data screening
	- Create dataset only contain weight variables. Univariate **descriptive** statistics.
		- sample size changes dramatically across age. 
		- Reporting errors in the data. Minimum values for weight at ages 7, 8, and 12 were less than 10 pounds, and maximum values for weights at ages 8, 9, and 10 were in the 200s
		- DV mean's trend. The increases, though, are not constant (i.e., linear) as age-to-age differences ranged from –1 (between ages 14 and 15) to +13 (between ages 12 and 13), highlighting the fact that gains in weight across this age range are *nonlinear* (i.e., a linear growth model will not fit these data when age is the time metric)
		- age-to-age differences in the *standard deviations* indicate that the amount of *between-child differences* in weight also *increased* through early and middle childhood and stabilized around age 11
		- Fifth, the skew and kurtosis values show that the distributions of weight, at most ages, are both positively skewed
		- ![[Pasted image 20231206103925.png|900]]
	-  **bivariate scatterplots** and univariate histograms
		- First, the positive skew
		- age 5 weights and age 6 weights is empty, which means that no individuals were measured at both ages
		- 8/9 year *bivariate scatterplot* there is an observation very far to the right that is all alone. Checking the axes, this individual appeared to have *gained 100 pounds in one year*, which is unlikely and suggests that additional cleaning of these data is required.
		- ![[Pasted image 20231206103614.png|500]]   ![[Pasted image 20231206104006.png|500]] 
- Longitudinal Measure
	- reliability: High internal consistency (e.g., Cronbach’s a > 0.80) of multiple- item questionnaires is interpreted as an indication of good reliability and is a good starting point. Cronbach’s a can be calculated separately at each measurement occasion to evaluate whether the test, scale, or survey is internally reliable over the course of the study.
	- scaling/sensitivity to change: 
		- Does the measurement tool capture the changes of interest? For example, IQ scores are explicitly age normed, such that the average is 100 and the standard deviation is 15. Normed scores are not appropriate for growth modeling because the very information (i.e., changes in the mean and variance) upon which the growth model is built have already been removed.
		- Some tools, particularly those developed in research settings focused on the assessment of between-person differences, are not neces- sarily sensitive to within-person changes.
			- Granular measurement tools (e.g., 5-point Likert- type scales on questionnaires) can lead to conclusions that the measured constructs are relatively stable, while fine-grained measures (e.g., 0- to 100-point slider-type interface) can lead to conclusions that the measured constructs are quite variable.
		- whether the measurement instrument can represent the entire range. ceiling or floor effects
	- measurement invariance: does the measurement tool measure the same construct in the same metric at each occasion?
