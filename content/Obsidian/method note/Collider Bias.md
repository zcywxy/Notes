**Bias** is a systematic, *nonrandom error* in the estimation of a treatment effect or the effect of an exposure or risk factor. Bias can *lead to invalid results* in observational studies and randomized clinical trials (RCTs). Bias is often broadly categorized into 3 groups: confounding, information (or measurement) bias, and selection bias. 
- Selection bias is a general term describing bias that occurs when study participants are identified in a manner such that they are no longer representative of the target population. This can occur when an exposure and outcome each influence a common third variable-*the collider*-and that variable has been controlled for in the statistical analysis of the study data. Collider bias threatens the internal validity of a study and the accurate estimation of causal relationships.
A **collider** is most simply defined as a variable that is **influenced by two other variables**, for example when a risk factor and an outcome both affect the **likelihood of being sampled**
![[Pasted image 20230221114651.png]]
This collision creates a spurious or artificial association between the 2 other variables (ie, A and B). Consider an extreme example in which the outcome (labeled as *C* in panel A) can *only be caused by either of* the 2 unrelated variables (ie, *A or B*) but *not* the combination of *A and B*. If the analysis is *restricted to* patients who had the outcome of *C*, patients either have A or B, but not both, and a *spurious (negative) association* is created between *A and B*. This might occur, for example, in an RCT that requires each patient to have 1 of 2 risk factors, but not both, because of the intent to enroll a medium-risk population (eg, because there already is a therapy for higher-risk patients with both risk factors). Then, if the enrolled population was used to examine the relationship between the 2 risk factors, a spurious (negative) association between them would be found.
![[Pasted image 20230420173815.png|300]]
A study by Valls-Pedret et al[6](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003r6) illustrates an example of potential collider bias in an RCT. In this secondary analysis of data from an *RCT* that *compared 2 Mediterranean diets* and *a control diet* in 447 participants at *high cardiovascular risk*, cognitive function was improved with both dietary interventions. However, *loss to follow-up* was *higher* in the *control* group (33%) as compared with the Mediterranean diet groups (16% and 23%). Differential loss to follow-up can introduce collider bias because the analysis is *restricted* to patients who are *not lost to follow-up* (ie, only those with follow-up data are included in the analysis) (panel B in the [Figure](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003f1)). If participants assigned to one of the Mediterranean diets were less likely to be lost to follow-up than those in the control group (which is supported by the trial) (arrow 1 in panel B) and participants with poor cognitive function were independently more likely to be lost to follow-up (arrow 2 in panel B), restricting the analysis to those not lost to follow-up could result in a spurious or noncausal association between diet and cognitive function. In contrast to what the trial found, these associations would result in bias toward finding a benefit in the control group. As such, collider bias does not explain the results of the trial but illustrates how collider bias can occur in an RCT (eg, through loss to follow-up).
![[Pasted image 20230420174040.png|300]]

Addressing collider bias is best done during the design of a study, for example by minimizing loss to follow-up or avoiding restricting the study population based on characteristics likely to be affected by both the exposure and outcome of interest. DAGs may be helpful in exploring potential causality and identifying collider bias.[5](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003r5),[7](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003r7) It is important to identify and distinguish collider bias from other types of bias and consider how the choice of study design and statistical analysis may introduce, increase, or reduce bias. For example, the choice of statistical method can account for confounding, while at the same time introduce collider bias.

In their study of *patients* with *COVID*-19, Fosbøl et al found *no increased mortality* among patients using *ACEIs* or ARBs.[4](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003r4)However, it has been hypothesized that *ACEI* or ARB use could result in *increased susceptibility to COVID*-19. If this is true, collider bias is a concern in this study because the analysis was restricted to patients with confirmed COVID-19 (panel C in the [Figure](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003f1)). If ACEI or ARB use increases the risk of COVID-19 (arrow 1 in panel C) and other unrelated risk factors cause COVID-19 (arrow 2 in panel C), restricting the analysis to patients with COVID-19 will create a spurious negative association between ACEI or ARB use and these risk factors. If these risk factors are also related to mortality (arrow 3 in panel C), a spurious association between ACEI or ARB use and mortality could appear. In other words, by requiring the participants to have COVID-19 for inclusion in the analysis (ie, controlling on that characteristic), a spurious negative association could be generated between the use of ACEIs or ARBs and risk factors for COVID-19. Since those same risk factors are associated with mortality, this, in turn, creates a spurious protective association between ACEI or ARB use and mortality.
![[Pasted image 20230420174309.png|300]]

