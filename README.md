# Predict-Fuel-Efficiency-with-Machine-Leaning

## Objective
Develop a machine learning model to prdict the miles per gallon (mpg) of a car for a given car features number of cylinders, engine displacement, 
power produced by engine, acceleration

## License

This content is distributed with a [Creative Commons Attribution 4.0 International (CC BY 4.0) license](https://creativecommons.org/licenses/by/4.0/).

You are free to:

- Share, copy and redistribute the material in any medium or format
- Adapt, remix, transform, and build upon the material for any purpose, even commercially.

This license is acceptable for Free Cultural Works.
The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- No additional restrictions: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
  
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
