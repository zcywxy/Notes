## Introduction
- **Polygenic Risk Scores (PRS)**: PRS are genetic markers used to determine an individual’s predisposition to specific phenotypes, influenced by the sum of certain genetic variants (single nucleotide polymorphisms, or SNPs) they carry.
- **Applications of PRS**: PRS have shown potential in predicting risks for various diseases, including inflammatory bowel disease, coronary artery disease, breast cancer, and type II diabetes. Notably, women of European descent with high PRS had a 3-fold increase in breast cancer risk.
- **Genotyping Advancements**: The development of more efficient genotyping techniques reduces barriers to the use of PRS, offering potential for enhanced prediction, diagnosis, and treatment of psychiatric illnesses.

**PRS in Psychiatric Disorders**:
- **Challenges**: PRS's application in psychiatric disorders faces challenges, especially due to inconsistent associations between psychiatric PRS and clinical outcomes.
- **Bipolar Disorder PRS (BP PRS) Studies**:
  - *Supporting Evidence*: BP PRS was sensitive to bipolar disorder diagnosis, was associated with a higher number of hospitalizations for bipolar disorder, and showed various associations with positive formal thought disorder, mania, and reduced odds of depression among psychotic disorder patients.
  - *Contradictory Evidence*: Several studies did not find significant associations between BP PRS and multiple clinical outcomes, such as general intelligence, age of onset, response to lithium, suicide attempts, etc. In some instances, BP PRS was even inversely associated with certain outcomes, like rapid cycling.
  
- **Population and Case-Control Studies**:
  - *Positive Findings*: BP PRS has shown significant associations with intelligence, psychosis risk factors, migration from rural to urban environments, and increased physical activity in population samples.
  - *Inconsistent Associations*: Despite these promising findings, BP PRS's association with clinical characteristics of bipolar disorder has been inconsistent, potentially due to the low prevalence of these phenotypes in the general population.
  - *Difference in Cases vs. Case-Control*: Studies have demonstrated that BP PRS is more strongly linked to bipolar disorder-related phenotypes in population and case-control samples than in cases alone. This difference was exemplified in two case-control studies.

**Proposed Hypothesis**:
The research team hypothesizes that analyzing genetic risk within cases only, especially strictly within hospitalized cases, might alter the distribution of genetic risk, leading to skewed associations between genetic risk and clinical outcomes. They plan to test this hypothesis by analyzing BP PRS's association with various bipolar disorder-related phenotypes in a cohort of first-admission psychosis patients and matched, never-psychotic controls.

## Method
**Study Source and Cohort:**
- Data was sourced from the Suffolk Health County Mental Health Project, a study of a cohort of individuals with first-admission psychosis admitted between 1989 and 1995 in Suffolk County, New York.
- 628 participants were initially involved, with 261 never-psychotic, demographically matched controls added during the 20-year follow-up. DNA was collected at the 20-year mark, and outcomes were assessed at the 25-year follow-up.

**Inclusion Criteria for Participants:**
- First admission for psychosis in the past 6 months.
- English comprehension, residence in Suffolk County, IQ > 70, and aged between 15 and 60.

**Measurement Criteria and Outcomes:**
1. **Remission:** Based on Andreasen's definition, assessing symptoms like hallucinations, delusions, and more with scales of SAPS and SANS.
	- **Symptom Severity:** Evaluated using SAPS and SANS with derived sub-scales, and the ratings were informed by multiple sources.
2. **Recovery:** Defined by Liberman, it uses eight ratings from the *Brief Psychiatric Rating Scale* (BPRS) for symptoms and the *Quality of Life Scale* (QLS) for psychosocial functioning.
	- **Role Functioning:** Assessed using a specific rating from the QLS.
	- **Social Function:** Composite score derived from three QLS items.
3. **Social Performance:** Evaluated through the University of California San Diego Performance-Based Skill Assessment (UPSA), a *behavioral test*.
4. **Residential & Economic Independence:** Determined by one's reliance on others or agencies for residence or financial support.
5. **Global Assessment of Functioning (GAF):** Consensus rating by psychiatrists using *varied data sources* from the past year.

**Polygenic Risk Score:**
- DNA extraction was from peripheral lymphocytes using the Illumina PsychArray-8 platform.
- Multiple quality control procedures ensured high-quality genetic data.
- PRS calculations were based on multiple studies, using tools like PRS-ice, Plink 1.9, and ADMIXTURE.

