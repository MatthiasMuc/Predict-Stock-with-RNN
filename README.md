# Predict-Stock-with-RNN
Final project work for education: AI Engineer (DigEthics)  
    
**Project Title**: Prediction of stock price for next day with an RNN with the example Microsoft stock  
**Description**:  
This project has been implemented as part of the education "AI Engineer".  
It uses an RNN to provide prediction of "Close" for next business day.  
The project uses several data source that will be used for the prediction.  
Several ways for feature selection are tested.  
Hyperparameter options are discussed, hyperparameter optimization is done with Optuna, an OpenSource framework.  
The project has been implemented in Python as Jupyter notebook, using Visual Studio Code as development environment.  
## Requirements
An enviroment with Python 3.9.6 is required.  
No tests have been done with different Python versions.
## Installation
It is recommended to use a virtual environment for setup.  
To run this project, you need to install the packages defined in requirements.txt:  
```pip install -r requirements.txt``` . 
On Linux machines, the script setup.sh provides a convinient way to install the dependancies in a virtual environment.
## Folder Structure
+ data/stocks contains all needed for different time periods (5/10/15/19 years).
+ notebooks contains the Jupyter notebook with the definition of the model, training and test execution.
+ results contains the result of the execution:
    + results.csv:
      Results of all training runs - one line for each execution
    + MSFT-enhanced.csv:
      All input data used for training and predictions
+ scripts contains the Python script loadStockData to download the data required.
## Configuration of Parameters for Execution
As of now, the configuration for a training and test run is done inside the code.  
In the section "CONFIGURATION PARAMETERS" variables are set that determine the execution of training and test, e.g.:
- Which dataset shall be used (5/10/15/19 years)
- Which method to be used for feature selection
- Shall optimization of hyperparameters with Optuna be done
## Execution
Start the execution og the notebook - that's it!  
Several graphs will be generated inside the notebook.  
Results will be written, as described above.


