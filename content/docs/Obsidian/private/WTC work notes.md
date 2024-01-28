### June 26 Meeting
1. comprehensive prelim: waiting for the committee decision.....
	1. if successfully pass, publish it with Minos.
2. WTC activity analysis: group the activity type. add Moca dot plot at the top of the up-set plot
	1. Now, came up with activity types include
3. Katherine project
	1. the cognition trajectory paper
		1. stable predictor paper
			1. revised analysis, and introduction. 
		2. time-varying predictor (symptoms and anti-psychotic) paper
			1. cross-lag model analysis on-going
				1. difference and stable
				2. slope, noise (error term), 
				3. multilevel model 
				4. a duleoutome model, correlate intercept and slope.
### May 15 Meeting
1. WTC activity analysis
2. Review
	- I am extracting mean of pathology and education
	- worried about categorical variables in pathology or education
	- ![[Pasted image 20230515102358.png]] 
1. Katherine cognition trajectory project
	- dates to meet?
	- trajectory project in WTC?
### May 1 Meeting
1. WTC activity sensitivity analysis with PTSD doesn't change the results.
	1. biomaker first increase and then decrease. different patterns
2. Review, successfully extract 95 effect size from 21 studies.
	- Q1: I have unstandardized beta coefficient as effect size. I also have unstandardized/standardized beta coefficients' standard error. I also need z transformation of the standardized coeff ![[Pasted image 20230406121530.png|150]] . However, the variance of Zr is simply a function of sample size ![[Pasted image 20230406123335.png|100]]. Seems SE from paper results are useless.

3. Katherine's Project: Revised the figure and comments on the draft.
	- collider bias thoughts
		- ![[Pasted image 20230501093329.png|300]] 
		- ![[Pasted image 20230420174803.png|700]] ![[Pasted image 20230420205958.png|500]]
		- ![[Pasted image 20230420210042.png]]
### April 17 Meeting agenda
## WTC activity work
1. Explore inconsistent results from cognition and blood biomarker. 
![[Pasted image 20230417092449.png|600]] ![[Pasted image 20230417092527.png|600]] 
sensitivity analysis to further adjust PTSD. (intro neuro which is untached with NFL which comes from axons)
2. Explore the neuroimaging biomarker
 ![[Pasted image 20230417092750.png|600]]
 collaborate with Minos. Background on the existing evidence, develop theory and hypotheises to test.
 
1. Different combination of the activity?
2. Time period effect? 
	1. Test linear effect: create long format dataset with time and activity variable. 
	2. collapse all activity exposure and other risk variables (risk score across different periods). test significance of categorical time variable
3. Activity and cognitive trajectory?
## Grant Application DDL Oct 20
Letter of reference 3 letters. Candidate? ask for 4.
Letters of Support from Collaborators, Contributors, and Consultants
## Katherine Projects
1. Collidder bias
	- Still discussing the type of bias we found
	- Katherine will present this in a conference and a master student write up the draft
2. Trajectory projects
	- Finished the analysis and figures
	- I will write up the draft
3. Future Projects
	- semi-supervised Machine learning to use unlabeled data in GWAS
	- genomic structural equation modeling
		- where is the dataset. 
		- ML can amplify the false positive
		- ML is not sensitive to small effect size, so we need tons of data.
		- Expected time

