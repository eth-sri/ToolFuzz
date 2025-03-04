#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_Data_Collection/01_Game_Data
mkdir -p $root_dir/01_Data_Collection/02_Player_Stats
mkdir -p $root_dir/01_Data_Collection/03_Team_Stats
mkdir -p $root_dir/02_Analysis/01_Player_Analysis
mkdir -p $root_dir/02_Analysis/02_Game_Analysis
mkdir -p $root_dir/02_Analysis/03_Team_Analysis
mkdir -p $root_dir/03_Reports/01_Weekly_Reports
mkdir -p $root_dir/03_Reports/02_Monthly_Reports
mkdir -p $root_dir/03_Reports/03_Annual_Reports
mkdir -p $root_dir/04_Presentations/01_Team_Presentations
mkdir -p $root_dir/04_Presentations/02_Conference_Presentations
mkdir -p $root_dir/05_Research/01_Articles
mkdir -p $root_dir/05_Research/02_Books
mkdir -p $root_dir/05_Research/03_Papers
mkdir -p $root_dir/06_Templates/01_Report_Templates
mkdir -p $root_dir/06_Templates/02_Presentation_Templates
mkdir -p $root_dir/06_Templates/03_Analysis_Templates

touch $root_dir/01_Data_Collection/01_Game_Data/game1_data.csv
touch $root_dir/01_Data_Collection/01_Game_Data/game2_data.csv
touch $root_dir/01_Data_Collection/02_Player_Stats/player1_stats.csv
touch $root_dir/01_Data_Collection/02_Player_Stats/player2_stats.csv
touch $root_dir/01_Data_Collection/03_Team_Stats/team1_stats.csv
touch $root_dir/01_Data_Collection/03_Team_Stats/team2_stats.csv
touch $root_dir/02_Analysis/01_Player_Analysis/player1_analysis.docx
touch $root_dir/02_Analysis/01_Player_Analysis/player2_analysis.docx
touch $root_dir/02_Analysis/02_Game_Analysis/game1_analysis.docx
touch $root_dir/02_Analysis/02_Game_Analysis/game2_analysis.docx
touch $root_dir/02_Analysis/03_Team_Analysis/team1_analysis.docx
touch $root_dir/02_Analysis/03_Team_Analysis/team2_analysis.docx
touch $root_dir/03_Reports/01_Weekly_Reports/week1_report.pdf
touch $root_dir/03_Reports/01_Weekly_Reports/week2_report.pdf
touch $root_dir/03_Reports/02_Monthly_Reports/month1_report.pdf
touch $root_dir/03_Reports/02_Monthly_Reports/month2_report.pdf
touch $root_dir/03_Reports/03_Annual_Reports/annual_report_2021.pdf
touch $root_dir/03_Reports/03_Annual_Reports/annual_report_2022.pdf
touch $root_dir/04_Presentations/01_Team_Presentations/team1_presentation.pptx
touch $root_dir/04_Presentations/01_Team_Presentations/team2_presentation.pptx
touch $root_dir/04_Presentations/02_Conference_Presentations/conference1_presentation.pptx
touch $root_dir/04_Presentations/02_Conference_Presentations/conference2_presentation.pptx
touch $root_dir/05_Research/01_Articles/article1.pdf
touch $root_dir/05_Research/01_Articles/article2.pdf
touch $root_dir/05_Research/02_Books/book1.pdf
touch $root_dir/05_Research/02_Books/book2.pdf
touch $root_dir/05_Research/03_Papers/paper1.pdf
touch $root_dir/05_Research/03_Papers/paper2.pdf
touch $root_dir/06_Templates/01_Report_Templates/weekly_report_template.docx
touch $root_dir/06_Templates/01_Report_Templates/monthly_report_template.docx
touch $root_dir/06_Templates/02_Presentation_Templates/team_presentation_template.pptx
touch $root_dir/06_Templates/02_Presentation_Templates/conference_presentation_template.pptx
touch $root_dir/06_Templates/03_Analysis_Templates/player_analysis_template.docx
touch $root_dir/06_Templates/03_Analysis_Templates/game_analysis_template.docx
