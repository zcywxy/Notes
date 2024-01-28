# Ch6: Estimation
A **random sample** is a selection of some members of the population such that each member is independently chosen and has a known nonzero probability of being selected. A **simple random sample** is a random sample in which each group member has the same probability of being selected. The reference, target, or study population is the group we want to study. The random sample is selected from the study population. For ease of discussion, we use the abbreviated term “random sample” to denote a simple random sample. Although many samples in practice are random samples, this is not the only type of sample used in practice. A popular alternative design is cluster sampling. Therefore, our random sample would consist of the people numbered 329, 242, . . . , 373 in the alphabetical list. In this particular case there were no repeats in the 20 three-digit numbers selected. If there had been repeats, then more three-digit numbers would have been selected until 20 unique numbers were selected. This process is called *random selection*. 因此，我们的随机样本将包括329,242人，…按字母顺序排列的名单中，有373人。在这个特殊的例子中，选择的20个三位数没有重复。如果有重复，则会选择更多的三位数字，直到选择20个唯一的数字。这个过程叫做随机选择。
![[Pasted image 20230411153906.png]] ![[Pasted image 20230411155849.png]] ![[Pasted image 20230411160817.png]] ![[Pasted image 20230411160830.png]] 

### Estimation of the mean of a distribution
A natural estimator to use for estimating the population mean μ is the sample mean ![[Pasted image 20230411154704.png]] . The sampling *distribution of $\overline X$ is* the distribution of values *of $\overline x$ over all possible samples of size n* that could have been selected from the reference population. Let *X1, . . . , Xn be a random sample* drawn from some population with mean μ. Then, for the sample mean $\overline X$, E($\overline X$)=µ (Equation 6.1). Note that Equation 6.1 holds for any population regardless of its underlying
distribution. In words, we refer to X as an unbiased estimator of μ. We refer to an estimator of a parameter θ as $\hat \theta$ . An estimator  $\hat \theta$ of a parameter θ is **un-biased** if E( $\hat \theta$)=θ. This means that the average value of $\hat \theta$ over a large number of
random samples of size n is θ. The unbiasedness of $\overline X$ is not sufficient reason to use it as an estimator of μ. For symmetric distributions, many unbiased estimators of μ exist, including the sample median and the average value of the largest and smallest data points in a sample. Why is $\overline X$ chosen rather than any of the other unbiased estimators? The reason is that if the underlying distribution of the population is normal, then it can be shown that the unbiased estimator with the smallest variance is given by $\overline X$. Thus, $\overline X$ is called the **minimum variance unbiased estimator** of μ. 

Let X1 , . . . , X n be a random sample from a population with underlying mean μ and variance $σ^2$ . The set of sample means in repeated random samples of size n from this population has variance $σ^2$/ n. The standard deviation of this set of sample means is thus σ/$\sqrt n$  and is referred to as the *standard error of the mean* or the standard error. 

The important point to understand is that the boundaries of the interval depend on the sample mean and sample variance and vary from sample to sample. Furthermore, *95% of such intervals* that could be constructed from repeated random samples of size n contain the parameter μ.
- **Point estimate of mean and confidence interval**
	- ![[Pasted image 20230411162252.png|600]] ![[Pasted image 20230411162536.png|580]] ![[Pasted image 20230411162411.png|600]]  ![[Pasted image 20230411162718.png|500]]  ![[Pasted image 20230411162814.png|600]] ![[Pasted image 20230411164836.png|700]] ![[Pasted image 20230411165310.png|500]] 
- **Sample variance confidence interval**
	- ![[Pasted image 20230411163304.png|600]] ![[Pasted image 20230411163722.png|600]] 
	- ![[Pasted image 20230411163406.png|600]] ![[Pasted image 20230411164316.png|700]]  
	 - ![[Pasted image 20230411163756.png|300]]  
## Hypothesis test
The p-value can also be thought of as the probability of obtaining a test statistic as extreme as or more extreme than the actual test statistic obtained, given that the null hypothesis is true.
- **One sample**
	-  ![[Pasted image 20230411170154.png|500]] ![[Pasted image 20230411170322.png|400]] ![[Pasted image 20230411170847.png|500]] 
- **Two sample**
	- ![[Pasted image 20230411172045.png|500]] ![[Pasted image 20230411172857.png|500]] 
- *F-test for equality of two variances*
	- ![[Pasted image 20230411172331.png|500]] ![[Pasted image 20230411172346.png|500]] ![[Pasted image 20230411172625.png|500]] 
- Test for beta coefficient
	- ![[Pasted image 20230411222302.png|600]] 

# Chapter 11 Regression and Correlation Methods
- Some definition
	- raw sum of squares for X 
		- ![[Pasted image 20230815170053.png|50]]
	- **Lxx**: corrected sum of squares of X
		- ![[Pasted image 20230815170130.png|200]] 
	- raw sum of squares for Y
		- ![[Pasted image 20230815170154.png|50]]
	- **Lyy**: corrected sum of squares of Y
		- ![[Pasted image 20230815170248.png|200]] 
	- raw sum of cross products
		- ![[Pasted image 20230815170419.png|50]] 
	- **Lxy**: corrected sum of cross products
		- ![[Pasted image 20230815170438.png|130]] 
	- **Lest-Squares slope**
		- b = Lxy /Lxx
	- **Total SS**: total sum of squares
		- ![[Pasted image 20230815170836.png|100]] 
		- Total SS = Reg SS + Res SS
	- **Reg SS**: regression sum of squares
		- ![[Pasted image 20230815170924.png|100]]  
	- **Res SS**: residual sum of squares
		- ![[Pasted image 20230815171020.png|100]]
	- **Reg MS**: regression mean square
		- Reg MS = Reg SS/k
		- the number of predictor variables (k) in the model (not including the constant)
	- **Res MS**: residual mean square， $S^2_{y•x}$
		- Res MS = Res SS/(n − k − 1)
		- We refer to n − k − 1 as the degrees of freedom for the residual sum of squares, or Res df
	- **R2** is defined as Reg SS/Total SS
- F test for simple linear regression
	- ![[Pasted image 20230815171615.png|400]] 
- t Test for simple linear regression
	- t=b/se(b)
	- ![[Pasted image 20230815172727.png|500]] 
	- ![[Pasted image 20230815173009.png|500]] 
- Correlation
	- ![[Pasted image 20230815174259.png|300]] 
	- ![[Pasted image 20230815174319.png|300]] 
	- The sample (Pearson) correlation coefficient (r) is defined by ![[Pasted image 20230815174414.png|100]] 
	- ![[Pasted image 20230815174812.png|500]] 
	- ![[Pasted image 20230815174858.png|70]] 
	- t test
		- ![[Pasted image 20230815175247.png|100]] 
	- ![[Pasted image 20230815175344.png|400]] 