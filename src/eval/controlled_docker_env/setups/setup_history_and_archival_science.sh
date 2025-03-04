#!/bin/bash

root_dir=$1

mkdir -p $root_dir/Archive/Ancient_History/Roman_Empire
mkdir -p $root_dir/Archive/Ancient_History/Greek_Civilization
mkdir -p $root_dir/Archive/Medieval_History/Crusades
mkdir -p $root_dir/Archive/Medieval_History/Renaissance
mkdir -p $root_dir/Archive/Modern_History/World_War_I
mkdir -p $root_dir/Archive/Modern_History/World_War_II
mkdir -p $root_dir/Research/Current_Projects/project_1
mkdir -p $root_dir/Research/Current_Projects/project_2
mkdir -p $root_dir/Research/Completed_Projects/project_1
mkdir -p $root_dir/Research/Completed_Projects/project_2
mkdir -p $root_dir/Publications/Books
mkdir -p $root_dir/Publications/Articles
mkdir -p $root_dir/Templates

touch $root_dir/Archive/Ancient_History/Roman_Empire/roman_empire_1.pdf
touch $root_dir/Archive/Ancient_History/Roman_Empire/roman_empire_2.pdf
touch $root_dir/Archive/Ancient_History/Greek_Civilization/greek_civilization_1.pdf
touch $root_dir/Archive/Ancient_History/Greek_Civilization/greek_civilization_2.pdf
touch $root_dir/Archive/Medieval_History/Crusades/crusades_1.pdf
touch $root_dir/Archive/Medieval_History/Crusades/crusades_2.pdf
touch $root_dir/Archive/Medieval_History/Renaissance/renaissance_1.pdf
touch $root_dir/Archive/Medieval_History/Renaissance/renaissance_2.pdf
touch $root_dir/Archive/Modern_History/World_War_I/world_war_I_1.pdf
touch $root_dir/Archive/Modern_History/World_War_I/world_war_I_2.pdf
touch $root_dir/Archive/Modern_History/World_War_II/world_war_II_1.pdf
touch $root_dir/Archive/Modern_History/World_War_II/world_war_II_2.pdf
touch $root_dir/Research/Current_Projects/project_1/notes.txt
touch $root_dir/Research/Current_Projects/project_1/references.pdf
touch $root_dir/Research/Current_Projects/project_1/draft.docx
touch $root_dir/Research/Current_Projects/project_2/notes.txt
touch $root_dir/Research/Current_Projects/project_2/references.pdf
touch $root_dir/Research/Current_Projects/project_2/draft.docx
touch $root_dir/Research/Completed_Projects/project_1/final_paper.pdf
touch $root_dir/Research/Completed_Projects/project_1/presentation.pptx
touch $root_dir/Research/Completed_Projects/project_2/final_paper.pdf
touch $root_dir/Research/Completed_Projects/project_2/presentation.pptx
touch $root_dir/Publications/Books/book_1.pdf
touch $root_dir/Publications/Books/book_2.pdf
touch $root_dir/Publications/Articles/article_1.pdf
touch $root_dir/Publications/Articles/article_2.pdf
touch $root_dir/Templates/Paper_Template.docx
touch $root_dir/Templates/Presentation_Template.pptx
