#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/archive/cases
mkdir -p ${root_dir}/archive/reports
mkdir -p ${root_dir}/archive/templates

mkdir -p ${root_dir}/cases/case_A/2023/court_documents
mkdir -p ${root_dir}/cases/case_A/2023/legal_notices
mkdir -p ${root_dir}/cases/case_A/2023/research
mkdir -p ${root_dir}/cases/case_A/2023/contracts
mkdir -p ${root_dir}/cases/case_A/2024/court_documents
mkdir -p ${root_dir}/cases/case_A/2024/legal_notices
mkdir -p ${root_dir}/cases/case_A/2024/research
mkdir -p ${root_dir}/cases/case_A/2024/contracts

mkdir -p ${root_dir}/cases/case_B/2023/court_documents
mkdir -p ${root_dir}/cases/case_B/2023/legal_notices
mkdir -p ${root_dir}/cases/case_B/2023/research
mkdir -p ${root_dir}/cases/case_B/2023/contracts
mkdir -p ${root_dir}/cases/case_B/2024/court_documents
mkdir -p ${root_dir}/cases/case_B/2024/legal_notices
mkdir -p ${root_dir}/cases/case_B/2024/research
mkdir -p ${root_dir}/cases/case_B/2024/contracts

mkdir -p ${root_dir}/reports/annual_reports
mkdir -p ${root_dir}/reports/monthly_reports
mkdir -p ${root_dir}/reports/case_reports

mkdir -p ${root_dir}/templates/contract_templates
mkdir -p ${root_dir}/templates/legal_notice_templates
mkdir -p ${root_dir}/templates/court_document_templates

# Create files

# Archive

touch ${root_dir}/archive/cases/archived_case_A_2021.zip
touch ${root_dir}/archive/cases/archived_case_B_2021.zip
touch ${root_dir}/archive/reports/archived_annual_report_2021.pdf
touch ${root_dir}/archive/reports/archived_monthly_report_2021.pdf
touch ${root_dir}/archive/templates/old_contract_template.docx
touch ${root_dir}/archive/templates/old_legal_notice_template.docx

# Cases

touch ${root_dir}/cases/case_A/2023/court_documents/court_order.pdf
touch ${root_dir}/cases/case_A/2023/court_documents/court_transcript.pdf
touch ${root_dir}/cases/case_A/2023/legal_notices/notice_001.pdf
touch ${root_dir}/cases/case_A/2023/legal_notices/notice_002.pdf
touch ${root_dir}/cases/case_A/2023/research/case_law.pdf
touch ${root_dir}/cases/case_A/2023/research/legal_opinion.pdf
touch ${root_dir}/cases/case_A/2023/contracts/contract_001.pdf
touch ${root_dir}/cases/case_A/2023/contracts/contract_002.pdf
touch ${root_dir}/cases/case_A/2024/court_documents/court_order.pdf
touch ${root_dir}/cases/case_A/2024/court_documents/court_transcript.pdf
touch ${root_dir}/cases/case_A/2024/legal_notices/notice_001.pdf
touch ${root_dir}/cases/case_A/2024/legal_notices/notice_002.pdf
touch ${root_dir}/cases/case_A/2024/research/case_law.pdf
touch ${root_dir}/cases/case_A/2024/research/legal_opinion.pdf
touch ${root_dir}/cases/case_A/2024/contracts/contract_001.pdf
touch ${root_dir}/cases/case_A/2024/contracts/contract_002.pdf
touch ${root_dir}/cases/case_B/2023/court_documents/court_order.pdf
touch ${root_dir}/cases/case_B/2023/court_documents/court_transcript.pdf
touch ${root_dir}/cases/case_B/2023/legal_notices/notice_001.pdf
touch ${root_dir}/cases/case_B/2023/legal_notices/notice_002.pdf
touch ${root_dir}/cases/case_B/2023/research/case_law.pdf
touch ${root_dir}/cases/case_B/2023/research/legal_opinion.pdf
touch ${root_dir}/cases/case_B/2023/contracts/contract_001.pdf
touch ${root_dir}/cases/case_B/2023/contracts/contract_002.pdf
touch ${root_dir}/cases/case_B/2024/court_documents/court_order.pdf
touch ${root_dir}/cases/case_B/2024/court_documents/court_transcript.pdf
touch ${root_dir}/cases/case_B/2024/legal_notices/notice_001.pdf
touch ${root_dir}/cases/case_B/2024/legal_notices/notice_002.pdf
touch ${root_dir}/cases/case_B/2024/research/case_law.pdf
touch ${root_dir}/cases/case_B/2024/research/legal_opinion.pdf
touch ${root_dir}/cases/case_B/2024/contracts/contract_001.pdf
touch ${root_dir}/cases/case_B/2024/contracts/contract_002.pdf

# Reports

touch ${root_dir}/reports/annual_reports/annual_report_2023.pdf
touch ${root_dir}/reports/monthly_reports/february_2023.pdf
touch ${root_dir}/reports/monthly_reports/january_2023.pdf
touch ${root_dir}/reports/case_reports/case_A_report_2023.pdf
touch ${root_dir}/reports/case_reports/case_B_report_2023.pdf

# Templates

touch ${root_dir}/templates/contract_templates/advanced_contract_template.docx
touch ${root_dir}/templates/contract_templates/basic_contract_template.docx
touch ${root_dir}/templates/legal_notice_templates/formal_notice_template.docx
touch ${root_dir}/templates/legal_notice_templates/informal_notice_template.docx
touch ${root_dir}/templates/court_document_templates/court_order_template.docx
touch ${root_dir}/templates/court_document_templates/court_transcript_template.docx