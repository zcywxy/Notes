进行一个研究分析的步骤通常包括以下几个阶段：

1.  明确研究目标：确定研究的目的和主要问题。这将有助于为分析和研究设计提供明确的方向。
2.  文献回顾：查阅相关领域的现有研究，以了解先前研究的发现、研究方法和理论框架。这可以帮助您确定研究的空白点，以及可能的理论和实证贡献。
3.  研究设计：根据研究问题和目标，选择合适的研究方法。这可能包括实验设计、观察研究、调查研究、案例研究等。此外，还需要确定数据收集方法和技术，例如问卷调查、访谈或实验室测试。
4.  数据收集：根据研究设计收集数据。确保数据收集过程中遵循伦理规范，并确保数据质量和完整性。
5.  数据整理：整理收集到的数据，以便进行分析。这可能包括数据清洗、数据转换和数据编码等步骤。
6.  数据分析：使用适当的统计方法和工具对数据进行分析，以回答研究问题并检验研究假设。可能涉及描述性统计、推论统计或建模等方法。
7.  结果解释：基于数据分析结果，对研究问题进行解释。评估结果的显著性、可靠性和实用性，并将其与现有文献中的发现进行比较。
8.  结论与建议：总结研究的主要发现，并提出实际应用的建议。这可能包括政策建议、实践指南或未来研究方向等。
9.  撰写报告或论文：将研究过程、方法、结果和结论整理成报告或学术论文。确保遵循适当的引用和格式规范。
10.  审核与反馈：在同行评审或导师审阅的基础上，对报告或论文进行修改和完善。这将有助于提高研究的质量和可信度。

数据分析的具体步骤可以根据项目的需求和目标有所不同，但通常包括以下几个阶段：

1.  数据清洗：在进行数据分析之前，需要对数据进行清洗。数据清洗包括识别并处理*缺失值、异常值、重复*数据和*不一致*的数据。这是确保数据质量的重要步骤。
2.  数据探索：通过描述性统计和可视化方法对数据进行初步探索。这可以帮助您了解*数据的分布、中心趋势和离散程度*，以及*各变量之间的关系*。常用的描述性统计方法包括计算均值、中位数、众数、标准差和四分位数等。常用的可视化方法包括条形图、直方图、箱线图、散点图和热力图等。
3.  特征工程：根据分析目标，对数据进行特征工程。这包括特征选择（选择与目标变量相关的特征）、特征转换（如对数转换、归一化或标准化等）和特征构建（通过组合现有特征创建新特征）等。
4.  数据建模：选择合适的统计模型或机器学习算法，以回答研究问题或实现预测。这可能涉及线性回归、逻辑回归、决策树、随机森林、支持向量机、神经网络等方法。在建模过程中，需要将数据集分为训练集和测试集，以便评估模型的性能。
5.  模型训练与评估：使用训练数据拟合模型，并使用测试数据评估模型的性能。评估指标可能包括准确率、精确度、召回率、F1分数、均方误差等。根据评估结果，调整模型参数或尝试其他模型，以优化性能。
6.  模型验证与优化：使用交叉验证、网格搜索或随机搜索等方法，对模型进行验证和优化。这可以帮助确保模型在未知数据上的泛化性能。
7.  结果解释与报告：基于模型结果，对研究问题进行解释。将关键发现、模型性能、模型限制和建议整理成报告，以便向其他人传达分析结果。
8.  部署与监控（可选）：如果数据分析项目涉及预测模型的实际应用，需要将模型部署到生产环境，并对其性能进行持续监控和维护。这可能涉及使用API将模型集成到现有系统
# 1. Data Cleaning
![[Pasted image 20230303124033.png|450]] ![[Pasted image 20230303123942.png|450]]

## Delte columns or rows with all NAs

```
Doing235813@
df[rowSums(is.na(df)) != ncol(df), ]

filter(df, rowSums(is.na(df)) != ncol(df))

# remove colums
df[,colSums(is.na(df))<nrow(df)]

df3 <- Filter(function(x)!all(is.na(x)), df)})

select(-all_of(names(.)[sapply(., function(x) all(is.na(x)))]))
```