**Statistical Analysis:**
- Demographic differences were evaluated using the Student t-test (continuous variables) and the chi-square test (categorical variables).
- The association between 25-year outcomes and genetic risk used *Poisson and negative binomial regression for count outcomes, and logistic regression for binary outcomes*.

Note: All evaluations were univariate regressions.

### Replication
**Sample:** 
- The replication data is sourced from the PsyCourse study, carried out in Germany and Austria. 
- The cohort comprises 1308 individuals diagnosed with disorders like schizophrenia, bipolar disorder, or depression, along with 456 control individuals from Göttingen and Munich.
	- **Background:** PsyCourse is a multicenter study conducted across multiple clinical sites in Germany and Austria, involving 18 clinical centers. Two centers also collect data from nonclinical individuals. The study adheres to ethical guidelines from the Declaration of Helsinki and has received approvals from respective ethics committees.
	- **Study Duration:** Participants are assessed at four intervals of 6 months each, labeled as T1 to T4. There are additional visits for clinical participants if they are re-admitted during the study period. Missing follow-up visits does not lead to exclusion.
	- **Data Collection:** During each visit, venous blood samples are collected for extracting DNA, RNA, plasma, and serum. A comprehensive set of phenotype data is also obtained, encompassing symptom dimensions, cognitive functions, and self-reports.
	- **Clinical Participants:** The study focuses on adult patients (18 years and above) with specific ICD-10 life-time diagnoses like SZ, SZA, BD, and more. The diagnosis is reassessed using the Structured Clinical Interview for DSM-IV during the first study visit. Participants are divided into groups based on their symptoms: predominantly psychotic symptoms and predominantly affective symptoms. Proficiency in the German language is a requirement for participation.
	- **Nonclinical Participants:** Individuals from specific areas are contacted and invited to participate. They undergo a similar protocol as the clinical participants. Their medical history, especially pertaining to affective or psychotic illnesses, is assessed.
	- **Informed Consent:** A comprehensive informed consent is obtained from participants, which allows for the storage and use of their data and biomaterials for research without specifying exact research objectives. Participants can also decide if they want to be informed about incidental findings from the study. Collaborations with other research disciplines are allowed using pseudonymized data. Participants also allow access to their past medical records.
	- **Opt-Out:** Participants can choose to opt-out, leading to either disposal of their biomaterial and data or irreversible anonymization of their data.
	- **Data Protection:** To protect the sensitive data, various measures like pseudonymization are in place. Four IT components, including identity and administrative tools, and databases for phenotype and biomaterials have been established for data management.
	- **Interviewers:** Interviewers are given written instructions and undergo thorough training in administering the phenotyping battery. Regular trainings are held for all investigators.
**Phenotyping:**
- Participants underwent assessments four times at 6-month intervals over 18 months post-enrollment.
- At each evaluation, the current level of psychiatric treatment was recorded: '1' indicating inpatient care and '0' otherwise. This data was summed across all evaluations, forming an ordinal variable that represents the number of times a participant received inpatient treatment.
- Among the cases, 49.6% had at least one psychiatric hospitalization, and 6% had two or more.

**Genotyping:**
- Genetic data was sourced from venous blood and analyzed using the Illumina Infinium PsychArray, capturing info on about 590,000 genetic markers.
- After standard quality control, genotypes were imputed using the 1000 Genomes Phase 3 reference panel via tools SHAPEIT2 and IMPUTE2. Any variant with an imputation quality less than 0.8 was excluded.
- Principal components analysis was conducted using Plink 1.9. Individuals who deviated considerably in their genetic ancestry (greater than three standard deviations on any of the first three principal components) were excluded.
- This left a final sample size of 1594 (1190 cases and 404 controls). Polygenic Risk Scores (PRS) for schizophrenia and bipolar disorder were estimated using PRSice and based on recent GWAS data from the Psychiatric Genomics Consortium. PRS data was adjusted for the first 10 principal components of population stratification before further analyses.

**Statistical Analysis:**
- The study examined the influence of sample stratification on the relationship between schizophrenia and bipolar disorder PRS. This was done by estimating Pearson correlations within the full sample, within cases, and among those who had one or two psychiatric hospitalizations.

## Results
1. **Demographics and Clinical Characteristics (Table 2):**
   - Cases were on average two years older than controls.
   - There were no significant differences between cases and controls regarding gender, race, or socioeconomic status.
   - Cases exhibited more severe symptoms and poorer functioning than controls.

