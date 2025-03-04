#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_PreProduction/01_Concepts/VR_Designs
mkdir -p $root_dir/01_PreProduction/01_Concepts/AR_Designs
mkdir -p $root_dir/01_PreProduction/01_Concepts/Styleframes
mkdir -p $root_dir/01_PreProduction/02_Script/Drafts
mkdir -p $root_dir/01_PreProduction/02_Script/Final
mkdir -p $root_dir/01_PreProduction/03_Storyboards
mkdir -p $root_dir/01_PreProduction/04_Animatic
mkdir -p $root_dir/01_PreProduction/05_References
mkdir -p $root_dir/02_Production/01_Modeling/VR_Models
mkdir -p $root_dir/02_Production/01_Modeling/AR_Models
mkdir -p $root_dir/02_Production/02_Texturing/VR_Textures
mkdir -p $root_dir/02_Production/02_Texturing/AR_Textures
mkdir -p $root_dir/02_Production/03_Rigging/VR_Rigs
mkdir -p $root_dir/02_Production/03_Rigging/AR_Rigs
mkdir -p $root_dir/02_Production/04_Animation/VR_Animations
mkdir -p $root_dir/02_Production/04_Animation/AR_Animations
mkdir -p $root_dir/02_Production/05_Lighting
mkdir -p $root_dir/02_Production/06_Effects
mkdir -p $root_dir/02_Production/07_Rendering/VR_Renders
mkdir -p $root_dir/02_Production/07_Rendering/AR_Renders
mkdir -p $root_dir/03_PostProduction/01_Compositing
mkdir -p $root_dir/03_PostProduction/02_Color_Grading
mkdir -p $root_dir/03_PostProduction/03_Sound_Design/Foley
mkdir -p $root_dir/03_PostProduction/03_Sound_Design/Music
mkdir -p $root_dir/03_PostProduction/04_VFX
mkdir -p $root_dir/03_PostProduction/05_Final_Output
mkdir -p $root_dir/04_Assets/VR_Assets
mkdir -p $root_dir/04_Assets/AR_Assets
mkdir -p $root_dir/04_Assets/Textures
mkdir -p $root_dir/05_Documents/Budget
mkdir -p $root_dir/05_Documents/Deliverables
mkdir -p $root_dir/05_Documents/Production_Schedule
mkdir -p $root_dir/05_Documents/Project_Notes
mkdir -p $root_dir/06_Renders/Archive
mkdir -p $root_dir/06_Renders/Final
mkdir -p $root_dir/06_Renders/Previews

# Create files

touch $root_dir/01_PreProduction/01_Concepts/VR_Designs/vr_sketch_v1.jpg
touch $root_dir/01_PreProduction/01_Concepts/VR_Designs/vr_sketch_v2.jpg
touch $root_dir/01_PreProduction/01_Concepts/AR_Designs/ar_sketch_v1.jpg
touch $root_dir/01_PreProduction/01_Concepts/Styleframes/styleframe_concept.jpg
touch $root_dir/01_PreProduction/02_Script/Drafts/script_draft.txt
touch $root_dir/01_PreProduction/02_Script/Final/final_script.txt
touch $root_dir/01_PreProduction/03_Storyboards/storyboard_scene1.jpg
touch $root_dir/01_PreProduction/04_Animatic/animatic_v1.mp4
touch $root_dir/01_PreProduction/05_References/reference_image.jpg
touch $root_dir/02_Production/01_Modeling/VR_Models/vr_model_v1.obj
touch $root_dir/02_Production/01_Modeling/AR_Models/ar_model_v1.obj
touch $root_dir/02_Production/02_Texturing/VR_Textures/vr_texture_v1.png
touch $root_dir/02_Production/02_Texturing/AR_Textures/ar_texture_v1.png
touch $root_dir/02_Production/03_Rigging/VR_Rigs/vr_rig_v1.blend
touch $root_dir/02_Production/03_Rigging/AR_Rigs/ar_rig_v1.blend
touch $root_dir/02_Production/04_Animation/VR_Animations/vr_animation_v1.mov
touch $root_dir/02_Production/04_Animation/AR_Animations/ar_animation_v1.mov
touch $root_dir/02_Production/05_Lighting/lighting_setup_scene1.blend
touch $root_dir/02_Production/06_Effects/effects_scene1_v1.blend
touch $root_dir/02_Production/07_Rendering/VR_Renders/vr_render_v1.psd
touch $root_dir/02_Production/07_Rendering/AR_Renders/ar_render_v1.psd
touch $root_dir/03_PostProduction/01_Compositing/scene1_composite_v1.exr
touch $root_dir/03_PostProduction/02_Color_Grading/scene1_color_grade_v1.dpx
touch $root_dir/03_PostProduction/03_Sound_Design/Foley/footsteps_foley.wav
touch $root_dir/03_PostProduction/03_Sound_Design/Music/background_music.mp3
touch $root_dir/03_PostProduction/04_VFX/scene1_vfx_v1.mov
touch $root_dir/03_PostProduction/05_Final_Output/final_output.mp4
touch $root_dir/04_Assets/VR_Assets/vr_asset.obj
touch $root_dir/04_Assets/AR_Assets/ar_asset.obj
touch $root_dir/04_Assets/Textures/wood_texture.png
touch $root_dir/05_Documents/Budget/budget_plan.xlsx
touch $root_dir/05_Documents/Deliverables/deliverables_checklist.txt
touch $root_dir/05_Documents/Production_Schedule/schedule.xlsx
touch $root_dir/05_Documents/Project_Notes/meeting_notes.txt
touch $root_dir/06_Renders/Archive/scene1_old_render.mp4
touch $root_dir/06_Renders/Final/scene1_final_render.mp4
touch $root_dir/06_Renders/Previews/scene1_preview.mp4