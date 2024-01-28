# Resilience in the World Trade Center Cohort
[link](file:///Users/yuan/Dropbox/papers/NLP/FINAL%20Syeda%20Mahwish%20practicum%20proposal.docx.pdf)
- Gap: Few studies exploring resilience in the 9/11 cohort
	- Resilience **Definition**
		1.  ability to bounce back” (Garmezy, 1971; Ledesma, 2014; Luthans, 2002; 1971; Rutter, 1979)
		2.  dynamic system to adapt successfully (Masten, 2014; Southwick et al., 2014)
		3.  “a *stable trajectory* of healthy functioning after a highly adverse event" ( Bonanno's (2004) and Southwick et al. (2014) )
			-  highlight the long-term recovery
	- In reality, resilience exists on a **continuum** and may be present in **different** degrees across multiple **domains** of life

Aim:  it is vital to utilize the existing data that has already been collected in order to date back closer to the events of 9/11(Pietrzak & Southwick, 2011).

- Method
	1. dataset annotation process, generate a set of prototypical *phrases* (e.g. "I am optimistic", "I am hopeful", "The future looks good for me"); resource: WTC Clinical interviews, Reddit
	2. using a language model such as *RoBERTA* (Robustly Optimized BERT Pretraining Approach) to match the *semantic*
	3. transform these phrases and prototypes into a *weighted lexicon*, each word is assigned a weight or *score* that reflects *resilience*
	5. utilizing RoBERTa to *evaluate* the presence of language resembling. *validation*
	6. apply this lexicon to *participant*’s language data to analyze each construct created into a *single resiliency score*

# Predicting PTSD symptom trajectories with AI-based language analyses of interviews
[link](file:///Users/yuan/Dropbox/papers/NLP/Predicting%20PTSD%20symptom%20trajectories%20with%20AI_based%20language%20analyses%20of%20interviews.pdf)
- **Existed**
	- Artificial Intelligence (*AI*)-based techniques have begun to show promise for quickly and accurately assessing *mental health* from human *behavioral data*, such as *language use patterns*. 
	- past work has shown that AI-based language techniques can distinguish *Twitter* users that have publicly disclosed a diagnosis of the PTSD from random selections of users 
	- AI-based language can detect a much wider range of responses (like an interview) compared to traditional score
- **Gap**
	- For *PTSD* in particular, although studies have *yet to validate* models *in* a *clinical* setting
- **Goal**
	- AI-based mental health assessments from language to *predict* future *PTSD* symptoms *trajectories* in a *clinical* setting
	- First, train model
	- then, compared to other variable like gender, age, occupation
	- last, quantify the language-based indicators to inform personalized therapeutic approaches
- **Method**
	- Total N=124, N=*113* responders in cross-sectional (not newly enrolled) and N=75 for trajectory. 
	- each interview last *1h*. It covered the responders’ memory of 9/11 attacks and disaster relief efforts, their work activities at the site, experiences and sensations over the days and weeks that followed, and how the WTC disaster ultimately impacted their lives since. Interviews were completed between *2010 and 2018*.
	- Audio transcribed into *text* using TranscribeMe.
	- Text convert to into "*features*" and then *input into*
		1. Four *psychological traits*: anxiety, depression, neuroticism, extraversion
			- features such as *words, phrases, and topics*, and map them to psychological constructs.  We focused on existing **pre-trained models** for constructs
				- These models were trained on large and diverse populations (approximately sample sizes of N=65000 for neuroticism and extraversion and N = 29 000 for degrees of depression and anxiousness).
		1. Three *lexicon* assessments: first-person singular pronouns, plural pronouns, use of articles
		2. Two *meta* variables: counts of words (frequency), and lengths of words

DLATK: Dictionary Learning and Text Analysis Toolkit. It is a software toolkit designed for analyzing text data, particularly in psychology research.
- Provides tools for cleaning and preprocessing text data, like stemming, spelling correction, removing stopwords, etc.
- Implements methods for analyzing text at different levels:
    - Word/phrase frequencies and correlations
    - Topic modeling using latent Dirichlet allocation (LDA)
	    - The Dirichlet distribution is used as a prior for the topic distributions and word distributions in LDA's Bayesian modeling framework.
    - Sentiment analysis
    - Linguistic inquiry word count (LIWC)
- Includes methods for linking text features to external variables, e.g. regressing topics against outcomes.
- Can handle data from multiple sources like speeches, social media, interviews.
- Outputs results in easy to use spreadsheet format.
- Builds on machine learning libraries like Scikit-Learn and NLTK.
- Open source Python library originally developed at University of Pennsylvania.

So in summary, DLATK facilitates text mining and analysis pipelines by providing a toolkit tailored for psychology/social science researchers with methods like topics modeling and LIWC built-in. It aims to make text analysis more accessible.
# Quantifying Healthy Aging in Older Veterans Using Computational Audio Analysis
[link](file:///Users/yuan/Dropbox/papers/NLP/Quantifying%20Healthy%20Aging%20in%20Older%20Veterans%20Using%20Computational%20Audio%20Analysis.pdf)
![[Pasted image 20230916140937.png|400]]
1. **Objective**: The primary aim is to determine predictors of age and years of life remaining using audio clips.
2. **Preprocessing**: Audio clips undergo a preprocessing step to ensure they're suitable for further analysis.
3. **VGGVox Embeddings**:
   - VGGVox is used to transform the audio clips. 
   - VGGVox is based on the VGG-M CNN model and excels in classifying or identifying speakers.
   - It has superior performance when compared to other models like i-vector.
   - It's pretrained on VoxCeleb datasets, which have short audio clips from YouTube interview videos.
4. **Audio Data to Spectrogram Transformation**:
   - The raw audio data, with a sampling rate of 16,000, is converted into spectrograms. A spectrogram visually represents the spectrum of frequencies of a signal as it varies with time.
   - These spectrograms are created with a frame length of 0.025 and are then normalized using mean and variance normalization.
5. **Embeddings**:
   - The VGGVox model uses these spectrograms to derive low-dimensional representations (embeddings) of the audio files. 
   - These embeddings are 1,024-dimensional feature vectors that convert 5 spectrograms to a more compact space. 
   - These embeddings capture the cosine similarity measurements that correspond to speaker similarity.
6. **Embedding Creation for Analysis**:
   - VGGVox embeddings are created for each of the remaining 10-second audio clips. This duration is similar to the average length of audio clips in the VoxCeleb datasets.
7. **Machine Learning Prediction**:
   - The derived VGGVox embeddings are used as features and fed into machine learning models to predict age.
# Machine Learning and Deep Learning in Natural Language Processing
[link](file:///Users/yuan/Dropbox/Books/Machine%20Learning%20and%20Deep%20Learning%20in%20Natural%20Language%20Processing.pdf)
Deep Learning (DL) has slowly become an essential tool for Natural Language Processing (NLP).
Automatic Speech Recognition (ASR), speaker identification, conditioned Text-to-Speech (TTS) synthesis or speech emotion recognition.

They allow to exploit techniques like **transfer learning and fine-tuning**, where the features computed by a DL neural network model trained on a large generic dataset are re-used on a specific problem with a smaller dataset, generally resulting in improved performances.

Traditionally, the speech features adopted for NLP are divided into two groups: **prosodic 韵律学的 and acoustic 声音的, 原声的 features** [11,12]. The former group includes features used to describe peculiarities of speech, such as: Pitch, Intensity, Harmonicity, Jitter, Shimmer, Speech Rate, Short-Term Energy, Short-Term Entropy, etc. The latter group includes features used to describe the acoustic properties of speech, such as: Spectrogram (magnitude or power), Mel- spectrogram, Mel Frequency Cepstral Coefficients (MFCC), Spectrogram statistics (centroid, spread, flux, rolloff, entropy), Chromagram, etc.

The internal representations learned by these models are particularly informative and can be directly transferred or easily adapted to many new problems. The most popular models in this sense are SoundNet [13], VGGish [14], and Wav2Vec [3, 15].

- two pre-processing steps: denoising and segmentation. 
	1. The denoising module takes care of removing (as much as possible) additional signals in the input audio clip which overlap with the voice to analyze. State-of-the-art solutions use DL models trained on many hours of data and can achieve impressive results. 
	2. Segmentation consists of the splitting of the audio clip in presence of longer pauses, which generally mark the end of an utterance. 

use SoundNet [13], VGGish [14], and Wav2Vec to produce the feature map and then use feature map as input, use CNN to build a classifier.
![[Pasted image 20230917163932.png]]
# Automated detection of mild cognitive impairment and dementia from voice recordings A natural language processing approach
[link](file:///Users/yuan/Dropbox/papers/NLP/Automated%20detection%20of%20mild%20cognitive%20impairment%20and%20dementia%20from%20voice%20recordings%20A%20natural%20language%20processing%20approach.pdf)
Transfer learning is a widely used technique in NLP applications that addresses the problem of training a classifier when a large, complete training data set is not available.35

The NP tests include sub-tests that assess naming and language, visuoperceptual skills, premorbid intelligence, abstract reasoning, attention, verbal memory (logical memory immediate and delayed recall), learning (paired-associate memory immediate and delayed recall), and visual memory (visual reproductions immediate and delayed recall).

Transfer NP test recording to text, and separate the participant and interviewer. separate the subtest.
- Encode by the Universal Sentence Encoder **USE**, a neural network based on the transformer architecture and attention mechanism, it takes an input text with an arbitrary length.
	- Although the USE can process text data of any length, feeding the entire transcript into the USE would result in a poor down- stream classification performance, mainly because USE generates a *fixed 512-dimensional vector for any input*.
		1. *Random Sampling (RS) method*: We constructed a paragraph by randomly selecting 25 P sentences from each interview, given that each transcript contains at least 25 P sentences. We repeated the random sampling for each interview until 30 paragraphs were collected. These 30 paragraphs are different from each other even if a transcript contains only 25 P sentences due to random order of the sentences. Then, the USE takes each paragraph as input and generates a 512-dimensional sentence embedding.
		2. *Sub-test Sampling (STS) method*: The STS method exploits the sub- test labels of the P sentences. This method groups the P sentences of the same sub-test together, compiling eight paragraphs from each interview (one for each sub-test). By passing these paragraphs to the USE, eight 512-dimensional vectors are generated for each interview. If any sub-test is missing throughout the interview, we fill the corresponding vector with zeroes.

proceeded with the classification task. machine-learning techniques such as the **Multilayer Perceptron (MLP)** and logistic regression.
1. feature selection of the embedding vectors, to improve downstream classification performance
	-  logistic regression–based recursive feature elimination (e.g., as in ref.39 ) on the training data to remove the weakest feature until the embedding vector is of size 50, resulting in reducing the 512-dimensional vectors to 50-dimensional vectors.
2. generating cognitive scores from the resulting lower dimensional vectors,
	- based on different subset strategy. RS method has 30 scores each participants. STS has 8 sub-test score.
		- For STS method, can generate the rank of importance of the sub-test
3. training a classifier by a combination of the cognitive scores and demographic information to arrive at the final prediction.
	1. In addition to these NLP-based methods, we developed an ensemble model that combines multiple other models in the prediction process. For instance, one can train a *logistic regression model* that *combines* the *RS and/or STS methods* with different variables such as the *demographics* or *APOE status*. The entire prediction procedure was implemented using the python deep-learning Keras library with a Tensorflow backend.

# AI-Based Speech Assessment of Cognitive Impairment Disorders
[link](file:///Users/yuan/Dropbox/papers/NLP/AI-Based%20Speech%20Assessment%20of%20Cognitive%20Impairment%20Disorders.pdf)

# Transformer-based deep neural network language models for Alzheimer’s disease risk assessment from targeted speech 
[link](file:///Users/yuan/Dropbox/papers/NLP/Transformer-based%20deep%20neural%20network%20language%20models%20for%20Alzheimer’s%20disease%20risk%20assessment%20from%20targeted%20speech.pdf)
![[Pasted image 20230916142152.png|400]]
# My proposal aim:
1. extract interview audio quality features by VGGVox pre-trained model
2. extract interview text features by  pre-trained model : RoBERTA, XLNET, XLM, 
3. using interview audio quality features + interview text features + activity exposure as input. Use different classifiers (NN, CNN, Bi-LSTM, LR) and Voter (Identity, Majority, Bi-LSTM) to predict cognitive health as well as trajectory.

## Data:
[Trauma and relationship strain Oral histories with World Trade Center disaster responders](file:///Users/yuan/Dropbox/papers/NLP/Trauma%20and%20relationship%20strain%20Oral%20histories%20with%20World%20Trade%20Center%20disaster%20responders.pdf)
The interviewer asked open-ended questions to elicit the respondent’s oral history. We used a semi-structured interview guide to encourage responders to shape their own narratives around various domains of inquiry, including what brought them to the disaster site on 9/11/01, their specific *roles in the recovery work*, the *impact* of the recovery work on *themselves* and their *families*, and the effects of the 9/1l/01 attacks on their *communities* and the *country*.

