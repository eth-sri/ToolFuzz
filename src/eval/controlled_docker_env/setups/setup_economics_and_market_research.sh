#!/bin/bash

root_dir=$1

mkdir -p $root_dir/archive/market_reports
mkdir -p $root_dir/archive/research_data
mkdir -p $root_dir/archive/templates
mkdir -p $root_dir/clients/client_A/2023/market_reports
mkdir -p $root_dir/clients/client_A/2023/research_data
mkdir -p $root_dir/clients/client_A/2023/presentations
mkdir -p $root_dir/clients/client_A/2024/market_reports
mkdir -p $root_dir/clients/client_A/2024/research_data
mkdir -p $root_dir/clients/client_A/2024/presentations
mkdir -p $root_dir/clients/client_B/2023/market_reports
mkdir -p $root_dir/clients/client_B/2023/research_data
mkdir -p $root_dir/clients/client_B/2023/presentations
mkdir -p $root_dir/clients/client_B/2024/market_reports
mkdir -p $root_dir/clients/client_B/2024/research_data
mkdir -p $root_dir/clients/client_B/2024/presentations
mkdir -p $root_dir/reports/annual_reports
mkdir -p $root_dir/reports/quarterly_reports
mkdir -p $root_dir/reports/monthly_reports
mkdir -p $root_dir/templates/report_templates
mkdir -p $root_dir/templates/research_templates
mkdir -p $root_dir/templates/presentation_templates

touch $root_dir/archive/market_reports/archived_market_report_2021.zip
touch $root_dir/archive/market_reports/archived_market_report_2022.zip
touch $root_dir/archive/research_data/archived_research_data_2021.zip
touch $root_dir/archive/research_data/archived_research_data_2022.zip
touch $root_dir/archive/templates/old_report_template.docx
touch $root_dir/archive/templates/old_research_template.xlsx
touch $root_dir/clients/client_A/2023/market_reports/Q1_market_report.pdf
touch $root_dir/clients/client_A/2023/market_reports/Q2_market_report.pdf
touch $root_dir/clients/client_A/2023/research_data/Q1_research_data.csv
touch $root_dir/clients/client_A/2023/research_data/Q2_research_data.csv
touch $root_dir/clients/client_A/2023/presentations/Q1_presentation.ppt
touch $root_dir/clients/client_A/2023/presentations/Q2_presentation.ppt
touch $root_dir/clients/client_A/2024/market_reports/Q1_market_report.pdf
touch $root_dir/clients/client_A/2024/market_reports/Q2_market_report.pdf
touch $root_dir/clients/client_A/2024/research_data/Q1_research_data.csv
touch $root_dir/clients/client_A/2024/research_data/Q2_research_data.csv
touch $root_dir/clients/client_A/2024/presentations/Q1_presentation.ppt
touch $root_dir/clients/client_A/2024/presentations/Q2_presentation.ppt
touch $root_dir/clients/client_B/2023/market_reports/Q1_market_report.pdf
touch $root_dir/clients/client_B/2023/market_reports/Q2_market_report.pdf
touch $root_dir/clients/client_B/2023/research_data/Q1_research_data.csv
touch $root_dir/clients/client_B/2023/research_data/Q2_research_data.csv
touch $root_dir/clients/client_B/2023/presentations/Q1_presentation.ppt
touch $root_dir/clients/client_B/2023/presentations/Q2_presentation.ppt
touch $root_dir/clients/client_B/2024/market_reports/Q1_market_report.pdf
touch $root_dir/clients/client_B/2024/market_reports/Q2_market_report.pdf
touch $root_dir/clients/client_B/2024/research_data/Q1_research_data.csv
touch $root_dir/clients/client_B/2024/research_data/Q2_research_data.csv
touch $root_dir/clients/client_B/2024/presentations/Q1_presentation.ppt
touch $root_dir/clients/client_B/2024/presentations/Q2_presentation.ppt
touch $root_dir/reports/annual_reports/annual_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q1_report_2023.pdf
touch $root_dir/reports/quarterly_reports/Q2_report_2023.pdf
touch $root_dir/reports/monthly_reports/january_2023.pdf
touch $root_dir/reports/monthly_reports/february_2023.pdf
touch $root_dir/templates/report_templates/advanced_report_template.docx
touch $root_dir/templates/report_templates/basic_report_template.docx
touch $root_dir/templates/research_templates/advanced_research_template.xlsx
touch $root_dir/templates/research_templates/basic_research_template.xlsx
touch $root_dir/templates/presentation_templates/advanced_presentation_template.ppt
touch $root_dir/templates/presentation_templates/basic_presentation_template.ppt