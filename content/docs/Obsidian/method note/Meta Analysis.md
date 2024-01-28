The analysis of that raw data, we might think of as a *primary data analysis*. Secondary analysis is very similar to primary data analysis. A secondary analysis is someone else's gathered the data. You are analyzing it. So an example would be the nape data or the eclsk data sets, early childhood, longitudinal studies. There's plenty of other massive data sets that people use, take subsets of variables and run analysis on, but we would typically call that a *secondary data analysis*. *Meta analysis* is literally, when we translate it is analysis of analyses, making the zoom pictures smaller. Meta analysis is analysis of analyses. The father of social science, meta analysis, gene glass is the one who coins the phrase, meta analysis. His quoted definition thereof is the statistical analysis of a large collection of analysis results from individual primary studies to integrate the findings. 

*Why Meta*: Lack of consensus in a field, identify areas where more research is needed, subjectivity of literature review, enhanced power for statistic test, parsimony, synthesize results from different operationalizations of same construct (different measures of stuent chievement with very different scales)

*Why hate Meta*: varying quality, missing data and reporting problems, difficult. quantitative meta-analysis does not replace narrative synthesis

Quantitative Meta-Analysis entails capturing the results in each primary study using an effect size that reflects the magnitude of the relationship between two variables and the direction of the relationship. Once the effect size(s) are calculated for each relevant primary studies, then the **effect sizes can be summarized to provide an overall average effect size** across studies, and sample and study descriptors that differ across studies can be explored as sources of heterogeneity (differences) in effect sizes.

There are **three primary parts** of quantitative meta-analysis that include
1) Finding the data to *calculate an effect size* (or effect sizes) capturing each primary study’s results  
2) *Calculate an average effect* recognizing different precisions  
3) Assess *sample and study characteristics* as predictors of effect sizes

once you have your effect sizes and their sampling error variances, everything else is straightforward. Pull them, test moderator hypotheses into publication bias. 

Getting to the point where you have data from which to *extract effect sizes and capturing and coding sample and study characteristics* involves (a lot of) additional work and training that we will *not cover*. In this workshop, the assumption is that you have already gathered up information that can be used to calculate effect sizes and coded sample/study descriptors

Choose the research question of interest.
Decide on inclusion strategy (which populations, outcomes, interventions/variables to include or exclude, study designs, etc.)
Can be a dynamic process
Creating *database* for calculating both *effect sizes and study/sample characteristics*.
**Gather as much detail as might be needed** (to avoid having to return to studies and re-code).
Studies will present descriptive and statistical data in a variety of ways.
**Keep formulas close at hand when selecting statistical results to use for calculating effect sizes**


# 1. Extract standadized Effect Sizes
effect size is a single number, single construct, statistical thing that captures really two things. It captures the *strength* of the relationships between two variables, like a treatment variable in an outcome variable, the strength of the relationship between the two variables of interest and the *direction* of the relationship.

1. *Standardized mean difference* - difference in interval-/ratio-scaled outcome for two groups (e.g., cognitive-behavioral therapy (CBT) intervention versus control group compared on depression)   
2. Pearson’s Correlation - standardized association *between two interval-/ratio- scaled* variables (e.g., association between anxiety and depression)
3. Difference in *dichotomous outcome for two groups* (several effect size choices) (e.g., CBT intervention versus waitlist control group compared on whether student is held back a year)
There are **other “effect sizes” that we will not have time to cover**. However, the core set of techniques and analyses you will learn are applicable to all effect sizes and their meta-analysis. We will learn how to test hypotheses about sample/study characteristics explaining variability in effect sizes
 
-    E.g., Differences in a CBT’s effectiveness in reducing depression as a function of the participants’ age 
-    E.g., Differences in the correlation between depression and anxiety associated with the socioeconomic status of participants
-    E.g., Differences in a treatment’s effectiveness on preventing student retention (held back a grade) that depend on the intensity of the treatment’s “dosage”

We will also learn how to handle a number of *complicated methodological dilemmas* typically encountered by meta-analysts.
Studies’ reporting **different statistics using different designs**
Dependencies in data - **multiple, related effect sizes reported**
**Missing data in terms of missing effects sizes** (Publication bias) and sample/study descriptor information (Missing “moderators”)

So it is very important that we are using sampling distributions and their characteristics (standard errors, means) that are a good fit with our sample’s test statistic’s empirical distribution.

## 1.1 Standardized mean difference

### 1.1.1 Independent Sample t-Statistic
![[Pasted image 20230324100746.png|200]] ![[Pasted image 20230324101033.png|200]] ![[Pasted image 20230324101340.png|230]]  ![[Pasted image 20230324101522.png|150]] 

*estimates* $\overline{Y}$ , *truth* $\overline{\mu}$,  $S_{(\overline{Y_1}-\overline{Y_2})}$ (as with all standard errors) is a function of the sample's standards deviation and of the sample size.where $S^2_P$ is the **pooled sample variance**, *weighted average of each sample's variance* estimates where the weighting is by a function of the sample size. $df_j$=($n_j$-1)for group j. 

We have the treated distribution of depression scores, and we have the untreated distribution of depression scores. *Both of those distribution have variances*. Both of the sample have estimates of the variances. *We typically assume homogeneous variances for our 2 groups*. So we are assuming that the treated groups, depression score variance equals the untreated groups, depression, score variance, which is why we just pull the two samples estimates of the variance together. 

### 1.1.2 Standardized mean difference $\delta$
![[Pasted image 20230324174646.png|100]]  ![[Pasted image 20230324180016.png|250]]  ![[Pasted image 20230324101340.png|230]] ![[Pasted image 20230324101522.png|150]] 
capturing the standardized difference between two groups on some interval- or ratio-scaled outcome. $\delta$=1, two group's means differeing by one standard deviation. or 50% of group 2's standardized scores are more than one standard deviation above group 1's mean, or 50% group 2 have higher scores than 84.13% of group 1
![[Pasted image 20230324175450.png|100]] ![[Pasted image 20230324175425.png|100]] 
==Different versions of effect size, and we will use bias corrected Hedges' g==
	**1. Glass's** $\delta$ uses $S_{Ctl}$ for S where $S_{Ctl}$ is the standard deviation of the control group. The treatment might affect variability in the scores, but the *reality* is most of the time we *assume homogeneous variances* for the treated and untreated or might know of it as additive treatment effect size. so then we are only using the information from one sample to get the standard deviation estimate, rather than actually using information from both samples to get a better estimate of sigma that we need in the denominator of our effect size. 
	**2. Cohen's d** uses the maximum liklihood estimate of $\sigma$, where  ![[Pasted image 20230324181245.png|100]] ![[Pasted image 20230324181104.png|150]] also, ![[Pasted image 20230324181435.png|100]] where N=(n1+n2). this is biased with small sample size, so no one use it.
	**3. Hedges' g** uses the *pooled sample variances* $S^2_p$ , weighted average of the two independent groups' sample variances ![[Pasted image 20230324181348.png|100]]
		- Hedges found his g follows ![[Pasted image 20230324181652.png|100]] , J(m) is a function of the gamma function ![[Pasted image 20230324181809.png|150]] , where for two independent samples, the degrees of freedom, **m=(n1+n2-2)**. this j of m is this really unpleasant and there's no conceptual way to explain it. This is the bias correction that we need to get an estimate of delta that is not biased. Simpler format of bias correction ![[Pasted image 20230324183016.png|150]].  ![[Pasted image 20230324183243.png|300]] this table showes the samller sample size is, the more bias correction we need.
		- we want to unbiased estimator where E(g)=$\delta$, unbiased estimate of $\delta$, $\hat{\delta}$ ![[Pasted image 20230324182659.png|100]] . 
		- Notation: people use **g** for *Hedges' bias-corrected estimator* and use **d** as the *biased estimator* (not representing Cohen's d)

### 1.1.3 Variance of delta estimates
Hedges' g, Cohen's d, and the bias-corrected version of g- $\hat\delta$ are assumed to follow the same large sample asymptotic distribution. The large-sample sampling distribution of g is approximately normal with a population variance of 
This is population parameter ![[Pasted image 20230324184210.png|300]]  This is what we used for **sample estimation**![[Pasted image 20230324185243.png|300]] , here the g represent bias corrected Hedges's g.
Thing that should make you uncomfortable is that the variance of the sampling distribution is a function of the parameter itself. we still use this formula for the variance, because this little second term is typically pretty small, because delta and their estimates tend to be pretty small. The scale the variance is very small. 

### 1.1.4 Calculate effect size in R
Wolfgang Viechtbauer is constantly updating **metafor package**. *m_Ctl* Control group's mean; *m_Tx* Treatment group's mean; *sd_Ctl* Control group's SD; *sd_Tx* Treatment group's SD. **escalc function calculate delta and its variance**
![[Pasted image 20230325085356.png|400]] ![[Pasted image 20230325091514.png|250]] ![[Pasted image 20230325091933.png|500]] 

If the sample size on which the d is based is sufficiently large, then the assumption of a normal distribution works well. However, a **t distribution** with m=n1+n2-2 degrees (when two independent samples are being compared) of freedom *works better.* we then use ![[Pasted image 20230325090626.png|150]] calculate confidence interval estimates of $\delta$. 

Caclulating delta from **diferent kinds of data**
	1. $\overline{Y_j}$ , $S_{\overline{Y_j}}$ **Standard error of means** , no $S_j$, j indexs group. 
		- Standard error of means, not standard deviation of group j  ![[Pasted image 20230325163917.png|80]] ![[Pasted image 20230325163947.png|150]] ![[Pasted image 20230325164116.png|400]] 
	2. Independent samples **t statistic**
		- based on previous t statistic function and d function. ![[Pasted image 20230325165104.png|120]] ![[Pasted image 20230325165229.png|350]] ![[Pasted image 20230326113819.png|300]]  ![[Pasted image 20230326114411.png|400]]  
		- ![[Pasted image 20230326113545.png|300]] using this code: The problem is that if you have a larger sample size in a primary study, the direct calculation using this gamma function for larger sample sizes, the rounding is problematic, and it won't calculate. And it will introduce missing data and a into your data frame. So do use the code above :)
	3. **2-tailed p-value** for independent samples t, *sign* of ($\overline{Y_1}$ - $\overline{Y_2}$)
		- get t statistic value from p and the direction
		- ![[Pasted image 20230326114820.png|400]] this provide the *positive t value* and *df=n1+n2-2* ![[Pasted image 20230326115038.png|400]] 
	4. 1-tailed p-value for independent samples t
		- ![[Pasted image 20230326115602.png|400]] not divided p by 2
	5. **Two-independent group's ANOVA** results: F(d$f_B$=1), sign of ($\overline{Y_1}$ - $\overline{Y_2}$)
		- The challenge is gonna be, if you see an F ratio recorded, making sure that it is the right kind of F ratio from. It's an F ratio for a one way ANOVA, where the between groups factor is the two independent groups
		- when only two groups in ANOVA ![[Pasted image 20230326120208.png|300]] d$f_{Error}$=m=n1+n2-2. remebre multply sign to get the t statistic
	6. p-value for 2-independent groups' F(d$f_B$=1), sign of ($\overline{Y_1}$ - $\overline{Y_2}$)
		- ![[Pasted image 20230326120747.png|200]] p is the two-tailed p-value, df1= the number of groups being compared minus one, df2=error degrees of freedom=(n1+n2-2) ![[Pasted image 20230326121053.png|350]] 
		- or **F ratio p=t test p**, just use fomula under 2-tailed p-value
	7. Three-independent group's ANOVA results F(d$f_B$=2), sign of ($\overline{Y_1}$ - $\overline{Y_2}$)
		- Review ANOVA to see how knowing the  $\overline{Y_j}$ , $n_j$ and F-ratio can be used to calculate $s_p$ and thus g
		- ![[Pasted image 20230326121517.png|300]] G is the number of groups (here, three), $n_j$ is the sample size for group j,  $\overline{Y_j}$ is the sample mean for group j, $\overline Y$. is the grand mean (mean of the entire sample irrespective of group membership)
		- ![[Pasted image 20230326155523.png|300]] We can calculate $MS_W$ mean squared within if we know F ratio and $MS_B$ (calculated form $\overline{Y_j}$ ). *$MS_W$ is actually pooled sample variance, it represents the average variability within each group*. A  high F-ratio indicates that the between-group variability is greater than the within-group variability, suggesting that there are significant differences between the group means.
		- ![[Pasted image 20230326160647.png|100]] biased estimate
		- ![[Pasted image 20230326160900.png|500]] ![[Pasted image 20230326160943.png|500]] ![[Pasted image 20230326161113.png|400]] 
	8. p-value for 3-independent group's ANOVA results F(d$f_B$=2),all three groups' $\overline Y_j$s 
		- $df_B$=number of goups -1. $df_W$=df1+df2+df3=(n1-1)+(n2-1)+(n3-1), also known as $df_{Error}$ 
		- ![[Pasted image 20230326161431.png|400]]

