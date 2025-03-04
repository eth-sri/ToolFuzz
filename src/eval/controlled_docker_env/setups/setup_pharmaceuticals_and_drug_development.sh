#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Research/01_Literature_Review
mkdir -p $root_dir/01_Research/02_Patents
mkdir -p $root_dir/01_Research/03_Research_Proposal
mkdir -p $root_dir/02_Drug_Development/01_Preclinical_Trials
mkdir -p $root_dir/02_Drug_Development/02_Clinical_Trials
mkdir -p $root_dir/02_Drug_Development/03_FDA_Approval
mkdir -p $root_dir/03_Manufacturing/01_Production_Schedule
mkdir -p $root_dir/03_Manufacturing/02_Quality_Control
mkdir -p $root_dir/03_Manufacturing/03_Packaging
mkdir -p $root_dir/04_Marketing/01_Market_Research
mkdir -p $root_dir/04_Marketing/02_Marketing_Strategy
mkdir -p $root_dir/04_Marketing/03_Advertising
mkdir -p $root_dir/05_Sales/01_Sales_Reports
mkdir -p $root_dir/05_Sales/02_Customer_Feedback
mkdir -p $root_dir/05_Sales/03_Returns_and_Refunds

touch $root_dir/01_Research/01_Literature_Review/related_article_1.pdf
touch $root_dir/01_Research/01_Literature_Review/related_article_2.pdf
touch $root_dir/01_Research/02_Patents/patent_1.pdf
touch $root_dir/01_Research/02_Patents/patent_2.pdf
touch $root_dir/01_Research/03_Research_Proposal/research_proposal.docx
touch $root_dir/02_Drug_Development/01_Preclinical_Trials/animal_study_report_1.pdf
touch $root_dir/02_Drug_Development/01_Preclinical_Trials/lab_results_1.xlsx
touch $root_dir/02_Drug_Development/02_Clinical_Trials/phase1_report.pdf
touch $root_dir/02_Drug_Development/02_Clinical_Trials/phase2_report.pdf
touch $root_dir/02_Drug_Development/02_Clinical_Trials/phase3_report.pdf
touch $root_dir/02_Drug_Development/03_FDA_Approval/fda_submission.docx
touch $root_dir/02_Drug_Development/03_FDA_Approval/fda_approval_letter.pdf
touch $root_dir/03_Manufacturing/01_Production_Schedule/production_schedule.xlsx
touch $root_dir/03_Manufacturing/02_Quality_Control/qc_report_1.pdf
touch $root_dir/03_Manufacturing/02_Quality_Control/qc_report_2.pdf
touch $root_dir/03_Manufacturing/03_Packaging/packaging_design.ai
touch $root_dir/03_Manufacturing/03_Packaging/packaging_test_report.pdf
touch $root_dir/04_Marketing/01_Market_Research/competitor_analysis.pdf
touch $root_dir/04_Marketing/01_Market_Research/target_market_report.pdf
touch $root_dir/04_Marketing/02_Marketing_Strategy/marketing_plan.docx
touch $root_dir/04_Marketing/02_Marketing_Strategy/marketing_budget.xlsx
touch $root_dir/04_Marketing/03_Advertising/ad_script.docx
touch $root_dir/04_Marketing/03_Advertising/ad_storyboard.pdf
touch $root_dir/05_Sales/01_Sales_Reports/sales_report_q1.pdf
touch $root_dir/05_Sales/01_Sales_Reports/sales_report_q2.pdf
touch $root_dir/05_Sales/01_Sales_Reports/sales_report_q3.pdf
touch $root_dir/05_Sales/01_Sales_Reports/sales_report_q4.pdf
touch $root_dir/05_Sales/02_Customer_Feedback/customer_survey_results.xlsx
touch $root_dir/05_Sales/02_Customer_Feedback/customer_complaints.docx
touch $root_dir/05_Sales/03_Returns_and_Refunds/return_policy.docx
touch $root_dir/05_Sales/03_Returns_and_Refunds/refund_report.pdf