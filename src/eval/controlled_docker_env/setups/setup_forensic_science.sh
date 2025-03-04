#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/DNA_Samples
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Fingerprints
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Photos
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_001/Reports
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_001/Witness_Statements
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_002/Evidence/DNA_Samples
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_002/Evidence/Fingerprints
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_002/Evidence/Photos
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_002/Reports
mkdir -p $root_dir/01_Case_Files/01_Open_Cases/Case_002/Witness_Statements
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_001/Evidence/DNA_Samples
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_001/Evidence/Fingerprints
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_001/Evidence/Photos
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_001/Reports
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_001/Witness_Statements
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_002/Evidence/DNA_Samples
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_002/Evidence/Fingerprints
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_002/Evidence/Photos
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_002/Reports
mkdir -p $root_dir/01_Case_Files/02_Closed_Cases/Case_002/Witness_Statements
mkdir -p $root_dir/02_Research/Articles
mkdir -p $root_dir/02_Research/Books
mkdir -p $root_dir/02_Research/Journals
mkdir -p $root_dir/03_Training/Certificates
mkdir -p $root_dir/03_Training/Courses
mkdir -p $root_dir/03_Training/Workshops
mkdir -p $root_dir/04_Tools/Software
mkdir -p $root_dir/04_Tools/Templates

touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/DNA_Samples/sample_001.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/DNA_Samples/sample_002.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Fingerprints/fingerprint_001.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Fingerprints/fingerprint_002.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Photos/crime_scene_001.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Evidence/Photos/crime_scene_002.jpg
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Reports/autopsy_report.pdf
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Reports/initial_report.pdf
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Witness_Statements/statement_001.pdf
touch $root_dir/01_Case_Files/01_Open_Cases/Case_001/Witness_Statements/statement_002.pdf

# ... and so on for all the other files