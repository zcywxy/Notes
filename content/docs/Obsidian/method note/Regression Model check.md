# influential points
Influential observations are data points that have a disproportionate impact on the results of a regression analysis. Identifying and investigating influential observations is an important step in model diagnostics.

In the context of logistic regression, you can use several diagnostic measures to identify influential observations, such as Cook's distance, leverage, and standardized residuals. Here's how you can identify influential observations in logistic regression using R:
```
model <- glm(response ~ predictor1 + predictor2 + ..., family = "binomial", data = your_data)
install.packages("car")
library(car)
influenceIndexPlot(model, id.n = 5, scale = 3, qq = FALSE)
```

-  **Cook's distance**: Observations with a high Cook's distance have a substantial influence on the estimates of the regression coefficients. There is no strict cutoff, but values above 1 or 4/n (where n is the number of observations) are often considered influential.
-  **Leverage (hat values)**: Leverage measures the influence of an observation on its own fitted value. High leverage observations can have a large impact on the regression line. A common threshold for influential leverage values is 2*(k+1)/n, where k is the number of predictors (including the intercept) and n is the number of observations.
-  **Standardized residuals**: Large standardized residuals indicate observations that do not fit the model well. A common threshold for identifying unusual standardized residuals is an absolute value greater than 2 or 3.