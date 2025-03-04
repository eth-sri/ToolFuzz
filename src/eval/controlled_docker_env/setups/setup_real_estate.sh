#!/bin/bash

root_dir=$1

mkdir -p $root_dir/archive/properties
mkdir -p $root_dir/archive/contracts
mkdir -p $root_dir/archive/templates
mkdir -p $root_dir/properties/property_A/2023/property_details
mkdir -p $root_dir/properties/property_A/2023/contracts
mkdir -p $root_dir/properties/property_A/2023/inspections
mkdir -p $root_dir/properties/property_A/2023/tax/Q1
mkdir -p $root_dir/properties/property_A/2023/tax/Q2
mkdir -p $root_dir/properties/property_A/2023/tax/Q3
mkdir -p $root_dir/properties/property_A/2023/tax/Q4
mkdir -p $root_dir/properties/property_A/2024/property_details
mkdir -p $root_dir/properties/property_A/2024/contracts
mkdir -p $root_dir/properties/property_A/2024/inspections
mkdir -p $root_dir/properties/property_A/2024/tax/Q1
mkdir -p $root_dir/properties/property_A/2024/tax/Q2
mkdir -p $root_dir/properties/property_A/2024/tax/Q3
mkdir -p $root_dir/properties/property_A/2024/tax/Q4
mkdir -p $root_dir/properties/property_B/2023/property_details
mkdir -p $root_dir/properties/property_B/2023/contracts
mkdir -p $root_dir/properties/property_B/2023/inspections
mkdir -p $root_dir/properties/property_B/2023/tax/Q1
mkdir -p $root_dir/properties/property_B/2023/tax/Q2
mkdir -p $root_dir/properties/property_B/2023/tax/Q3
mkdir -p $root_dir/properties/property_B/2023/tax/Q4
mkdir -p $root_dir/properties/property_B/2024/property_details
mkdir -p $root_dir/properties/property_B/2024/contracts
mkdir -p $root_dir/properties/property_B/2024/inspections
mkdir -p $root_dir/properties/property_B/2024/tax/Q1
mkdir -p $root_dir/properties/property_B/2024/tax/Q2
mkdir -p $root_dir/properties/property_B/2024/tax/Q3
mkdir -p $root_dir/properties/property_B/2024/tax/Q4
mkdir -p $root_dir/reports/annual_reports
mkdir -p $root_dir/reports/monthly_reports
mkdir -p $root_dir/reports/quarterly_reports
mkdir -p $root_dir/templates/contract_templates
mkdir -p $root_dir/templates/inspection_templates
mkdir -p $root_dir/templates/tax_templates