2. **25-Year Outcomes and PRS Association (Table 3):**
   - **For the Full Cohort:**
     - Schizophrenia PRS (SZ PRS) was associated with poorer outcomes, including:
       - Lower odds of recovery and remission.
       - Reduced chances of attaining residential and economic independence at the 25-year mark.
       - It predicted worse functioning and more severe symptoms across all domains.
     - Bipolar PRS (BP PRS) had a limited range of associations, indicating:
       - Lower odds of remission and economic independence.
       - Poorer overall functioning and increased severity of psychotic symptoms.
   - **For Cases Only:**
     - SZ PRS still predicted a lower probability of remission, but all other associations were no longer significant.
     - BP PRS associations not only shifted closer to a neutral effect (towards one) but also changed directions. Among cases, it was associated with higher odds of economic independence and better performance-based function.

3. **Sensitivity Analysis Results (Table 4):**
   - When analyzing the effect of bipolar versus schizophrenia PRS on 25-year outcomes, the observed patterns were akin to those of BP PRS. Higher genetic risk for bipolar, in contrast to schizophrenia, correlated with better 25-year outcomes among cases.

4. **Conceptual Replication:**
   - Sample stratification's influence on the correlation between SZ and BP PRS was examined using data from the PsyCourse study. 
   - Within the entire sample, there was a strong correlation between SZ and BP PRS (r=0.497, p<0.001).
   - This correlation slightly reduced when considering only cases (r=0.483, p<0.001) and decreased further among those with at least one psychiatric hospitalization (r=0.479, p<0.001). It was weakest among participants with two or more hospitalizations over the study's 18 months (r=0.357, p<0.01).

## Discussion
1. **Main Results:** The research found that associations in case-control samples align with expectations. However, within cases only, the results differ, particularly for the bipolar PRS (BP PRS) where associations are opposite. These findings point out the effects of selection bias on genetic predictions.
2. **Collider Bias Explanation:** Collider bias arises when two predictors influence the chance of being selected into the sample, potentially creating false associations between unrelated factors. The recruitment of psychiatric patients during their inpatient hospitalization could lead to such bias, as both the PRS and the severity of symptoms can influence the likelihood of hospitalization.
	1. **Deep Dive into Collider Bias:** This bias can lead to misguided research findings, possibly influencing incorrect treatment methods or interventions. Recent studies highlighted that patients diagnosed with schizophrenia (SCZ) and bipolar disorder (BP) have distinct associations with cognitive functioning based on their PRS. 
	2. **Clinical Consequences of Collider Bias:** In inpatient settings, collider bias might enhance responsiveness to early interventions or influence medication dosage. However, it can also skew perceived treatment responses or predictions of patient outcomes. In outpatient settings, the bias can distort diagnostic accuracy, potentially affecting treatment choices and risk assessments. To ensure accuracy in clinical scenarios, it's vital to consider collider bias and use balanced cohorts in studies.
3. **Research Implications:** For more accurate understandings of genetic risk and phenotype associations, researchers should employ samples that span the full spectrum of genetic risk. If samples are only of high genetic risk, associations can be misleading.
4. **Clinical Implications:** Genetic predictions' accuracy may vary based on the setting. In an inpatient context, a higher genetic risk for bipolar disorder might be linked with better outcomes. In contrast, in outpatient scenarios, it might forecast worse results. Predictions should rely on studies with comparable patient cohorts.
5. **Limitations:** The study doesn't have longitudinal data for controls, just a 20-year follow-up. It also had a small sample size and a primary focus on European ancestry individuals, which can limit the generalizability of the results.


We lack of the Differences PRS between BP and SZ
Table 1 for genotyped vs un-genotyped cases. Should be cases include and cases exclude
How to understand the table

Replicate Table: Control comes from general population, could potentially include the cases. Not matched.
case and control table 1: add PRS description.

Time: 10 minutes limit.
population, all SZ are hospitalized, large proportion of BP are hospitalized. Sever symptoms. 
Externalized symptoms. Cohort in imates.

Take way: Overall genetic risk, select sever symptoms population and select less harmful PRS 

recovery:
distribution of PRS against of outcomes in case, controls, and mix. density function.

descriptive plot for PRS and outcomes box plot stratified by population
scatter plot for continuous. 

