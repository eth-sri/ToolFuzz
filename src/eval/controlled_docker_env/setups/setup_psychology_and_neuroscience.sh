#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Research/01_Literature_Review
mkdir -p $root_dir/01_Research/02_Experimental_Design
mkdir -p $root_dir/01_Research/03_Data
mkdir -p $root_dir/02_Analysis/01_Statistical_Analysis
mkdir -p $root_dir/02_Analysis/02_Visualization/figures
mkdir -p $root_dir/02_Analysis/03_Results
mkdir -p $root_dir/03_Publication/01_Drafts
mkdir -p $root_dir/03_Publication/02_Final_Submission
mkdir -p $root_dir/03_Publication/03_Reviews_and_Revisions
mkdir -p $root_dir/04_Teaching/01_Lecture_Materials
mkdir -p $root_dir/04_Teaching/02_Assignments
mkdir -p $root_dir/04_Teaching/03_Exams
mkdir -p $root_dir/05_Grants_and_Funding/01_Proposals
mkdir -p $root_dir/05_Grants_and_Funding/02_Reports
mkdir -p $root_dir/05_Grants_and_Funding/03_Financials

touch $root_dir/01_Research/01_Literature_Review/paper1.pdf
touch $root_dir/01_Research/01_Literature_Review/paper2.pdf
touch $root_dir/01_Research/02_Experimental_Design/design_draft.docx
touch $root_dir/01_Research/02_Experimental_Design/final_design.docx
touch $root_dir/01_Research/03_Data/raw_data.csv
touch $root_dir/01_Research/03_Data/cleaned_data.csv
touch $root_dir/02_Analysis/01_Statistical_Analysis/analysis_script.R
touch $root_dir/02_Analysis/01_Statistical_Analysis/analysis_output.txt
touch $root_dir/02_Analysis/02_Visualization/figures/figure1.png
touch $root_dir/02_Analysis/02_Visualization/figures/figure2.png
touch $root_dir/02_Analysis/02_Visualization/visualization_script.R
touch $root_dir/02_Analysis/03_Results/results_draft.docx
touch $root_dir/02_Analysis/03_Results/final_results.docx
touch $root_dir/03_Publication/01_Drafts/draft1.docx
touch $root_dir/03_Publication/01_Drafts/draft2.docx
touch $root_dir/03_Publication/02_Final_Submission/final_paper.docx
touch $root_dir/03_Publication/02_Final_Submission/supplementary_material.pdf
touch $root_dir/03_Publication/03_Reviews_and_Revisions/reviewer_comments.pdf
touch $root_dir/03_Publication/03_Reviews_and_Revisions/revised_paper.docx
touch $root_dir/04_Teaching/01_Lecture_Materials/lecture1.ppt
touch $root_dir/04_Teaching/01_Lecture_Materials/lecture2.ppt
touch $root_dir/04_Teaching/02_Assignments/assignment1.docx
touch $root_dir/04_Teaching/02_Assignments/assignment2.docx
touch $root_dir/04_Teaching/03_Exams/midterm.docx
touch $root_dir/04_Teaching/03_Exams/final.docx
touch $root_dir/05_Grants_and_Funding/01_Proposals/proposal1.docx
touch $root_dir/05_Grants_and_Funding/01_Proposals/proposal2.docx
touch $root_dir/05_Grants_and_Funding/02_Reports/report1.pdf
touch $root_dir/05_Grants_and_Funding/02_Reports/report2.pdf
touch $root_dir/05_Grants_and_Funding/03_Financials/budget.xlsx
touch $root_dir/05_Grants_and_Funding/03_Financials/expenses.xlsx