touch $root_dir/archive/properties/archived_property_A_2021.zip
touch $root_dir/archive/properties/archived_property_B_2021.zip
touch $root_dir/archive/contracts/archived_contract_A_2021.pdf
touch $root_dir/archive/contracts/archived_contract_B_2021.pdf
touch $root_dir/archive/templates/old_lease_agreement_template.docx
touch $root_dir/archive/templates/old_purchase_agreement_template.docx
touch $root_dir/properties/property_A/2023/property_details/property_description.pdf
touch $root_dir/properties/property_A/2023/property_details/property_images.pdf
touch $root_dir/properties/property_A/2023/contracts/lease_agreement.pdf
touch $root_dir/properties/property_A/2023/contracts/purchase_agreement.pdf
touch $root_dir/properties/property_A/2023/inspections/inspection_report_feb.csv
touch $root_dir/properties/property_A/2023/inspections/inspection_report_jan.csv
touch $root_dir/properties/property_A/2023/tax/Q1/tax_filing.pdf
touch $root_dir/properties/property_A/2023/tax/Q1/tax_receipt.pdf
touch $root_dir/properties/property_A/2023/tax/Q2/tax_filing.pdf
touch $root_dir/properties/property_A/2023/tax/Q2/tax_receipt.pdf
touch $root_dir/properties/property_A/2023/tax/Q3/tax_filing.pdf
touch $root_dir/properties/property_A/2023/tax/Q3/tax_receipt.pdf
touch $root_dir/properties/property_A/2023/tax/Q4/tax_filing.pdf
touch $root_dir/properties/property_A/2023/tax/Q4/tax_receipt.pdf
touch $root_dir/properties/property_A/2024/property_details/property_description.pdf
touch $root_dir/properties/property_A/2024/property_details/property_images.pdf
touch $root_dir/properties/property_A/2024/contracts/lease_agreement.pdf
touch $root_dir/properties/property_A/2024/contracts/purchase_agreement.pdf
touch $root_dir/properties/property_A/2024/inspections/inspection_report_feb.csv
touch $root_dir/properties/property_A/2024/inspections/inspection_report_jan.csv
touch $root_dir/properties/property_A/2024/tax/Q1/tax_filing.pdf
touch $root_dir/properties/property_A/2024/tax/Q1/tax_receipt.pdf
touch $root_dir/properties/property_A/2024/tax/Q2/tax_filing.pdf
touch $root_dir/properties/property_A/2024/tax/Q2/tax_receipt.pdf
touch $root_dir/properties/property_A/2024/tax/Q3/tax_filing.pdf
touch $root_dir/properties/property_A/2024/tax/Q3/tax_receipt.pdf
touch $root_dir/properties/property_A/2024/tax/Q4/tax_filing.pdf
touch $root_dir/properties/property_A/2024/tax/Q4/tax_receipt.pdf
touch $root_dir/properties/property_B/2023/property_details/property_description.pdf
touch $root_dir/properties/property_B/2023/property_details/property_images.pdf
touch $root_dir/properties/property_B/2023/contracts/lease_agreement.pdf
touch $root_dir/properties/property_B/2023/contracts/purchase_agreement.pdf
touch $root_dir/properties/property_B/2023/inspections/inspection_report_feb.csv
touch $root_dir/properties/property_B/2023/inspections/inspection_report_jan.csv
touch $root_dir/properties/property_B/2023/tax/Q1/tax_filing.pdf
touch $root_dir/properties/property_B/2023/tax/Q1/tax_receipt.pdf
touch $root_dir/properties/property_B/2023/tax/Q2/tax_filing.pdf
touch $root_dir/properties/property_B/2023/tax/Q2/tax_receipt.pdf
touch $root_dir/properties/property_B/2023/tax/Q3/tax_filing.pdf
touch $root_dir/properties/property_B/2023/tax/Q3/tax_receipt.pdf
touch $root_dir/properties/property_B/2023/tax/Q4/tax_filing.pdf
touch $root_dir/properties/property_B/2023/tax/Q4/tax_receipt.pdf
touch $root_dir/properties/property_B/2024/property_details/property_description.pdf
touch $root_dir/properties/property_B/2024/property_details/property_images.pdf
touch $root_dir/properties/property_B/2024/contracts/lease_agreement.pdf
touch $root_dir/properties/property_B/2024/contracts/purchase_agreement.pdf
touch $root_dir/properties/property_B/2024/inspections/inspection_report_feb.csv
touch $root_dir/properties/property_B/2024/inspections/inspection_report_jan.csv
touch $root_dir/properties/property_B/2024/tax/Q1/tax_filing.pdf
touch $root_dir/properties/property_B/2024/tax/Q1/tax_receipt.pdf
touch $root_dir/properties/property_B/2024/tax/Q2/tax_filing.pdf
touch $root_dir/properties/property_B/2024/tax/Q2/tax_receipt.pdf
touch $root_dir/properties/property_B/2024/tax/Q3/tax_filing.pdf
touch $root_dir/properties/property_B/2024/tax/Q3/tax_receipt.pdf
touch $root_dir/properties/property_B/2024/tax/Q4/tax_filing.pdf
touch $root_dir/properties/property_B/2024/tax/Q4/tax_receipt.pdf
touch $root_dir/reports/annual_reports/annual_report_2023.pdf
touch $root_dir/reports/monthly_reports/february_2023.pdf
touch $root_dir/reports/monthly_reports/january_2023.pdf
touch $root_dir/reports/quarterly_reports/Q1_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q2_report_2023.pdf
touch $root_dir/templates/contract_templates/lease_agreement_template.docx
touch $root_dir/templates/contract_templates/purchase_agreement_template.docx
touch $root_dir/templates/inspection_templates/monthly_inspection_template.xlsx
touch $root_dir/templates/inspection_templates/annual_inspection_template.xlsx
touch $root_dir/templates/tax_templates/property_tax_template.docx
touch $root_dir/templates/tax_templates/income_tax_template.docx
