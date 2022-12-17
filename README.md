# EEG-ImpulseBuying
This research investigates the effects of a robot recommendation system on people's tendency to make impulsive purchases online in an e-commerce context. We collected participants' brain activity when they made rational and unplanned purchases and studied participants' real-time cognitive perceptions of the different conditions of the experiment (like the marketing strategies and robot recommendations).

The initial results show that marketing strategies and robot recommendations can cause impulsive buying behavior and lead to different cognitive responses.

### Data Collection
---
We use EMOTIV EPOC X to collect participant’s brainwave. Among the 14 channels, we focus on the eight electrodes (AF3, F7, AF4, F8, F3, FC5, FC6, and F4) placed in the frontal cortex to capture cognitive-related brain activities.

### Data Analysis Pipeline
---
The preprocessing procedures includes: 
1. FFT band powers calculation -- EmotivPRO
2. Baseline normalization -- src/eeg_norm.py
3. 5-second epoch extraction -- src/ana_*.py

We retrieved the EEG signals of planned buying to serve as the baseline and calculated the power variations resulted from the impulsive buying behavior under different situations. 

We compared participants' brain activities between buying:
- Unplanned item (Impulsive Buying Behavior) vs. Reject unplanned item (No Impusive Buying Behavior) -- src/ana_ibnib.py
- Discount vs. Limited Edition/Quantity -- src/ana_disedi.py 
- Regretted vs. Unregretted -- src/ana_regret.py 
- Related add-on vs. Unrelated add-on -- src/ana_relurel.py 
- Before robot recommendation vs. After robot recommendation -- src/ana_barobot.py 
