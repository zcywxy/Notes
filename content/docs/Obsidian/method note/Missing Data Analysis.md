# Missing Data Mechanisms
- Partitioning the Realized Data
	- ![[Pasted image 20230919132929.png|490]]  ![[Pasted image 20230919160042.png|600]] 
- **Missing Completely at Random**
	- Missingness is unrelated to the *observed data* (perceived control over pain) and the *unseen data* (depression)
	- ![[Pasted image 20230919131905.png|520]]  ![[Pasted image 20230919160443.png|400]] 
- **Conditionally Missing at Random CMAR** 
	- Missingness is related to the observed data (perceived control over pain) but unrelated to the unseen data (depression).
		- Individuals with low perceived control are more likely to have missing data due to their diminished functional status
		- The Big Three assume a CMAR process by default
		- assume that *everything we need to know about those missing depression* scores **is contained within the observed data**, in this case, perceived control. Over pain. 
	- ![[Pasted image 20230919132020.png|550]] ![[Pasted image 20230919160827.png|400]]
- **Missing Not at Random**
	- Missingness is related to the unseen data (depression) and potentially to the observed data (perceived control) as well
	- Individuals with the highest levels of depression are more likely to be missing due to their debilitating 使衰弱  symptoms
	- ![[Pasted image 20230919132241.png|550]] ![[Pasted image 20230919161416.png|400]]

# Testing Assumptions
- The Big Three achieve unbiasedness if the process is conditionally MAR 
	- the unseen score values carry no important information. We literally don't even need them, because if I know your perceived control over pain, I have everything that I need to understand your missing depression score
- This **CMAR** assumption is *untestable* because it stipulates no relation between missingness and the unseen scores
	- Because we don't have those unseen scores. We couldn't use the data to sort of prove that those scores don't have an influence. Ultimately, we're gonna be adopting an assumption that is purely untestable.
- When in doubt, conduct sensitivity analyses that **compare the estimates** from *CMAR and MNAR assumptions*
	- we have tools that are pretty straightforward to use where we could model that missing not at random process. So we don't have to perform our analyses under this missing at random assumption. We could supplement those analyses with a model that makes a different assumption that allows the unseen score values to carry weight in estimation. 
	- **sensitivity analysis**, essentially fit or model multiple times, same model, but making *different assumptions* about why the data are *missing*. 
- if they have a longitudinal study where they have complete scores at baseline, but missing this at later time points, they tested whether missing this was related to scores at baseline. Would it be an appropriate way to test for missing not at random?
	- Does one's baseline status sort of tell us something about whether or not they're gonna drop out? Let's say that it does. Right. Let's say that the people who dropped out tend to have significantly higher baseline scores or it could be significantly lower. 
	- all were able to say is that missing? This is not haphazard. If you find that the baseline scores differ with dropouts and complete as all you've done is rule out the missing completely at random assumption.We've got something systematic going on. And the data do not allow us to figure out what that something is. Essentially
	- Let's say that there aren't differences at baseline. 
	- There still could be differences between dropouts and completers on some other variable. Right? Beyond the baseline scores, maybe some demographic variable or something like that.
# Older method
1. delete missing values (complete delete, pairwise delete)
	- deletion gives an unrepresentative sample with biased estimates of center, spread, and associations
		- ![[Pasted image 20230919132718.png|500]] 
1. impute them
	- mean imputation infuses the data with constant scores, producing biased estimates under any process. We will underestimate the relationships
		- ![[Pasted image 20230919130855.png|500]] 
2. Regression Imputation
	- Imputations fall directly on the regression line, restricting variability and attenuating associations. We will overestimate the relationships
		- ![[Pasted image 20230919130812.png|500]]


