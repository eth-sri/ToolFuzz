#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Data_Collection/01_Raw_Data
mkdir -p $root_dir/01_Data_Collection/02_Cleaned_Data
mkdir -p $root_dir/02_Data_Analysis/01_Exploratory_Data_Analysis
mkdir -p $root_dir/02_Data_Analysis/02_Statistical_Analysis
mkdir -p $root_dir/03_Modeling/01_Preprocessing
mkdir -p $root_dir/03_Modeling/02_Model_Training
mkdir -p $root_dir/03_Modeling/03_Model_Evaluation
mkdir -p $root_dir/04_Visualization/01_Data_Visualization
mkdir -p $root_dir/04_Visualization/02_Model_Visualization
mkdir -p $root_dir/05_Reports/01_Data_Reports
mkdir -p $root_dir/05_Reports/02_Model_Reports
mkdir -p $root_dir/06_Archives/01_Old_Data
mkdir -p $root_dir/06_Archives/02_Old_Models

touch $root_dir/01_Data_Collection/01_Raw_Data/customer_data.csv
touch $root_dir/01_Data_Collection/01_Raw_Data/transaction_data.csv
touch $root_dir/01_Data_Collection/02_Cleaned_Data/cleaned_customer_data.csv
touch $root_dir/01_Data_Collection/02_Cleaned_Data/cleaned_transaction_data.csv
touch $root_dir/02_Data_Analysis/01_Exploratory_Data_Analysis/customer_eda.ipynb
touch $root_dir/02_Data_Analysis/01_Exploratory_Data_Analysis/transaction_eda.ipynb
touch $root_dir/02_Data_Analysis/02_Statistical_Analysis/customer_statistical_analysis.ipynb
touch $root_dir/02_Data_Analysis/02_Statistical_Analysis/transaction_statistical_analysis.ipynb
touch $root_dir/03_Modeling/01_Preprocessing/customer_preprocessing.ipynb
touch $root_dir/03_Modeling/01_Preprocessing/transaction_preprocessing.ipynb
touch $root_dir/03_Modeling/02_Model_Training/customer_model_training.ipynb
touch $root_dir/03_Modeling/02_Model_Training/transaction_model_training.ipynb
touch $root_dir/03_Modeling/03_Model_Evaluation/customer_model_evaluation.ipynb
touch $root_dir/03_Modeling/03_Model_Evaluation/transaction_model_evaluation.ipynb
touch $root_dir/04_Visualization/01_Data_Visualization/customer_data_visualization.ipynb
touch $root_dir/04_Visualization/01_Data_Visualization/transaction_data_visualization.ipynb
touch $root_dir/04_Visualization/02_Model_Visualization/customer_model_visualization.ipynb
touch $root_dir/04_Visualization/02_Model_Visualization/transaction_model_visualization.ipynb
touch $root_dir/05_Reports/01_Data_Reports/customer_data_report.pdf
touch $root_dir/05_Reports/01_Data_Reports/transaction_data_report.pdf
touch $root_dir/05_Reports/02_Model_Reports/customer_model_report.pdf
touch $root_dir/05_Reports/02_Model_Reports/transaction_model_report.pdf
touch $root_dir/06_Archives/01_Old_Data/old_customer_data.csv
touch $root_dir/06_Archives/01_Old_Data/old_transaction_data.csv
touch $root_dir/06_Archives/02_Old_Models/old_customer_model.pkl
touch $root_dir/06_Archives/02_Old_Models/old_transaction_model.pkl