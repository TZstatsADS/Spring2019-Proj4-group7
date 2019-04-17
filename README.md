�?# Project: OCR (Optical Character Recognition) 

![image](figs/intro.png)

### [Full Project Description](doc/project4_desc.md)

Term: Spring 2019

+ Team #
+ Team members
	+ team member Shen, Yu ys3167@columbia.edu
	+ team member He, Yuting yh3054@columbia.edu
	+ team member Ma, Qiaozhen qm2138@columbia.edu
	+ team member Lin, Nelson nl2600@columbia.edu
	+ team member Zeng, Yiyang yz3403@columbia.edu

+ Paper: D1 + C4

+ Project summary: In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. For error detection, we are assigned the C1, which is the Rule-based techniques. In this paper, there are 8 rules for us to detect the error.For the error correction part. We are assigned the D4, which is "Probability scoring with contextual constraints".  We separate this part into 2 steps.First, we need to correct the error.  According to this paper, there are these 4 ways to correct the errors. For example, we can add a character into a misspelled word when a character of this word is deleted.  Using these methods, we can get some correction candidates for each word. And the candidate with the highest score is assumed to be the correct word.Then we need to calculate the scores. There are 3 methods to estimate these probabilities. The GT method is better than other 2 methods. So we decided to use this method. The score is defined as product of 4 parts. Pr(c) is the probability of a correction candidate existing in the ground truth. To get Pr(c), we need the frequency of a correction candidate existing in the ground truth, r. r* is the frequency by adjusted by GT method. Pr(t|c) is the channel probabilities, which can be calculated from the four confusion matrix using the given formula. To calculate Pr(l|c) and Pr(r|c), we need the frequency of bigram combined with the correction candidate and its left word or right word that can be found in the ground truth. Also we need to adjust the frequency by GT method. After we get the score of all candidates, the correction candidate with highest score is chosen. At last, we evaluate the performance of the algorithm based on recall and precision.


	
**Contribution statement**: 
+ Shen, Yu: Major contributor, Presenter, finsh and debug correction part with He, Yuting and Ma, Qiaozhen, write README.md.
+ He, Yuting: Major contributor, read and understand the paper, finsh and debug correction part with Shen, Yu and Ma, Qiaozhen.
+ Ma, Qiaozhen: Major contributor, read and understand the paper, finsh and debug correction part with Shen, Yu and He, Yuting.
+ Zeng, Yiyang: read and understand the paper, finsh and debug correction part with other team members.
+ Lin, Nelson: read and understood paper. Wrote part3 - D1 paper implementation. debugged with correction with other team members

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
