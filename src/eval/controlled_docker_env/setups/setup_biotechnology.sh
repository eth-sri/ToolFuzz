#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Research/01_Literature_Review
mkdir -p ${root_dir}/01_Research/02_Experimental_Design
mkdir -p ${root_dir}/01_Research/03_Data
mkdir -p ${root_dir}/02_Experiments/01_Setup
mkdir -p ${root_dir}/02_Experiments/02_Results
mkdir -p ${root_dir}/02_Experiments/03_Analysis
mkdir -p ${root_dir}/03_Patents/01_Applications
mkdir -p ${root_dir}/03_Patents/02_Granted
mkdir -p ${root_dir}/04_Publications/01_Drafts
mkdir -p ${root_dir}/04_Publications/02_Published
mkdir -p ${root_dir}/05_Presentations/01_Conferences
mkdir -p ${root_dir}/05_Presentations/02_Seminars
mkdir -p ${root_dir}/06_Grants/01_Applications
mkdir -p ${root_dir}/06_Grants/02_Awarded

touch ${root_dir}/01_Research/01_Literature_Review/paper1.pdf
touch ${root_dir}/01_Research/01_Literature_Review/paper2.pdf
touch ${root_dir}/01_Research/02_Experimental_Design/experiment1.docx
touch ${root_dir}/01_Research/02_Experimental_Design/experiment2.docx
touch ${root_dir}/01_Research/03_Data/data1.csv
touch ${root_dir}/01_Research/03_Data/data2.csv
touch ${root_dir}/02_Experiments/01_Setup/setup1.docx
touch ${root_dir}/02_Experiments/01_Setup/setup2.docx
touch ${root_dir}/02_Experiments/02_Results/result1.csv
touch ${root_dir}/02_Experiments/02_Results/result2.csv
touch ${root_dir}/02_Experiments/03_Analysis/analysis1.xlsx
touch ${root_dir}/02_Experiments/03_Analysis/analysis2.xlsx
touch ${root_dir}/03_Patents/01_Applications/application1.pdf
touch ${root_dir}/03_Patents/01_Applications/application2.pdf
touch ${root_dir}/03_Patents/02_Granted/patent1.pdf
touch ${root_dir}/03_Patents/02_Granted/patent2.pdf
touch ${root_dir}/04_Publications/01_Drafts/draft1.docx
touch ${root_dir}/04_Publications/01_Drafts/draft2.docx
touch ${root_dir}/04_Publications/02_Published/paper1.pdf
touch ${root_dir}/04_Publications/02_Published/paper2.pdf
touch ${root_dir}/05_Presentations/01_Conferences/conference1.pptx
touch ${root_dir}/05_Presentations/01_Conferences/conference2.pptx
touch ${root_dir}/05_Presentations/02_Seminars/seminar1.pptx
touch ${root_dir}/05_Presentations/02_Seminars/seminar2.pptx
touch ${root_dir}/06_Grants/01_Applications/application1.pdf
touch ${root_dir}/06_Grants/01_Applications/application2.pdf
touch ${root_dir}/06_Grants/02_Awarded/grant1.pdf
touch ${root_dir}/06_Grants/02_Awarded/grant2.pdf

echo "Setup complete"