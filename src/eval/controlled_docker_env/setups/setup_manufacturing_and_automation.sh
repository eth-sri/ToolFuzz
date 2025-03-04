#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Design/01_Concepts/Machine_Designs
mkdir -p ${root_dir}/01_Design/01_Concepts/Automation_Schemes
mkdir -p ${root_dir}/01_Design/01_Concepts/Assembly_Drawings
mkdir -p ${root_dir}/01_Design/02_Specifications/Drafts
mkdir -p ${root_dir}/01_Design/02_Specifications/Final
mkdir -p ${root_dir}/01_Design/03_Simulations
mkdir -p ${root_dir}/01_Design/04_References
mkdir -p ${root_dir}/02_Manufacturing/01_Materials/material_certificates
mkdir -p ${root_dir}/02_Manufacturing/02_Machining/machining_reports
mkdir -p ${root_dir}/02_Manufacturing/03_Assembly/assembly_reports
mkdir -p ${root_dir}/02_Manufacturing/04_Quality_Control/qc_reports
mkdir -p ${root_dir}/03_Automation/01_Programming
mkdir -p ${root_dir}/03_Automation/02_Testing/test_reports
mkdir -p ${root_dir}/03_Automation/03_Installation/installation_reports
mkdir -p ${root_dir}/04_Documents/Project_Proposal
mkdir -p ${root_dir}/04_Documents/Project_Plan
mkdir -p ${root_dir}/04_Documents/Meeting_Notes
mkdir -p ${root_dir}/04_Documents/Manuals
mkdir -p ${root_dir}/05_Archive/Old_Designs
mkdir -p ${root_dir}/05_Archive/Old_Documents
mkdir -p ${root_dir}/05_Archive/Old_Reports

touch ${root_dir}/01_Design/01_Concepts/Machine_Designs/machine_design_v1.dwg
touch ${root_dir}/01_Design/01_Concepts/Machine_Designs/machine_design_v2.dwg
touch ${root_dir}/01_Design/01_Concepts/Automation_Schemes/automation_scheme_v1.dwg
touch ${root_dir}/01_Design/01_Concepts/Assembly_Drawings/assembly_drawing_v1.dwg
touch ${root_dir}/01_Design/02_Specifications/Drafts/specification_draft.txt
touch ${root_dir}/01_Design/02_Specifications/Final/final_specification.txt
touch ${root_dir}/01_Design/03_Simulations/simulation_result1.csv
touch ${root_dir}/01_Design/04_References/reference_image.jpg
touch ${root_dir}/02_Manufacturing/01_Materials/material_list.xlsx
touch ${root_dir}/02_Manufacturing/01_Materials/material_certificates/material_certificate_1.pdf
touch ${root_dir}/02_Manufacturing/02_Machining/machining_instructions.docx
touch ${root_dir}/02_Manufacturing/02_Machining/machining_reports/machining_report_1.pdf
touch ${root_dir}/02_Manufacturing/03_Assembly/assembly_instructions.docx
touch ${root_dir}/02_Manufacturing/03_Assembly/assembly_reports/assembly_report_1.pdf
touch ${root_dir}/02_Manufacturing/04_Quality_Control/qc_checklist.xlsx
touch ${root_dir}/02_Manufacturing/04_Quality_Control/qc_reports/qc_report_1.pdf
touch ${root_dir}/03_Automation/01_Programming/plc_program_v1.0
touch ${root_dir}/03_Automation/01_Programming/robot_program_v1.0
touch ${root_dir}/03_Automation/02_Testing/test_plan.docx
touch ${root_dir}/03_Automation/02_Testing/test_reports/test_report_1.pdf
touch ${root_dir}/03_Automation/03_Installation/installation_instructions.docx
touch ${root_dir}/03_Automation/03_Installation/installation_reports/installation_report_1.pdf
touch ${root_dir}/04_Documents/Project_Proposal/proposal.pdf
touch ${root_dir}/04_Documents/Project_Plan/project_plan.xlsx
touch ${root_dir}/04_Documents/Meeting_Notes/meeting_notes.txt
touch ${root_dir}/04_Documents/Manuals/user_manual.pdf
touch ${root_dir}/04_Documents/Manuals/maintenance_manual.pdf
touch ${root_dir}/05_Archive/Old_Designs/old_design.dwg
touch ${root_dir}/05_Archive/Old_Documents/old_document.docx
touch ${root_dir}/05_Archive/Old_Reports/old_report.pdf