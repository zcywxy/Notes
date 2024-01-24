# Shapiro-Wilk test
```
shapiro.test(sample_data)
```
The output will show the W statistic and the p-value. If the p-value is greater than your chosen significance level (typically 0.05), you can assume the data is normally distributed.


# Q-Q plot
```
ggplot(data.frame(sample_data), aes(sample = sample_data)) + stat_qq() + stat_qq_line() + ggtitle("Q-Q Plot")
```
In a Q-Q plot, if the points fall along the diagonal line, it indicates that the data is normally distributed. If the points deviate significantly from the line, the data may not be normally distributed.


# Histogram
```
ggplot(data.frame(sample_data), aes(x = sample_data)) + geom_histogram(aes(y = ..density..), bins = 30, fill = "lightblue", color = "black") + geom_density(color = "red") + ggtitle("Histogram and Density Plot")
```

A histogram allows you to visualize the data distribution. If the histogram shows a bell-shaped curve (symmetric and unimodal), it suggests that the data might be normally distributed. If the shape deviates from a bell curve, the data may not be normally distributed.

# Anderson-Darling test
```
install.packages("nortest") 
library(nortest) 

ad.test(sample_data)
```

The Anderson-Darling test is a modification of the Kolmogorov-Smirnov test and gives more weight to the tails of the distribution. To perform the Anderson-Darling test in R, you can use the `ad.test()` function from the "nortest" package.

# Lilliefors test
```
install.packages("nortest")
library(nortest)
lillie.test(sample_data)
```

The Lilliefors test is a modification of the Kolmogorov-Smirnov test for small sample sizes when the parameters (mean and variance) are unknown. To perform the Lilliefors test in R, you can use the `lillie.test()` function from the "nortest" package.

# Jarque-Bera test
```
install.packages("moments")
library(moments)
jarque.bera.test(sample_data)
```
The Jarque-Bera test is based on the skewness and kurtosis of the data. It tests the null hypothesis that the data comes from a normal distribution against the alternative hypothesis that it does not. To perform the Jarque-Bera test in R, you can use the `jarque.bera.test()` function from the "moments" package.