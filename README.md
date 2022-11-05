# Predict Fuel Efficiency with Machine Leaning

## Objective
Develop a machine learning model to predict the miles per gallon (mpg) of a car for given car features such as the number of cylinders, engine displacement, power produced by the engine, acceleration, weight of a car, and model year as well as deploy the model to Amazon Web Services (AWS).

## Content
* `Data` contains data set used to train, validate, and test algorithm.
* `templates` contains index.html for web page.
* `server` contains model pickle file and server.py developed by using Flask.
* `Fuel_Efficiency_Prediction.ipynb` is a python code for developed model.

  
## Steps Performed

* Exploratory Data Analysis (EDA) 
* Perform hyperparameter tuning using GridSearchCV to find the most suitable model with optimal parameters for the given problem.
* Build a web application using Flask.
* Deploy the web application to an Amazon Web Services (AWS) EC2 instance.


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
