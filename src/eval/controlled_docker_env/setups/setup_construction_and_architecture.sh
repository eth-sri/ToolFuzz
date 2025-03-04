#!/bin/bash

root_dir=$1

mkdir -p ${root_dir}/01_Projects/01_Project_A/01_Design/blueprints
mkdir -p ${root_dir}/01_Projects/01_Project_A/01_Design/3D_Models
mkdir -p ${root_dir}/01_Projects/01_Project_A/01_Design/Renderings
mkdir -p ${root_dir}/01_Projects/01_Project_A/02_Construction/safety_reports
mkdir -p ${root_dir}/01_Projects/01_Project_A/03_Post_Construction/project_photos
mkdir -p ${root_dir}/01_Projects/02_Project_B/01_Design/blueprints
mkdir -p ${root_dir}/01_Projects/02_Project_B/01_Design/3D_Models
mkdir -p ${root_dir}/01_Projects/02_Project_B/01_Design/Renderings
mkdir -p ${root_dir}/01_Projects/02_Project_B/02_Construction/safety_reports
mkdir -p ${root_dir}/01_Projects/02_Project_B/03_Post_Construction/project_photos
mkdir -p ${root_dir}/02_Archives/old_projects
mkdir -p ${root_dir}/02_Archives/old_blueprints
mkdir -p ${root_dir}/03_Templates
mkdir -p ${root_dir}/04_Documents/contracts
mkdir -p ${root_dir}/04_Documents/invoices
mkdir -p ${root_dir}/04_Documents/meeting_notes

touch ${root_dir}/01_Projects/01_Project_A/01_Design/blueprints/blueprint_v1.pdf
touch ${root_dir}/01_Projects/01_Project_A/01_Design/blueprints/blueprint_v2.pdf
touch ${root_dir}/01_Projects/01_Project_A/01_Design/3D_Models/model_v1.skp
touch ${root_dir}/01_Projects/01_Project_A/01_Design/3D_Models/model_v2.skp
touch ${root_dir}/01_Projects/01_Project_A/01_Design/Renderings/rendering_v1.jpg
touch ${root_dir}/01_Projects/01_Project_A/01_Design/Renderings/rendering_v2.jpg
touch ${root_dir}/01_Projects/01_Project_A/02_Construction/construction_schedule.xlsx
touch ${root_dir}/01_Projects/01_Project_A/02_Construction/permits.pdf
touch ${root_dir}/01_Projects/01_Project_A/02_Construction/safety_reports/safety_report_jan.pdf
touch ${root_dir}/01_Projects/01_Project_A/02_Construction/safety_reports/safety_report_feb.pdf
touch ${root_dir}/01_Projects/01_Project_A/03_Post_Construction/final_inspection.pdf
touch ${root_dir}/01_Projects/01_Project_A/03_Post_Construction/project_photos/photo1.jpg
touch ${root_dir}/01_Projects/01_Project_A/03_Post_Construction/project_photos/photo2.jpg
touch ${root_dir}/01_Projects/02_Project_B/01_Design/blueprints/blueprint_v1.pdf
touch ${root_dir}/01_Projects/02_Project_B/01_Design/blueprints/blueprint_v2.pdf
touch ${root_dir}/01_Projects/02_Project_B/01_Design/3D_Models/model_v1.skp
touch ${root_dir}/01_Projects/02_Project_B/01_Design/3D_Models/model_v2.skp
touch ${root_dir}/01_Projects/02_Project_B/01_Design/Renderings/rendering_v1.jpg
touch ${root_dir}/01_Projects/02_Project_B/01_Design/Renderings/rendering_v2.jpg
touch ${root_dir}/01_Projects/02_Project_B/02_Construction/construction_schedule.xlsx
touch ${root_dir}/01_Projects/02_Project_B/02_Construction/permits.pdf
touch ${root_dir}/01_Projects/02_Project_B/02_Construction/safety_reports/safety_report_jan.pdf
touch ${root_dir}/01_Projects/02_Project_B/02_Construction/safety_reports/safety_report_feb.pdf
touch ${root_dir}/01_Projects/02_Project_B/03_Post_Construction/final_inspection.pdf
touch ${root_dir}/01_Projects/02_Project_B/03_Post_Construction/project_photos/photo1.jpg
touch ${root_dir}/01_Projects/02_Project_B/03_Post_Construction/project_photos/photo2.jpg
touch ${root_dir}/02_Archives/old_projects/project_C.zip
touch ${root_dir}/02_Archives/old_projects/project_D.zip
touch ${root_dir}/02_Archives/old_blueprints/blueprint_C.pdf
touch ${root_dir}/02_Archives/old_blueprints/blueprint_D.pdf
touch ${root_dir}/03_Templates/blueprint_template.dwg
touch ${root_dir}/03_Templates/3D_model_template.skp
touch ${root_dir}/04_Documents/contracts/contract_A.pdf
touch ${root_dir}/04_Documents/contracts/contract_B.pdf
touch ${root_dir}/04_Documents/invoices/invoice_A.pdf
touch ${root_dir}/04_Documents/invoices/invoice_B.pdf
touch ${root_dir}/04_Documents/meeting_notes/meeting_notes_jan.docx
touch ${root_dir}/04_Documents/meeting_notes/meeting_notes_feb.docx
