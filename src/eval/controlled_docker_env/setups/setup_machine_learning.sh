#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Data/01_Raw
mkdir -p $root_dir/01_Data/02_Processed
mkdir -p $root_dir/01_Data/03_External
mkdir -p $root_dir/02_Code/01_Preprocessing
mkdir -p $root_dir/02_Code/02_Models
mkdir -p $root_dir/02_Code/03_Evaluation
mkdir -p $root_dir/02_Code/04_Visualization
mkdir -p $root_dir/03_Results/01_Model_Outputs
mkdir -p $root_dir/03_Results/02_Evaluation_Reports
mkdir -p $root_dir/03_Results/03_Visualizations
mkdir -p $root_dir/04_Documentation
mkdir -p $root_dir/05_Archive

touch $root_dir/01_Data/01_Raw/dataset1.csv
touch $root_dir/01_Data/01_Raw/dataset2.csv
touch $root_dir/01_Data/02_Processed/dataset1_processed.csv
touch $root_dir/01_Data/02_Processed/dataset2_processed.csv
touch $root_dir/01_Data/03_External/external_data1.csv
touch $root_dir/01_Data/03_External/external_data2.csv
touch $root_dir/02_Code/01_Preprocessing/data_cleaning.py
touch $root_dir/02_Code/01_Preprocessing/data_transformation.py
touch $root_dir/02_Code/02_Models/model1.py
touch $root_dir/02_Code/02_Models/model2.py
touch $root_dir/02_Code/02_Models/model3.py
touch $root_dir/02_Code/03_Evaluation/model_evaluation.py
touch $root_dir/02_Code/03_Evaluation/performance_metrics.py
touch $root_dir/02_Code/04_Visualization/data_visualization.py
touch $root_dir/02_Code/04_Visualization/model_visualization.py
touch $root_dir/03_Results/01_Model_Outputs/model1_output.csv
touch $root_dir/03_Results/01_Model_Outputs/model2_output.csv
touch $root_dir/03_Results/01_Model_Outputs/model3_output.csv
touch $root_dir/03_Results/02_Evaluation_Reports/model1_evaluation.pdf
touch $root_dir/03_Results/02_Evaluation_Reports/model2_evaluation.pdf
touch $root_dir/03_Results/02_Evaluation_Reports/model3_evaluation.pdf
touch $root_dir/03_Results/03_Visualizations/data_visualization.png
touch $root_dir/03_Results/03_Visualizations/model_visualization.png
touch $root_dir/04_Documentation/01_Project_Proposal.pdf
touch $root_dir/04_Documentation/02_Methodology.pdf
touch $root_dir/04_Documentation/03_Final_Report.pdf
touch $root_dir/04_Documentation/04_Presentation.pptx
touch $root_dir/05_Archive/old_code.zip
touch $root_dir/05_Archive/old_data.zip