Fosbøl et al addressed the potential for collider bias arising from limiting the study to patients with COVID-19 by *showing that ACEI* or ARB use was *not associated* with susceptibility to confirmed *COVID*-19.[4](https://jamanetwork.com/journals/jama/fullarticle/2790247#jgm220003r4) Thus, arrow 1 in panel C can be removed, and there is no longer a collision of causal relationships affecting COVID-19 illness.

To make reliable inference about the causes of infection and disease severity, it is important that the biases which induce spurious associations in observational data are understood and assessed. Bias due to confounding remains well-understood and attempts to address it are typically made (bar rare exceptions e.g. ref. [11](https://www.nature.com/articles/s41467-020-19478-2#ref-CR11 "Goren, A. et al. A preliminary observation: Male pattern hair loss among hospitalized COVID-19 patients in Spain—a potential clue to the role of androgens in COVID-19 severity. J. Cosmet. Dermatol 19, 1545–1547 (2020).")). But the problem of collider bias (sometimes referred to as selection bias, sampling bias, ascertainment bias, Berkson’s paradox) has major implications for many published studies of COVID-19 and is seldom addressed.

it is possible to distort the association between two variables that do not directly influence the collider. If the factors that influence sample selection themselves influence the variables of interest, the relationship between these variables of interest can become distorted. This is sometimes referred to as M-bias due to the shape of the Direct Acyclic Graph
![[Pasted image 20230221114949.png]]
Among hospitalized patients, the relationships between any variables that relate to hospitalization will be distorted compared to among the general population. The magnitude of this distortion can be large, inducing associations that do not exist in the general population or attenuating, inflating or reversing the sign of existing associations[16](https://www.nature.com/articles/s41467-020-19478-2#ref-CR16 "Munafò, M. R. et al. Collider scope: when selection bias can substantially influence observed associations. Int J. Epidemiol. 47, 226–35. (2018).").

Collider bias can arise when researchers *restrict analyses on a collider variable*. Impact both *external validity* (not reflect patterns in the population of interest) and *internal validity* (associations induced by collider bias are properties of the sample, rather than the individuals that comprise it, so the associations estimated using the sample will not be a reliable indication of the individual level causal effects).

It is this second characteristic which distinguishes collider bias within the more general concept of **selection bias**. Selection bias can occur when there are effect modifiers (confounder) that are distributed differently in the sample than in the population, thus causing effects to differ between the two. However, while this limits the generalizability of causal effects on the population, those **effects are valid within the sample**


The term “risk factor” has been used synonymously for both causal factors and predictors in the literature[79](https://www.nature.com/articles/s41467-020-19478-2#ref-CR79 "Shader, R. I. Risk factors versus causes. J. Clin. Psychopharmacol. 39, 293–294 (2019)."),[80](https://www.nature.com/articles/s41467-020-19478-2#ref-CR80 "Shmueli, G. To explain or to predict? Stat. Sci. 25, 289–310 (2010)."). An aetiological study seeks to identify causes of the outcome of interest (“causal factors”), whereas a predictive study aims to develop scores that predict the outcome from a range of variables (“predictors”) which need not be causal. While the term ‘risk factor’ can be ambiguous and refer to either a hypothesised causal determinant or a predictor of the disease, we use it throughout this paper for the sake of brevity as causal inference and prediction analyses both share a vulnerability to the detrimental impacts of collider bias in the COVID-19 context—where typically the selected samples are being used to develop models relevant to the general population. But for clarity we outline below how collider bias differentially impacts causal inference and prediction.

*Risk factors* measured in observational studies may associate with outcomes of interest (e.g. hospitalised with COVID-19), for many reasons. For example, the factor may affect the outcome (*true causal interpretation*), statistical evidence of association may be purely due to chance, the outcome may affect the factor (*reverse causation*), there may be a third factor that causes both the exposure and the outcome (*confounding*), or the exposure and outcome (or causes of the exposure and/or outcome) may influence the likelihood of being selected into the study (*collider bias*).

Aetiological studies are in principle only concerned with the causal effect and aim to avoid all forms of bias. By contrast, some forms of bias such as confounding or reverse causation can actually improve the performance of a prediction study. As long as the causal structure by which the study sample is drawn from the target population is the same as in the population in which predictions will be made, it can be of benefit to leverage these distinct association mechanisms to improve prediction accuracy[81](https://www.nature.com/articles/s41467-020-19478-2#ref-CR81 "Myers, J. A. et al. Effects of adjusting for instrumental variables on bias and precision of effect estimates. Am. J. Epidemiol. 174, 1213–22. (2011)."),[82](https://www.nature.com/articles/s41467-020-19478-2#ref-CR82 "Pearl, J. Invited commentary: understanding bias amplification. Am. J. Epidemiol. 174, 1223–1227 (2011).").

Similarly, under certain circumstances, *collider bias* can *improve prediction performance* if the *training sample* and the *sample to be predicted* have *the same patterns* of sample selection. For example, if the factors causing having a test for COVID-19 are the same/similar across the UK, a predictive model for the result being positive that was developed in London will perform well in the North East of England if those samples are both non-randomly selected in the same way. However, collider bias is a problem for the generalisability of both causal inference and prediction in the target population when the training sample is non-randomly selected, because it induces artefactual associations that are idiosyncratic to that dataset. If the intention is to predict COVID-19 status, rather than COVID-19 status conditional on being tested, the prediction will underperform.
![[Pasted image 20230221121127.png]]

![[Pasted image 20230221122040.png|500]]![[Pasted image 20230328225531.png|300]]![[Pasted image 20230328231634.png|300]] ![[Pasted image 20230420212803.png]] 

**If polygenic risk scores are to be used clinically**, it will be very important to build prediction models on samples that are selected in the same way that prediction samples will be selected.

Q: PRS are populatioinal based. and clinically is symptom based. How can they be the same. Do u mean add controls into each prediction sample?

![[Pasted image 20230420174803.png|700]] ![[Pasted image 20230420205958.png|500]] ![[Pasted image 20230420210042.png]] 