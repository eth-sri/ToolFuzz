#!/bin/bash

root_dir=$1

mkdir -p $root_dir/archive/clients
mkdir -p $root_dir/archive/reports
mkdir -p $root_dir/archive/templates
mkdir -p $root_dir/clients/client_A/2023/financial_statements
mkdir -p $root_dir/clients/client_A/2023/loan_documents
mkdir -p $root_dir/clients/client_A/2023/investment_documents
mkdir -p $root_dir/clients/client_A/2023/tax/Q1
mkdir -p $root_dir/clients/client_A/2023/tax/Q2
mkdir -p $root_dir/clients/client_A/2023/tax/Q3
mkdir -p $root_dir/clients/client_A/2023/tax/Q4
mkdir -p $root_dir/clients/client_A/2024/financial_statements
mkdir -p $root_dir/clients/client_A/2024/loan_documents
mkdir -p $root_dir/clients/client_A/2024/investment_documents
mkdir -p $root_dir/clients/client_A/2024/tax/Q1
mkdir -p $root_dir/clients/client_A/2024/tax/Q2
mkdir -p $root_dir/clients/client_A/2024/tax/Q3
mkdir -p $root_dir/clients/client_A/2024/tax/Q4
mkdir -p $root_dir/clients/client_B/2023/financial_statements
mkdir -p $root_dir/clients/client_B/2023/loan_documents
mkdir -p $root_dir/clients/client_B/2023/investment_documents
mkdir -p $root_dir/clients/client_B/2023/tax/Q1
mkdir -p $root_dir/clients/client_B/2023/tax/Q2
mkdir -p $root_dir/clients/client_B/2023/tax/Q3
mkdir -p $root_dir/clients/client_B/2023/tax/Q4
mkdir -p $root_dir/clients/client_B/2024/financial_statements
mkdir -p $root_dir/clients/client_B/2024/loan_documents
mkdir -p $root_dir/clients/client_B/2024/investment_documents
mkdir -p $root_dir/clients/client_B/2024/tax/Q1
mkdir -p $root_dir/clients/client_B/2024/tax/Q2
mkdir -p $root_dir/clients/client_B/2024/tax/Q3
mkdir -p $root_dir/clients/client_B/2024/tax/Q4
mkdir -p $root_dir/reports/annual_reports
mkdir -p $root_dir/reports/monthly_reports
mkdir -p $root_dir/reports/quarterly_reports
mkdir -p $root_dir/templates/loan_templates
mkdir -p $root_dir/templates/investment_templates
mkdir -p $root_dir/templates/tax_templates

