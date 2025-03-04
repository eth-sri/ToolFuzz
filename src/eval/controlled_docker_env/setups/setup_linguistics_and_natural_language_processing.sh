#!/bin/bash
root_dir=$1

mkdir -p $root_dir/01_Research/01_Papers
mkdir -p $root_dir/01_Research/02_Books
mkdir -p $root_dir/01_Research/03_Articles
mkdir -p $root_dir/02_Projects/01_Project_A/01_Data
mkdir -p $root_dir/02_Projects/01_Project_A/02_Scripts
mkdir -p $root_dir/02_Projects/01_Project_A/03_Results
mkdir -p $root_dir/02_Projects/02_Project_B/01_Data
mkdir -p $root_dir/02_Projects/02_Project_B/02_Scripts
mkdir -p $root_dir/02_Projects/02_Project_B/03_Results
mkdir -p $root_dir/03_Teaching/01_Lectures
mkdir -p $root_dir/03_Teaching/02_Assignments
mkdir -p $root_dir/03_Teaching/03_Exams
mkdir -p $root_dir/04_Publications/01_Conference_Papers
mkdir -p $root_dir/04_Publications/02_Journal_Articles
mkdir -p $root_dir/05_Resources/01_Tools
mkdir -p $root_dir/05_Resources/02_Datasets
mkdir -p $root_dir/05_Resources/03_Tutorials

touch $root_dir/01_Research/01_Papers/paper1.pdf
touch $root_dir/01_Research/01_Papers/paper2.pdf
touch $root_dir/01_Research/02_Books/book1.pdf
touch $root_dir/01_Research/02_Books/book2.pdf
touch $root_dir/01_Research/03_Articles/article1.pdf
touch $root_dir/01_Research/03_Articles/article2.pdf
touch $root_dir/02_Projects/01_Project_A/01_Data/raw_data.csv
touch $root_dir/02_Projects/01_Project_A/01_Data/processed_data.csv
touch $root_dir/02_Projects/01_Project_A/02_Scripts/data_processing.py
touch $root_dir/02_Projects/01_Project_A/02_Scripts/model_training.py
touch $root_dir/02_Projects/01_Project_A/03_Results/model_output.txt
touch $root_dir/02_Projects/01_Project_A/03_Results/visualization.png
touch $root_dir/02_Projects/02_Project_B/01_Data/raw_data.csv
touch $root_dir/02_Projects/02_Project_B/01_Data/processed_data.csv
touch $root_dir/02_Projects/02_Project_B/02_Scripts/data_processing.py
touch $root_dir/02_Projects/02_Project_B/02_Scripts/model_training.py
touch $root_dir/02_Projects/02_Project_B/03_Results/model_output.txt
touch $root_dir/02_Projects/02_Project_B/03_Results/visualization.png
touch $root_dir/03_Teaching/01_Lectures/lecture1.ppt
touch $root_dir/03_Teaching/01_Lectures/lecture2.ppt
touch $root_dir/03_Teaching/02_Assignments/assignment1.docx
touch $root_dir/03_Teaching/02_Assignments/assignment2.docx
touch $root_dir/03_Teaching/03_Exams/exam1.docx
touch $root_dir/03_Teaching/03_Exams/exam2.docx
touch $root_dir/04_Publications/01_Conference_Papers/conference_paper1.pdf
touch $root_dir/04_Publications/01_Conference_Papers/conference_paper2.pdf
touch $root_dir/04_Publications/02_Journal_Articles/journal_article1.pdf
touch $root_dir/04_Publications/02_Journal_Articles/journal_article2.pdf
touch $root_dir/05_Resources/01_Tools/tool1.txt
touch $root_dir/05_Resources/01_Tools/tool2.txt
touch $root_dir/05_Resources/02_Datasets/dataset1.csv
touch $root_dir/05_Resources/02_Datasets/dataset2.csv
touch $root_dir/05_Resources/03_Tutorials/tutorial1.pdf
touch $root_dir/05_Resources/03_Tutorials/tutorial2.pdf
