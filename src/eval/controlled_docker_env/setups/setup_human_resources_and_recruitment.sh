#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Recruitment/01_Job_Postings
mkdir -p $root_dir/01_Recruitment/02_Applications
mkdir -p $root_dir/01_Recruitment/03_Interviews
mkdir -p $root_dir/01_Recruitment/04_Offer_Letters
mkdir -p $root_dir/02_Human_Resources/01_Employee_Records
mkdir -p $root_dir/02_Human_Resources/02_Payroll
mkdir -p $root_dir/02_Human_Resources/03_Benefits
mkdir -p $root_dir/02_Human_Resources/04_Training_and_Development
mkdir -p $root_dir/03_Policies_and_Procedures
mkdir -p $root_dir/04_Reports
mkdir -p $root_dir/05_Templates

touch $root_dir/01_Recruitment/01_Job_Postings/job_posting_001.docx
touch $root_dir/01_Recruitment/01_Job_Postings/job_posting_002.docx
touch $root_dir/01_Recruitment/02_Applications/applicant_A_resume.pdf
touch $root_dir/01_Recruitment/02_Applications/applicant_B_resume.pdf
touch $root_dir/01_Recruitment/03_Interviews/interview_notes_applicant_A.docx
touch $root_dir/01_Recruitment/03_Interviews/interview_notes_applicant_B.docx
touch $root_dir/01_Recruitment/04_Offer_Letters/offer_letter_applicant_A.pdf
touch $root_dir/01_Recruitment/04_Offer_Letters/offer_letter_applicant_B.pdf
touch $root_dir/02_Human_Resources/01_Employee_Records/employee_A_record.pdf
touch $root_dir/02_Human_Resources/01_Employee_Records/employee_B_record.pdf
touch $root_dir/02_Human_Resources/02_Payroll/payroll_2023.xlsx
touch $root_dir/02_Human_Resources/02_Payroll/payroll_2024.xlsx
touch $root_dir/02_Human_Resources/03_Benefits/benefits_overview.pdf
touch $root_dir/02_Human_Resources/03_Benefits/benefits_enrollment_form.docx
touch $root_dir/02_Human_Resources/04_Training_and_Development/training_program_overview.pdf
touch $root_dir/02_Human_Resources/04_Training_and_Development/development_plan_template.docx
touch $root_dir/03_Policies_and_Procedures/company_policies.pdf
touch $root_dir/03_Policies_and_Procedures/HR_procedures.pdf
touch $root_dir/04_Reports/annual_HR_report_2023.pdf
touch $root_dir/04_Reports/quarterly_HR_report_Q1_2024.pdf
touch $root_dir/05_Templates/job_posting_template.docx
touch $root_dir/05_Templates/interview_notes_template.docx
touch $root_dir/05_Templates/offer_letter_template.docx
touch $root_dir/05_Templates/employee_record_template.docx
