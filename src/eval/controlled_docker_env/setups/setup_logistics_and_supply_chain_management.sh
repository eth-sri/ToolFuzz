#!/bin/bash

root_dir=$1

mkdir -p $root_dir/archive/contracts
mkdir -p $root_dir/archive/reports
mkdir -p $root_dir/archive/templates
mkdir -p $root_dir/clients/client_A/2023/contracts
mkdir -p $root_dir/clients/client_A/2023/delivery_schedules
mkdir -p $root_dir/clients/client_A/2023/inventory
mkdir -p $root_dir/clients/client_A/2023/orders
mkdir -p $root_dir/clients/client_A/2024/contracts
mkdir -p $root_dir/clients/client_A/2024/delivery_schedules
mkdir -p $root_dir/clients/client_A/2024/inventory
mkdir -p $root_dir/clients/client_A/2024/orders
mkdir -p $root_dir/clients/client_B/2023/contracts
mkdir -p $root_dir/clients/client_B/2023/delivery_schedules
mkdir -p $root_dir/clients/client_B/2023/inventory
mkdir -p $root_dir/clients/client_B/2023/orders
mkdir -p $root_dir/clients/client_B/2024/contracts
mkdir -p $root_dir/clients/client_B/2024/delivery_schedules
mkdir -p $root_dir/clients/client_B/2024/inventory
mkdir -p $root_dir/clients/client_B/2024/orders
mkdir -p $root_dir/reports/annual_reports
mkdir -p $root_dir/reports/monthly_reports
mkdir -p $root_dir/reports/quarterly_reports
mkdir -p $root_dir/templates/contract_templates
mkdir -p $root_dir/templates/delivery_schedule_templates
mkdir -p $root_dir/templates/inventory_templates

touch $root_dir/archive/contracts/archived_contract_A_2021.zip
touch $root_dir/archive/contracts/archived_contract_B_2021.zip
touch $root_dir/archive/reports/archived_annual_report_2021.pdf
touch $root_dir/archive/reports/archived_monthly_report_2021.pdf
touch $root_dir/archive/templates/old_delivery_schedule_template.docx
touch $root_dir/archive/templates/old_inventory_template.xlsx
touch $root_dir/clients/client_A/2023/contracts/contract_v1.pdf
touch $root_dir/clients/client_A/2023/contracts/contract_v2.pdf
touch $root_dir/clients/client_A/2023/delivery_schedules/delivery_schedule_Q1.csv
touch $root_dir/clients/client_A/2023/delivery_schedules/delivery_schedule_Q2.csv
touch $root_dir/clients/client_A/2023/inventory/inventory_Q1.csv
touch $root_dir/clients/client_A/2023/inventory/inventory_Q2.csv
touch $root_dir/clients/client_A/2023/orders/order_001.pdf
touch $root_dir/clients/client_A/2023/orders/order_002.pdf
touch $root_dir/clients/client_A/2024/contracts/contract_v1.pdf
touch $root_dir/clients/client_A/2024/contracts/contract_v2.pdf
touch $root_dir/clients/client_A/2024/delivery_schedules/delivery_schedule_Q1.csv
touch $root_dir/clients/client_A/2024/delivery_schedules/delivery_schedule_Q2.csv
touch $root_dir/clients/client_A/2024/inventory/inventory_Q1.csv
touch $root_dir/clients/client_A/2024/inventory/inventory_Q2.csv
touch $root_dir/clients/client_A/2024/orders/order_001.pdf
touch $root_dir/clients/client_A/2024/orders/order_002.pdf
touch $root_dir/clients/client_B/2023/contracts/contract_v1.pdf
touch $root_dir/clients/client_B/2023/contracts/contract_v2.pdf
touch $root_dir/clients/client_B/2023/delivery_schedules/delivery_schedule_Q1.csv
touch $root_dir/clients/client_B/2023/delivery_schedules/delivery_schedule_Q2.csv
touch $root_dir/clients/client_B/2023/inventory/inventory_Q1.csv
touch $root_dir/clients/client_B/2023/inventory/inventory_Q2.csv
touch $root_dir/clients/client_B/2023/orders/order_001.pdf
touch $root_dir/clients/client_B/2023/orders/order_002.pdf
touch $root_dir/clients/client_B/2024/contracts/contract_v1.pdf
touch $root_dir/clients/client_B/2024/contracts/contract_v2.pdf
touch $root_dir/clients/client_B/2024/delivery_schedules/delivery_schedule_Q1.csv
touch $root_dir/clients/client_B/2024/delivery_schedules/delivery_schedule_Q2.csv
touch $root_dir/clients/client_B/2024/inventory/inventory_Q1.csv
touch $root_dir/clients/client_B/2024/inventory/inventory_Q2.csv
touch $root_dir/clients/client_B/2024/orders/order_001.pdf
touch $root_dir/clients/client_B/2024/orders/order_002.pdf
touch $root_dir/reports/annual_reports/annual_report_2023.pdf
touch $root_dir/reports/monthly_reports/february_2023.pdf
touch $root_dir/reports/monthly_reports/january_2023.pdf
touch $root_dir/reports/quarterly_reports/Q1_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q2_report_2023.pdf
touch $root_dir/templates/contract_templates/advanced_contract_template.docx
touch $root_dir/templates/contract_templates/basic_contract_template.docx
touch $root_dir/templates/delivery_schedule_templates/monthly_delivery_schedule_template.xlsx
touch $root_dir/templates/delivery_schedule_templates/weekly_delivery_schedule_template.xlsx
touch $root_dir/templates/inventory_templates/advanced_inventory_template.xlsx
touch $root_dir/templates/inventory_templates/basic_inventory_template.xlsx
