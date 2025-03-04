#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Research/01_Papers
mkdir -p $root_dir/01_Research/02_Datasets
mkdir -p $root_dir/01_Research/03_References
mkdir -p $root_dir/02_Development/01_Code
mkdir -p $root_dir/02_Development/02_Models
mkdir -p $root_dir/02_Development/03_Tests
mkdir -p $root_dir/03_Documentation/01_Reports
mkdir -p $root_dir/03_Documentation/02_Presentations
mkdir -p $root_dir/03_Documentation/03_Manuals
mkdir -p $root_dir/04_Deployment/01_Containers
mkdir -p $root_dir/04_Deployment/02_Scripts
mkdir -p $root_dir/04_Deployment/03_Logs
mkdir -p $root_dir/05_Backup/01_Code_Backup
mkdir -p $root_dir/05_Backup/02_Models_Backup
mkdir -p $root_dir/05_Backup/03_Datasets_Backup

touch $root_dir/01_Research/01_Papers/paper1.pdf
touch $root_dir/01_Research/01_Papers/paper2.pdf
touch $root_dir/01_Research/02_Datasets/dataset1.csv
touch $root_dir/01_Research/02_Datasets/dataset2.csv
touch $root_dir/01_Research/03_References/reference1.pdf
touch $root_dir/02_Development/01_Code/script1.py
touch $root_dir/02_Development/01_Code/script2.py
touch $root_dir/02_Development/02_Models/model1.h5
touch $root_dir/02_Development/02_Models/model2.h5
touch $root_dir/02_Development/03_Tests/test1.py
touch $root_dir/02_Development/03_Tests/test2.py
touch $root_dir/03_Documentation/01_Reports/report1.pdf
touch $root_dir/03_Documentation/01_Reports/report2.pdf
touch $root_dir/03_Documentation/02_Presentations/presentation1.ppt
touch $root_dir/03_Documentation/02_Presentations/presentation2.ppt
touch $root_dir/03_Documentation/03_Manuals/manual1.pdf
touch $root_dir/03_Documentation/03_Manuals/manual2.pdf
touch $root_dir/04_Deployment/01_Containers/dockerfile1
touch $root_dir/04_Deployment/01_Containers/dockerfile2
touch $root_dir/04_Deployment/02_Scripts/deploy1.sh
touch $root_dir/04_Deployment/02_Scripts/deploy2.sh
touch $root_dir/04_Deployment/03_Logs/log1.txt
touch $root_dir/04_Deployment/03_Logs/log2.txt
touch $root_dir/05_Backup/01_Code_Backup/script1_backup.py
touch $root_dir/05_Backup/01_Code_Backup/script2_backup.py
touch $root_dir/05_Backup/02_Models_Backup/model1_backup.h5
touch $root_dir/05_Backup/02_Models_Backup/model2_backup.h5
touch $root_dir/05_Backup/03_Datasets_Backup/dataset1_backup.csv
touch $root_dir/05_Backup/03_Datasets_Backup/dataset2_backup.csv