`sapply(., function(x) all(is.na(x)))` checks if all values in each column of the data frame `.` are NA. It returns a logical vector indicating which columns have all values as NA.
## coalesce_join
[original blog](https://alistaire.rbind.io/blog/coalescing-joins/)

When aggregating data, it is not uncommon to need to combine datasets containing identical non-key variables in varying states of completeness. There are various ways to accomplish this task. One possibility an coalescing join, a join in which missing values in `x` are filled with matching values from `y`. Such behavior does not exist in current dplyr joins, [though it has been discussed, and so may someday](https://github.com/tidyverse/tidyr/issues/183). For now, let’s build an `coalesce_join` function.
```
coalesce_join <- function(x, y, 
                          by = NULL, suffix = c(".x", ".y"), 
                          join = dplyr::full_join, ...) {
  joined <- join(x, y, by = by, suffix = suffix, ...)
  # names of desired output
  cols <- union(names(x), names(y))
  
  to_coalesce <- names(joined)[!names(joined) %in% cols]
  suffix_used <- suffix[ifelse(endsWith(to_coalesce, suffix[1]), 1, 2)]
  # remove suffixes and deduplicate
  to_coalesce <- unique(substr(
    to_coalesce, 
    1, 
    nchar(to_coalesce) - nchar(suffix_used)
  ))
  
  coalesced <- purrr::map_dfc(to_coalesce, ~dplyr::coalesce(
    joined[[paste0(.x, suffix[1])]], 
    joined[[paste0(.x, suffix[2])]]
  ))
  names(coalesced) <- to_coalesce
  
  dplyr::bind_cols(joined, coalesced)[cols]
}
```

## Across
Manipulate **same actions to multiple colums** [[Why I love dplyr's across]]

A *lambda function*, also known as an anonymous function, is a type of function in programming that does not have a name and is *defined on-the-fly within the code*. Lambda functions are often used when a simple function is needed for a short period of time and creating a named function would be unnecessary or cumbersome. In R, a lambda function is created using the "function" keyword, followed by the function's arguments and a body of code. Unlike Python, R does not have a specific "lambda" keyword. *function(x, y) {x + y}*. In R, it is also possible to define a lambda function using the formula notation. The formula notation uses the tilde ("~") operator to separate the function arguments from the function body. Here is an example of a lambda function defined using the formula notation: *function(x) {x ~ x^2}*
We’ll **use `~` to indicate that we’re supplying a lambda function and use `.x` to indicate where the variable in `across` is used**. 
```
	ac_items %>% group_by(category) %>% summarise(across(where(is.numeric), mean, na.rm = TRUE, .names = "{col}_"))
	
	ac_items %>%
	  group_by(category) %>%
	  summarise(across(c(sell_value, buy_value),
	                   list(mean = mean, sd = sd), na.rm = TRUE, .names = "{col}_{fn}"))
	
	ac_items %>%
	  group_by(category) %>%
	  mutate(across(c(sell_value, buy_value), ~ .x / max(.x, na.rm = TRUE),
	                .names = "{col}_prop")) %>%
	  select(category, ends_with("prop")) # to show new cols
```


## Map
![[Pasted image 20230303124555.png|650]] ![[Pasted image 20230303124650.png|650]]
## String
[Stringr Cheatsheet](https://evoldyn.gitlab.io/evomics-2018/ref-sheets/R_strings.pdf)

# 2. Data Exploring
## Assign corresponding (factor) type to the data
Check the **amount of unique value for each column** in dataframe
```
colnames(df)[apply(df,2,function(x) { length(unique(na.omit(x)))==2})]
```

Summary **labels** for both var and values
```
labelled::look_for(df, details = TRUE)
```

**Drop unused levels and lables** (sometimes the NA is embeded by value labels)
```
droplevels() %>% drop_unused_value_labels()
```

Transform labled **numbers to factor**

In R, a *factor* is a variable used to *represent categorical data*. A factor is essentially a vector of integers that represents a set of categorical values, where each integer corresponds to a specific level or category. Factors are created using the "factor()" function. One of the main *differences between factors and character* vectors in R is that *factors* are used to represent categorical data *with a fixed set of levels*, whereas *character vectors can contain any string of characters*. Additionally, factors in R are treated as nominal or ordinal data, while character vectors are treated as text data. Factors have some advantages over character vectors when working with categorical data, such as the ability to easily subset and manipulate levels, and they use less memory than character vectors.
```
#vars_factor_all is a vector of variable names to be transformed
df %>% mutate_at(vars_factor_all, haven::as_factor)
```

haven::as_factor will transfer named numbers to factors
![[Pasted image 20230303103742.png|400]]![[Pasted image 20230303104626.png|600]]
```
[1] MALE   FEMALE FEMALE FEMALE MALE  
Levels: MALE FEMALE
```

unlabeled number will treat numbers as character
```
	num [1:1042] 0 0 0 0 0 0 0 0 0 0 ...
	 - attr(*, "format.spss")= chr "F1.0"
	
	 Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 1 1 1 ...
```

label factor levels
```
df_2$group_3  <- factor(df_2$group_3, levels=c(0,1), 
                           labels=c("Control_include",
                                    "Case_include"))

```
 
label factor levels for multiple vars
 ```
 label_fun<- function(var,label){
  val_labels(var) <- label
  return(var)
}

labels_location <- c(other=1, "south canal"=2, barges=3,"adjacent pile"=4, pile=5)
labels_yesno <- c(no=0, yes=1)
labels_protect_fre4 <- c(always=1 ,"most times"=2, "some times"=3, rare=4)

eaq_3 <- eaq_3  %>% 
  mutate(across(contains(c("clothes","shower","respir","carti")),~label_fun(.x,label = labels_protect_fre4))) %>% 
  mutate(across(contains("location"),~label_fun(.x,label = labels_location))) %>% 
  mutate(across(contains("enclosed"),~label_fun(.x,label = labels_yesno) ))
```


**Relabel the var labels**

Named list to label variables
```
new_names <- list(age="Age",
                 dx_aoo_psychosis="Age of 1st psychotic episode",
                 d_sex="Gender",
                 d_ses_complete="Occupation (lower number=higher earning)",
                 d_race_complete="Race",
                 white_race="White",
                 d_sv1038="Type of Dwelling",
                 SO1019="Education",
                 DUP_Nora="Days between the first symptom and first treatment",
                 fam_sz="Family history of schizophrenia",
                 fam_aff="Family history of affection disorder",
                 fam_sub="Family history of substance abuse",
                 cig01lt="Lifetime ever smoked",
                 homeless01_before="Homeless at baseline",
                 d_lives_indep01="living independently at baseline",
                 d_finance_pub01="receive public assistance at baseline")
var_label(df_2) <- new_names
```

subset named list by names and label regression results
```
	regression_lab <- new_names[names(new_names)[names(new_names) %in% unique(two_PRS_all_logi$Regression)]]
	
	paste0(names(regression_lab),"=","'",regression_lab,"'",collapse = ",")
	
	two_PRS_case_logi <- two_PRS_case_logi %>% 
	  mutate(Regression_lab=recode(Regression,lib_XXV='Recovery at 25yr',homeless_XXV='Homeless at 25yr',live_indep_XXV='living independently at 25yr',DMXXV_Q20B='Economically independent at 25yr',pub_assistance_XXV='receive public assistance at 25yr',andr_XXV='remission at 25yr')) %>% 
	  filter(Regression %in% c("lib_XXV","andr_XXV","live_indep_XXV","DMXXV_Q20B"))
```
## Description statistics

[table1 function](https://cran.r-project.org/web/packages/table1/vignettes/table1-examples.html)
```
table1(~age+dx_aoo_psychosis+d_sex+d_race_complete+d_ses_complete,data = df_2,overall=F,extra.col=list(P=pvalue))#render.missing=NULL
```

![[Pasted image 20230303120409.png|400]]

`str()`

## Description plots

## for loop: binary vs continuous violin plots
```
vars_binary <- colnames(df_plot)[apply(df_plot,2, function(x) length(unique(x)))<=3]

your_plot <- list()
for (j in 1:length(vars_binary)) {
  #plot
  p <- ggbetweenstats(
  data  = df_plot,
  x     = !!vars_binary[j],
  y     = "T2_slope")#,
  #effsize.type = "d",
  #var.equal = TRUE)
  # save plot to list
  your_plot[[j]] <- p
}
##cowplot: put plots together

PLOT <- plot_grid(plotlist = your_plot,ncol = 4 ,align = "hv") #4 colums of plots
##calculate the total height, each plot is 6
height <- length(your_plot)/4*6
##Save final plots
ggsave(PLOT,filename = paste0("results/","cow_violinplot",".jpg"),
       limitsize = FALSE,width = 22,height = height)
```

![[Pasted image 20230303123047.png]]

## continuous vs continuous correlation plot
```
# vars_continuous <- colnames(df_plot)[apply(df_plot,2, function(x) length(unique(x)))>7]
library(ggExtra)
library(hrbrthemes)

#self defined function for single plot
my_scatter_plot <- function(var){
 p <- ggplot(df_plot, aes_string(x="T2_slope", y=var)) + 
    geom_point(size=1) +
  geom_smooth(method = "lm")+
  #stat_ellipse(aes(color = SZ), type = "t")+
  stat_cor(method = "spearman")+
  theme_ipsum()
 ggMarginal(p, type = "density")
}

#use lapply to plot all vars and save plot results to the list
scatter_plot_list <- lapply(vars_continuous,my_scatter_plot)

#put multiple plot into one place, here plot column=5
scatter_PLOT <- plot_grid(plotlist=scatter_plot_list,ncol=5,align="hv")
ggsave(scatter_PLOT,filename=paste0("results/","cow_scatterplot.three.piece",".jpg"),limitsize=FALSE,width=20,height=20)  
```

![[Pasted image 20230303123530.png]]
```
my_scatter_SZ <- function(var){
 pmain <- ggplot(cog_pre_long_exp, aes_string(x="T2_slope", y=var,color="SZ")) + 
    geom_point(size=1) +
  geom_smooth(method = "lm")+
  #stat_ellipse(aes(color = SZ), type = "t")+
  stat_cor(method = "spearman")+
  ggpubr::color_palette("jco")
 
 # Marginal densities along x axis
 xdens <- axis_canvas(pmain, axis = "x")+
  geom_density(data = cog_pre_long_exp, aes_string(x = "T2_slope", fill = "SZ"),
              alpha = 0.7, size = 0.2)+
  ggpubr::fill_palette("jco")
# Marginal densities along y axis
# Need to set coord_flip = TRUE, if you plan to use coord_flip()
ydens <- axis_canvas(pmain, axis = var, coord_flip = TRUE)+
  geom_density(data = cog_pre_long_exp, aes_string(x = "T2_slope", fill = "SZ"),
                alpha = 0.7, size = 0.2)+
  coord_flip()+
  ggpubr::fill_palette("jco")
p1 <- insert_xaxis_grob(pmain, xdens, grid::unit(.2, "null"), position = "top")
p2<- insert_yaxis_grob(p1, ydens, grid::unit(.2, "null"), position = "right")
ggdraw(p2)

}
#my_scatter_SZ(continuous[6])
scatter_SZ_list <- lapply(continuous,my_scatter_SZ)
scatter_SZ_PLOT <- plot_grid(plotlist=scatter_SZ_list,ncol=3,align="hv")
ggsave(scatter_SZ_PLOT,filename=paste0("results/","cow_scatterplot_SZ",".jpg"),limitsize=FALSE,width=12,height=20) 
```
![[Pasted image 20230327203744.png]]
## histgram

```
outcomes <- c('infarcts','andr_XXV','lib_XXV','pub_assistance_XXV','d_empXXV')
my_density <- function(outcomes){
  ggplot(cog_pre_long_exp, aes(x = T2_slope)) +
  geom_histogram(aes(y=..density..),fill = "white", colour = "black") +
    geom_density(lwd = 1, colour = 4,
               fill = 4, alpha = 0.25)+
  facet_grid(get(outcomes) ~ .)+
  xlab(paste0("T2_Slope"," by ",outcomes))
}

densitylist <- lapply(outcomes,my_density)
PLOT_density <- plot_grid(plotlist=densitylist,ncol=3,align="hv")
ggsave(PLOT_density,filename=paste0("results/","cow_densityplot",".jpg"),limitsize=FALSE,width=12,height=8) 
```
![[Pasted image 20230327203541.png]]

```
your_plot <- list()
outcoms <- c('infarcts','andr_XXV','lib_XXV','pub_assistance_XXV','d_empXXV')
for (i in 1:length(outcoms)){
  print(i)
  p <- ggplot(cog_pre_long_exp, aes_string(x = "T2_slope", fill = outcoms[i])) +
  geom_histogram(position = "identity", alpha = 0.4)
  your_plot[[i]] <- p
}
##cowplot拼图
library(cowplot)
PLOT_3 <- plot_grid(plotlist = your_plot,ncol = 2 ,align = "hv") 
ggsave(PLOT_3,filename = paste0("results/","cow_hist_2",".jpg"),limitsize = FALSE,width = 12,height = 12)
```
![[Pasted image 20230327203648.png]]


# 3. Analysis

## 3.1 bivariate analysis for main outcome and interested covar
```{r}
	out_var <- c("mci","dementia")
	pre_var <- c(
	  #demo and comorbidity vars
	  'age','gender','race','educ','hypertension',"cholesterol",'diabetes','stroke','current_smoke','drink',
	  #other interested structured exposure var
	  "location_Sept",'location_Oct','location_NovDec','location_JanJun',"concrete_Sept",'concrete_Oct','concrete_NovDec','concrete_JanJun',"diesel_exhaust_SeptOct",'diesel_exhaust_NovDec','diesel_exhaust_JanJun',"nondiesel_exhaust_SeptOct",'nondiesel_exhaust_NovDec','nondiesel_exhaust_JanJun',"hours_Sept","hours_Oct","hours_NovDec","hours_JanJun",
	  #structured protection var
	  "respir_Sept",'respir_Oct','respir_NovDec','respir_JanJun',"respir_change_Sept",'respir_change_Oct','respir_change_NovDec','respir_change_JanJun',"carti_change_Sept",'carti_change_Oct','carti_change_NovDec','carti_change_JanJun',"clothes_SeptOct",'clothes_NovDec','clothes_JanJun',"shower_SeptOct",'shower_NovDec','shower_JanJun',
	  #merged structured var
	  "respir_all_Sept","respir_all_Oct","respir_all_NovDec","respir_all_JanJun","clothes_shower_SeptOct","clothes_shower_NovDec","clothes_shower_JanJun","exhaust_SeptOct","exhaust_NovDec","exhaust_JanJun"
	  )
	
	colnames(df)
	out <- data.frame(Outcome=character(), #1
	                  Predictor=character(), #2
	
	                  N=double(),#3
	                  Coeff=double(), #4
	                  CI=character(), #5
	                  p=double(), #6
	                  
	                  stringsAsFactors = FALSE) #23
	list=list()
	q=1
	j="educ"
	for(i in out_var){
	  for(j in pre_var){
	    if (length(unique(na.omit(pull(df,i))))>=3){
	        f <- formula(paste(i,"~",j))
	        model<-lm(f, data=df)
	        out[q,1]=i #outcome
	        out[q,2]=j #predictor
	        out[q,3]=length(model$residuals) #number of obs
	        out[q,4]=round(summary(model)[["coefficients"]][2,1],2)# pre coef
	        out[q,5]=paste0("(",round(confint.default(model)[2,1],2),", ",round(confint.default(model)[2,2],2),")") #CI
	        out[q,6]=round(summary(model)[["coefficients"]][2,4],3)# pre p
	
	        q=q+1 
	    }
	    else if (length(unique(na.omit(pull(df,i))))<=2){
	        if(!is.factor(pull(df,j))|length(unique(na.omit(pull(df,j))))==2){
	          f <- formula(paste(i,"~",j))
	        model<-glm(f, data=df,family = "binomial")
	        out[q,1]=i
	        out[q,2]=j
	        out[q,3]=length(model$residuals)#number of obs
	        out[q,4]=round(exp(summary(model)[["coefficients"]][2,1]),2)#pre coef
	        out[q,5]=paste0("(",round(exp(confint.default(model)[2,1]),2),", ",round(exp(confint.default(model)[2,2]),2), ")")
	        out[q,6]=round(summary(model)[["coefficients"]][2,4],3)#p
	
	        q=q+1
	        }
	        else if(is.factor(pull(df,j)) & length(unique(na.omit(pull(df,j))))>2){
	          f <- formula(paste(i,"~",j))
	        model<-glm(f, data=df,family = "binomial")
	        n <- length(unique(na.omit(pull(df,j))))
	        for(n in 1:n){
	        out[q,1]=i
	        out[q,2]=names(model[["coefficients"]])[n]
	        out[q,3]=length(model$residuals)#number of obs
	        out[q,4]=round(exp(summary(model)[["coefficients"]][n,1]),2)#pre coef
	        out[q,5]=paste0("(",round(exp(confint.default(model)[n,1]),2),", ",round(exp(confint.default(model)[n,2]),2), ")")
	        out[q,6]=round(summary(model)[["coefficients"]][n,4],3)#p
	        q=q+1
	        }
	        
	        
	        }
	    }
	        
	  }
	}
	out

```
## 3.2 correlation analysis among predictors


## For loop example for regression
```
sy <- apply(model$model[1],2,sd)
sx <- apply(model$model[-1],2,sd)
#lmer model dose not have fitted data
sx <- sd(pull(cog_pre_long,i),na.rm = TRUE)
sy <- sqrt(var(logit(fitted(bc)))+(pi^2/3))
summary(model)[["dims"]][["N"]] # number of observations for lme results
length(model$residuals)#number of obs
```

```
out_var <-c('andr_XXV', 'lib_XXV', 'd_empXXV', 'pub_assistance_XXV', 'socfuncXXV', 'DCC_Abeta40', 'DCC_Abeta42','abeta42_40', "pTau",'DCC_GFAP', 'DCC_Nflight', 'RNAAge')
# out_var <- colnames(df_outcome)[-c(1,4)]
# paste0(paste0("'", out_var, "'"), collapse = ", ")
pre_var <- c("T2_slope","IQ_diff")
out <- data.frame(Outcome=character(), #1
                  Predictor=character(), #2

                  N=double(),#3
                  Coeff=double(), #4
                  CI=character(), #5
                  p=double(), #6
                  
                  stringsAsFactors = FALSE) #23
q=1
for(i in out_var){
  for(j in pre_var){
    if (length(unique(pull(cog_pre_long_scale_wide,i)))>3){
        f <- formula(paste(i,"~",j,"+AGE_25Y_imp"))
        model<-lm(f, data=cog_pre_long_scale_wide)
        out[q,1]=i #outcome
        out[q,2]=j #predictor
        out[q,3]=length(model$residuals) #number of obs
        out[q,4]=round(summary(model)[["coefficients"]][2,1],2)# pre coef
        out[q,5]=paste0("(",round(confint.default(model)[2,1],2),", ",round(confint.default(model)[2,2],2),")") #CI
        out[q,6]=round(summary(model)[["coefficients"]][2,4],2)# pre p
        
        out[q+1,2]="AGE_25Y_imp" #cov
        out[q+1,4]=round(summary(model)[["coefficients"]][3,1],2)# cov coef
        out[q+1,5]=paste0("(",round(confint.default(model)[3,1],2),", ",round(confint.default(model)[3,2],2),")") #CI
        out[q+1,6]=round(summary(model)[["coefficients"]][3,4],2)# cov p
        
        q=q+2 
    }
    else if (length(unique(pull(cog_pre_long_scale_wide,i)))<=3){
        f <- formula(paste(i,"~",j,"+AGE_25Y_imp"))
        model<-glm(f, data=cog_pre_long_scale_wide,family = "binomial")
        out[q,1]=i
        out[q,2]=j
        out[q,3]=length(model$residuals)#number of obs
        out[q,4]=round(exp(summary(model)[["coefficients"]][2,1]),2)#pre coef
        out[q,5]=paste0("(",round(exp(confint.default(model)[2,1]),2),", ",round(exp(confint.default(model)[2,2]),2), ")")
        out[q,6]=round(summary(model)[["coefficients"]][2,4],2)#p
        
        out[q+1,2]="AGE_25Y_imp" #cov
        out[q+1,4]=round(exp(summary(model)[["coefficients"]][3,1]),2)# cov coef
        out[q+1,5]=paste0("(",round(exp(confint.default(model)[3,1]),2),", ",round(exp(confint.default(model)[3,2]),2), ")") 
        out[q+1,6]=round(summary(model)[["coefficients"]][3,4],2)# cov p
        
        q=q+2
    }
        
  }
}
results_three.piece.outcome.bi <- out %>% 
  mutate(
  p=scales::pvalue(p),
  Outcome_label=recode(Outcome,
  andr_XXV='Remission at 25yr',
 	lib_XXV='Recovery at 25yr',
 	d_empXXV='Employment 25yr',
 	pub_assistance_XXV='Receive public assistance at 25yr',
 	socfuncXXV='Interview of social function at 25yr',
 	DCC_Abeta40='Beta-amyloid 40 pg/mL',
 	DCC_Abeta42='Beta-amyloid 42 pg/mL',
 	abeta42_40='Beta-amyloid ratio 42/40',
 	pTau='Phosphorylated tau protein (pTau)',
 	DCC_GFAP='Glial fibrillary acidic protein (GFAP) pg/mL',
 	DCC_Nflight='Neurofilament light protein pg/mL',
 	RNAAge='RNA age')) %>% select(Outcome_label,Predictor,N,Coeff,CI,p)
```

![[Pasted image 20230303130555.png]]

## Function + do.call

```
calculate_OR_p <- function(data, bin_var, fixed_var) {
  x =  pull(data, fixed_var)
  y =  pull(data, bin_var)
  f=formula(paste(fixed_var,"~",bin_var))
  model=glm(f,data = data,family = "binomial")
  OR=round(exp(summary(model)[["coefficients"]][2,1]),2)
  p=scales::pvalue(summary(model)[["coefficients"]][2,4])
  p_original=summary(model)[["coefficients"]][2,4]
  
  result=data.frame(fixed_var, bin_var, OR=OR,p=p,p_original=p_original)
  result=result %>% mutate(complete_obs_pairs=sum(!is.na(x) & !is.na(y)), 
                           complete_obs_ratio=complete_obs_pairs/length(x)) %>%   rename(x=fixed_var, y=bin_var)
  return(result)
}

list=list()
i=1
for (bin_var in vars_binary){result=calculate_OR_p(df_2,bin_var,"mci")
  list[[i]] <- result
  i=i+1}
outcome_2 <- do.call(rbind,list)[57:length(list),] %>% separate(y,c("occupation","time"))%>% mutate(across(c(occupation,time),to_factor))
outcome_2$time <- factor(outcome_2$time, levels = c("Sept", "Oct", "NovDec","JanJun"))
```

![[Pasted image 20230303130406.png]]

# Cheat Sheet
## Labelled
![[Pasted image 20230417165709.png]]
![[Pasted image 20230417165728.png]]
## Stringr
![[Pasted image 20230303125031.png]]
![[Pasted image 20230303125119.png]]
![[Pasted image 20230303125423.png]]
![[Pasted image 20230303125449.png]]

# Quarto
https://themockup.blog/posts/2022-06-13-gtextras-cran/
![[Pasted image 20230922145137.png|300]] ![[Pasted image 20230922145204.png|300]] ![[Pasted image 20230922145243.png|800]] 
![[Pasted image 20230922145321.png|500]] 