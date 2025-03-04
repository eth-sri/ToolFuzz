#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Projects/01_Project_A/01_Design
mkdir -p $root_dir/01_Projects/01_Project_A/02_Implementation
mkdir -p $root_dir/01_Projects/01_Project_A/03_Testing
mkdir -p $root_dir/01_Projects/01_Project_A/04_Documentation
mkdir -p $root_dir/01_Projects/02_Project_B/01_Design
mkdir -p $root_dir/01_Projects/02_Project_B/02_Implementation
mkdir -p $root_dir/01_Projects/02_Project_B/03_Testing
mkdir -p $root_dir/01_Projects/02_Project_B/04_Documentation
mkdir -p $root_dir/02_Templates
mkdir -p $root_dir/03_Standards/IEEE_Standards
mkdir -p $root_dir/03_Standards/ITU_Standards
mkdir -p $root_dir/04_Training/01_Materials
mkdir -p $root_dir/04_Training/02_Certifications/CCNA
mkdir -p $root_dir/04_Training/02_Certifications/CCNP
mkdir -p $root_dir/05_Resources/01_Manuals
mkdir -p $root_dir/05_Resources/02_Tools

touch $root_dir/01_Projects/01_Project_A/01_Design/network_design_v1.pdf
touch $root_dir/01_Projects/01_Project_A/01_Design/network_design_v2.pdf