### 1.1.5 Calculating the Standardized Mean Difference from repeated measures design data
**Repeated measures** *variablity of change scores within a person* (how an individual changes as a result of a treatment) vs. **Independent group** measures *variability of raw scores within group* (comparative effectiveness of two treatments)
1. **Pre- and Post design**, matched pairs' scores.
	- For repeated measurement (**RM**) metric
		- $D_i$=$Post_i$-$Pre_i$ ,  $\overline D$= ($\overline {Y}_{Post}- \overline {Y}_{Pre})$  
		- One sample size t-test, use difference score ![[Pasted image 20230326172507.png|300]]  ![[Pasted image 20230326172841.png|100]] ![[Pasted image 20230326172914.png|300]]
		- $\mu_{D_0}$ is the null hypothesized value for the true mean difference. $S_{\overline D}$ is the sample standard error of the $\overline D$ , and n is the number of pairs of scores. sample variance of the difference scores  $SS_D$ is the sum of squared differences in difference scores.
		-  ![[Pasted image 20230326201712.png|200]] ![[Pasted image 20230326201025.png|200]]  ![[Pasted image 20230326201801.png|150]] ,  ![[Pasted image 20230326173211.png|170]] 
		-  $\sigma_D$ is the *standard deviation of the difference scores*. $\sigma$ represents, assumed *homogeneous, standard deviation of the pre and post-test score distributions*.  $\rho$ is the *correlation between pre- and post-test scores*. 
		- Variances of estimate ![[Pasted image 20230326203236.png|150]]  and bias corrected version ![[Pasted image 20230326210426.png|150]] 
		- Sample version of some equations ![[Pasted image 20230326204454.png|100]] r is correlation between pre- and post- test scores.  
		-   ![[Pasted image 20230326203310.png|200]] degrees of freedom m=n-1, where n is the number of participants in the RM design   
		- Other statistics maybe useful to convert ![[Pasted image 20230326204907.png|70]] ![[Pasted image 20230326204936.png|70]] ![[Pasted image 20230326205145.png|400]] ![[Pasted image 20230326210006.png|200]] ![[Pasted image 20230326210052.png|100]] 
		- *complicated* way to present the same function we used for *independent goup design* ![[Pasted image 20230326211641.png|200]] ![[Pasted image 20230326211658.png|200]] ![[Pasted image 20230326211805.png|100]] ![[Pasted image 20230326211826.png|200]]
	- **RM to IG**
		- because ![[Pasted image 20230326202635.png|130]]  ![[Pasted image 20230326201801.png|150]], so ![[Pasted image 20230326202659.png|130]] ![[Pasted image 20230326202925.png|300]] 
		- ![[Pasted image 20230326204702.png|300]] and biase corrected version ![[Pasted image 20230326210606.png|300]]
		- and  and  another way: ![[Pasted image 20230326203046.png|200]] ![[Pasted image 20230326203120.png|220]] 
	- **IG to RM**
		- ![[Pasted image 20230326202834.png|220]] 
	- ==R code to practice==
		- ==remain to complete. start from Day1 pm-1, 1:04:14==
2. **IGRM** (Independent groups, repeated measures) design repeated measures in treat and control groups
	- notation: *IGrm means IG metric version* obtained from IGRM design data and RMig means RM metric
	- **IG** metric
		- ![[Pasted image 20230327085518.png|200]] , is the difference in the $\delta_{IG_{RM}}$ for the Treatment ($Tx$) versus the control (Ctl) group
		- ![[Pasted image 20230327085821.png|300]] , or we can pooled $S_{pre}$ because we have two groups (Tx and Ctl) of pre score. so that will be ![[Pasted image 20230327085944.png|300]]  
		- ![[Pasted image 20230327090106.png|200]] ![[Pasted image 20230327090128.png|350]] 
		- ![[Pasted image 20230327090250.png|200]] Tx and Ctl are independent, so it meets equation ![[Pasted image 20230327090342.png|300]] and then because ![[Pasted image 20230327090504.png|300]] , finally ![[Pasted image 20230327090533.png|300]] 
	- **RM** metric
		- ![[Pasted image 20230327090722.png|200]] 
		- ![[Pasted image 20230327091107.png|300]] ![[Pasted image 20230327091349.png|400]] ![[Pasted image 20230327091423.png|200]] ![[Pasted image 20230327093543.png|200]] 
		- ![[Pasted image 20230327093621.png|400]] 
	- Examples and ANCOVA version and other practiced version to calculate under different situations
		-  ==remain to complete. start from Day1 pm-2, 17:44==

## 1.2 Pearson's Correlation estimates, r
*the coefficients of regression model is not the same thing with correlation*.  They are partial correlation functions, and only if it is simple linear regression. then the standardized coefficients eaqual to the correlation.
### 1.2.1 Estimating Pearson's Correlation
- This is the *maximum liklihood estimator* of the population correlation. An expected value is the long run average. So you take samples of individuals, calculate correlation estimate, calculate another one for another sample. You build your sampling distribution of estimates of the correlation. The expected value is the average of all of those estimates of the correlation. And remember, your sampling distribution is based on each correlation is based on the same sample size. For non-extreme values (close to |0.5|), the worse the bias is. The larger n, the less bias.
- ![[Pasted image 20230406114333.png|300]]  ![[Pasted image 20230406114508.png|300]] ![[Pasted image 20230406114750.png|200]] 
- The large-sample (for n= seveal hundred) sampling distribution of rxy is assumed to follow a *t-statistic* distribution (*df=n-2*) with a mean of $\rho$xy and *variance* of ![[Pasted image 20230406115239.png|100]] , the sample version is ![[Pasted image 20230406115306.png|100]] , confidence interval ![[Pasted image 20230406120721.png|100]]
- ![[Pasted image 20230406121023.png|300]]  
### 1.2.2 Fisher's Zr Transformation
- Meta-analysts has different opinions about whether or not to use Fisher's Zr transformation
- the challenges with the correlation are its variance depends on the parameter. The shape of the distribution for estimates of r can be particularly skewed, especially when the correlations true value is strong, whether it's strong negative or strong positive. the *distribution of r* is only approximately normal and with *skew* that gets worse for more *extreme values* for $\rho$. Fisher derived a commonly used transformation. 
- ![[Pasted image 20230406121530.png|150]] Back-transformation ![[Pasted image 20230406122439.png|150]] variance ![[Pasted image 20230406123335.png|100]] , follow z distribution
- when close to 0, r and Zr is similar. the sign is always the same between r and Zr
- DescTools package
	- calculate Zr ![[Pasted image 20230406123831.png|140]] Back-transform Zr to obtain r ![[Pasted image 20230406123838.png|200]] 
- escalc package
	- ![[Pasted image 20230406124431.png|500]]  
### 1.2.3 Calculate
*If* you do *use* the *Zr transformation*, then analyses are run using Zr instead of r. Once analyses are completer, you need to *back-transform* the result to the r metric for a *pooled estimate and confidence interval* of the estimates of the correlation.
1. **Calculate effect size** variance for each study
	- Calculate variance of correlation ![[Pasted image 20230406125438.png|230]] ![[Pasted image 20230406125618.png|500]] ![[Pasted image 20230406125702.png|400]] 
	- Calculate z transformed and its variance![[Pasted image 20230406125743.png|500]] 
1. **Pooling Correlations**
	- This dataset is quite *samll* with only *16 correlations* and although there is some within-study dependence, it's so minimal that we are going to *ignore the dependence* (there are *only 2 studies that reported all of two effect sizes*).
	- ![[Pasted image 20230406130358.png|600]] ![[Pasted image 20230406130422.png|600]] Zrs code should add test="knha". It'll affect the standard error.
2. **Within-study dependence**
	- metaSEM package contains the following dataset.
	- classroom management self-efficacy (CMSE) and each of three variables including emotional exhaustion (EE), depersonalization (DP), and (lowered) personal accomplishment (PA)
	- original ![[Pasted image 20230406132509.png|500]] add n ![[Pasted image 20230406132948.png|500]] 48 effect sizes from 16 studies, which is quite a small dataset to be using with RVE
	- original author do not provide the sample size per correlation, bu we know the r and vr, so ![[Pasted image 20230406132705.png|100]] 
	- ![[Pasted image 20230406132805.png|500]]
	- ![[Pasted image 20230406133100.png|300]] ![[Pasted image 20230406133209.png|500]] 
	- ![[Pasted image 20230406133347.png|400]] ![[Pasted image 20230406133445.png|400]] ![[Pasted image 20230406133504.png|500]] 
	- **GLS for dependence**
		- psi between two correlations ![[Pasted image 20230406140057.png|500]] 
		- psi for two Zr ![[Pasted image 20230406204943.png|200]] 
3. **Moderator model**
	- per_fem *percent female*. Its values *only differ across studies*, not within studies. Thereforem we do not need to create the within- and between-studies versions of the moderator. But, let's *grand-mean center it*.
	- ![[Pasted image 20230406133844.png|500]] or, create mean center var first ![[Pasted image 20230406133945.png|400]] 
	- ![[Pasted image 20230406134058.png|400]] ![[Pasted image 20230406134303.png|500]] 
		- interpretation of this first coefficient is the predicted fisher transformed old correlation between the personalization cmsc for a study using the average% female in their sample. you might want to use back transform the result into the correlation matrix and in the correlation metric to make it more understandable.
		- The ee coefficient is the fisher transformed pooled estimate of the correlation predicted for emotional exhaustion. 
		- female says for two studies that differ by one in terms of their percent female of their sample, the same the study with the higher% female is predicted to have a more positive by.0197 correlation, whether it's dp or ee or pa correlation
4. **publication bias**
	- ![[Pasted image 20230406205543.png|300]] model estimated measure-specific Fisher-transformed correlations. Use GLS to recognize within-study dependence using a $\Psi$ matrix created using the imput_covariance_matrix function.
	- ![[Pasted image 20230406205720.png|300]] ![[Pasted image 20230406205736.png|300]] ![[Pasted image 20230406205753.png|400]] ![[Pasted image 20230406205939.png|200]]
	- Egger's regreesion
		- transformed Zr to avoid dependence between effect size estimate and variance of the estimates
		- don't need regtest, just use meta regression and replace predictor with standard error of the effect sizes
		- ![[Pasted image 20230406210636.png|600]] 
	- Trim & Fill
		- ![[Pasted image 20230406210826.png|400]] 
		- ![[Pasted image 20230406210953.png|500]] 
	- Selection model
		- ![[Pasted image 20230406212317.png|400]] 
		- when you use no intercept model , there is still intercept coef. but this intercept is reference group, not the traditional intercept
		- one tail test. have to *make all effect size positive*. eg. if *self-efficacy and emotional exhaustion is negative*. then *reversed* the direction of the correlation and interpret it as relation between *self-efficacy and lack of emtional exhaustion*
## 1.3 Dichotomous outcome
1. **risk difference(difference in proportions)**, 
	- ![[Pasted image 20230406220041.png|200]] ![[Pasted image 20230406220058.png|160]] ![[Pasted image 20230406220129.png|300]] ![[Pasted image 20230406220206.png|200]] this effect size can be assumed to be approximately normally distributed. CI ![[Pasted image 20230406220319.png|100]]
	- ![[Pasted image 20230406220442.png|400]] 
	- not suggest to use the risk difference because the variance of $\hat \Delta$ is affected by the value of the proportions $\pi_1$ and $\pi_2$ . With more variability for true proportions closer to 0.5 then for true proporteions closer to the extreme values (0 and 1).
2. ratio of two probabilities = **(log of the) relative risk**, 
	- ![[Pasted image 20230406221112.png|200]] ![[Pasted image 20230406221402.png|300]] ![[Pasted image 20230406221431.png|200]] 
	- ![[Pasted image 20230406221648.png|400]] this gives you lnRR instead of RR. make sure exp() the estimates.
	- limitation: given a  value of f for one of the probabilities, asy $\hat \pi_2$, the range of mathematically possible values for the resulting $RR_S$ is from zero up to 1/f. This could lead to the misleading appearance of heterogeneity in studies' RR sizes only because the values of studies' $\hat \pi_2$s differ.
	- The heterogeneity estimated for a set of $RR_S$ can look very different if success versus failure is the focus. 
3. **(log of the) odds ratio**
	- ![[Pasted image 20230406224800.png|300]] ln(OR) is effect size ![[Pasted image 20230406225154.png|200]]  ![[Pasted image 20230406225222.png|400]] ![[Pasted image 20230406225618.png|200]]
	- if any of the cell frequencies are too small (nij<5), then it is recommended to add 0.5 to each cell's frequency before calculating the OR and $V_{ln(OR)}$ .
	- ![[Pasted image 20230406225639.png|500]]
4. **Pooling Effect Size**
	- samll size, 6 studies
	 - ![[Pasted image 20230406230419.png|300]] ![[Pasted image 20230406230433.png|300]] ![[Pasted image 20230406230503.png|300]] ![[Pasted image 20230406230519.png|200]] ![[Pasted image 20230406230725.png|400]]
		 - patients in the treatment group, those who receive idocaine are estimated to have 2 . 94 % higher probability of death than patients in the control group. 
	 - ![[Pasted image 20230406231014.png|400]] ![[Pasted image 20230406231032.png|400]] 
		 - exp(0.53)=1.699. on average the relative *probability (risk) of death* for those in the treatment versus control group is *1.699 more likely*.
	- ![[Pasted image 20230406231243.png|500]] ![[Pasted image 20230406231259.png|400]] 
		- pooled fixed-effects ln(OR) estimates is 0.5677 which translates into an odds ratio, OR, of 1.7642 indicating that on average the odds of death is higher for the treatment than for the control group.