### Reading Related paper
https://www.cdc.gov/wtc/pdfs/research/Summary-of-WTC-Health-Program-Research-2021-03282022.pdf
1. Pathway Analysis for Plasma b-Amyloid, Tau  and Neurofilament Light (ATN) in World Trade Center Responders at Midlife[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7229074/pdf/40120_2020_Article_189.pdf]
2. Modeling Exposure to Air Pollution from the WTC Disaster Based on Reports of Perceived Air Pollution
3. World Trade Center Site Exposure Duration Is Associated with Hippocampal and Cerebral White Matter Neuroinflammation
4. Quantitative bias analysis in an asthma study of rescue-recovery workers and volunteers from the 9/11 World Trade Center attacks
5. Paresthesias Among Community Members Exposed to the World Trade Center Disaster: cleaning associated with paresthesias 感觉异常
6. Trajectories of PTSD risk and resilience in World Trade Center responders: an 8-year prospective cohort study
7. Frank's grant: Trauma Exposure and Cognitive Im- pairment: Understanding Polygen- ic Liability and the Causative and Moderating Effects of Exposure, PTSD, and Psychiatric Comorbidity in WTC Responders
8. Dimensional structure and course of post-traumatic stress symptomatology in World Trade Center responders
9. Risk, coping and PTSD symptom trajectories in World Trade Center responders
10. Latent typologies of posttraumatic stress disorder in World Trade Center responders
11. The Burden of Subthreshold Posttraumatic Stress Disorder in World Trade Center Responders in the Second Decade After 9/11
12. Metabolomics of World Trade Center-Lung Injury: a machine learning approach
13. Genomics of Particulate Matter Exposure Associated Cardiopulmonary Disease: A Narrative Review.
14. Validation of Predictive Metabolic Syndrome Biomarkers of World Trade Center Lung Injury: a 16-Year Longitudinal Study.
15. Synergistic Effect of WTC-Particulate Matter and Lysophosphatidic Acid Exposure and the Role of RAGE: In-Vitro and Translational Assessment. International journal of environmental research and public health.
16. Complementary biobank of rodent tissue samples to study the effect of world trade center exposure on cancer development.
17. Development and Validation of a Clinical Frailty Index for the World Trade Center General Responder Cohort.
### Questions

### NHATS PM2.5 data application
1. Data use agreement: stucks on the institution representative signiture?
	-  https://agreements.myresearch.stonybrook.edu/Agreements/sd/Rooms/DisplayPages/LayoutInitial?Container=com.webridge.entity.Entity[OID[0A851D8B711D2440A6552C71BC9DE8D8]]
	- ![[Pasted image 20230320095839.png|1200]]
### PM2.5 WTC activity project
1. include biomarker results in the abstract?
2. which model should be used for skewed biomarker? log transformed?
![[Pasted image 20230320091159.png|1000]]
This is depends on the assumption distribution for example: GFAP is assumed distributed as two parts in Sean's paper
3. Want to use other interested protection var like respiratory change and shower.
	- Based on mediator theory. The PPE either is usefull or not, and thus, no activity related exposure or yes.
	- Check whether respi_change can be useful beyond the ppe_bi, respi_change is significant risk factor when ppe_bi=no (some participants have inconsistent info, all resp related vars are 0, while respi wear frequency 0 represents rare, respir_change frequence 0 represents daily. it must be typo of no for all protection vars). so i decide don't include this into ppe_bi.
4. Collapse 18 groups to fewer
5. In your previous nuronetwork model, you include 68 exposure-activities. except for the 55 activity code, what else? exposure: exhaust.
6. 18 together , control is not doing 18 activities. activity combination pattern.
### Katherine project
1. Fixed the convereg problem by fill missing values and remove random T1 component.
2. Almost done with collider bias project.
![[Pasted image 20230320093448.png]]
![[Pasted image 20230320093513.png]] ![[Pasted image 20230320093545.png]]
3. continuous var are not normal
![[Pasted image 20230320094409.png|400]] ![[Pasted image 20230320094430.png|400]] ![[Pasted image 20230320094607.png|400]] ![[Pasted image 20230320094714.png|400]]
![[Pasted image 20230320094815.png|400]] ![[Pasted image 20230320094901.png|400]] ![[Pasted image 20230320094940.png|400]]

## Archived Meeting Notes

### PM2.5 WTC activity project
1.  Your project on activities only considerd as activity if participants did it for more than 16 hours. How? bothe occupation code and nlp actitivity can have different activity at same period of time. however, there is only one working hours for each time-period. I replicate your method by assigning all period activity to 0 if period hours less than 16.
		Answer:
2.  How do you develop risk score through neural network
		Answer: need outcome prevenlence dementia. memory bayesian, prior, input is activity and hours together. 
