#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Projects/01_ProjectA/01_Code/tests
mkdir -p $root_dir/01_Projects/01_ProjectA/02_Documentation
mkdir -p $root_dir/01_Projects/01_ProjectA/03_Data/input
mkdir -p $root_dir/01_Projects/01_ProjectA/03_Data/output
mkdir -p $root_dir/01_Projects/02_ProjectB/01_Code/tests
mkdir -p $root_dir/01_Projects/02_ProjectB/02_Documentation
mkdir -p $root_dir/01_Projects/02_ProjectB/03_Data/input
mkdir -p $root_dir/01_Projects/02_ProjectB/03_Data/output
mkdir -p $root_dir/02_Research/01_Papers
mkdir -p $root_dir/02_Research/02_Notes
mkdir -p $root_dir/03_Tools/01_Scripts
mkdir -p $root_dir/03_Tools/02_Libraries/library1
mkdir -p $root_dir/03_Tools/02_Libraries/library2
mkdir -p $root_dir/04_Tutorials/01_Python
mkdir -p $root_dir/04_Tutorials/02_Machine_Learning

touch $root_dir/01_Projects/01_ProjectA/01_Code/main.py
touch $root_dir/01_Projects/01_ProjectA/01_Code/utils.py
touch $root_dir/01_Projects/01_ProjectA/01_Code/tests/test_main.py
touch $root_dir/01_Projects/01_ProjectA/01_Code/tests/test_utils.py
touch $root_dir/01_Projects/01_ProjectA/02_Documentation/README.md
touch $root_dir/01_Projects/01_ProjectA/03_Data/input/data.csv
touch $root_dir/01_Projects/01_ProjectA/03_Data/output/results.csv
touch $root_dir/01_Projects/02_ProjectB/01_Code/main.py
touch $root_dir/01_Projects/02_ProjectB/01_Code/utils.py
touch $root_dir/01_Projects/02_ProjectB/01_Code/tests/test_main.py
touch $root_dir/01_Projects/02_ProjectB/01_Code/tests/test_utils.py
touch $root_dir/01_Projects/02_ProjectB/02_Documentation/README.md
touch $root_dir/01_Projects/02_ProjectB/03_Data/input/data.csv
touch $root_dir/01_Projects/02_ProjectB/03_Data/output/results.csv
touch $root_dir/02_Research/01_Papers/paper1.pdf
touch $root_dir/02_Research/01_Papers/paper2.pdf
touch $root_dir/02_Research/02_Notes/research_notes.txt
touch $root_dir/03_Tools/01_Scripts/data_cleaning.py
touch $root_dir/03_Tools/01_Scripts/data_visualization.py
touch $root_dir/03_Tools/02_Libraries/library1/lib1.py
touch $root_dir/03_Tools/02_Libraries/library2/lib2.py
touch $root_dir/04_Tutorials/01_Python/python_basics.md
touch $root_dir/04_Tutorials/01_Python/python_advanced.md
touch $root_dir/04_Tutorials/02_Machine_Learning/ml_basics.md
touch $root_dir/04_Tutorials/02_Machine_Learning/ml_advanced.md