5. Dependent effect size
	- RVE_Tip.CSV ![[Pasted image 20230406231645.png|600]] 
	- ![[Pasted image 20230406231806.png|300]] 
## 1.4 Other equations | effect size
- ![[Pasted image 20230406233057.png|200]] ![[Pasted image 20230406233110.png|150]] 
- ![[Pasted image 20230406233236.png|300]] ![[Pasted image 20230406233302.png|300]] ![[Pasted image 20230406233316.png|400]] 
- ![[Pasted image 20230406233413.png|400]] ![[Pasted image 20230406233428.png|400]] 
# 2. Pooling effect size (intercept only), t statistic & Meta-regression (with predictors)
This is actually the weighted meta regression with intercept only.
Fixed, Random, and Mixed-effect, Q statistic to test assumption of homogeneous effect sizes. T represents effect size estimate and  𝛳 represents effects size parameter.
## 2.1 Fixed effect model
 ==fixed-effects model==, it is assumed that the variability in **effect size estimate values results solely from sampling error**. Each study's estimate is sampled from a population with a known true effect size value.
	- If it can be assumed that each of the k studies used the same sample size, n, then a simple average of the k studies' effect size estimates could be computed to provide the best estimate of the *population effect size parameter*:![[Pasted image 20230318185234.png|70]]
	- When unequal sample size per study, weighted averages are commonly used. Larger sample size based estimates are going to be more precise. **Precision was pretty much the inverse of the vairiability of a sampling distribution, the inverse of the variance of the estimator**, the more precise, an estimate, the smaller the standard error of a sampling distribution.
	- Studies with more precision (typically associated with larger sample sizes) will be given more weight in the computation of the combined/ synthesized/ pooled final estimate of the effect size parameter.
	- Under fixed effect model, the true effect size for study i is the same: ![[Pasted image 20230318190628.png|150]] 
	- Each study i, has a sampling error variance, $V_{Ti}$ , that is associated with its effect size estimate, Ti. This $V_{Ti}$ captures the precision of the associated effect size estimate, Ti. It seems ideal to use some function of the effect size estimate's precision as the weight we assign to each effect size when pooling them across studies. Our weighted **average estimate of θ would be calculated** as: ![[Pasted image 20230318192241.png|100]] ![[Pasted image 20230318192332.png|80]]  variance of the estimator.
	- The variance of the pooled (weighted) effect size estimate $\overline{T.}$ , is ![[Pasted image 20230318194045.png|180]] 
	- We typically assume that the sampling distribution of pooled estimates of $\delta$ , the $\overline{\delta.}$ s, follows the t distribution for the simplest kind of data such that ![[Pasted image 20230319111618.png|150]] . rma metafor function in r and most assume a normal distribution. Again, it is actually, the distribution is better approximated with a t statistic. When each study has one effect size then degree of freedom is number of studies k-1. $\delta_0$ is typically 0
		**1. Pooling effect size with fixed effect model**
			- Hand calculation: It's useful to do things by hand when you can just for single examples so that when you start using a black box of code, what that black box is doing because there's lots of defaults built into any black box code, including our functions of packages, knowing how to do things by hand programming, helps you really understand that the code is doing what you wanted to do
			- The estimates, bias corrected hedges gs, which i'm *calling delta* in my dataset. ![[Pasted image 20230319205800.png|110]] n.tx means number of treatment, n.ctl means number of control.
			- **By hand**: sampling error is calculated ![[Pasted image 20230319210018.png|300]] ![[Pasted image 20230321114713.png|300]]
			- **By software**: ![[Pasted image 20230321120939.png|500]] ![[Pasted image 20230321121143.png|500]]  ![[Pasted image 20230321121704.png|200]] 
			- *k is the number of studies*. The null hypothesis: $B_0$=0. *Change to t distribution's p value*. the test statistic of t distribution (tval) and z distribution (zval) are the same. just p value differences
		**2. Fixed effects meta-regression models**
			- expanding intercept only model to include moderator variables, but the residuals in the model is assumed to be just sampling error. centered interval-scaled/ratio-scaled moderators. categorical moderator. no-intercept models
			- example data: researcher gathered a set of estimates of $\delta$ capturing the effect of **parent involvement interventions** (control without intervention) on **academic achievement**. *School.type variable*: whether the sample consisted primarily of private, charter, or public school kids. PerBus: the precent of the sample who were school-bus-users. ![[Pasted image 20230322084933.png|300]] . private=0, charater=1,public=2. the bias corrected estimate of delta called delta, and associated sampling error variance of fixed effect.
			- ![[Pasted image 20230322085816.png|150]] ![[Pasted image 20230322085904.png|450]] ![[Pasted image 20230322090213.png|350]] ![[Pasted image 20230322090521.png|500]] 
			- intercept only model doesn't need to specify model.the p value when you're using rma is always a two tailed p. if you have multiple moderators, very difficult to figure out how to tell the software do a one child test in this direction for this moderator, or make sure you do it in a different direction for this other moderator. For two studies that differ by one on their % bussing variable, predicted *difference in the parent involvements effect on academic achievement is . 0177*. 
			- ![[Pasted image 20230322091511.png|350]] using rma to get mean centered moderator. ![[Pasted image 20230322091733.png|200]] centering changes intercept and intercept (SE).
			- *make sure the nominal variables are categorical ("factor")* not interval-or ratio-scaled ("numeric"). regression model will sutomatically converts the nominal variable to a set of dummy-cided moderator variables. If we treat nominal as numeric, it would be difficult to interprete. Because a change for two studies that differ by one on school type, which two are we comparing? So the more the school type, the stronger the effect. we will dummy code the categorical and use private school as the reference category
			- ![[Pasted image 20230322092600.png|200]] ![[Pasted image 20230322092622.png|350]] ![[Pasted image 20230322092648.png|450]] ![[Pasted image 20230322093112.png|350]] ![[Pasted image 20230322093136.png|500]] 
			- if researcher wanted to test the following *omnibus test*: $H_0$: Parent involvement treatment effects on academic achievement *do not differ as a function of school type*. We cannot use individual predictor's slopes. We could use the model's QM, which captures the variability in the effect size explained by the pair of modelrator variables togehter. Here, QB=QM=98.5314
			- Instead of reporting coeff, Sometimes it's helpful to prove to translate those coefficient estimates into values that they might want to make sense of. what is my predictive treatment effect for studies with certain values on the set or individual moderator? 
			- ![[Pasted image 20230322094143.png|500]] to get school type specific outcome.
			- Or we can use and althernative *model without intercept*. ![[Pasted image 20230322094311.png|250]]  ![[Pasted image 20230322094404.png|400]] ![[Pasted image 20230322094611.png|300]]
			- *Testing Nested models* ![[Pasted image 20230322094818.png|400]] ![[Pasted image 20230322094839.png|400]] calculate p by hand![[Pasted image 20230322095001.png|400]] or use anova ![[Pasted image 20230322095037.png|300]] 

