#!/bin/bashsetup_art.sh


root_dir=$1
# Root directory
mkdir -p "${root_dir}"

# Create client folders, years, document types, and quarterly tax folders explicitly
for client in client_A client_B; do
  for year in 2023 2024; do
    mkdir -p "${root_dir}/clients/$client/$year/financial_statements"
    mkdir -p "${root_dir}/clients/$client/$year/invoices"
    mkdir -p "${root_dir}/clients/$client/$year/payroll"
    for quarter in Q1 Q2 Q3 Q4; do
      mkdir -p "${root_dir}/clients/$client/$year/tax/$quarter"
    done
  done
done

# Create reports folders
mkdir -p "${root_dir}/reports/annual_reports"
mkdir -p "${root_dir}/reports/monthly_reports"
mkdir -p "${root_dir}/reports/quarterly_reports"

# Create templates folders
mkdir -p "${root_dir}/templates/invoice_templates"
mkdir -p "${root_dir}/templates/payroll_templates"
mkdir -p "${root_dir}/templates/tax_templates"

# Create archive folders
mkdir -p "${root_dir}/archive/clients"
mkdir -p "${root_dir}/archive/reports"
mkdir -p "${root_dir}/archive/templates"

# Add dummy files in client folders
for client in client_A client_B; do
  for year in 2023 2024; do
    # Financial Statements
    touch "${root_dir}/clients/$client/$year/financial_statements/balance_sheet.pdf"
    touch "${root_dir}/clients/$client/$year/financial_statements/profit_loss_statement.pdf"
    
    # Invoices
    touch "${root_dir}/clients/$client/$year/invoices/invoice_001.pdf"
    touch "${root_dir}/clients/$client/$year/invoices/invoice_002.pdf"
    
    # Payroll
    touch "${root_dir}/clients/$client/$year/payroll/employee_payroll_jan.csv"
    touch "${root_dir}/clients/$client/$year/payroll/employee_payroll_feb.csv"

    # Tax by Quarter
    for quarter in Q1 Q2 Q3 Q4; do
      touch "${root_dir}/clients/$client/$year/tax/$quarter/tax_filing.pdf"
      touch "${root_dir}/clients/$client/$year/tax/$quarter/tax_receipt.pdf"
    done
  done
done

# Add dummy files in reports folders
touch "${root_dir}/reports/annual_reports/annual_report_2023.pdf"
touch "${root_dir}/reports/monthly_reports/january_2023.pdf"
touch "${root_dir}/reports/monthly_reports/february_2023.pdf"
touch "${root_dir}/reports/quarterly_reports/Q1_report_2023.pdf"
touch "${root_dir}/reports/quarterly_reports/Q2_report_2023.pdf"

# Add dummy files in templates folders
touch "${root_dir}/templates/invoice_templates/basic_invoice_template.docx"
touch "${root_dir}/templates/invoice_templates/advanced_invoice_template.docx"
touch "${root_dir}/templates/payroll_templates/monthly_payroll_template.xlsx"
touch "${root_dir}/templates/payroll_templates/weekly_payroll_template.xlsx"
touch "${root_dir}/templates/tax_templates/standard_tax_template.docx"
touch "${root_dir}/templates/tax_templates/corporate_tax_template.docx"

# Add dummy files in archive folders
touch "${root_dir}/archive/clients/archived_client_A_2021.zip"
touch "${root_dir}/archive/clients/archived_client_B_2021.zip"
touch "${root_dir}/archive/reports/archived_annual_report_2021.pdf"
touch "${root_dir}/archive/reports/archived_monthly_report_2021.pdf"
touch "${root_dir}/archive/templates/old_invoice_template.docx"
touch "${root_dir}/archive/templates/old_payroll_template.xlsx"