touch $root_dir/archive/clients/archived_client_A_2021.zip
touch $root_dir/archive/clients/archived_client_B_2021.zip
touch $root_dir/archive/reports/archived_annual_report_2021.pdf
touch $root_dir/archive/reports/archived_monthly_report_2021.pdf
touch $root_dir/archive/templates/old_loan_agreement_template.docx
touch $root_dir/archive/templates/old_investment_plan_template.xlsx
touch $root_dir/clients/client_A/2023/financial_statements/balance_sheet.pdf
touch $root_dir/clients/client_A/2023/financial_statements/profit_loss_statement.pdf
touch $root_dir/clients/client_A/2023/loan_documents/loan_agreement.pdf
touch $root_dir/clients/client_A/2023/loan_documents/loan_schedule.pdf
touch $root_dir/clients/client_A/2023/investment_documents/investment_plan.pdf
touch $root_dir/clients/client_A/2023/investment_documents/investment_receipt.pdf
touch $root_dir/clients/client_A/2023/tax/Q1/tax_filing.pdf
touch $root_dir/clients/client_A/2023/tax/Q1/tax_receipt.pdf
touch $root_dir/clients/client_A/2023/tax/Q2/tax_filing.pdf
touch $root_dir/clients/client_A/2023/tax/Q2/tax_receipt.pdf
touch $root_dir/clients/client_A/2023/tax/Q3/tax_filing.pdf
touch $root_dir/clients/client_A/2023/tax/Q3/tax_receipt.pdf
touch $root_dir/clients/client_A/2023/tax/Q4/tax_filing.pdf
touch $root_dir/clients/client_A/2023/tax/Q4/tax_receipt.pdf
touch $root_dir/clients/client_A/2024/financial_statements/balance_sheet.pdf
touch $root_dir/clients/client_A/2024/financial_statements/profit_loss_statement.pdf
touch $root_dir/clients/client_A/2024/loan_documents/loan_agreement.pdf
touch $root_dir/clients/client_A/2024/loan_documents/loan_schedule.pdf
touch $root_dir/clients/client_A/2024/investment_documents/investment_plan.pdf
touch $root_dir/clients/client_A/2024/investment_documents/investment_receipt.pdf
touch $root_dir/clients/client_A/2024/tax/Q1/tax_filing.pdf
touch $root_dir/clients/client_A/2024/tax/Q1/tax_receipt.pdf
touch $root_dir/clients/client_A/2024/tax/Q2/tax_filing.pdf
touch $root_dir/clients/client_A/2024/tax/Q2/tax_receipt.pdf
touch $root_dir/clients/client_A/2024/tax/Q3/tax_filing.pdf
touch $root_dir/clients/client_A/2024/tax/Q3/tax_receipt.pdf
touch $root_dir/clients/client_A/2024/tax/Q4/tax_filing.pdf
touch $root_dir/clients/client_A/2024/tax/Q4/tax_receipt.pdf
touch $root_dir/clients/client_B/2023/financial_statements/balance_sheet.pdf
touch $root_dir/clients/client_B/2023/financial_statements/profit_loss_statement.pdf
touch $root_dir/clients/client_B/2023/loan_documents/loan_agreement.pdf
touch $root_dir/clients/client_B/2023/loan_documents/loan_schedule.pdf
touch $root_dir/clients/client_B/2023/investment_documents/investment_plan.pdf
touch $root_dir/clients/client_B/2023/investment_documents/investment_receipt.pdf
touch $root_dir/clients/client_B/2023/tax/Q1/tax_filing.pdf
touch $root_dir/clients/client_B/2023/tax/Q1/tax_receipt.pdf
touch $root_dir/clients/client_B/2023/tax/Q2/tax_filing.pdf
touch $root_dir/clients/client_B/2023/tax/Q2/tax_receipt.pdf
touch $root_dir/clients/client_B/2023/tax/Q3/tax_filing.pdf
touch $root_dir/clients/client_B/2023/tax/Q3/tax_receipt.pdf
touch $root_dir/clients/client_B/2023/tax/Q4/tax_filing.pdf
touch $root_dir/clients/client_B/2023/tax/Q4/tax_receipt.pdf
touch $root_dir/clients/client_B/2024/financial_statements/balance_sheet.pdf
touch $root_dir/clients/client_B/2024/financial_statements/profit_loss_statement.pdf
touch $root_dir/clients/client_B/2024/loan_documents/loan_agreement.pdf
touch $root_dir/clients/client_B/2024/loan_documents/loan_schedule.pdf
touch $root_dir/clients/client_B/2024/investment_documents/investment_plan.pdf
touch $root_dir/clients/client_B/2024/investment_documents/investment_receipt.pdf
touch $root_dir/clients/client_B/2024/tax/Q1/tax_filing.pdf
touch $root_dir/clients/client_B/2024/tax/Q1/tax_receipt.pdf
touch $root_dir/clients/client_B/2024/tax/Q2/tax_filing.pdf
touch $root_dir/clients/client_B/2024/tax/Q2/tax_receipt.pdf
touch $root_dir/clients/client_B/2024/tax/Q3/tax_filing.pdf
touch $root_dir/clients/client_B/2024/tax/Q3/tax_receipt.pdf
touch $root_dir/clients/client_B/2024/tax/Q4/tax_filing.pdf
touch $root_dir/clients/client_B/2024/tax/Q4/tax_receipt.pdf
touch $root_dir/reports/annual_reports/annual_report_2023.pdf
touch $root_dir/reports/monthly_reports/february_2023.pdf
touch $root_dir/reports/monthly_reports/january_2023.pdf
touch $root_dir/reports/quarterly_reports/Q1_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q2_report_2023.pdf
touch $root_dir/templates/loan_templates/standard_loan_agreement_template.docx
touch $root_dir/templates/loan_templates/advanced_loan_agreement_template.docx
touch $root_dir/templates/investment_templates/standard_investment_plan_template.xlsx
touch $root_dir/templates/investment_templates/advanced_investment_plan_template.xlsx
touch $root_dir/templates/tax_templates/corporate_tax_template.docx
touch $root_dir/templates/tax_templates/standard_tax_template.docx