3. Binary respir variable only always and others
		Answer: yes. the most risk in mind is probablly not correct.
5. PPE variable, only full body is protective? what's your rationale on PPE variable in your project
		Answer: dust is everywhere. 
7. If people left the WTC site rescue. Instead of assigning missing value, should i recode activity to 0 and the protection the highest level?
		Answer: yes
		normal missing is refusing/stoping to answer
	
1.  Next, I want to do FA and PCA for those exposed. Try to merge activity and timeline. PCA/FA performed on _tetrachoric_ (for binary data) or _polychoric_ (for ordinal data) correlations. What do you think? Last time you said based on the effect size across time and activity. merge activity first. Do you think i can merge activity based on the 4.4 logistic regression results?
2. Trajectory of cognition?
### Meta-Analysis project
1. Standard situation: correlation between two continuous vars. calculate correlation rho and Fisher's Zr transformation
		A:
2. For correlation between interaction of two continuous var and one continuous var. can i assumme the interaction term the simple continuous var. use its mean and sd to do what in the standard situation?
		A: education is not normal distributed. 
3. One study has multiple interaction coefficient for different pathology or cognition test. how to deal with that?
		A: group by outcome to do meta; goup by pathology; For one meta analysis, one study can only choose one result, cannot choose all.
4. rayanne selected 25 included paper. i exclude incidence outcome and cognition decline outcome.
5. 
	-  From last Monday meeting, I learned that beta~D=t/sqrt(n-1), where t=qt(pvalue/2, n-1, lower.tail=FALSE)×(effect sign). However, I came across a weird issue with dummy variable. Bellowing is an example of one effect size. The green color number is the beta calculated based on raw effect size, sd of variables, and mean of variables. For dummy vraibles (pathology and education), I calculated sd=sqrt(npq), mean=p. If I use mean=np, the green number will go even higher. So, I don't know how to impute sd and mean for dummy variables. This 16 is very abnormal (most effect size <1 and the beta 0.144 calculated based on p and n seems normal).![[Pasted image 20230523100427.png]]
	- So i realized that it should be *mean=p and sd=sqrt(pq)*

### Katherine project
1. In predicting the trajectory. the model cannot converge after adding  time varying variable. Only exclude random T1 component works. That time varying var only have values on 6m, 24 m and 20 year. the T1 is -14. Any solution suggested?
		A: T1 is trajectory of IQ no-decline. predictors: symptoms and anti-psychoti treatment.   cannot have random slope at least 3 seperate observations in T1 for every subjects.
3. p-Tau project, she said there is another person doing it at the same time. She want to wait and let us collaborate.

0 Didn’t wear one; 1 Dust/ surgical/ disposable mask; 2 Half-face; 3 Full face; 4 Other; 5 Don’t know

Time of the disease status. cumulative disease status after 911 and before COVID.
looking at symptoms instead of certification.
### Conference
1. https://wcn-neurology.com/?utm_source=Marketo&utm_medium=email&mkt_tok=MzA1LVFVSy01MTkAAAGKVqghI7ovpPADmlU-CLyZCRcrQBRQ383qj-__8-motTNQHmkXnfOLhr8vbLlE4IGv4v4ke_dGufNAwStXWqu7sidEi4eSzMSQqpBRPNEA_HImzrU

### 1. validate activity label with structured data 

supervisory, enclosed, burning. eaq data only. n=12388.

#### Delete NLP missing data. 

```{r read the data}
	eaq_Sept_vali <- eaq_6 %>% filter(!is.na(observation_Sept))
	eaq_Oct_vali <- eaq_6 %>% filter(!is.na(observation_Oct))
	eaq_NovDec_vali <- eaq_6 %>% filter(!is.na(observation_NovDec))
	eaq_JanJun_vali <- eaq_6 %>% filter(!is.na(observation_JanJun))
```

**Not all text data can be converged to the NLP label results**. Success rate of NLP for Sept=76%. Oct=75%, NovDec=74%, JanJun=75%

