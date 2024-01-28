# Determine the Knots
When constructing the segments variables
![[Pasted image 20230413195313.png|500]]
```{r Two knots piecewise model}
knot1 <- seq(from=-20, to=0, by=1).                                                                                                                                                                                    knot2 <- seq(from=1, to=25, by=1)
seg1 <- function(x, knot1) ifelse(x<=knot1, x, knot1)
seg2 <- function(x, knot1, knot2) ifelse(x<=knot1, 0, ifelse(x <= knot2, x-knot1, knot2-knot1))
seg3 <- function(x, knot2) ifelse(x>knot2, x-knot2, 0)
knots_models <- function(k1,k2) {
  out <- tryCatch(
    {
      fixed <- eval(substitute(IQ~seg1(IQ_Time,k1)+seg2(IQ_Time,k1,k2)+seg3(IQ_Time,k2), list(k1=k1, k2=k2)))
      fit <- lme(fixed, random=~1|ID, data=cog_dat_long, subset=cog_dat_long$ID %in% anytwoiq_ids, na.action=na.omit)
      update(fit, correlation=corCAR1(form = ~ 1|ID))
      BIC(fit)
    },
    error=function(cond) {
      message("Error message:")
      message(cond)
      return(NA)
    },
    warning=function(cond) {
      message("Warning message:")
      message(cond)
      fixed <- eval(substitute(IQ~seg1(IQ_Time,k1)+seg2(IQ_Time,k1,k2)+seg3(IQ_Time,k2), list(k1=k1, k2=k2)))
      fit <- lme(fixed, random=~1|ID, data=cog_dat_long, subset=cog_dat_long$ID %in% anytwoiq_ids, na.action=na.omit)
      update(fit, correlation=corCAR1(form = ~ 1|ID))
      BIC(fit)
    })    
  return(out)
}
knots_models_v <- Vectorize(knots_models)
knots_results <- outer(knot1,knot2,knots_models_v)
knots_results[knots_results==min(knots_results, na.rm=T)]

k1 <- -14
k2 <- 22
```

# Determine the correlation structure
![[Pasted image 20230413200348.png]]
![[Pasted image 20230413195711.png|500]] ![[Pasted image 20230413195746.png|500]] 
![[Pasted image 20230413195824.png]] ![[Pasted image 20230413195839.png]] ![[Pasted image 20230413195910.png|400]] ![[Pasted image 20230413200043.png]] ![[Pasted image 20230413200121.png]] ![[Pasted image 20230413200246.png]] 
# Fit the model and plot
```
T1 <- seg1(cog_dat_long$AIQ_Time,-14)
T2 <- seg2(cog_dat_long$AIQ_Time,-14,22)
T3 <- seg3(cog_dat_long$AIQ_Time,22)

SZ#Final Model: CAR1 with random T1, T2 slope
summary(lme(AIQ~1 + T1+T2+T3, 
                random=~T1+T2|ID, data=cog_dat_long,na.action=na.omit,
                correlation = corCAR1(form =  ~ 1 | ID),method = "ML", 
                control =list(msMaxIter = 1000, msMaxEval = 1000)))
```

```
ggplot(aes(x = AIQ_Time, y = AIQ), data = cog_pre_long) +
  geom_line(aes(group = ID), color = "gray") + 
  geom_smooth(aes(group = 1), size = 3, color = "red", se = FALSE) +
  theme_bw()
```
![[Pasted image 20230413222657.png]]