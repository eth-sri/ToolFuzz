#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_PreProduction/01_Script/Drafts
mkdir -p $root_dir/01_PreProduction/01_Script/Final
mkdir -p $root_dir/01_PreProduction/02_Storyboard
mkdir -p $root_dir/01_PreProduction/03_Casting/Auditions
mkdir -p $root_dir/01_PreProduction/03_Casting/Final_Cast
mkdir -p $root_dir/01_PreProduction/04_Location_Scouting/location_photos
mkdir -p $root_dir/02_Production/01_Filming/Daily_Rushes
mkdir -p $root_dir/02_Production/01_Filming/Final_Scenes
mkdir -p $root_dir/02_Production/02_Props
mkdir -p $root_dir/02_Production/03_Costumes/costume_designs
mkdir -p $root_dir/02_Production/04_Set_Design/set_photos
mkdir -p $root_dir/03_PostProduction/01_Editing/Rough_Cut
mkdir -p $root_dir/03_PostProduction/01_Editing/Final_Cut
mkdir -p $root_dir/03_PostProduction/02_Sound_Editing/Sound_Effects
mkdir -p $root_dir/03_PostProduction/02_Sound_Editing/Music
mkdir -p $root_dir/03_PostProduction/03_Color_Grading
mkdir -p $root_dir/03_PostProduction/04_VFX
mkdir -p $root_dir/04_Distribution/Marketing_Materials/Posters
mkdir -p $root_dir/04_Distribution/Marketing_Materials/Trailers
mkdir -p $root_dir/04_Distribution/Release_Formats/DVD
mkdir -p $root_dir/04_Distribution/Release_Formats/Streaming
mkdir -p $root_dir/05_Documents/Budget
mkdir -p $root_dir/05_Documents/Production_Schedule
mkdir -p $root_dir/05_Documents/Contracts
mkdir -p $root_dir/05_Documents/Meeting_Notes

touch $root_dir/01_PreProduction/01_Script/Drafts/script_draft_v1.txt
touch $root_dir/01_PreProduction/01_Script/Final/final_script_v1.txt
touch $root_dir/01_PreProduction/02_Storyboard/storyboard_v1.jpg
touch $root_dir/01_PreProduction/03_Casting/Auditions/audition_clip_v1.mp4
touch $root_dir/01_PreProduction/03_Casting/Final_Cast/cast_list.txt
touch $root_dir/01_PreProduction/04_Location_Scouting/location_photos/location_photo_v1.jpg
touch $root_dir/02_Production/01_Filming/Daily_Rushes/daily_rush_v1.mp4
touch $root_dir/02_Production/01_Filming/Final_Scenes/final_scene_v1.mp4
touch $root_dir/02_Production/02_Props/prop_list.txt
touch $root_dir/02_Production/03_Costumes/costume_designs/costume_design_v1.jpg
touch $root_dir/02_Production/04_Set_Design/set_photos/set_photo_v1.jpg
touch $root_dir/03_PostProduction/01_Editing/Rough_Cut/rough_cut_v1.mp4
touch $root_dir/03_PostProduction/01_Editing/Final_Cut/final_cut_v1.mp4
touch $root_dir/03_PostProduction/02_Sound_Editing/Sound_Effects/sound_effect_v1.wav
touch $root_dir/03_PostProduction/02_Sound_Editing/Music/background_music_v1.mp3
touch $root_dir/03_PostProduction/03_Color_Grading/color_grade_v1.dpx
touch $root_dir/03_PostProduction/04_VFX/vfx_clip_v1.mov
touch $root_dir/04_Distribution/Marketing_Materials/Posters/poster_v1.jpg
touch $root_dir/04_Distribution/Marketing_Materials/Trailers/trailer_v1.mp4
touch $root_dir/04_Distribution/Release_Formats/DVD/dvd_cover_v1.jpg
touch $root_dir/04_Distribution/Release_Formats/Streaming/thumbnail_v1.jpg
touch $root_dir/05_Documents/Budget/budget_plan.xlsx
touch $root_dir/05_Documents/Production_Schedule/schedule.xlsx
touch $root_dir/05_Documents/Contracts/actor_contract_v1.pdf
touch $root_dir/05_Documents/Meeting_Notes/meeting_notes_v1.txt