Bellowing is the example of texts failed to be converted by NLP.

```{r}
eaq_6 %>% filter(is.na(observation_Sept)&!is.na(act1_text_Sept)) %>% select(mrn,act1_text_Sept,observation_Sept)
```

#### Two way table description

Take a close look at how the single period structured supervise is different from the mean supervis

 + If super_base is NA, then stru_super_Sept is NA
 + 49 participants has mean=0, single=1, this is due to round, they have small number, which means only few variables is 1 out of total 12 variables
 + over 8100 participants have 0 on mean, but NA on single, which means, information is gathered in later time period. 
```{r}
	table(round(eaq_Sept_vali$stru_super_mean,digits = 0), eaq_Sept_vali$stru_super_Sept, useNA = "always")
```

The single structured supervise looks good. Lets test structure and NLP supervise on Sept.

 * Conditional on 6723 structured **NA**: 2324 NLP is NA, 6658 NLP is 0, 65 is 1. If activity description does not contain supervise then the value is filled by 0 instead of missing. **NLP did identify 65 (1%) more supervise under missing structured data**.
 * Conditional on 1647 merged **1**: 308 NLP is 1, 1339 NLP is 0. which means **NLP cannot capture most of the positive structured supervise**.
 * Conditional on 785 merged **0**: 772 NLP is 0,  13 is 1. which means **NLP capture most of the negative structured supervise**
```{r}
	table(eaq_Sept_vali$stru_super_Sept, eaq_Sept_vali$Supervision_Sept, useNA = "always")
	table(eaq_Sept_vali$enclosed_Sept, eaq_Sept_vali$Enclosed_Sept, useNA = "always")
	table(eaq_Sept_vali$burn_Sept, eaq_Sept_vali$Steel_Sept, useNA = "always")
	table(eaq_Oct_vali$stru_super_Oct, eaq_Oct_vali$Supervision_Oct, useNA = "always")
	table(eaq_Oct_vali$enclosed_Oct, eaq_Oct_vali$Enclosed_Oct, useNA = "always")
	table(eaq_Oct_vali$burn_Oct, eaq_Oct_vali$Steel_Oct, useNA = "always")
	table(eaq_NovDec_vali$stru_super_NovDec, eaq_NovDec_vali$Supervision_NovDec, useNA = "always")
	table(eaq_NovDec_vali$enclosed_NovDec, eaq_NovDec_vali$Enclosed_NovDec, useNA = "always")
	table(eaq_NovDec_vali$burn_NovDec, eaq_NovDec_vali$Steel_NovDec, useNA = "always")
	table(eaq_JanJun_vali$stru_super_JanJun, eaq_JanJun_vali$Supervision_JanJun, useNA = "always")
	table(eaq_JanJun_vali$enclosed_JanJun, eaq_JanJun_vali$Enclosed_JanJun, useNA = "always")
	table(eaq_JanJun_vali$burn_JanJun, eaq_JanJun_vali$Steel_JanJun, useNA = "always")
```

#### Odds ratio and screening test statistics

![[Odds.jpg|500]] ![[ppv.jpg|500]]

