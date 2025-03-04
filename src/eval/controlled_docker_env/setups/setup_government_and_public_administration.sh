#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/archive/legislation
mkdir -p ${root_dir}/archive/reports
mkdir -p ${root_dir}/archive/templates
mkdir -p ${root_dir}/departments/department_A/2023/budget
mkdir -p ${root_dir}/departments/department_A/2023/legislation
mkdir -p ${root_dir}/departments/department_A/2023/policies
mkdir -p ${root_dir}/departments/department_A/2023/reports
mkdir -p ${root_dir}/departments/department_A/2024/budget
mkdir -p ${root_dir}/departments/department_A/2024/legislation
mkdir -p ${root_dir}/departments/department_A/2024/policies
mkdir -p ${root_dir}/departments/department_A/2024/reports
mkdir -p ${root_dir}/departments/department_B/2023/budget
mkdir -p ${root_dir}/departments/department_B/2023/legislation
mkdir -p ${root_dir}/departments/department_B/2023/policies
mkdir -p ${root_dir}/departments/department_B/2023/reports
mkdir -p ${root_dir}/departments/department_B/2024/budget
mkdir -p ${root_dir}/departments/department_B/2024/legislation
mkdir -p ${root_dir}/departments/department_B/2024/policies
mkdir -p ${root_dir}/departments/department_B/2024/reports
mkdir -p ${root_dir}/reports/annual_reports
mkdir -p ${root_dir}/reports/monthly_reports
mkdir -p ${root_dir}/reports/quarterly_reports
mkdir -p ${root_dir}/templates/budget_templates
mkdir -p ${root_dir}/templates/legislation_templates
mkdir -p ${root_dir}/templates/policy_templates
mkdir -p ${root_dir}/templates/report_templates

touch ${root_dir}/archive/legislation/archived_legislation_2021.zip
touch ${root_dir}/archive/legislation/archived_legislation_2022.zip
touch ${root_dir}/archive/reports/archived_annual_report_2021.pdf
touch ${root_dir}/archive/reports/archived_monthly_report_2021.pdf
touch ${root_dir}/archive/templates/old_policy_template.docx
touch ${root_dir}/archive/templates/old_report_template.xlsx
touch ${root_dir}/departments/department_A/2023/budget/budget_plan.pdf
touch ${root_dir}/departments/department_A/2023/budget/budget_report.pdf
touch ${root_dir}/departments/department_A/2023/legislation/legislation_001.pdf
touch ${root_dir}/departments/department_A/2023/legislation/legislation_002.pdf
touch ${root_dir}/departments/department_A/2023/policies/policy_001.pdf
touch ${root_dir}/departments/department_A/2023/policies/policy_002.pdf
touch ${root_dir}/departments/department_A/2023/reports/annual_report.pdf
touch ${root_dir}/departments/department_A/2023/reports/monthly_report.pdf
touch ${root_dir}/departments/department_A/2024/budget/budget_plan.pdf
touch ${root_dir}/departments/department_A/2024/budget/budget_report.pdf
touch ${root_dir}/departments/department_A/2024/legislation/legislation_001.pdf
touch ${root_dir}/departments/department_A/2024/legislation/legislation_002.pdf
touch ${root_dir}/departments/department_A/2024/policies/policy_001.pdf
touch ${root_dir}/departments/department_A/2024/policies/policy_002.pdf
touch ${root_dir}/departments/department_A/2024/reports/annual_report.pdf
touch ${root_dir}/departments/department_A/2024/reports/monthly_report.pdf
touch ${root_dir}/departments/department_B/2023/budget/budget_plan.pdf
touch ${root_dir}/departments/department_B/2023/budget/budget_report.pdf
touch ${root_dir}/departments/department_B/2023/legislation/legislation_001.pdf
touch ${root_dir}/departments/department_B/2023/legislation/legislation_002.pdf
touch ${root_dir}/departments/department_B/2023/policies/policy_001.pdf
touch ${root_dir}/departments/department_B/2023/policies/policy_002.pdf
touch ${root_dir}/departments/department_B/2023/reports/annual_report.pdf
touch ${root_dir}/departments/department_B/2023/reports/monthly_report.pdf
touch ${root_dir}/departments/department_B/2024/budget/budget_plan.pdf
touch ${root_dir}/departments/department_B/2024/budget/budget_report.pdf
touch ${root_dir}/departments/department_B/2024/legislation/legislation_001.pdf
touch ${root_dir}/departments/department_B/2024/legislation/legislation_002.pdf
touch ${root_dir}/departments/department_B/2024/policies/policy_001.pdf
touch ${root_dir}/departments/department_B/2024/policies/policy_002.pdf
touch ${root_dir}/departments/department_B/2024/reports/annual_report.pdf
touch ${root_dir}/departments/department_B/2024/reports/monthly_report.pdf
touch ${root_dir}/reports/annual_reports/annual_report_2023.pdf
touch ${root_dir}/reports/monthly_reports/february_2023.pdf
touch ${root_dir}/reports/monthly_reports/january_2023.pdf
touch ${root_dir}/reports/quarterly_reports/Q1_report_2023.pdf
touch ${root_dir}/reports/quarterly_reports/Q2_report_2023.pdf
touch ${root_dir}/templates/budget_templates/budget_plan_template.xlsx
touch ${root_dir}/templates/budget_templates/budget_report_template.xlsx
touch ${root_dir}/templates/legislation_templates/legislation_template.docx
touch ${root_dir}/templates/legislation_templates/legislation_amendment_template.docx
touch ${root_dir}/templates/policy_templates/policy_draft_template.docx
touch ${root_dir}/templates/policy_templates/policy_final_template.docx
touch ${root_dir}/templates/report_templates/annual_report_template.docx
touch ${root_dir}/templates/report_templates/monthly_report_template.docx
