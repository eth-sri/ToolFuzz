#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_PreProduction/01_Concepts/Character_Designs
mkdir -p $root_dir/01_PreProduction/01_Concepts/Environment_Designs
mkdir -p $root_dir/01_PreProduction/01_Concepts/Game_Design_Document
mkdir -p $root_dir/01_PreProduction/02_Script/Drafts
mkdir -p $root_dir/01_PreProduction/02_Script/Final
mkdir -p $root_dir/01_PreProduction/03_Storyboards
mkdir -p $root_dir/01_PreProduction/04_Animatic
mkdir -p $root_dir/01_PreProduction/05_References
mkdir -p $root_dir/02_Production/01_Modeling/Characters
mkdir -p $root_dir/02_Production/01_Modeling/Environments
mkdir -p $root_dir/02_Production/02_Texturing/Characters
mkdir -p $root_dir/02_Production/02_Texturing/Environments
mkdir -p $root_dir/02_Production/03_Rigging/Characters
mkdir -p $root_dir/02_Production/03_Rigging/Props
mkdir -p $root_dir/02_Production/04_Animation/Blocking
mkdir -p $root_dir/02_Production/04_Animation/Final
mkdir -p $root_dir/02_Production/04_Animation/Rough
mkdir -p $root_dir/02_Production/05_Programming/AI
mkdir -p $root_dir/02_Production/05_Programming/Gameplay
mkdir -p $root_dir/02_Production/05_Programming/UI
mkdir -p $root_dir/02_Production/06_Sound/Effects
mkdir -p $root_dir/02_Production/06_Sound/Music
mkdir -p $root_dir/02_Production/07_Testing/Bug_Reports
mkdir -p $root_dir/02_Production/07_Testing/Test_Plans
mkdir -p $root_dir/03_PostProduction/01_Marketing/Press_Kit
mkdir -p $root_dir/03_PostProduction/01_Marketing/Trailers
mkdir -p $root_dir/03_PostProduction/02_Release/Patches
mkdir -p $root_dir/03_PostProduction/02_Release/Versions
mkdir -p $root_dir/03_PostProduction/03_Reviews
mkdir -p $root_dir/04_Assets/Backgrounds
mkdir -p $root_dir/04_Assets/Characters
mkdir -p $root_dir/04_Assets/Props
mkdir -p $root_dir/04_Assets/Textures
mkdir -p $root_dir/05_Documents/Budget
mkdir -p $root_dir/05_Documents/Deliverables
mkdir -p $root_dir/05_Documents/Production_Schedule
mkdir -p $root_dir/05_Documents/Project_Notes
mkdir -p $root_dir/06_Builds/Archive
mkdir -p $root_dir/06_Builds/Final
mkdir -p $root_dir/06_Builds/Previews

# Create files

touch $root_dir/01_PreProduction/01_Concepts/Character_Designs/character_sketch_v1.jpg
touch $root_dir/01_PreProduction/01_Concepts/Character_Designs/character_sketch_v2.jpg
touch $root_dir/01_PreProduction/01_Concepts/Environment_Designs/environment_sketch_v1.jpg
touch $root_dir/01_PreProduction/01_Concepts/Game_Design_Document/GDD_v1.docx
touch $root_dir/01_PreProduction/02_Script/Drafts/script_draft.txt
touch $root_dir/01_PreProduction/02_Script/Final/final_script.txt
touch $root_dir/01_PreProduction/03_Storyboards/storyboard_scene1.jpg
touch $root_dir/01_PreProduction/04_Animatic/animatic_v1.mp4
touch $root_dir/01_PreProduction/05_References/reference_image.jpg
touch $root_dir/02_Production/01_Modeling/Characters/character_model_v1.obj
touch $root_dir/02_Production/01_Modeling/Environments/environment_model_v1.obj
touch $root_dir/02_Production/02_Texturing/Characters/character_texture_v1.png
touch $root_dir/02_Production/02_Texturing/Environments/environment_texture_v1.png
touch $root_dir/02_Production/03_Rigging/Characters/character_rig_v1.blend
touch $root_dir/02_Production/03_Rigging/Props/prop_rig_v1.blend
touch $root_dir/02_Production/04_Animation/Blocking/blocking_scene1_v1.mov
touch $root_dir/02_Production/04_Animation/Final/final_animation_scene1.mov
touch $root_dir/02_Production/04_Animation/Rough/rough_animation_scene1_v1.mov
touch $root_dir/02_Production/05_Programming/AI/enemy_AI_v1.cs
touch $root_dir/02_Production/05_Programming/Gameplay/player_movement_v1.cs
touch $root_dir/02_Production/05_Programming/UI/main_menu_v1.cs
touch $root_dir/02_Production/06_Sound/Effects/explosion_effect_v1.wav
touch $root_dir/02_Production/06_Sound/Music/background_music_v1.mp3
touch $root_dir/02_Production/07_Testing/Bug_Reports/bug_report_v1.txt
touch $root_dir/02_Production/07_Testing/Test_Plans/test_plan_v1.txt
touch $root_dir/03_PostProduction/01_Marketing/Press_Kit/press_kit_v1.pdf
touch $root_dir/03_PostProduction/01_Marketing/Trailers/game_trailer_v1.mp4
touch $root_dir/03_PostProduction/02_Release/Patches/patch_v1.1.zip
touch $root_dir/03_PostProduction/02_Release/Versions/game_v1.0.zip
touch $root_dir/03_PostProduction/03_Reviews/review_v1.txt
touch $root_dir/04_Assets/Backgrounds/background_image.jpg
touch $root_dir/04_Assets/Characters/character_asset.obj
touch $root_dir/04_Assets/Props/prop_asset.obj
touch $root_dir/04_Assets/Textures/wood_texture.png
touch $root_dir/05_Documents/Budget/budget_plan.xlsx
touch $root_dir/05_Documents/Deliverables/deliverables_checklist.txt
touch $root_dir/05_Documents/Production_Schedule/schedule.xlsx
touch $root_dir/05_Documents/Project_Notes/meeting_notes.txt
touch $root_dir/06_Builds/Archive/game_v0.1.zip
touch $root_dir/06_Builds/Final/game_v1.0.zip
touch $root_dir/06_Builds/Previews/game_preview_v0.5.zip