```{r message=FALSE, warning=FALSE}
	out <- data.frame(vars=character(), #1
	                  OR=double(), #2
	                  PPV=double(), #3
	                  Sensitivity=double(), #4
	                  NPV=double(), #5
	                  Specificity=double(),#6
	                  AUC=double(),#7
	                  cor=double(), #8
	                  p=double(), #9
	                  stringsAsFactors = FALSE)
	time <- c("Sept","Oct","NovDec","JanJun")
	# a <- c(paste0("Enclosed_",time),paste0("Steel_",time),paste0("Supervision_",time))
	# b <- c(paste0("enclosed_",time),paste0("burn_",time),paste0("stru_super_",time))
	q=1
	
	#j="Sept"
	for(i in 1:3){
	    for(j in time){
	      dt <- paste0("eaq_",j,"_vali")
	      # stru <- which(colnames(eaq_6)==b[i])
	      # nlp <- which(colnames(eaq_6)==a[i])
	      a <- c(paste0("Enclosed_",j),paste0("Steel_",j),paste0("Supervision_",j))
	      b <- c(paste0("enclosed_",j),paste0("burn_",j),paste0("stru_super_",j))
	      
	      stru <- factor(pull(get(dt), b[i]),levels = c("0","1"))
	      nlp <- factor(pull(get(dt), a[i]),levels = c("0","1"))
	      cof <- confusionMatrix(nlp,reference =stru, positive="1")
	      mat <- table(nlp,stru)
	      out[q,1] <- paste0(a[i]," ",b[i])
	      out[q,2] <- round(oddsratio(mat)$measure[2,1],2)
	      out[q,3] <- round(cof[["byClass"]][3],2)
	      out[q,4] <- round(cof[["byClass"]][1],2)
	      out[q,5] <- round(cof[["byClass"]][4],2)
	      out[q,6] <- round(cof[["byClass"]][2],2)
	      out[q,7] <- round(auc(as.numeric(to_character(stru)),as.numeric(to_character(nlp))),2)
	      out[q,8] <- round(as.numeric(cor.test(as.numeric(to_character(stru)),as.numeric(to_character(nlp)),method = "pearson",use="complete.obs")[4]),2)
	      out[q,9] <- round(as.numeric(cor.test(as.numeric(to_character(stru)),as.numeric(to_character(nlp)),method = "pearson",use="complete.obs")[3]),2)
	  
	      q=q+1
	    }
	}
```
#### Validate with cognition outcomes: Cross Sectional Analysis with activity variables
Choose the latest visidt data and moca is not the second visit. df_2, n=9688
```{r}
df_2<- df %>% filter(!is.na(moca)) %>% group_by(mrn,.add = TRUE) %>% 
  mutate(moca_visit=row_number(),
         moca_visit_max=n()) %>% ungroup() %>% 
  filter(!moca_visit==2) %>% mutate(moca_visit_select=if_else(moca_visit_max==2,1,as.numeric(moca_visit_max))) %>% 
  filter(moca_visit==moca_visit_select) %>% 
  select(mrn,visdt,moca,moca_visit,moca_visit_max,moca_visit_select,everything()) %>% 
  select(-c(moca_visit_max,moca_visit_select))
```

#### Multinomial logistic regression

**Example of Sept Supervision**

1. Structure supervision as predictor
2. NLP supervision as predictor
3. NLP as predictor when structure is missing

Results: structure var contains more positive exposure, thus more power. NLP results are usable supplement.
```{r}
	m_super_stru_sept <- multinom(moca_c ~ stru_super_Sept+age+gender+race+po+hours_Sept+location_Sept+respir_Sept, data = df_2[!is.na(df_2$observation_Sept),])
	
	m_super_nlp_sept <- multinom(moca_c ~ Supervision_Sept+age+gender+race+po+hours_Sept+location_Sept+respir_Sept, data = df_2[!is.na(df_2$observation_Sept),])
	
	m_super_stru_miss_sept <- multinom(moca_c ~ Supervision_Sept+age+gender+race+po+hours_Sept+location_Sept+respir_Sept, data =df_2[is.na(df_2$stru_super_Sept)&!is.na(df_2$observation_Sept),])
	
	table(df_2[!is.na(df_2$observation_Sept),]$stru_super_Sept,df_2[!is.na(df_2$observation_Sept),]$Supervision_Sept,useNA = "always")
	
	tbl_regression(m_super_stru_sept, exp = TRUE)
	tbl_regression(m_super_nlp_sept, exp = TRUE)
	
	table(df_2[is.na(df_2$stru_super_Sept)&!is.na(df_2$observation_Sept),]$moca_c,df_2[is.na(df_2$stru_super_Sept)&!is.na(df_2$observation_Sept),]$Supervision_Sept,useNA = "always")
	tbl_regression(m_super_stru_miss_sept, exp = TRUE)
```

