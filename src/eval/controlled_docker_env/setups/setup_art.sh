#!/bin/bash

# Root project directory
PROJECT_NAME=$1
mkdir -p "$PROJECT_NAME"

# Pre-Production
mkdir -p "$PROJECT_NAME/01_PreProduction/01_Concepts/Character_Designs"
touch "$PROJECT_NAME/01_PreProduction/01_Concepts/Character_Designs/character_sketch_v1.jpg"
touch "$PROJECT_NAME/01_PreProduction/01_Concepts/Character_Designs/character_sketch_v2.jpg"

mkdir -p "$PROJECT_NAME/01_PreProduction/01_Concepts/Environment_Designs"
touch "$PROJECT_NAME/01_PreProduction/01_Concepts/Environment_Designs/environment_sketch_v1.jpg"

mkdir -p "$PROJECT_NAME/01_PreProduction/01_Concepts/Styleframes"
touch "$PROJECT_NAME/01_PreProduction/01_Concepts/Styleframes/styleframe_concept.jpg"

mkdir -p "$PROJECT_NAME/01_PreProduction/02_Script/Drafts"
touch "$PROJECT_NAME/01_PreProduction/02_Script/Drafts/script_draft.txt"

mkdir -p "$PROJECT_NAME/01_PreProduction/02_Script/Final"
touch "$PROJECT_NAME/01_PreProduction/02_Script/Final/final_script.txt"

mkdir -p "$PROJECT_NAME/01_PreProduction/03_Storyboards"
touch "$PROJECT_NAME/01_PreProduction/03_Storyboards/storyboard_scene1.jpg"

mkdir -p "$PROJECT_NAME/01_PreProduction/04_Animatic"
touch "$PROJECT_NAME/01_PreProduction/04_Animatic/animatic_v1.mp4"

mkdir -p "$PROJECT_NAME/01_PreProduction/05_References"
touch "$PROJECT_NAME/01_PreProduction/05_References/reference_image.jpg"

# Production
mkdir -p "$PROJECT_NAME/02_Production/01_Modeling/Characters"
touch "$PROJECT_NAME/02_Production/01_Modeling/Characters/character_model_v1.obj"

mkdir -p "$PROJECT_NAME/02_Production/01_Modeling/Environments"
touch "$PROJECT_NAME/02_Production/01_Modeling/Environments/environment_model_v1.obj"

mkdir -p "$PROJECT_NAME/02_Production/02_Texturing/Characters"
touch "$PROJECT_NAME/02_Production/02_Texturing/Characters/character_texture_v1.png"

mkdir -p "$PROJECT_NAME/02_Production/02_Texturing/Environments"
touch "$PROJECT_NAME/02_Production/02_Texturing/Environments/environment_texture_v1.png"

mkdir -p "$PROJECT_NAME/02_Production/03_Rigging/Characters"
touch "$PROJECT_NAME/02_Production/03_Rigging/Characters/character_rig_v1.blend"

mkdir -p "$PROJECT_NAME/02_Production/03_Rigging/Props"
touch "$PROJECT_NAME/02_Production/03_Rigging/Props/prop_rig_v1.blend"

mkdir -p "$PROJECT_NAME/02_Production/04_Animation/Blocking"
touch "$PROJECT_NAME/02_Production/04_Animation/Blocking/blocking_scene1_v1.mov"

mkdir -p "$PROJECT_NAME/02_Production/04_Animation/Rough"
touch "$PROJECT_NAME/02_Production/04_Animation/Rough/rough_animation_scene1_v1.mov"

mkdir -p "$PROJECT_NAME/02_Production/04_Animation/Final"
touch "$PROJECT_NAME/02_Production/04_Animation/Final/final_animation_scene1.mov"

mkdir -p "$PROJECT_NAME/02_Production/05_Lighting"
touch "$PROJECT_NAME/02_Production/05_Lighting/lighting_setup_scene1.blend"

mkdir -p "$PROJECT_NAME/02_Production/06_Effects"
touch "$PROJECT_NAME/02_Production/06_Effects/effects_scene1_v1.blend"

mkdir -p "$PROJECT_NAME/02_Production/07_Rendering/Render_Layers"
touch "$PROJECT_NAME/02_Production/07_Rendering/Render_Layers/scene1_layer1.exr"

mkdir -p "$PROJECT_NAME/02_Production/07_Rendering/Comps"
touch "$PROJECT_NAME/02_Production/07_Rendering/Comps/scene1_comp_v1.psd"

# Post-Production
mkdir -p "$PROJECT_NAME/03_PostProduction/01_Compositing"
touch "$PROJECT_NAME/03_PostProduction/01_Compositing/scene1_composite_v1.exr"

mkdir -p "$PROJECT_NAME/03_PostProduction/02_Color_Grading"
touch "$PROJECT_NAME/03_PostProduction/02_Color_Grading/scene1_color_grade_v1.dpx"

mkdir -p "$PROJECT_NAME/03_PostProduction/03_Sound_Design/Foley"
touch "$PROJECT_NAME/03_PostProduction/03_Sound_Design/Foley/footsteps_foley.wav"

mkdir -p "$PROJECT_NAME/03_PostProduction/03_Sound_Design/Music"
touch "$PROJECT_NAME/03_PostProduction/03_Sound_Design/Music/background_music.mp3"

mkdir -p "$PROJECT_NAME/03_PostProduction/04_VFX"
touch "$PROJECT_NAME/03_PostProduction/04_VFX/scene1_vfx_v1.mov"

mkdir -p "$PROJECT_NAME/03_PostProduction/05_Final_Output"
touch "$PROJECT_NAME/03_PostProduction/05_Final_Output/final_output.mp4"

# Assets
mkdir -p "$PROJECT_NAME/04_Assets/Characters"
touch "$PROJECT_NAME/04_Assets/Characters/character_asset.obj"

mkdir -p "$PROJECT_NAME/04_Assets/Props"
touch "$PROJECT_NAME/04_Assets/Props/prop_asset.obj"

mkdir -p "$PROJECT_NAME/04_Assets/Textures"
touch "$PROJECT_NAME/04_Assets/Textures/wood_texture.png"

mkdir -p "$PROJECT_NAME/04_Assets/Backgrounds"
touch "$PROJECT_NAME/04_Assets/Backgrounds/background_image.jpg"

# Documents
mkdir -p "$PROJECT_NAME/05_Documents/Production_Schedule"
touch "$PROJECT_NAME/05_Documents/Production_Schedule/schedule.xlsx"

mkdir -p "$PROJECT_NAME/05_Documents/Budget"
touch "$PROJECT_NAME/05_Documents/Budget/budget_plan.xlsx"

mkdir -p "$PROJECT_NAME/05_Documents/Project_Notes"
touch "$PROJECT_NAME/05_Documents/Project_Notes/meeting_notes.txt"

mkdir -p "$PROJECT_NAME/05_Documents/Deliverables"
touch "$PROJECT_NAME/05_Documents/Deliverables/deliverables_checklist.txt"

# Renders
mkdir -p "$PROJECT_NAME/06_Renders/Previews"
touch "$PROJECT_NAME/06_Renders/Previews/scene1_preview.mp4"

mkdir -p "$PROJECT_NAME/06_Renders/Final"
touch "$PROJECT_NAME/06_Renders/Final/scene1_final_render.mp4"

mkdir -p "$PROJECT_NAME/06_Renders/Archive"
touch "$PROJECT_NAME/06_Renders/Archive/scene1_old_render.mp4"
