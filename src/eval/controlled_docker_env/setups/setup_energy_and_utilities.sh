#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/archive/projects
mkdir -p ${root_dir}/archive/reports
mkdir -p ${root_dir}/archive/templates
touch ${root_dir}/archive/projects/archived_project_A_2021.zip
touch ${root_dir}/archive/projects/archived_project_B_2021.zip
touch ${root_dir}/archive/reports/archived_annual_report_2021.pdf
touch ${root_dir}/archive/reports/archived_monthly_report_2021.pdf
touch ${root_dir}/archive/templates/old_energy_audit_template.docx
touch ${root_dir}/archive/templates/old_utility_plan_template.xlsx

mkdir -p ${root_dir}/projects/project_A/2023/energy_audit
mkdir -p ${root_dir}/projects/project_A/2023/utility_plan
mkdir -p ${root_dir}/projects/project_A/2023/compliance/Q1
mkdir -p ${root_dir}/projects/project_A/2023/compliance/Q2
mkdir -p ${root_dir}/projects/project_A/2023/compliance/Q3
mkdir -p ${root_dir}/projects/project_A/2023/compliance/Q4
mkdir -p ${root_dir}/projects/project_A/2024/energy_audit
mkdir -p ${root_dir}/projects/project_A/2024/utility_plan
mkdir -p ${root_dir}/projects/project_A/2024/compliance/Q1
mkdir -p ${root_dir}/projects/project_A/2024/compliance/Q2
mkdir -p ${root_dir}/projects/project_A/2024/compliance/Q3
mkdir -p ${root_dir}/projects/project_A/2024/compliance/Q4

mkdir -p ${root_dir}/projects/project_B/2023/energy_audit
mkdir -p ${root_dir}/projects/project_B/2023/utility_plan
mkdir -p ${root_dir}/projects/project_B/2023/compliance/Q1
mkdir -p ${root_dir}/projects/project_B/2023/compliance/Q2
mkdir -p ${root_dir}/projects/project_B/2023/compliance/Q3
mkdir -p ${root_dir}/projects/project_B/2023/compliance/Q4
mkdir -p ${root_dir}/projects/project_B/2024/energy_audit
mkdir -p ${root_dir}/projects/project_B/2024/utility_plan
mkdir -p ${root_dir}/projects/project_B/2024/compliance/Q1
mkdir -p ${root_dir}/projects/project_B/2024/compliance/Q2
mkdir -p ${root_dir}/projects/project_B/2024/compliance/Q3
mkdir -p ${root_dir}/projects/project_B/2024/compliance/Q4

mkdir -p ${root_dir}/reports/annual_reports
mkdir -p ${root_dir}/reports/monthly_reports
mkdir -p ${root_dir}/reports/quarterly_reports
touch ${root_dir}/reports/annual_reports/annual_report_2023.pdf
touch ${root_dir}/reports/monthly_reports/february_2023.pdf
touch ${root_dir}/reports/monthly_reports/january_2023.pdf
touch ${root_dir}/reports/quarterly_reports/Q1_report_2023.pdf
touch ${root_dir}/reports/quarterly_reports/Q2_report_2023.pdf

mkdir -p ${root_dir}/templates/energy_audit_templates
mkdir -p ${root_dir}/templates/utility_plan_templates
mkdir -p ${root_dir}/templates/compliance_templates
touch ${root_dir}/templates/energy_audit_templates/advanced_energy_audit_template.docx
touch ${root_dir}/templates/energy_audit_templates/basic_energy_audit_template.docx
touch ${root_dir}/templates/utility_plan_templates/monthly_utility_plan_template.xlsx
touch ${root_dir}/templates/utility_plan_templates/weekly_utility_plan_template.xlsx
touch ${root_dir}/templates/compliance_templates/corporate_compliance_template.docx
touch ${root_dir}/templates/compliance_templates/standard_compliance_template.docx