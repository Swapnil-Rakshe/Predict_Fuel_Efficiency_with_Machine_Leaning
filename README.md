# Predict-Fuel-Efficiency-with-Machine-Leaning

## Objective
Develop a machine learning model to prdict the miles per gallon (mpg) of a car for a given car features such as number of cylinders, engine displacement, 
power produced by engine, acceleration, weight of car, and model year and deploy the model to Amazon Web Services (AWS).

## Content
`Data` contains data set used to train, validate, and test algorithm

  
## Getting started
    
The python algorithm is derived from oxford java step counter algorithm. Please read the references available on site 'https://oxford-step-counter.github.io/'

Step detection algorithm consist of five steps:

* Pre-processing stage
* Filtering stage
* Scoring stage
* Detection stage
* Post-processing stage
    
For each stage a separate function is defined. As stated in the reference file the optimal set of parameters are used for the step detection.
    
The notebook `OxfordPythonStepCounter.ipynb` is present in the folder `python-step-counter`. It contains all the description about how to execute this python file.
    
To run this notebook in colab, simply open the file and click on the **Open In Colab** Badge (<a href="https://colab.research.google.com/github/kristofvl/DataSet/blob/master/python-step-counter/OxfordPythonStepCounter.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> ) present at the top in the notebook.

**Sample Results**:

<pre>
../validation/user1_armband_1506423438471.csv 
steps detected by current algorithm : 315 
 from data in current csv files ...  
	 steps detected by GTD: 335 
	 steps detected by algorithm 316
     
File name : user1_armband_1506423438471.csv 
steps detected by current algorithm : 315 
 from data in current csv files ... 
	 steps detected by GTD: 335 
	 steps detected by algorithm 316

File name : user1_backpocket_1506422470497.csv 
steps detected by current algorithm : 504
 from data in current csv files ... 
	 steps detected by GTD: 343
	 steps detected by algorithm 501
</pre>
