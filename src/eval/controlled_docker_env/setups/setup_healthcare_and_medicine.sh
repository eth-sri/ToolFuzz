#!/bin/bash

root_dir=$1

# Patient Records
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2021/Consultation_Notes
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2021/Lab_Results
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2021/Prescriptions
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2021/X_Rays
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2022/Consultation_Notes
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2022/Lab_Results
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2022/Prescriptions
mkdir -p ${root_dir}/01_Patient_Records/01_Patient_A/2022/X_Rays
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2021/Consultation_Notes
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2021/Lab_Results
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2021/Prescriptions
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2021/X_Rays
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2022/Consultation_Notes
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2022/Lab_Results
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2022/Prescriptions
mkdir -p ${root_dir}/01_Patient_Records/02_Patient_B/2022/X_Rays

# Medical Research
mkdir -p ${root_dir}/02_Medical_Research/01_Research_Papers
mkdir -p ${root_dir}/02_Medical_Research/02_Research_Data

# Clinical Guidelines
mkdir -p ${root_dir}/03_Clinical_Guidelines/01_Disease_Management
mkdir -p ${root_dir}/03_Clinical_Guidelines/02_Surgical_Procedures

# Administrative
mkdir -p ${root_dir}/04_Administrative/01_Staff_Rosters
mkdir -p ${root_dir}/04_Administrative/02_Meeting_Minutes
mkdir -p ${root_dir}/04_Administrative/03_Policies_and_Procedures

# Create files
for dir in $(find ${root_dir}/ -type d); do
  touch ${dir}/dummy_file
done