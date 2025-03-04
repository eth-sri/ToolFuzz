#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Research/01_Astronomy/Galaxy_Research
mkdir -p $root_dir/01_Research/01_Astronomy/Star_Research
mkdir -p $root_dir/01_Research/02_Space_Exploration/Mission_Research
mkdir -p $root_dir/01_Research/02_Space_Exploration/Planet_Research

mkdir -p $root_dir/02_Data/01_Astronomy_Data/Galaxy_Data
mkdir -p $root_dir/02_Data/01_Astronomy_Data/Star_Data
mkdir -p $root_dir/02_Data/02_Space_Exploration_Data/Mission_Data
mkdir -p $root_dir/02_Data/02_Space_Exploration_Data/Planet_Data

mkdir -p $root_dir/03_Publications/01_Astronomy_Publications/Galaxy_Publications
mkdir -p $root_dir/03_Publications/01_Astronomy_Publications/Star_Publications
mkdir -p $root_dir/03_Publications/02_Space_Exploration_Publications/Mission_Publications
mkdir -p $root_dir/03_Publications/02_Space_Exploration_Publications/Planet_Publications

mkdir -p $root_dir/04_Presentations/01_Astronomy_Presentations/Galaxy_Presentations
mkdir -p $root_dir/04_Presentations/01_Astronomy_Presentations/Star_Presentations
mkdir -p $root_dir/04_Presentations/02_Space_Exploration_Presentations/Mission_Presentations
mkdir -p $root_dir/04_Presentations/02_Space_Exploration_Presentations/Planet_Presentations

mkdir -p $root_dir/05_Images/01_Astronomy_Images/Galaxy_Images
mkdir -p $root_dir/05_Images/01_Astronomy_Images/Star_Images
mkdir -p $root_dir/05_Images/02_Space_Exploration_Images/Mission_Images
mkdir -p $root_dir/05_Images/02_Space_Exploration_Images/Planet_Images

touch $root_dir/01_Research/01_Astronomy/Galaxy_Research/galaxy_research_paper_v1.pdf
touch $root_dir/01_Research/01_Astronomy/Galaxy_Research/galaxy_research_paper_v2.pdf

# ... and so on for all the files