# Prepare Missing Analysis
- Inclusive Analysis Strategy
	- The idea behind an inclusive strategy is that we're gonna introduce one or more additional variables that we wouldn't have used. Had the data been complete. These extra variables, they call **auxiliary variables**.
	- Collins et al. (2001) Typology
		-  ![[Pasted image 20230919180330.png|110]] ![[Pasted image 20230919165149.png|100]] ![[Pasted image 20230919164835.png|105]]
		- Type C: useless
			- Variable A predict the missingness but not predict Y
			- those types of variables it ends up are of **no use to us** whatsoever, like we're gonna get absolutely no benefit to including a variable like a in our analysis. that might seem counter intuitive, because they do predict why people are missing, right? 
			- But they *don't have the capacity to introduce bias* unless they also correlate with y essentially, if they're uncorrelated with y then there's nothing to adjust for. There's no non response bias present. Those are the variables we want to ignore.
		-  Type B: good
			- It would make sense to **contemplate考虑, including that variable in our analysis**, because if a correlate with y then what that implies is some of the lost information and why some of the information contained in those missing scores. We could actually recapture that from a right? A tells us something about the missing scores and Y, but it doesn't tell us anything about why people are missing. 
				- It ends up that these type b variables they are useful to us be good to include a but *if* I *don't include* A，i'm not going to achieve any non-response bias as a result. There's *no damage* really in *forgetting* about a or leaving it out of our analysis, at least in terms of bias. The only real upside is that we *can improve power by including it*.
		- Type A: really want it
			- those are the variables that are *really useful* to include, because they're the ones that are gonna eliminate or reduce non response bias. These are the ones that are really gonna *help us satisfy that conditionally missing at random assumption*. If we can find one or two of these type A auxiliary variables, then we might be able to make a stronger argument that we've done a good job of satisfying this assumption. We've got this sort of hierarchy of extra variables. 
	- **Chronic Pain Data Example to choose Auxiliary Variable**
		- ![[Pasted image 20230919181325.png|600]]
		- Test which variable is correlated the missingness of variables
			- ![[Pasted image 20230919181612.png|400]] 
		- **Semipartial (Residual) Correlations, 0.3 is cutoff**
			- Q:  if an auxiliary variable is moderately strongly related to the outcome of interest, wouldn't this suggest that it should have been included as a predictor all along? Your model has an omitted variable problem without it? 
				- most of the really salient source of correlation, is already in your model to that person's ., like finding an extra variable that has a lot of correlation with the thing that's missing
			- It's actually *not the bivariate correlation* that matters here. It's the *residual correlation matters*
				- It's whether the part of depression that remains after we've sort of accounted for the analysis variables, whether that leftover part Of depression, sort of the unexplained variation in depression, correlate with the auxiliary variables that really matters.
			- A semipartial correlation ($r_{sp}$) is the correlation between one variable and the residual of another
			- A third variable (already in the analysis) is partialled out of the incomplete variable but not the auxiliary variables
			- Correlate the (a) residuals and auxiliary variables, (b) other analysis variables and auxiliary variables, and (c) auxiliary variables with each other
			- ![[Pasted image 20230919182055.png|400]] ![[Pasted image 20230919183126.png|400]] 
			- In summary to A, B, or C type
				- ![[Pasted image 20230919183348.png|400]]
			- simulations showed that there's not really any downside risk to Including an auxiliary variable. I like to keep the number really low, because when we move into maximum likelihood estimation with auxiliary variables, it ends up that those models the auxiliary variable models that we're gonna use with femoral tend to experience convergence failures a lot. Having fewer auxiliary variables is better. But you can certainly err on the side of inclusion rather than exclusion. There's no harm in doing that. 
			- collinearity is your friend, in this case, with the auxiliary variables, like you actually want variables with lots of correlation, like that's really the hallmark of a good auxiliary variable. 
				- usually want to avoid collinearity, because our beta weights become really unstable and have large standard errors and can flip signs and do weird things like that
				- But the auxiliary variables aren't going to enter as predictors into the model. 
				- Those sorts of symptoms of collinearity that we are taught to be aware of in regression class aren't going to be an issue, the way that we're gonna use the auxiliary variables.
# Modern Methods: The Big Three
## Maximum Likelihood
Classic FIML Estimation in Structural Equation Modeling Framework
Employee Data
![[Pasted image 20230919185034.png|400]] 
![[Pasted image 20230919185111.png|200]]
![[Pasted image 20230919190605.png|600]]

![[Pasted image 20230919190844.png|500]]

These deviation scores are really, just super simple concepts, how far away is a score from the center of the distribution? How well does this pair of scores match the parameters? 

Then the covariance matrix is just there to like standardize the distances, compute, convert them to z score units, essentially. 
## Bayesian Estimation

## Multiple Imputation

