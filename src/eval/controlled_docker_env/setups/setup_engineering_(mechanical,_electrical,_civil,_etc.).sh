#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Projects/01_Project_A/01_Design/CAD_Files
mkdir -p $root_dir/01_Projects/01_Project_A/01_Design/Calculations
mkdir -p $root_dir/01_Projects/01_Project_A/01_Design/Specifications
mkdir -p $root_dir/01_Projects/01_Project_A/02_Manufacturing/Manufacturing_Plans
mkdir -p $root_dir/01_Projects/01_Project_A/02_Manufacturing/Quality_Control
mkdir -p $root_dir/01_Projects/01_Project_A/03_Testing/Test_Reports
mkdir -p $root_dir/01_Projects/01_Project_A/03_Testing/Test_Setup
mkdir -p $root_dir/01_Projects/02_Project_B/01_Design/CAD_Files
mkdir -p $root_dir/01_Projects/02_Project_B/01_Design/Calculations
mkdir -p $root_dir/01_Projects/02_Project_B/01_Design/Specifications
mkdir -p $root_dir/01_Projects/02_Project_B/02_Manufacturing/Manufacturing_Plans
mkdir -p $root_dir/01_Projects/02_Project_B/02_Manufacturing/Quality_Control
mkdir -p $root_dir/01_Projects/02_Project_B/03_Testing/Test_Reports
mkdir -p $root_dir/01_Projects/02_Project_B/03_Testing/Test_Setup
mkdir -p $root_dir/02_Resources/01_Materials
mkdir -p $root_dir/02_Resources/02_Tools
mkdir -p $root_dir/02_Resources/03_Software
mkdir -p $root_dir/03_Documents/01_Standards
mkdir -p $root_dir/03_Documents/02_Patents
mkdir -p $root_dir/03_Documents/03_Reports
mkdir -p $root_dir/04_Archives/01_Old_Projects
mkdir -p $root_dir/04_Archives/02_Old_Documents
mkdir -p $root_dir/04_Archives/03_Old_Resources

# Create files

for dir in $(find $root_dir -type d); do
  touch $dir/dummy_file.txt
  done