## 2.2 Random effects model
Under the ==random-effects model==, it is not assumed that there is a single population effect size parameter. Instead, it is assumed that *there is a population ("universe") of parameter values*. some of the variablity among effect size estimates is due to variability in effect parameters and the rest is due to sampling variability. 
	![[Pasted image 20230318102521.png|500]] ![[Pasted image 20230318102635.png|345]]
	- In general, the random effects model is essentially *a multi level model*, is that *iterative estimation* is required for better estimates. And you do *need to have a reasonable amount of variability between studies and number of studies to get the good estimate* of the random effects variability.
	- Choice of model affects estimates of the standard error associated with the relevant model's parameter estimates. The *standard error* associated with *random-effects analyses are typically larger* since they include the 
		1. variability of studies' parameter values in the universe of (super-population) of parameter values.
		2. sampling error variability
	- The **random-effects variance**, $\tau^2_{\theta}$ , between study variability, is incorporated into the weights used for pooling. The random-effects variance for study i's effect size estimate is: ![[Pasted image 20230318214721.png|150]] . $V_{i,FE}$ is the sampling error (within studies)
	- Once we have the random-effects variance of each study's effect size estimate, we can convert it into its precision and use that as the weight used to calculate our **random-effects pooled estimate** of $\mu_{\theta}$ : ![[Pasted image 20230318215357.png|100]] ![[Pasted image 20230318215428.png|170]]
	- **Simple unweighted total variability in effect size estimates**: ![[Pasted image 20230319093434.png|130]] $\overline{T}$ is the simple mean of the effect size estimates. The total vairability $S^2_T$ is a function of both between- and within-studies variability: ![[Pasted image 20230319093719.png|300]] $\sigma^2_{T_i|\theta_i}$ is sampling error. Simple version is ![[Pasted image 20230319094455.png|200]] . So ![[Pasted image 20230319094806.png|100]] , ![[Pasted image 20230322104559.png|150]] it is possible to have negative values as the estimates of $\tau^2_\theta$ , be sure to set negative values to zero (although we won't use this formula). *There is a number of different iterative estimation procedures* you can use. That will give us better estimate of $\tau^2_\theta$ .
	-  *KH Standard Error correction*: 
		- ![[Pasted image 20230321123037.png|400]]
		- 在进行meta-analysis时，我们通常需要考虑不同研究之间的异质性（heterogeneity），即研究效应的差异不仅仅是由于抽样误差所导致的，还可能受到其他因素的影响，如研究设计、样本特征等。在这种情况下，我们可以使用随机效应模型（random effects model）来估计研究效应的真实分布，从而更好地解释和预测研究效应。然而，由于*不同研究的样本量和研究效应的方差可能不同*，因此*随机效应模型可能存在偏差*。为了解决这个问题，可以使用*KH标准误校正*（KH standard Error Correction）方法，该方法可以有效地纠正随机效应模型中的偏差，并*提高效应估计的准确性*。KH标准误校正方法是一种基于最大似然估计的方法，它可以考虑不同研究中的样本量和效应方差的异质性，并进行校正，从而得到更为准确的效应估计和置信区间。该方法的基本思想是对随机效应模型中的方差进行重新估计，从而得到更为准确的标准误和置信区间。通过KH标准误校正方法，可以降低随机效应模型的偏差，提高meta-analysis的效果和可靠性。总之，KH标准误校正方法是一种有效的纠正随机效应模型偏差的方法，在meta-analysis中应用广泛，能够提高效应估计的准确性和可靠性。
	- many meta analysts make the *assumption that our estimates of delta gs are normally distributed* and use statistic for constructing testing statistical significance and constructing confidence interval estimates for delta. *This sd for random effects* are too *small*.
	- The defult of rma function is to do random effects. But this random effects default does not include the sd correction. So you have to specify in the "test" parameter ![[Pasted image 20230321123553.png|400]]
## 2.3 Mixed effects model
Under a ==mixed effects model==, *some of the random variability* between studies in effect size is *explained* using study or *sample characteristics (fixed effects)* while the *remaining variability is attributed to unmeasured differences among studies' parameters (random)* and to sampling error.
	- we're gonna model variability in the residuals as random effects
	- generally, like when pooling effect size, we prefer mixed model than fixed model in meta-regreesion, but there is Q statsitic to test. $Q_W$ (the QE output by rma) which tests the residual variability to see if there is more than we'd expect under an assumption that residual variability is soley sampling error.
	- In random effect model for pooling effect size, random effects equal to *total variability around the simple mean of the effect sizes* minus the sampling error variability. However, the *simple mean* of the effect sizes is *not our best predicted value* when we actually have some moderator in *meta aggression model*. It is not just a pooling model with only an intercept, but actually includes some moderator in there. Then we're still gonna get similar random effects structure. Estimate of the **conditional** $\tau^2$ (between studies, random-effects) variability in the residuals.
	- ![[Pasted image 20230322105631.png|200]] we use the **total variability in the residuals, (Ti-T'i)** rather than in the **effect size estimates, (Ti- $\overline{T}$ )** . because we have moderator in our model. this is a *conceptual formula* that we might use to estimate the random effects component that we're gonna use in our weights. But the reality is, in the iterative estimation procedures that are built into the metaphor are made package and other meta aggression packages. You're not actually gonna use this conceptual formula to do the calculating of that between studies random effects, variability in the residuallized effect sizes. 
	- **Miexd-effects model weights** ![[Pasted image 20230322111059.png|150]] vi is sampling error. $\tau^2_{ME}$ is radom effects, between studies variability in the residulized effect sizes (part of variability not explained by moderators). 
	- ![[Pasted image 20230322111734.png|400]] ![[Pasted image 20230322111926.png|500]] 
	- When we used Knapp-Hartung correction, we use t over the z, F-ratio for testing the set of moderators over $\chi^2$ statistics of QM
	- **Test for Nested model**. ![[Pasted image 20230322113600.png|400]] ![[Pasted image 20230322114210.png|500]] The defualt is RMEL in mixed model, so in order to use anova to test nested model, we need to specify method="ML". 
		- *REML (Restricted Maximum Likelihood)* is a statistical method used for estimating the parameters of linear mixed models (LMM) and generalized linear mixed models (GLMM). It is an extension of the maximum likelihood method that addresses the bias in the estimation of the variance-covariance matrix of the random effects in LMMs and GLMMs. The *standard maximum likelihood (ML)* method estimates the variance-covariance matrix of the random effects based on all the data, including the fixed effects. However, this approach can result in *biased estimates of the variance-covariance matrix*, particularly *when the number of fixed effects is large* compared to the sample size. *REML* addresses this issue by using a likelihood function that is derived from the *residual sum of squares obtained after the fixed effects have been removed from the model*. By conditioning on the fixed effects, REML provides an unbiased estimate of the variance-covariance matrix of the random effects. This method is particularly useful in situations where the fixed effects are of secondary interest, and the focus is on estimating the variance-covariance matrix of the random effects. In summary, REML is a statistical method used for estimating the parameters of LMMs and GLMMs that provides an unbiased estimate of the variance-covariance matrix of the random effects by conditioning on the fixed effects.
		- Or more efficiently, use Knapp-Hartung's correction estimate the full model.
		- ![[Pasted image 20230322113932.png|400]] so the output is ![[Pasted image 20230322114018.png|400]] then use code to run a test of 4th and 5th coefficients together: ![[Pasted image 20230322114109.png|400]] 

## 2.4 Testing Homogeneity of effects - Q Statistic
Homogeneity test statistic Q, is used to test statistically whether the between-studies variance component, $\tau^2_{\theta}$ , differs significantly from zero. The null hypothesis, *$H_0$*, associated with use of this first Q statistic is that *effect size estimates are homogeneous*. $H_0$: $\tau^2_{\theta}$=0. effect size are assumed sampled from a population with a single true parameter and thus that the variability in effect size estimates is solely a function of sampling error. 

If insufficient evidence is found to reject the $H_0$ of homogeneous effects (i.e., **fail to reject H0**), then when combining effect size estimates, a **fixed-effects model can be assumed**.
	However, if the *$H_0$ is rejected*, then the meta-analyst should recognize the added variability (hterogeneity of parameters accross studies) when pooling estimates and *assume a random-effects model*. **For pooling, we would assume just a random effects model.**
	Or, if the $H_0$ is rejected, then the meta-analyst can try to *explain some of the variability* in effect size estimates *using study/sample characteristics*.
		The homogeneity of the effect size estimates after *controlliing for differences in these charaacteristics* can then be re-evaluated to *see whether to assume a fixed or random-effects model* **for the residuals**.

The conceptual formula for Q is: ![[Pasted image 20230318210408.png|150]] , under $H_0$ can be assumed to follow a $\chi^2$ distribution with k-1 degrees of freedom.
	- It's *not the one that's typically used in software*, because there's too much rounding error involved in their simplifications or computational formulas that are typically the ones used
	- It's very much like an F ratio. We calculate the **squared deviations**, *how much each effect size estimate varies from the pooled estimate* and compare that to the relevant sampling error variance. We're looking at how much variability there is in comparing it to what we would expect. If it were just due to sampling error. Our **Vs are sampling error variances that we calculate for each effect size**. That says *how much sampling error variability* there is for each effect size.
	- The larger your cue statistic is, the more variability we're seeing in our effect size, then we would expect given sampling error. When the Q statistic is large, we reject the assumption that sampling errors is the only thing that making our effect sizes vary. 

The computational formular is: ![[Pasted image 20230318211827.png|200]] 

The $\chi^2$ is sensitive to sample size
	This means that we might end up rejecting the $H_0$ for very small amounts of heterogeneity

Descriptor of homogeneity $I^2$ : ![[Pasted image 20230318212827.png|200]]  the proportion of the total variability that you see amongst the effect sizes that has to do with between study variability in effect size parameters
	- rules of thumb for interpreting $I^2$
	- can be used to complement the statistical test (Q) of homogeneity

# 3. Within-study dependence
**Dependence sources**
	- In a **multiple-treatment study**, there might be multiple treatments being compared with a single comparison condition
	- In a **multiple-outcome study**, there might be a single treatment being compared with a single control condition however the comparisons are conducted using *multiple, related outcomes* (this dependence is not only comes from same individuals).  
	- **Other soures**, might have within-study dependence either from the use of a common control group- study design artifact- or from using correlated measures (or other example). We might not have yet the known variances and covariances. And more importantly, you might not have all the values you need to calculate them
		- MT and MO
		- ![[Pasted image 20230331202626.png|500]] 

**Ignoring Dependence** sides effects
	- the same problems as encountered in primary study data analyses when we ignore dependence in our data. Resulting *SE estimates incorrect (small)* and thus your test statistics and associated inferences
	- What if *choose one effect size* per study?
		- How will you choose which effect size to include?
		- why introduce missingness into your data? Especially when we have a number of ways to handle this dependence
		- because you're going to reduce the power, by lowing the number of effect size of your estimating, you're introducing missing data. You could introduce bias depends how you select the effect size to include and exclude. And you are removing interesting source of variability in your data.
	- How about i use some *weighted mean effect size for each study*
		- So this is like when in regular primary data analysis, you have individuals within classrooms, in your sample, and you say, I don't want to handle that within classroom dependence and learn multilevel modeling or robust standard errors. I wanna use a mean score for each class and just analyze that. So you are not then gonna be able to explore individual differences and how they influence outcomes, because you're aggravating everything to the class level. I think it's called the *ecological fallacy* where if you're just aggravating, then you're talking about things at the aggregate and things within the class might look somewhat different than the relationships amongst variables across classes. Meta analysis, all the same thing would apply
		- again *lose information*
		- *limite* moderator analyse *to between-study moderators*
	- Dived my studies' effect size into sub-groups and just look at effect sizes by *sub-group*? (shifting unit of analysis)
		- lose ability to test differences and moderator effects across (dependent) sub-groups
		- not be able to seperate out effect size estimates by sub-group
		- You might inflate type one error by having overlapping subgroups, depending on how you're defining them.
	- How about i learn about principled statistical methods specifically designed to handle within-study dependence
		- Yes
But we're also going to learn how to calculate the *known covariance formula between pairs of effects* within studies that their dependence is compromised because of the particular type of source of dependence. 
## 3.1 Multiple Treatments
- If we can *assume homogeneous variances across all the groups* being compared the multiple treatment versus the single comparison group, then remember that the estimate of each standardized mean difference, g, biased corrected ones involves use of the standard deviation that is based on a pooled sample variance. If we can assume that all the treatment groups and that comparison group, their population variance on the outcome is they are homogeneous. Then here is the formulas that we're gonna use. 
	- ![[Pasted image 20230327105622.png|300]] ![[Pasted image 20230329093733.png|150]] ![[Pasted image 20230329094118.png|200]] ![[Pasted image 20230329094203.png|200]] ![[Pasted image 20230329094433.png|200]] 
	- For each treatment group, we can calculate effect size of this treatment group
	- Dependent effect size means that there is a non-zero covariance among the pairs fo effect size estimates. the large sample **covariance between effect sizes** gi(for treatment group i versus the control group) and gj (for treatment grorup j versus the same control group) in a single multiple-treatment study was derived to be
	- ![[Pasted image 20230329101809.png|200]] 
	- **Example**
		- ![[Pasted image 20230329102738.png|300]] two treatment and one control. ==sdpi== is *pooled sample standard deviation across the three groups*. degrees of freedom m=(ntx1+nTx2+nCtl-3)=N-3 for bias correction. N=nTx1+ nTx2 + nCtl
		- ![[Pasted image 20230329105728.png|400]] ![[Pasted image 20230329105652.png|400]] ![[Pasted image 20230329105816.png|400]] 
		- ![[Pasted image 20230329110050.png|350]] ![[Pasted image 20230329110114.png|350]] ![[Pasted image 20230329110251.png|400]] 
		- $\Psi$ is the covariance matrix. we can build the covariance matrix ![[Pasted image 20230329110548.png|400]] 
		- Unbalanced data
			- ![[Pasted image 20230330105934.png|300]] ![[Pasted image 20230330110124.png|500]]  ![[Pasted image 20230330112233.png|500]] 
			- Build the block diagnal matrix ![[Pasted image 20230330112310.png|500]] ![[Pasted image 20230330112402.png|300]] ![[Pasted image 20230330112439.png|500]]  
## 3.2 Multiple Outcome
- correlation between outcomes i and j for the control group $\rho^{Ctl}_{ij}$ and for the treatment group  $\rho^{Tx}_{ij}$. We typically assume homogeneous covariance matrices, $\Psi$, for the control and treatment groups (ie,  $\rho^{Ctl}_{\delta_i,\delta_j}$ = $\rho^{Tx}_{\delta_i,\delta_j}$= $\rho_{\delta_i,\delta_j}$ ). $\rho_{\delta_i,\delta_j}$ is the correlation between effect sizes
	- for multiple outcome, study the variance of the standardized mean difference effect size. The formula is exactly the same as the one we typically see for standardized mean difference estimates. However, the covariance a little bit more complicated.
	- ![[Pasted image 20230329120621.png|200]] ![[Pasted image 20230329120742.png|300]] 
	- **Example**
		- General
			- ![[Pasted image 20230329120904.png|400]] *readM1 is reading mean in control group*, readM2 is reading mean in treatment group. r is the correlation between math and reading
			- ![[Pasted image 20230329121138.png|400]] ![[Pasted image 20230329121226.png|400]] ![[Pasted image 20230329121247.png|300]] ![[Pasted image 20230329121331.png|500]] 
		- **MO effect sizes with no missing gs**
			- ![[Pasted image 20230329222317.png|300]] ![[Pasted image 20230329222711.png|400]] ![[Pasted image 20230329222733.png|500]] ![[Pasted image 20230329222815.png|400]] 
			- ![[Pasted image 20230329223001.png|400]] ![[Pasted image 20230329223104.png|400]] ![[Pasted image 20230329223209.png|400]] 
			- ![[Pasted image 20230329223516.png|500]] GLS by hand code ![[Pasted image 20230329223737.png|400]]
			- you're gonna have to have a study id variable in there, variance sampling a variance cluster variable, and then a correlation. And either you submit a single value for all of the within study covariances, or you can have for each study here is the correlation value that I want you to use. But again, within a study, it just wants one value for that correlation. 
			- **clubSanwich package** *impute_covariance_matrix* function. you're gonna have to have a study id variable in there, variance sampling a variance cluster variable, and then a correlation. And either you submit *a single value for all of the within study covariances*, or you can have *for each study here is the correlation value that I want you to use*. But again, *within a study, it just wants one value for that correlation*. ![[Pasted image 20230329225018.png|150]] . even if you have 3 pairs of effect size, say, 3 outcomes, instead of three covariance, it assumed single value for the correlation between pairs of effect sizes, thus, single covariance
			- ![[Pasted image 20230329225256.png|500]] 
			- Does the psi matrix matter? Yes. The values you use for the correlations (between pairs of effect sizes) and thus of the covariance matrix elements found in $\hat\Psi$ impact the results.
			- ![[Pasted image 20230329225639.png|400]] ![[Pasted image 20230329225658.png|400]] ![[Pasted image 20230329225754.png|400]] 
		- **Balanced data and GLS**
			-  a balanced meta-analytic database, would include **k studies** each reporting **p=2 effect size estimates**, **q coefficients** (design matrix column number)
			- ![[Pasted image 20230329231128.png|100]] ![[Pasted image 20230329231518.png|300]] 
		- **Unbalanced data**
			- ![[Pasted image 20230329231719.png|400]] ![[Pasted image 20230329232553.png|400]] ![[Pasted image 20230329232740.png|500]] 
			- ![[Pasted image 20230329232834.png|250]] ![[Pasted image 20230329232854.png|300]] ![[Pasted image 20230329233056.png|500]] this is gpooled estimate of delta for this data set with 12 effect sizes. And i've handled the within study dependence using gls the . 337 is the pooled estimate of treatment effect on academic achievement. We're not distinguishing between math versus reading, because it's just an intercept only model.
			- ![[Pasted image 20230329233153.png|400]] to test difference in the effects for reading versus math ![[Pasted image 20230329233424.png|500]] 
## 3. 3 GLS
 - generalized least squares. directly model the covariance between pairs of effect sizes
	 - ![[Pasted image 20230329130701.png|250]] ![[Pasted image 20230329140451.png|200]] This is ==Mega Psi==. ![[Pasted image 20230331221428.png|400]] This is the **covariance matrix of estimated beta**.
	 - Mega Psi and covariance matrix of estimated beta
		 - ![[Pasted image 20230331223430.png|400]] 
		 - The Mega Psi (Ψ) matrix is a term used in the context of *multivariate analysis*, particularly in structural equation modeling (SEM). It represents the *covariance matrix of the residuals or errors for each observed variable in the model*. In other words, the Ψ matrix captures the *unexplained variance* (the part not accounted for by the model) in the observed variables. The Ψ matrix is *usually diagonal*, with *non-zero elements only on the diagonal*, indicating that the residuals of different *observed variables* are assumed to be *uncorrelated*.
		 - In the context of linear regression or other regression-based models, the covariance matrix of estimated beta (β) is a matrix that represents the uncertainty or variability in the estimates of the regression coefficients (β). This matrix provides information about the precision of the estimated coefficients and is often used to calculate confidence intervals or to perform hypothesis tests on the coefficients. It is derived from the *inverse of the Fisher Information matrix*, which is a function of the sample data.
	- **relationship** between generalized least squares **(GLS)** estimation and ordinary least squares **(OLS)** regression
		- ![[Pasted image 20230329130612.png|200]] ![[Pasted image 20230329130701.png|250]] ![[Pasted image 20230329131050.png|400]] X is the design matrix, $\hat\Psi$ is a block-diagonal matrix (It is a symmetric matrix with matrices along its diagonal and zeros everywhere else) containing study-specific covariance matrices, $\hat\Psi_i$s, along its diagonal. and so $\hat\Psi^{-1}$ is the inverse of the $\hat\Psi$ 
		- example of *block-diagonal matrix* ![[Pasted image 20230329131452.png|200]] ![[Pasted image 20230329131735.png|200]] ![[Pasted image 20230329131840.png|200]] ![[Pasted image 20230329132641.png|300]] ![[Pasted image 20230329132705.png|300]] You can even have a single one by one matrix as an element along the diagonal, doesn't have to be more than one square matrices along the diagonal. As I just said, matrices along the diagonal do not have to have the same dimensions as each other. the dimensions of each studies matrix are gonna be symmetric
		- We can use gls even the data are independent. So the study specific side matrices just have a one by one element, the variance of the relevant studies effect size. And then there's zeros everywhere. 
		- ![[Pasted image 20230329132935.png|200]] ![[Pasted image 20230329132948.png|200]] ![[Pasted image 20230329133009.png|400]] 
		- GLS allows us to incorporate into the weighting, both the sampling error variance, the known sampling variance, but also the known sampling error covariance amongst pair of effect sizes within a study.
	- Interpret the resulting parameter estimated using GLS when a meta-regression **model with just an intercept** (ie. no moderators) is estimated:
		- Start with the simplest scenario with k effect size estimates, gs, from *k studies*. for a meta-analytic data, *Y=g*, so ![[Pasted image 20230329133910.png|200]] 
		- ![[Pasted image 20230329134013.png|100]] ![[Pasted image 20230329134029.png|400]] ![[Pasted image 20230329134107.png|100]] ![[Pasted image 20230329134146.png|300]], finally, we get 1×1 estimate. which is intercept, and is *"weighted" mean* ![[Pasted image 20230329134340.png|200]] 
		- ![[Pasted image 20230329134939.png|400]] ![[Pasted image 20230329135011.png|400]] ![[Pasted image 20230329135037.png|300]] 
		- This is just something to see directly with 3 studies to *demonstration how GLS works*, that it does give you a *weighted pool effect estimate* when you use gls and you use the sine matrix when you *don't have dependent effects*, when you do have *dependent effects*, you just *incorporate the covariance*, and it still gives you this *weighted effect* that *models* the *within study dependence*, in the effect sizes and appropriately handles the standard errors and everything else. 
		- Pooling gs with **hand code GLS**
			- ![[Pasted image 20230329135654.png|400]] 10 studies. with delta and variance of delta ![[Pasted image 20230329140202.png|400]] 
			- ![[Pasted image 20230329135735.png|400]] ![[Pasted image 20230329135814.png|400]]  create design matrix ![[Pasted image 20230329135938.png|400]] 
			- ![[Pasted image 20230329140105.png|400]] ![[Pasted image 20230329135847.png|400]] 
			- The covariance matrix for that is really just a variance squared standard error of that estimate of the intercept
		- Pooling gs with GLS by **rma.mv function** in metafor package
			- ![[Pasted image 20230329221502.png|400]] need to tell the V, known covariance matrix, $\hat\Psi$ 
	- **Q-Test of homogeneity** with dependent and **Testing moderators** 
		- ![[Pasted image 20230330193150.png|300]] the rma.mv will do that for you
		- ![[Pasted image 20230331113644.png|300]] ![[Pasted image 20230331114931.png|400]]  
		- n_e, number of experimental group. n_c number of control group. SAT_M/SAT_V, dummy variable indicate effect size (delta) is math or verbal. X is the coaching hours and X_M and X_V is the interaction term of coaching hours and dummy variable SAT_M/SAT_V, which is the coaching hours on math or verbal
			- **Pooled estimates** of the treatment effect on both SAT Math and on SAT Verbal while recognizing the within-study dependence using rma.mv. *No-intercept model* 
				- ![[Pasted image 20230331115220.png|200]] ![[Pasted image 20230331115243.png|500]] ![[Pasted image 20230331115458.png|400]] ![[Pasted image 20230331120028.png|300]] 
			- Outcome-**General Moderator**
				- ![[Pasted image 20230331120943.png|300]] ![[Pasted image 20230331121007.png|600]] ![[Pasted image 20230331121047.png|500]] 
				- for two studies that differ by one on the coaching variable, the predicted difference in the effect size is - .004. The more coaching, the smaller effect size
			- **Outcome-Specific Moderator**
				- ![[Pasted image 20230331150042.png|400]] ![[Pasted image 20230331150111.png|600]] ![[Pasted image 20230331151205.png|500]] 
				- Then the slope in the sat separate model, sat verbal model, represents, again, for two studies that differ by 1 hour in terms of how much coaching they do for sat verbal. This coefficient will be the predicted difference in treatment effects on sat verbal.  With the study having 1 hour more of coaching being predicted to have a smaller treatment effect on math sat and that difference will be - . 009. The Thes of Moderators ask if any of those four coefficients different from 0, and $H_0$  is: $\beta _{M_0}$=$\beta _{M_1}$=$\beta _{V_0}$=$\beta _{V_1}$=0
				- You can use the model's results to test whether the relationship between coaching, x, and the treatment effects on SAT-M might differe from that relationship with the SAT-V. $H_0$: $\beta _{M_1}$-$\beta _{V_1}$=0. 
					- need to fill out the contents of the L argument that specifies the contrast coefficients applied to the relevant regression model's coefficient estimates: $H_0$: (0)($\beta _{M_0}$)+ (1)($\beta _{M_1}$)+ (0)($\beta _{V_0}$) + (-1)($\beta _{V_1}$)=0
					- ![[Pasted image 20230331152438.png|400]] ![[Pasted image 20230331152458.png|400]] 
			- **Mixed effects** models with GLS
				- by defualt, a random or mixed-effects model is estimated when using rma.mv. 
				- ![[Pasted image 20230331202018.png|500]] ![[Pasted image 20230331202034.png|500]] 
	- **Two/Three level GLS**
		- what we learned before is two-level GLS ![[Pasted image 20230402202244.png|200]] ![[Pasted image 20230402202310.png|110]] ![[Pasted image 20230402202330.png|130]] , eij is the level one sampling error, the known variance-covariance matrix. level 2 is the super population, the distribution of each study's true effect size.
		- ![[Pasted image 20230402202724.png|200]] ![[Pasted image 20230402202310.png|110]] ![[Pasted image 20230402202330.png|130]] the extra random is the unknown random effects within studies. ![[Pasted image 20230402203145.png|120]] , this vij reflects heterogeneity among within-study residuals over and above the known sampling error
		- ![[Pasted image 20230402203753.png|400]] 
		- we have study Ids, but we also have effect size Ids. If you want to add a level to your model to allow within study random effects, as well as between study random effects over and above sampling error, then you're gonna need an id variable both for within study id and your study id. So in this example, the *effect size ID is Esid*
		- I created us omega psi matrix for you. I was *lazy*, using this *impute covariance matrix* to create my sine matrix *using a single value*, assumed for the correlation between pairs of exercises. The reason is because *we're ultimately gonna use RVE* which will handle the fact that we used a *bad psi matrix*. When we're using *gls* we want to use it works best for its standard errors. *Covariance of the beta hat vector works best when we use the exact mega sign matrix*.
		- ![[Pasted image 20230402204747.png|300]] ![[Pasted image 20230402205123.png|400]] this is *mixed effects model with GLS*. random=~1|Studyid (I want to intercept different across studyid) requests only a random intercept and identifies that Studyid is the clustering (level-2)variable. don't forget to use the test="t"
			- ![[Pasted image 20230402205947.png|400]] 
		- ![[Pasted image 20230402210330.png|400]]  We want within study random effects. We want between study random effects. Studyid/ Esid specifies that Esid are clustered across/within studies, and associated intercept random effects (random=~1) are modeled at both levels. make my intercept vary within studies, from effect size to effect size, within studies as well as across studies. those are my two additional levels of clustering over and above sampling error that I want to be recognized in the model that I estimated.
			- ![[Pasted image 20230402211219.png|500]] 
## 3.4 RVE
- Robust Variance Estimation. method directly adjusts standard errors and is agnostic about the covariance values (robust variance estimation, **RVE**)
	- To use *GLS*, you *need* values for the *covariance between your pairs of effect sizes within studies*. And the value is important. *It affects the results* from using gls. The most important part of GLS is creation of that of good values in your $\Psi$, your mega $\Psi$ matrix.  For each study, it has its own little $\Psi$ matrix, the covariance matrix amongst pairs of effect sizes. But, studies don't always fall neatly within the types of dependence we mentioned. So we have *multiple treatments, we have multiple outcomes*. We do have formulas that we haven't covered them for handling the intersection of multiple outcome and multiple treatments. But there are other sources of dependence for which we don't necessarily have known covariance is, but for which we would need them. So that's our transition to thinking about alternatives where we still want to handle the within study dependence. But maybe in scenarios where we don't necessarily have a good sense of what the covariance is really should be and can be. The most important thing is that the choice of *weights* with *RVE* will *not impact the accuracy of the models*, parameter estimates. We'll just make the standard errors a little bigger sometimes if they're *less efficient*. But it's it's better than what can happen with gls when you don't use the right weight matrix that inverse mega sine matrix.
	- **RVE** provide robust standard error estimates for clustered data.
		- ![[Pasted image 20230331223606.png|600]]  
		- The innovation in RVE is the way that $\hat \Psi_j$is estimated for each study j's set of dependent effect size. $\hat \Psi_j$=$\hat\epsilon_j$ $\hat\epsilon^{'}_j$ , where for each study j, $g_j$=$X_j\hat\beta$+  $\hat\epsilon_j$ . What we're doing here is *calculating the product of the residuals with their transpose*. *Doing that for each study* to calculate its *psi matrix*. The caveat here is that for a single study, calculating that matrix product *doesn't give a great estimate of the study psi matrix*. However, as you might remember this theorem under the central limits theorem, things *do well when you're calculate things across multiple samples and think of the studies as multiple samples*
		- Using this residuals-based estimate provides an *unbiased* estimate of the effect sizes' known *sampling error covariance matrix, $\hat\Psi$* to obtain an *unbiased estimate of the coefficients' covariance matrix, cov($\hat\beta$)*.
		- RVE can work well for handling within-study dependence in effect sizes when the effect sizes' within-study covariance matrix elements are not all exactly known
		- RVE with a sufficiently large number of studies, k, does not require that the dependence (covariance between pairs of dependent effect sizes) be modeled exactly correctly nor that the effect size estimates' distribution is multivariate normally distributed.
		- **Small sample RVE adjustment, A**, ![[Pasted image 20230401224356.png|500]] 
		- *approximate inverse-(co)variance weights* provide the most efficient results. so W=$\hat\Psi^{-1}$ 
		- gls is premised on the assumption that you have the exact inverse covariance weights. And if you don't, then your standard errors won't work.  Which will mean that your statistical inferences will be off as well. But *rve* is not impacted in the same way. Your *choice of weights* affect *efficiency*, but it doesn't lead to bias in your standard errors if or the wrong kind of bias in your standard errors. If you don't use the exact inverse covariance weights.  The optimal weights result in optimal efficiency doesn't affect estimation blasts. 
	- **RVE dependence types**
		- in a meta-analysis, you *might encounter either or both of these kinds* of data structure dependencies or others. It is typically suggested that, when using RVE, you *choose the most commonly encountered* type in your data set and *use the relevant optimal weights*.
		- *Correlated effects* include multiple-outcome and multiple-treatment sources of within-study dependence, among others
			- ![[Pasted image 20230402102030.png|300]] for *effect size i in study j*. 
				- kj is the number of effect size estimates in study j. $\overline\rho$ is the average correlation between effect sizes across effect sizes and studies, a single value, (doesn't really greatly affect the results, which is the whole reason that we like using rve unlike gls the choice of the correlation covariance between pairs of effect sizes. With GLS it can make a big difference for correlated affects tau squared). 
				- $\hat\tau^2$ is the estimate of *between-study variability* in true effect sizes and 
				- $\overline v_j$ is the *mean* of study j's effect size estimates *sampling error variances*.
				- If you *don't known the average correlation* among pairs of effect sizes within and across studies, *using $\overline \rho$=1 to obtain conservative estimates*. ![[Pasted image 20230402103217.png|100]]
					- Each stuy's set of effect size estimates then does not depend on kj, studies that report more effect size estimates will not be awarded more weight because study reports more effect sizes. This can introduce a problem in moderator analyses
		- *Hierachical effects* refer to a scenario in which dependence is associated with a study-level descriptor like investigator or lab
			- ![[Pasted image 20230402103504.png|200]] 
				-  $\hat\tau^2$ is the estimate of *between-study variability* in true effect sizes and 
				- $\hat\omega^2$ captures the within-study variability in true effect sizes, and
				- $v_{ij}$ is the sampling error variance for effect size i in study j.
				- The default in the robot function, when we're estimating these random effects, variance components, it uses method of moment estimates for these random effects, variance components, which don't require a distribution assumptions, but that can *lead to some less* *well estimated random effects* experiences. But the goal of RVE is to get good estimates of the standard errors.
	- RVE-**Sample size caveats**
		- $\Psi$ estimate doesn't work well in single studies, but across a set of studies, it works well increasingly well. this really has to do with *number of studies in the meta analysis*, not necessarily the size of the samples on which effect sizes are based. decide if you have a large enough balanced, enough dataset, is to look at the *degrees of freedom associated with the relevant coefficient estimates*. This degrees of freedom is *not less than four*, because if it is less than four, then you definitely need to use a stricter alpha level and use small sample size adjustment A. if you have a categorical moderator and the vast majority of the studies have a value of one on that, versus a small set of studies that have a value of zero. That's an *unbalanced moderator*, and you'll see its influence on *making the degrees of freedom smaller*. 
	- Additional **caveats**
		- RVE is *not accurate* in estimating effect size variability, the *random component* $\hat\tau^2$ and $\hat\omega^2$. Those are calculated using a single value $\hat\rho$ . These only affect precision (standard error estimates and efficience). Thus, RVE tests of homogeneity of effect sizes (or their residuals) are not expected to be particularly accurate.
	- **Centering of Moderator variables**
		- When we have multiple effects per study, we have a moderator model. It is possible that a moderate as value also varies within study. We have multiple effects. There might be some characteristic of the samples associated with those effect sizes, the multiple effects within the study that also varies. So the moderator as values don't aren't always common across the effect sizes within a study. So we kind of have to learn about something that you think about with *conventional multi level modeling*, which is *within cluster and across or between cluster predictors* and how we handle *centering of those variables*. 
		- ![[Pasted image 20230402125649.png|300]] ![[Pasted image 20230402125711.png|260]] so we can model the *relationship*, $\hat\beta_1$, *within-study values on X and g* might differe from the realtionship, $\hat\beta_2$, *between study-leve, $\overline X_j$, values on X and g*- thereby *avoiding the ecological fallacy*. Using X rather than partitioning X results in a slope for the moderator that is a mixture of the within- and between study relationship between that moderator and g. If there's not enough within or between-study variability then you can't do this.
		- Example
			- ![[Pasted image 20230402130607.png|250]] moderator is per1st.
			- robumeta package has two built-in group.mean and group.center functions
				- *group.mean*, calculate simple mean of a variable for each group where each study is the group.![[Pasted image 20230402131219.png|100]] ![[Pasted image 20230402130845.png|400]] ![[Pasted image 20230402130936.png|400]] ![[Pasted image 20230402131029.png|230]] 
				- *group.center*, calculate the study-mean centered values. ![[Pasted image 20230402131145.png|200]] ![[Pasted image 20230402131245.png|400]] ![[Pasted image 20230402131301.png|400]] ![[Pasted image 20230402131458.png|300]] 
	- **Using robu function for RVE Pooling**
		- from robumeta package
		- small=TRUE employs Tipton's small-sample bias correction and is the default
		- ![[Pasted image 20230402133834.png|300]] ![[Pasted image 20230402135514.png|500]] 
			- Our degrees of freedom are greater than four substantially. We have 400 outcomes, which is effect size estimates. Some studies have one. Some one of the studies has 24 of excise estimates. I would not want to create a 24 × 24 psi matrix, but you would have to, if you wanted to use unique elements and only use gls to estimate your model, you'd have to create at least one study specific side matrix that had × 24 by 24 matrix with variances and all the relevant 24 × 23 off diagonal elements. 
			- By default, robot uses an average correlation between pairs of effect sizes of . 8.
				- ![[Pasted image 20230402150446.png|200]] test how rho changes the results. ![[Pasted image 20230402150546.png|500]] 
	- Using **robu to test moderator**
		- create the between-studies moderator per1st.B, and within-studies moderator per1st.W
		- ![[Pasted image 20230402151024.png|500]] ![[Pasted image 20230402151221.png|300]] ![[Pasted image 20230402151325.png|400]] ![[Pasted image 20230402151454.png|500]]  
	- Using clubSandwich to **test omnibus hypotheses**
		- ![[Pasted image 20230402151947.png|300]] ![[Pasted image 20230402152003.png|100]] , the contrast matrix C ![[Pasted image 20230402175124.png|200]] 
		- The Wald test can be used to test hypotheses about coefficients, here, ![[Pasted image 20230402174114.png|50]] where $\hat\beta$ is a (q×1) vector of regression model coefficient estimates. 
		- Wald test statistics ![[Pasted image 20230402190055.png|200]]  $V^{RVE}$ is the RVE-based estimate of the covariance matrix for the $\hat\beta$s. 
		- ![[Pasted image 20230402190642.png|300]] the *obeject* output by estimating the model using robu. the constraints C matrix. the covariance matrix for the $\hat\beta$, $V^{RVE}$. 
			- ![[Pasted image 20230402190954.png|400]] we can have $V^{RVE}$ from this but, the function of wald test can extract it too. The *vcov="CR2"* option tells R that *standard errors* should be corrected using the *bias-reduced linearization estimator* introsuced and recommended by Tipton and Pustejovsky.
			- ![[Pasted image 20230402191422.png|300]] ![[Pasted image 20230402191639.png|300]] , in the wald test, we can use constrain_zero function. ![[Pasted image 20230402191522.png|400]] 
		- Example
			- ![[Pasted image 20230402191755.png|400]] ![[Pasted image 20230402191815.png|300]] ![[Pasted image 20230402191900.png|400]]
### Robu package
[link](file:///Users/yuan/Dropbox/papers/EducationCog/robumeta-%20An%20R-package%20for%20robust%20variance%20estimation%20in%20meta-analysis.pdf)

RVE has small samples adjustment and is important when number of studies is less than 40, and also suggest implementing them in all RVE analyses. 

Difficulties in estimating the within-study covariance matrix. In RVE, ![[Pasted image 20230830193314.png|300]] 

- Inverse variance weights
	1. Traditional meta
		1. produce the most efficient estimate of beta
		2. estimate the variance of beta
	2. In RVE
		1. only important in produce the beta, efficiency
			1. The *efficiency of one estimator* is often compared to another by looking at *their variances*. If Estimator A has a smaller variance than Estimator B, Estimator A is said to be more efficient relative to B. This is known as "relative efficiency."
## 3.5 Combine RVE and GLS
- General rationale
	- RVE 
		-  is *robust* to use of an approximate working model for the *covariances among effect sizes*. 
		- use method-of-moments-based estimates of $\tau^2$ that are "approximately efficient" while likelihood-based estimation is used for the multivariate meta-analysis modeling framework (GLS)
		- lead to *less precise* meta-regression model coefficient estimates when there is *within-study variability* in moderators.
	- GLS 
		- is not robust to mis-specification of the covariances but allows more flexible working models to be used when testing meta-regresison models.
	-  Combine
		- use *GLS* to estimate model-including *both fixed- and random-effects parameters*. 
		- because those variance component estimates, as tau squared are better estimated with gls you can *fit* that information: the *fixed effects parameter estimates into RVE*, and
		- *when* RVE is calculating its *weights*, it can *use* those better estimated *varince components from GLS* and *provide robust standard errors* that you might not get from gls when you pair it with poorly estimated sign matrices
- feed rma.mv output into clubSandwich's coef_test function which then calculates robust standard errors for the three-level model's coefficient estimates
	- ![[Pasted image 20230402220250.png|500]] 
- Caution
	- This is cutting edge idea, use it with caution
	- coefficients estimates from GLS might be slightly different when you change the $\rho$ value which is used to create the Psi matrix
	- ![[Pasted image 20230402221108.png|200]] 

# Publication bias and Missing data
publication bias, it is more likely for an effect size to be published when it's statistically significant, then what that means is that the largest effect size estimates are the ones that are published. if only the largest effect sizes are published, because they're more likely to be statistically significant, then when you pull together those estimates of effect sizes, they're going to be biased overestimates of the true values.
- **Funnel Plot**
	- If we plot effect size estimates (x axis) against their sample size (Y), given no bias, we'd expect a symmetric plot centered around the average value for g. the shape of the plot should include more variability in effect size estimates for smaller sample sizes narrowing to a less vairable spread of effect estimates for larger sample sizes (the top of the funnel)
	- ![[Pasted image 20230402222602.png|400]]  or effect size estimates (X axis) against their standard errors (Y) but with the Y axis in the reverse direction. ![[Pasted image 20230402222758.png|400]] 
	- ![[Pasted image 20230402222922.png|600]] 
	- you can choose to center the plot around the pooled estimate of your treatment effect. To center the plot around the pooled estimate, you first have to run the meta-regression model being estimated (here, using rma). the default uses the standard error as the yaxis
	- ![[Pasted image 20230403095632.png|400]] ![[Pasted image 20230403095657.png|500]]  
	- Asymmetry in Funnel Plots could result because
		- *Small* studies might have higher quality of *implementation* (and thus larger true ES values)- or the opposite (worse and thus smaller)
		- The *quality* of some studies' design might lead to *heterogeneity*
		- *Heterogeneity in general*
		- The *variance of the effect size* is a function of the effect size parameter (introducing a correlation between the two) with the *stronger the effect size* the stronger the relationship between the precision and the effect size and thus the *more asymmetry* that might be noticed. When we calculate v for g we use g in the equation. There's already some kind of relationship in there, which can lead us to make inferences about asymmetry
	- Thus, identification of asymmetry might better be interpreted as a difference in ES by size of study and further investigation should be conducted to identify whether the primary source of the difference might be publication bias
- you should definitely not just use one test, a publication bias to judge whether there's evidence for publication bias
- **Rank Correlation test**
	- Kendall's tau test, also termed Begg and Mazumdar's rank correlation test, can be used which provides a measure of the association between the *rank of the suty sizes* (specifically of the variances or standard errors of the effect sizes) and the *rank of the effect size estimates'* values.
		- The $H_0$ is that the rank correlation does not differ from zero which translates into the funnel plot is not asymmetric=no publication bias. Thus, a statistically significant rank correlation is interpreted as support for publication bias.
		- metafor package function rank test. ![[Pasted image 20230403101912.png|150]] 
		- Simply looks the correlation between effect size estimates and standard errors. This *non-parametric* statistical test of funnel plot asymmetry has notoriously *low power*
- **Egger's Regression**
	- use of a weighted regression model specified as: ![[Pasted image 20230403111940.png|100]] . precision of effect size estimate $s_g$ is used as predictor and conventional (inverse variance) effect size estimate weights are used.
	- the test of the slope provides the test of the funnel plot's symmetry. ![[Pasted image 20230403112407.png|100]] the null hypothesis is that there is no relationship between our standard error and our effect size estimate. There is no publication bias, no evidence of publication bias. 
	- ![[Pasted image 20230403113020.png|300]] ![[Pasted image 20230403113113.png|400]] 
	- random effects example ![[Pasted image 20230403113337.png|400]] 
	- Problem: ![[Pasted image 20230403113825.png|100]] ![[Pasted image 20230403113847.png|200]] $s_g$ is depends on the effect size value even when there might be no publication bias, and thus inflate the Type I error rate.
	- ![[Pasted image 20230403114144.png|400]] 
- **Trim and Fill**
	- non parametric method. assesses the potential number of missing effect sizes which- if added back into your actual meta-analytic database-might lead to a funnel plot that looks symmetric. *Estimating the number of missing "unpublished" studies, k0*.
	- You should make sure that your results are coded where the intended result is a positive effect. don't change the results of studies to make everything positive, but change how you're calculating them. So that published studies being positive, mean that the treatment effect is working. 
	- what the iterative process does is it uses the observed data frame of effect sizes and *reduces down* as many of the most extreme, *extremely large positive effect sizes*, as is needed *to* result in a reduced data set that is *symmetric*, *how many of exercises do I have to remove* from my observed dataset to give me a symmetric dataset. You're removing the five most extreme on the right hand side and that results in this curtailed set of data that are symmetric. Number five is then used to fill out your data frame to make it a symmetric plot.  *mirror image* of that is added to the other side
	- One primary assumption is as follows: the k0 unpublished effect size estimates are the k0 leftmost (smallest) value that have been suppressed. Thus a *directional (positive effect size) hypothesis is assumed* and the effect sizes of the smallest magnitude or in the wrong (negative) direction are assumed unpublished.
	- ![[Pasted image 20230403120200.png|500]] ![[Pasted image 20230403120227.png|500]] 
		- What we see right here is the *estimated number of missing studies on the left hand side*. Your assumption when you're using this, is that we have positive effects (that on the left hand side are the ones that are smaller, estimates of delta and or even negative). And those are not appearing because there is publication bias. Either they're not statistically significant or in the wrong direction. They're not going up here. And *my estimate of the number of effect sizes that are missing is five*. And we also see a *p value* which *test* the *null hypothesis that there is no publication bias*. A significant p value would tell us there is there is some evidence of significant publication bias. What we have that I think is interesting is, remember, *there are 11 effect sizes in the original data frame*. What is provided in the *output is a pulled fixed effects estimate of delta using 16 effects*.  what the trim and fill procedure does is it not only estimates the number of possible unpublished studies sitting it out there that you need added back into your dataset to make it symmetric, but it then *re estimates* your pooled effect, a*dding back in those most extreme five effect sizes that it's our hypothesized to be missing*. 
		![[Pasted image 20230403122106.png|400]] ![[Pasted image 20230403122122.png|200]] 
	- cannot handle moderator or within study dependence.
- **Selection modeling**
	- assumed only statistically significant results are published. Used maximum likelihood estimation to derive the distribution of effect size estimates. Assuming normality for the estimates, if there is no publication bias, then effect size estimates can fall anywhere within the orange shaded distribution. If publicatio bias, then only the effect size estimates appearing in the blue shaded part of the distribution will be observed ("published")
	- *Infer the entire distribution for effect sizes* assuming that just the *blue* distribution is *available*. Then, a *corrected pooled effect size estimate* can be calculated under the assumption that only statistically significant effect size estimates are observed.
	- *can* test entire model *including moderators* but *cannot* include *dependent effect sizes*
	- ![[Pasted image 20230403123648.png|200]] ![[Pasted image 20230403124057.png|200]] 
	- ![[Pasted image 20230405205850.png|400]]
	- ![[Pasted image 20230405205906.png|400]] 
	- **Selection Modeling Extension**
		- can recognize that published sutides include both statistically significant and non-significant results. Includes a *step function* for the *probability of publication* associated with intervals of *p-values*. 
			- Example: if p<0.05, 100% are published, and p>0.05, 20% publish.
				- ![[Pasted image 20230403124941.png|300]] ![[Pasted image 20230403125003.png|300]]
			- To use the selection model, the meta-analyst choose the cutpoints *defining the intervals for the p-values*. Estimating the model provides the weightes associated with each interval the user defined
			- The weight for the most significant interval of p-value is fixed to a value of 1 to ensure the model is not under-identified. The weights are not probabilities. *weight* estimate of *0.5* then means that the probability of effect sizes with p-values in the *relevant interval are one-half as likely to be published as the effect sizes in the most statistically significant interval*
			- First, an unadjsuted model not including the "weights" for p-value intervals is automatically estimated
			- Next, the adjsuted model is estimated that includes the user-specified p-value intervals so that their associated weights can be estimated
			- A *likelihood ratio test LRT* is provided that compares the first model with the model including the weights that adjsut for publication bias.
			- The null hypothesis that is being tested with this likelihood ratio test is that the probability of exercise being published does not depend on interval within which the p value lies. It doesn't depend on its p value. That's the null hypothesis. The degrees of freedom for like the ratio test is the number of intervals that you're specifying for, which you're estimating weights. 
		- **weightfunc funtion in weightr package**
			- 1. **simple example with default p values interval**
				- ![[Pasted image 20230403131203.png|500]] 
				- ![[Pasted image 20230403131247.png|600]]  
				- I didn't specify my my step functions or my intervals for the p values. This is *the default p values interval* that's given less than . 025 and . 025 ~ 1.  probability of an effect size with the p value in this interval(.025~1) is 1 . 224 times as likely as in the smaller p value.
			- 2. **more complex example**
				- p-value intervals: 0<= p <0.01, 0.01< p <0.05, 0.05< p <0.50, 0.5< p <= 1.0. Those are p values of effect size estimator.
				- ![[Pasted image 20230405203901.png|500]]
				- ![[Pasted image 20230405204452.png|600]] 
				- Unadjusted intercept is 0.4573 and adjsuted intercept estimate of 0.4282 based on the selection model that includes weight estimates.
				- even LRT is significant , but the direction is backwards. even though this likelihood ratio is statistically significant, I would pause and make sure that you look at what the pattern looks like before you say we have publication bias here.  the *likelihood ratio is a chi square distributed* test statistic. It's s*ensitive* meaning that *for larger data sets*, it can be *overpowered*. So it can find some small evidence here for publication bias when there really is publication bias. But the evidence is vary that the *true degree of publication bias might be practically non significant*.  The other slight piece of evidence for publication bias is that when we use this different model for the intervals, *pooled effect does go down a little bit*. That's another piece that actually does *match with a little bit of evidence or publication bias*, but the pattern of publication bias is slightly odd.
			- 3. **Vevea & Woods (2005) model**
				-  ![[Pasted image 20230406111820.png|400]] 
				- ![[Pasted image 20230406111902.png|600]] 
				- Due to the challenges of estimating these models, Vevea and Woods (2005) came up with an extension (actually a restricted version) of Vevea and Hedges' (1995) selection model
				- This model, *user specifies (does not estimate) the weights* for the p-value intervals
				- This is helpful with smaller meta-analytic database sizes (as there can be convergence problems estimating the more complicated models). For example, if there are too few (or no) effect sizes within an interval, there might be convergence problems with the more parameterized Vevea & Hedges (1995) model
				- A meta-analyst can *specify a number of* models in which the *weights* are fixed and *compare* the impact of the selection *patterns* on the adjusted meta-regression model's parameter *estimates* provideing a form of *sensitivity analysis*. Thus, this model provides an assessment of the robustness of the meta-regression model parameter estimates to different possible patterns of publication bias (modeled as a function of p-values).
				- However, because the *weight parameters are fixed, not estimated*, *no LRT is available to test improvement in model fit* for the adjusted versus unadjusted model. In addition, no standard errors will be estimated given the weights for the p-value intervals are fixed not estimated.
			- 4. **PET-PEESE** not suggested
				- pet peeve says test your eggs regression model, predicting the effect size estimate with its standard error. If the intercept in your anchors regression model is statistically significant, then re estimate it using, we estimate that model, using the variance of the effect size as a predictor. 
				-  if you have a moderator model, should you only be looking at the intercept? This might apply *only* to when you're *pooling effect size estimates*. 
# Meta Regression, some Q statistics
- meta analysts are even more possibly interested in is not just coming up with that average. But if a lot of variability is found in the effect sizes, then exploring what might be at the root of that heterogeneity. which include predictors of effect sizes, where the predictors are sample and study characteristics that distinguish the studies and samples used that led to the effect sizes. *The outcome is already effect size, so this is moderator analysis*. We still want to use weights with meta-regression, not OLS. OLS regression assumes that all observations have equal weight in the analysis, meaning that each data point contributes equally to the calculation of the regression line. Weighted regression, on the other hand, allows for different weights to be assigned to different observations, which can be used to give more emphasis to certain observations in the analysis.
- Regular (non-meta-analysis) statistical software estimate a weighted meta-regression don't correct for the stadard error, the correction formular should be ![[Pasted image 20230321222832.png|100]]  where $S_{BJ}$ is the standard error typically estimated by statistical software for typical (non-meta-analytic) weighted regression analysis and MSE is the residual Mean Square (Mean squared error) usually reported in the accompanying variance dcomposition output. SO, *use meta-analysis software*
- Instead of using a moderator's slope to test the moderator's relationship with treament effect, it is possible to test the variability in the treatment effect estimates that are explained by the moderators ($R^2$).
- **QB** In meta-analysis, the test of the **variability explained by the model's predictors** is also considered a form of Q-statistic-actually the $Q_B$ ($Q_{Between}$)that is assumed to follow a $\chi^2$ distribution (with df= number of moderators) 
- **QW** $Q_W$ ($Q_{Within}$ or $Q_{Error}$) that can be used to test **homogeneity in the residuals**-*calculated using the weighted* $SS_{Error}$ that is reported in the weighted meta-regression output. follow a $\chi^2$ *distribution with (k-s-1) degress of freedom* where *k* is the *number of effect size* estimates being tested and *s* is the *number of moderators* in the model being estimated
	- if Qw is statistically significant. we still have a lot of variability left even with these moderator in our model.
		- adding more moderators ro the model
			- want to *test whether* a *new* block of *predictors* *contributes* significantly to the explanation of the variability in the effect size
			- Qchange $Q_{Change}$ -statistic is the difference in the weighted $SS_{Error}$ for the model including the extra block of predictors compared to the weighted $SS_{Error}$ for the model witouth the extra block of predictors.
			- ![[Pasted image 20230322082149.png|300]]  $SS_{Error,j}$ is the sum of squared Errors (=Residuals) for model j. Rst is the restricted model with a set of s moderators, and full is the full model with s moderators and an *additional r moderators being tested*
		- adapting the fixed-effects meta-regression model to a mixed-effects model

# Multiple Regression Review
Y=$B_0$+$B_1$X
any intercept in a model that has a predictor is that predicted y value when x is zero.
The slope is the predicted difference in y here for two individuals who differ by one on X.

**Null model** A null model is one that doesn't have any predictors. 
Y=$B_0$
Based on ordinary leaset squares regression, the intercept is just gonna be the predicted y and our best estimate of y is gonna be the mean. So our intercept with no predictors in the model and oridinarily least squares regression, the intercept is the sample mean y. If you're doing weighted regression ( *lm(y ~ 1, weights = w)* ), the intercept is the weighted mean.

Centering predictors only impact the intercept

Multiple predictors: controlling for variable means when variables retain same across individuals, the change of one predictor associated with differences in y

Researchers commonly test the model itseld as a whole to see whether variability in the outcome Y, is explained by the set of predictors- atest of model's $R^2$ 
	- The test is done by using an F-ratio for the ANOVA that aways accompanies a regression analysis and captures the amount of v ariability in the outcome explained by the set of predictors

*Categorical* predictor like treatment group, will trun to *dummy* variable. we need to use one-fewer-than-the -number-of-categories in the nominal variables. reference group

Moderator: effect on variable A depend on the variable B. ![[Pasted image 20230321221016.png|500]]

# Matrix algebra concepts
the part that is connecting the matrix algebra to what we're gonna do is through the *design matrices*, as well as showing what is done with ordinarily squares regression, to build the pathway, to getting to generalizedly, squares, or weighted regression. our data are more complicated than for the last day and a half. We've been treating it. If you have a small meta analysis, this might not be the case as your data frames, your as your meta analytic databases get bigger and bigger, it is more likely that they will not contain just one effect size per study that they might have a couple or more effect sizes per study that are relevant to you that you want to handle.  

the effect sizes themselves might have some kind of dependence. All of the things that we've been doing for for pooling and estimating meta aggression models have been premised on an assumption that our effect size estimates are independent. 

The dimensions of a matrix are always presented as the **number of rows by the number of columns.**  If you want to *add matrices together or subtract* a matrix from another matrix, then the **dimensions have to be exactly the same**. 

The product of two matrices is going to have the same number of columns is the first matrix, the row dimensions of the second matrix. ![[Pasted image 20230322155548.png|300]] 

Identity matrix, I, a square (same number of row and columns)

The inverse of a matrix, $R^{-1}$, can provide a form of matrix division such that $R^{-1}$R=R$R^{-1}$=I 

![[Pasted image 20230322162225.png|500]]  ![[Pasted image 20230322162251.png|500]]  ![[Pasted image 20230329102207.png|400]] ![[Pasted image 20230322162351.png|500]] 

## Design Matrix
we don't actually think that it's matrix algebra based and that there's a **design matrix** involved that we're using when we're specifying our model
![[Pasted image 20230322162727.png|500]] ![[Pasted image 20230322163036.png|500]] ![[Pasted image 20230322163218.png|500]]  ![[Pasted image 20230322163300.png|400]]  

You would use ordinary least squares regression, unweighted stuff, and to get to obtain your vector of coefficient estimates. Set up our design matrix, calculate the transpose, multiply it by the design, make yourself take the inverse of that product, calculate transpose of x and then also use the values on y to get our vector of three coefficient estimates. 
![[Pasted image 20230322165635.png|500]] ![[Pasted image 20230322170318.png|500]] ![[Pasted image 20230322170956.png|600]]  
s is the number of regression coefficients estimated in the model which is also the number of elements in $\hat{\beta}$, $\epsilon$ is the vector of residuals.

# Core statistics Review
## variance
![[Pasted image 20230406120041.png|200]] ![[Pasted image 20230406120301.png]] ![[Pasted image 20230406120315.png]] ![[Pasted image 20230406120329.png]] 

## residual matrix
![[Pasted image 20230401222529.png|500]] ![[Pasted image 20230401222627.png|400]] ![[Pasted image 20230401222702.png|200]] 

## linear contrast
A linear contrast is a statistical technique used to *compare specific groups or levels within a categorical independent variable*, particularly in the context of Analysis of Variance (ANOVA) or regression analysis. Linear contrasts involve *creating a weighted linear combination of group means* or estimated parameters to test specific hypotheses or make comparisons of interest. In a linear contrast, *each group mean or parameter estimate is multiplied by a specific weight*, and the *weighted values are then summed to form the contrast*. The weights are chosen based on the specific comparison or hypothesis being tested. These weights must sum to zero for a valid contrast. For example, suppose you have a one-way ANOVA with four different groups, and you are interested in *comparing the average of the first two groups* with the *average of the last two groups*. You could define a linear contrast with weights of *0.5, 0.5, -0.5, and -0.5* for the four groups, respectively. This contrast would represent the difference between the averages of the first two groups and the last two groups. Once the contrast is defined, you can *test whether the contrast is statistically significant*. This involves calculating the contrast value, its standard error, and the corresponding test statistic (typically an F or t statistic). If the test statistic is significant, it indicates that the specific comparison of interest (defined by the linear contrast) is statistically significant, and the null hypothesis can be rejected. In summary, linear contrasts provide a way to make specific comparisons or test particular hypotheses within the context of ANOVA or regression analysis, by creating a weighted linear combination of group means or parameter estimates.
## Sampling versus Frequency distributions

A **sampling distribution** is really a *theoretical distribution of a statistic*. No one actually, except for those of us who simulate, and those of us who make students come in and repeatedly sample for a whole weekend, there we rarely actually have access to the empirical sampling distribution for statistics. The kinds of the first sampling distribution that you probably learned about was the *sampling distribution of sample means*, central limit theorem. There's *sampling distribution of sample variances*, there's *sampling distributions of sample standard deviations*, *sampling distributions of sample correlations*. That *doesn't* tell you necessarily *what a distribution sampling distribution is*. It is the *distribution of the statistic that we would obtain* if we went and took repeated samples from a frequency distribution. For example, if you want to create a sampling distribution of the sample mean, you would have an original individuals, frequency distribution. So every person's score on depression, you go in get **a sample of ten people calculate the mean**. That is your *first data point in your sampling distribution of the mean*. Then you go to the frequency distribution, get another sample of ten independently sampled. Individuals calculate their sample mean on depression and so on. So you repeatedly sample. All of these means you build them up and create your sampling distribution of sample means. **each sampling distribution is based on samples of the same size**. 

## Characteristics of statistics

We tend only to use statistics (such as $\overline{Y}$ ), because **we like sampling distribution's characteristics** (unbiased, consistent, efficiency)
	- *unbiased*: An unbiased sample estimator is one that while we recognize the estimates $\overline{Y}$ don't equal the truth $\overline{\mu}$, the *average of all those estimates equals the truth*. ![[Pasted image 20230324092607.png|100]]
	- *consistent*: A consistent statistic is one where *the larger the sample size on*, which that statistic is based, *the more precise the estimate is*. A more precise statistic is one that is closer to truth. ![[Pasted image 20230324093024.png|100]] in this figure, the green one has larger sample size, and there are more sample estimates closer to the trueth. Smaller sd, more precise, smaller sd.
	- *efficiency*: we are prefer efficient estimators-those with the smallest variances (of their sampling distributions). For examle, the sample mean and sample median are unbiased estimates of the population mean. However, the variance of the sample mean is less than the variance of the sample median and it is thus a more efficient central tendency estimator.
	- sometimes there are **payoffs between the different estimation procedures**. Sometimes something might have a little bit more biased with small sample sizes, but be more efficient or vice versa.


## Core steps in Null Hypothesis Testing

1. Assume the null hypothesis, $H_0$ , is true as a starting point
2. Set up your criterion ($\alpha$ level) for whether your sample's results are likely or not if the $H_0$ is true
3. Calculate your sample's test statistic (and its p-value)
4. See whether your sample's test results are likely or not given the $H_0$ is true

It is critical that the p value that's calculated for your data is well aligned with the actual sampling distribution, shape and characteristics. It is very important that we are using sampling distributions and their characteristics (standard errors, means) that are a good fit with our sample's test statistic's empirical distribution.

## Confidence Interval Estimation

Let's think about a sample mean. It's a single value, a single estimate of the population mean. What a confidence interval does is literally not just a point estimate, but builds an *interval around that point estimate*. The confidence interval is also an estimate of the relevant parameter. You can have a confidence interval aspect of the mean or of an effect size. And the additional information that you get is captured in the width of our confidence interval. If it's a really wide whith, then that implies you have a pretty imprecise estimate. Of course, it's all contextualize. Who knows if something's wider or not? What isn't, for example, 95 % confidence interval? **It's an interval within which the parameter might lie. Is the parameter in there or not. You don't know**. 

![[Pasted image 20230324100015.png|200]] $C_{\alpha/2}$ is the critical test statisti (e.g., t or Z) cutting off ($\alpha/2$)% of the relevant sampling distribution, and $S_{Statistic}$ is the standard error of the statistic's sampling distribution. ![[Pasted image 20230324100223.png|100]] CI for $\mu_Y$ 

## Independent assumption
In the context of model assumptions, "independent" refers to the idea that the observations or **data points being analyzed are not influenced by or related to one another**. Independence is a crucial assumption in many statistical models, as it helps ensure that the results and conclusions drawn from the analysis are valid and unbiased.

For example, in *linear regression*, one of the key assumptions is the *independence of errors (residuals)*. This means that the error term for any given observation should not be related to the error terms of other observations. *If the errors are correlated, it can lead to biased estimates of the model parameters*, incorrect inferences, and unreliable predictions.

In time series analysis, the assumption of independence is often relaxed, as data points collected over time are more likely to exhibit correlations or dependencies. However, even in these cases, it is crucial to account for these dependencies to ensure accurate modeling and analysis.

In summary, the assumption of independence in a statistical model means that the observations or errors in the model are not related to each other, helping to ensure unbiased and reliable results.

### asymptotic distribution
An asymptotic distribution is a probability distribution that describes the behavior of a statistic as the sample size approaches infinity. One of the most well-known asymptotic results is the Central Limit Theorem (CLT). The CLT states that the sum or average of a large number of independent, identically distributed (i.i.d.) random variables with finite mean and variance will converge to a normal distribution, regardless of the shape of the original distribution. In this case, the normal distribution is the asymptotic distribution of the sample mean. In summary, an asymptotic distribution is the limiting probability distribution of a statistic as the sample size grows indefinitely. Asymptotic results provide important insights and approximations for statistical inference in large sam

# Data Extraction in meta-analysis
https://www.cebm.ox.ac.uk/resources/data-extraction-tips-meta-analysis
## General Issues
1. *Highlight* the *extracted data* on the pdfs of your included studies. This will help if the other data extractor disagrees with you, as you’ll be able to quickly find the data that you extracted. You obviously need to do this on your own copies of the pdfs.
2. Keep a *record* of your *data sources*. If a study involves multiple publications, record what you found in each publication, so if the other data extractor disagrees with you, you can quickly find the source of your extracted data.
3. Create *folders* to *group sources* together. This is useful when studies involve multiple publications.
4. Provide *informative names of sources*. When studies involve multiple publications, it is useful to identify, through names of files, which is the protocol publication (source of data for quality assessment) and which includes the main results (sources of data for meta- analysis).
5. Document all your calculations and estimates. *Using calculators* does not leave a record of what you did. It’s better to do your *calculations in EXCEL*, or better still, in a *computer program*. Calculations coded (written) in a computer program are easier to read and manage than formulae in an EXCEL cell, particularly as some calculations for data extraction involve long equations with multiple brackets.
6. Extract data into an *EXCEL spreadsheet*. The data can be imported into computer programs or copied into Review Manager, the software used in Cochrane Reviews.
7. Extract only *one number per cell*. The two sets of extracted data will need to be compared and the final data set agreed for the meta-analysis. In order to do both these analyses, the data has to be presented in a particular form, with only one number per cell in the EXCEL spreadsheet.
8. If a variety of data is reported, tabulate. When a variety of data is reported across trials, in terms of different measures of the same outcome, or different stages of the trial (e.g. baseline, or endpoint), the number of columns in your data extraction file in EXCEL will multiply. This can be overwhelming, and to help decide how to analyse the data (in terms of what effect estimate to use) it might be useful to produce a simple table to provide an overview of what data are available. Let me give you an example. In a systematic review I worked on, we were interested in the effect of treatment on albumin excretion, but this was reported in some studies as albumin excretion rate and in other studies as albumin creatinine ratio. Between the included studies, data was reported in terms of endpoint data, change from baseline, percentage change from baseline and percentage difference between the two treatment arms. In our review, we found it helpful just considering these six variables, and we decided that using a ratio of means effect measure (which will be covered in a future blog post) we were able to pool more data.
9. *Flag* studies for which you *have made estimates*. These studies will need to be *excluded as a sensitivity analysis* to ensure that your conclusions are not sensitive to the estimates that you’ve made. So it’s important that you can quickly identify them when you’re doing the meta-analysis.
10. *Flag* studies which have *low* assessments of *quality*. You may also wish to exclude studies with low quality as a *sensitivity analysis*, so also flagging these will ensure that all the information that’s required for the sensitivity analysis is together.
11. *Extract* the data *twice*, in pairs and independently, compare the two sets of data and resolve any discrepancies, with a third person adjudicating if necessary. This is a well- established recommendation. If the outcomes are subjective, it may be necessary to have more than two people extract the data.
12. *Keep a copy of the data*, as reported, *untouched*. Perform your data extraction methods on a copy of the original data. If there are any queries later you can always go back to the original data without having to extract it again.
13. If you have data queries, try *contacting the authors*. You may want clarification about published data or enquire about data that you want but are not reported. When contacting authors it’s important to emphasise that you’re only asking for summary data that are readily available. Otherwise, authors may assume that you are inviting them to collaborate, which can lead to awkwardness. First email the corresponding author, and if they don’t reply, try contacting the final author listed on the publication, as they’re usually the principal investigator of the study.
14. *Check* your *units*. For example, in a review I worked on, some studies reported albumin excretion rate in mg/24hr and others reported it in μg/min. Data need to be converted to a common unit.
15. Look out for *dropouts*. When dealing with *clinical trial* data, for each treatment arm, you need to establish how many patients relate to the summary data that you’ve extracted. If you’ve extracted baseline data, then you can find the number of patients in each treatment arm in the CONSORT flow diagram. If you are extracting data for change from baseline or endpoint data you need to check for reports of the number of patients in each group who have not completed follow-up.
16. Automate as much as you can. *Calculations coded (written) in a computer program* can easily checked for errors and these calculations can be repeatedly rerun, without introducing human errors.
17. *Don’t exclude* studies just because the data you want are *not reported*. Try to make *sensible estimates* from the given data so that as many studies as possible that meet your eligibility criteria are included in the meta-analysis. Follow my blog to find out how to convert data from what you’re given into what you want.
18. Be careful when there’s *more than one intervention* group. Sometimes a trial may report more than one intervention group and a control group. For example, in a trial of patients with type 2 diabetes Goldstein et al (2007) reported the effects of two glycaemic controlling drugs, Sitagliptin and Metformin, on HbAiC levels (Table). HbAiC levels are routinely measured in patients with diabetes to establish how well their diabetes is controlled.![[Pasted image 20230411112010.png|300]]
19. Look out for *multiple reports from the same study*. These can be referred to as duplicate publications. They can range from reproductions of a published article, based on an identical population and outcomes (identical manuscript), to reports of *subgroups* or *expanded populations and different outcomes*. Including duplicate data can introduce considerable biases to your analysis. Often duplicate publications are covert, in that they don’t cross reference the original study publication. The recommendations for spotting overlapping data (duplicate publications) include *comparing the author names, study locations and settings, population sizes, dates and study durations*, and information about the study interventions. In the review mentioned above, it was also necessary to compare the blood pressure variability measures that were reported in each publication. Data extraction often involves an element of ‘*detective work*’ to find the data you want whilst checking for covert duplicate publications and patient dropouts.
20. *Extract data from the graph* using WebplotDigitizer online tool https://automeris.io/WebPlotDigitizer/
21. ![[Pasted image 20230411113934.png|400]] ![[Pasted image 20230411113951.png|300]] ![[Pasted image 20230411114009.png|400]] 
22. In order to include a study in a meta-analysis, you might have made an estimate that’s not recommended by the Cochrane Handbook. For example, estimating the standard deviation by the range or by the inter-quartile range when data are not normally distributed. Rerun the meta-analysis *excluding studies with estimates*.
23. 1.  You might have been unclear about the data reported and the authors didn’t reply to your request for clarification, so you made an assumption. For example, you weren’t sure if the reported statistic was a standard deviation or standard error. Rerun the meta-analysis *applying other assumptions*.
24. 1.  You might have been *able to make more than one estimate from reported data*. For example, the worked example that I gave previously (post C4) showed that empty cells in the table could be completed using summary data in the row (using the change score or endpoint equations) or the column (using the group or rearranged group equations). Rerun the meta-analysis *using alternative data*.
https://training.cochrane.org/handbook/current/chapter-06#section-6-5-2



 