Loop for enclose/burn/supervision in Sept/Oct/NovDec/JanJun
```{r}
	out <- data.frame(y.level=character(), #1
	                  term=character(), #2
	                  estimate=double(), #3
	                  std.error=double(), #4
	                  statistic=double(), #5
	                  p.value=double(),#6
	                  conf.low=double(),#7
	                  conf.high=double(), #8
	                  stringsAsFactors = FALSE)
	time <- c("Sept","Oct","NovDec","JanJun")
	
	for(i in 1:3){
	    for(j in time){
	      a <- c(paste0("Enclosed_",j),paste0("Steel_",j),paste0("Supervision_",j))
	      b <- c(paste0("enclosed_",j),paste0("burn_",j),paste0("stru_super_",j))
	      
	      dt <- df_2 %>% filter(!is.na(get(paste0("observation_",j))))
	      
	      f <- formula(paste0("moca_c~",a[i],"+age+gender+race+po+",paste0("hours_",j),"+",paste0("location_",j),"+",paste0("respir_",j)))
	      f2 <- formula(paste0("moca_c~",b[i],"+age+gender+race+po+",paste0("hours_",j),"+",paste0("location_",j),"+",paste0("respir_",j)))
	      m1 <- multinom(f, data = dt)
	      m2 <- multinom(f2, data = dt)
	      
	      temp <- rbind(tidy(m1, conf.int = TRUE, exponentiate = TRUE)[c(2,13),],tidy(m2, conf.int = TRUE, exponentiate = TRUE)[c(2,13),])
	      
	      out <- rbind(out,temp)
	  
	      
	    }
	}
```

### 2. Descriptive Analysis of NLP results with MCI status
#### 1) Select vars. *df*
MCI<=23, CI<=22, Possible dementia <=17
```{r}
df <- merge  %>% 
  mutate(race=to_factor(race),
         gender=to_factor(gender),
         moca_c=case_when(is.na(moca)~NA_real_,
                             moca>23~0,
                             moca<=23 & moca>=18~1,
                             moca<=17~2),
          moca_c=factor(moca_c,levels =0:2,labels = c("Normal","MCI","Dementia")),
         mci=if_else(moca>23,0,1)
         ) %>% 
  select(mrn,visdt,visit,moca,moca_c,mci,everything())
```

#### 2) Create outcome MCI variable. *df_2*
Delete data without moca, Choose the first first available moca. df_2, n=9688
```{r}
df_2<- df %>% filter(!is.na(moca)) %>% group_by(mrn,.add = TRUE) %>% 
  mutate(moca_visit=row_number()) %>% ungroup() %>% 
  filter(moca_visit==1) %>% 
  select(mrn,visdt,moca,moca_visit,mci,everything()) #%>% 
  #mutate(mci=factor(mci))
```

#### 3) Appoint data type

