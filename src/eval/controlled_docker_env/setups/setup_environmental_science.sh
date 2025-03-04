#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Research/01_Literature_Review
mkdir -p ${root_dir}/01_Research/02_Data_Collection
mkdir -p ${root_dir}/01_Research/03_Analysis
mkdir -p ${root_dir}/02_Projects/01_Project_A/01_Reports
mkdir -p ${root_dir}/02_Projects/01_Project_A/02_Data
mkdir -p ${root_dir}/02_Projects/01_Project_A/03_Presentations
mkdir -p ${root_dir}/02_Projects/02_Project_B/01_Reports
mkdir -p ${root_dir}/02_Projects/02_Project_B/02_Data
mkdir -p ${root_dir}/02_Projects/02_Project_B/03_Presentations
mkdir -p ${root_dir}/03_Publications/01_Papers
mkdir -p ${root_dir}/03_Publications/02_Conference_Proceedings
mkdir -p ${root_dir}/04_Teaching/01_Lecture_Notes
mkdir -p ${root_dir}/04_Teaching/02_Assignments
mkdir -p ${root_dir}/04_Teaching/03_Exams
mkdir -p ${root_dir}/05_Grants/01_Submitted
mkdir -p ${root_dir}/05_Grants/02_Awarded

touch ${root_dir}/01_Research/01_Literature_Review/paper1.pdf
touch ${root_dir}/01_Research/01_Literature_Review/paper2.pdf
touch ${root_dir}/01_Research/02_Data_Collection/field_data1.csv
touch ${root_dir}/01_Research/02_Data_Collection/lab_data1.csv
touch ${root_dir}/01_Research/03_Analysis/data_analysis1.ipynb
touch ${root_dir}/01_Research/03_Analysis/data_analysis2.ipynb
touch ${root_dir}/02_Projects/01_Project_A/01_Reports/interim_report.docx
touch ${root_dir}/02_Projects/01_Project_A/01_Reports/final_report.docx
touch ${root_dir}/02_Projects/01_Project_A/02_Data/field_data.csv
touch ${root_dir}/02_Projects/01_Project_A/02_Data/lab_data.csv
touch ${root_dir}/02_Projects/01_Project_A/03_Presentations/project_overview.pptx
touch ${root_dir}/02_Projects/01_Project_A/03_Presentations/project_results.pptx
touch ${root_dir}/02_Projects/02_Project_B/01_Reports/interim_report.docx
touch ${root_dir}/02_Projects/02_Project_B/01_Reports/final_report.docx
touch ${root_dir}/02_Projects/02_Project_B/02_Data/field_data.csv
touch ${root_dir}/02_Projects/02_Project_B/02_Data/lab_data.csv
touch ${root_dir}/02_Projects/02_Project_B/03_Presentations/project_overview.pptx
touch ${root_dir}/02_Projects/02_Project_B/03_Presentations/project_results.pptx
touch ${root_dir}/03_Publications/01_Papers/paper1.docx
touch ${root_dir}/03_Publications/01_Papers/paper2.docx
touch ${root_dir}/03_Publications/02_Conference_Proceedings/conference1.pdf
touch ${root_dir}/03_Publications/02_Conference_Proceedings/conference2.pdf
touch ${root_dir}/04_Teaching/01_Lecture_Notes/lecture1.docx
touch ${root_dir}/04_Teaching/01_Lecture_Notes/lecture2.docx
touch ${root_dir}/04_Teaching/02_Assignments/assignment1.docx
touch ${root_dir}/04_Teaching/02_Assignments/assignment2.docx
touch ${root_dir}/04_Teaching/03_Exams/exam1.docx
touch ${root_dir}/04_Teaching/03_Exams/exam2.docx
touch ${root_dir}/05_Grants/01_Submitted/grant1.pdf
touch ${root_dir}/05_Grants/01_Submitted/grant2.pdf
touch ${root_dir}/05_Grants/02_Awarded/grant1.pdf
touch ${root_dir}/05_Grants/02_Awarded/grant2.pdf
