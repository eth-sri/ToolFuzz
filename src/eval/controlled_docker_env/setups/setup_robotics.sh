#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Research/01_Papers
mkdir -p $root_dir/01_Research/02_Patents
mkdir -p $root_dir/01_Research/03_References
mkdir -p $root_dir/02_Design/01_Concepts
mkdir -p $root_dir/02_Design/02_CAD_Models
mkdir -p $root_dir/02_Design/03_Simulations
mkdir -p $root_dir/03_Prototyping/01_Prototype_Versions/prototype_v1
mkdir -p $root_dir/03_Prototyping/01_Prototype_Versions/prototype_v2
mkdir -p $root_dir/03_Prototyping/02_Tests
mkdir -p $root_dir/04_Production/01_Manufacturing_Plans
mkdir -p $root_dir/04_Production/02_Assembly_Guides
mkdir -p $root_dir/04_Production/03_Quality_Control
mkdir -p $root_dir/05_Documentation/01_User_Manuals
mkdir -p $root_dir/05_Documentation/02_Technical_Specs
mkdir -p $root_dir/05_Documentation/03_Maintenance_Guides
mkdir -p $root_dir/06_Support/01_FAQs
mkdir -p $root_dir/06_Support/02_Troubleshooting_Guides
mkdir -p $root_dir/06_Support/03_Software_Updates

touch $root_dir/01_Research/01_Papers/paper1.pdf
touch $root_dir/01_Research/01_Papers/paper2.pdf
...
touch $root_dir/06_Support/03_Software_Updates/update2.zip