```
	vars_binary <- c('gender','heart_disease','cholesterol','stroke','hypertension','diabetes','ever_smoke','current_smoke','enclosed_Sept','burn_Sept','concrete_Sept','act1_supervis_Sept','act2_supervis_Sept','act3_supervis_Sept','dust_SeptOct','fumes_SeptOct','smoke_SeptOct','diesel_exhaust_SeptOct','nondiesel_exhaust_SeptOct','partici_Oct','enclosed_Oct','burn_Oct','concrete_Oct','act1_supervis_Oct','act2_supervis_Oct','act3_supervis_Oct','partici_NovDec','enclosed_NovDec','burn_NovDec','concrete_NovDec','act1_supervis_NovDec','act2_supervis_NovDec','act3_supervis_NovDec','dust_NovDec','fumes_NovDec','smoke_NovDec','diesel_exhaust_NovDec','nondiesel_exhaust_NovDec','partici_JanJun','enclosed_JanJun','burn_JanJun','concrete_JanJun','act1_supervis_JanJun','act2_supervis_JanJun','act3_supervis_JanJun','dust_JanJun','fumes_JanJun','smoke_JanJun','diesel_exhaust_JanJun','nondiesel_exhaust_JanJun','po','partici_Sept','stru_super_Sept','stru_super_Oct','stru_super_NovDec','stru_super_JanJun','Cable_Sept','Clean_Sept','Construction_Sept','DebrisRemoval_Sept','Enclosed_Sept','Excavation_Sept','HeavyEquipment_Sept','Inspection_Sept','Morgue_Sept','Repair_Sept','Safety_Sept','Search_Sept','Security_Sept','Steel_Sept','Supervision_Sept','Support_Sept','Transportation_Sept','Utility_Sept','Cable_Oct','Clean_Oct','Construction_Oct','DebrisRemoval_Oct','Enclosed_Oct','Excavation_Oct','HeavyEquipment_Oct','Inspection_Oct','Morgue_Oct','Repair_Oct','Safety_Oct','Search_Oct','Security_Oct','Steel_Oct','Supervision_Oct','Support_Oct','Transportation_Oct','Utility_Oct','Cable_NovDec','Clean_NovDec','Construction_NovDec','DebrisRemoval_NovDec','Enclosed_NovDec','Excavation_NovDec','HeavyEquipment_NovDec','Inspection_NovDec','Morgue_NovDec','Repair_NovDec','Safety_NovDec','Search_NovDec','Security_NovDec','Steel_NovDec','Supervision_NovDec','Support_NovDec','Transportation_NovDec','Utility_NovDec','Cable_JanJun','Clean_JanJun','Construction_JanJun','DebrisRemoval_JanJun','Enclosed_JanJun','Excavation_JanJun','HeavyEquipment_JanJun','Inspection_JanJun','Morgue_JanJun','Repair_JanJun','Safety_JanJun','Search_JanJun','Security_JanJun','Steel_JanJun','Supervision_JanJun','Support_JanJun','Transportation_JanJun','Utility_JanJun')
	#vars_cate <- colnames(merge)[apply(merge,2, function(x) length(unique(x)))<=6]
	vars_cate <- c('marital_stat_code','educ','incom_gp','race','version','atten','visio','lang','anim','drink','location_Sept','respir_Sept','respir_change_Sept','carti_change_Sept','clothes_SeptOct','shower_SeptOct','location_Oct','respir_Oct','respir_change_Oct','carti_change_Oct','location_NovDec','respir_NovDec','respir_change_NovDec','carti_change_NovDec','clothes_NovDec','shower_NovDec','location_JanJun','respir_JanJun','respir_change_JanJun','carti_change_JanJun','clothes_JanJun','shower_JanJun',"currentwork","act1_code_Sept","act2_code_Sept","act3_code_Sept","act1_code_Oct","act2_code_Oct","act3_code_Oct","act1_code_NovDec","act2_code_NovDec","act3_code_NovDec","act1_code_JanJun","act2_code_JanJun","act3_code_JanJun")
	#vars_cate <- vars_cate[!vars_cate %in% vars_binary]
	vars_chara <- c("act1_text_Sept","act1_text_Oct", "act1_text_NovDec","act1_text_JanJun","observation_Sept","observation_Oct","observation_NovDec","observation_JanJun" )
	
	vars_conti <- c('age','ser7','delaytw','orient','accocl','rthru','rspeed','pspeed','lsddet','accidn','sbp','dbp','height','weight','bmi','re_experiencing','avoidance','numbing','hyperarousal','pcl_sum','hours_Sept','hours_Oct','hours_NovDec','hours_JanJun','stru_super_mean')

```

#### 4) Plot for continuous/binary vs mci
bar plot and chi-saure analysis for binary and categor
violin plot and wilcox.test for continuous
```{r}
	library(ggstatsplot)
	
	your_plot <- list()
	for (j in 1:length(vars_conti)) {
	  #画图
	  p <- ggbetweenstats(
	  data  = df_2,
	  x     = mci,
	  y     = !!vars_conti[j])
	  # 把图保存在list里
	  your_plot[[j]] <- p
	}
	##cowplot拼图
	library(cowplot)
	PLOT <- plot_grid(plotlist = your_plot,ncol = 5 ,align = "hv") ##一行放5个图，假设每个小图图定为高4，宽4
	##计算高度
	height <- length(your_plot)/4*4
	##保存图片
	ggsave(PLOT,filename = paste0("Results/","cow_violinplot",".pdf"),
	       limitsize = FALSE,width = 20,height = height)
```

Bar plot for character vars
```{r}
	vars_bar <- c(vars_binary,vars_cate)
	your_plot <- list()
	for (j in 1:length(vars_bar)) {
	  #画图
	  p <- ggbarstats(
	  data  = df_2,
	  x     = mci,
	  y     = !!vars_bar[j])
	  # 把图保存在list里
	  your_plot[[j]] <- p
	}
	##cowplot拼图
	library(cowplot)
	PLOT <- plot_grid(plotlist = your_plot,ncol = 5 ,align = "hv") ##一行放5个图，假设每个小图图定为高4，宽4
	##计算高度
	height <- length(your_plot)/4*4
	##保存图片
	ggsave(PLOT,filename = paste0("Results/","cow_barplot",".pdf"),
       limitsize = FALSE,width = 20,height = height)
```

#### 5) 3D plot for occupation, time, association

Cramer's V
```{r}
	# Function to calculate Cramer's V for a binary variable
	# fixed_var="mci"
	# bin_var="gender"
	# data=df_2
	#rm(fixed_var,bin_var,data,result)
	calculate_cramer_p <- function(data, bin_var, fixed_var) {
	  x =  pull(data, fixed_var)
	  y =  pull(data, bin_var)
	  tb=table(x,y)
	  if(sum(chisq.test(tb)$expected<=5)==0){v <- cramerV(tb)
	    type="uncorrect"
	    }else if(sum(chisq.test(tb)$expected<=5)>0){v <- cramerV(as.character(x), as.character(y), bias.correct = TRUE)
	    type="correct"
	  }
	  
	  result=data.frame(fixed_var, bin_var, assoc=v,type=type)
	  result=result %>% mutate(p = chisq.test(tb)$p.value,
	                           complete_obs_pairs=sum(!is.na(x) & !is.na(y)), 
	                           complete_obs_ratio=complete_obs_pairs/length(x)) %>%   rename(x=fixed_var, y=bin_var)
	  return(result)
	}
	
	list=list()
	i=1
	for (bin_var in vars_binary){result=calculate_cramer_p(df_2,bin_var,"mci")
	  list[[i]] <- result
	  i=i+1}
	outcome <- do.call(rbind,list)
	outcome
```

```{r}
	outcome <- do.call(rbind,list)[57:128,] %>% separate(y,c("occupation","time"))%>% mutate(across(c(occupation,time),to_factor))
	outcome$time <- factor(outcome$time, levels = c("Sept", "Oct", "NovDec","JanJun"))
	#outcome <- outcome %>% mutate(across(c(occupation,time),as.integer))
	outcome
```

```{r}
	library("plotly")
	
	plot_ly(outcome, x = ~occupation, y = ~time, z = ~assoc, 
                 type = 'scatter3d', mode = 'lines', color=~occupation)
```

Odds ratio
```{r}
	# fixed_var="mci"
	# bin_var="Security_Sept"
	# data=df_2
	# rm(fixed_var,bin_var,data,result)
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
	outcome_2 <- do.call(rbind,list)[57:128,] %>% separate(y,c("occupation","time"))%>% mutate(across(c(occupation,time),to_factor))
	outcome_2$time <- factor(outcome_2$time, levels = c("Sept", "Oct", "NovDec","JanJun"))
	#outcome <- outcome %>% mutate(across(c(occupation,time),as.integer))
	outcome_2 <- outcome_2 %>% filter(p_original<=0.05)
	outcome_2
```

```{r}
plot_ly(outcome_2, x = ~occupation, y = ~time, z = ~OR, 
                 type = 'scatter3d', mode = 'lines', color=~occupation)
```
