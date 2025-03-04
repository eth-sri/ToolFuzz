#!/bin/bash

root_dir=$1

mkdir -p $root_dir/01_PreProduction/01_Songwriting/Lyrics
mkdir -p $root_dir/01_PreProduction/01_Songwriting/Melodies
mkdir -p $root_dir/01_PreProduction/02_Arrangement
mkdir -p $root_dir/01_PreProduction/03_Demos
mkdir -p $root_dir/01_PreProduction/04_References
mkdir -p $root_dir/02_Production/01_Recording/Instruments
mkdir -p $root_dir/02_Production/01_Recording/Vocals
mkdir -p $root_dir/02_Production/02_Editing
mkdir -p $root_dir/02_Production/03_Mixing
mkdir -p $root_dir/02_Production/04_Mastering
mkdir -p $root_dir/03_PostProduction/01_Album_Artwork
mkdir -p $root_dir/03_PostProduction/02_Lyric_Sheet
mkdir -p $root_dir/03_PostProduction/03_Press_Release
mkdir -p $root_dir/03_PostProduction/04_Music_Video
mkdir -p $root_dir/04_Assets/Samples
mkdir -p $root_dir/04_Assets/Plugins
mkdir -p $root_dir/04_Assets/Presets
mkdir -p $root_dir/05_Documents/Budget
mkdir -p $root_dir/05_Documents/Contracts
mkdir -p $root_dir/05_Documents/Production_Schedule
mkdir -p $root_dir/05_Documents/Project_Notes
mkdir -p $root_dir/06_Releases/Singles
mkdir -p $root_dir/06_Releases/Albums
mkdir -p $root_dir/06_Releases/Live_Sessions

touch $root_dir/01_PreProduction/01_Songwriting/Lyrics/song_lyrics_v1.txt
touch $root_dir/01_PreProduction/01_Songwriting/Lyrics/song_lyrics_v2.txt
touch $root_dir/01_PreProduction/01_Songwriting/Melodies/melody_idea_v1.mid
touch $root_dir/01_PreProduction/01_Songwriting/Melodies/melody_idea_v2.mid
touch $root_dir/01_PreProduction/02_Arrangement/arrangement_v1.mid
touch $root_dir/01_PreProduction/02_Arrangement/arrangement_v2.mid
touch $root_dir/01_PreProduction/03_Demos/demo_v1.mp3
touch $root_dir/01_PreProduction/03_Demos/demo_v2.mp3
touch $root_dir/01_PreProduction/04_References/reference_track.mp3
touch $root_dir/02_Production/01_Recording/Instruments/guitar_take1.wav
touch $root_dir/02_Production/01_Recording/Instruments/piano_take1.wav
touch $root_dir/02_Production/01_Recording/Vocals/lead_vocal_take1.wav
touch $root_dir/02_Production/01_Recording/Vocals/backing_vocal_take1.wav
touch $root_dir/02_Production/02_Editing/edited_guitar_take1.wav
touch $root_dir/02_Production/02_Editing/edited_vocal_take1.wav
touch $root_dir/02_Production/03_Mixing/mix_v1.mp3
touch $root_dir/02_Production/03_Mixing/mix_v2.mp3
touch $root_dir/02_Production/04_Mastering/master_v1.wav
touch $root_dir/02_Production/04_Mastering/master_v2.wav
touch $root_dir/03_PostProduction/01_Album_Artwork/album_cover.jpg
touch $root_dir/03_PostProduction/02_Lyric_Sheet/lyric_sheet.pdf
touch $root_dir/03_PostProduction/03_Press_Release/press_release.docx
touch $root_dir/03_PostProduction/04_Music_Video/music_video.mp4
touch $root_dir/04_Assets/Samples/drum_sample.wav
touch $root_dir/04_Assets/Plugins/favorite_reverb.vst
touch $root_dir/04_Assets/Presets/vocal_chain.fxp
touch $root_dir/05_Documents/Budget/budget_plan.xlsx
touch $root_dir/05_Documents/Contracts/recording_contract.pdf
touch $root_dir/05_Documents/Production_Schedule/schedule.xlsx
touch $root_dir/05_Documents/Project_Notes/meeting_notes.txt
touch $root_dir/06_Releases/Singles/single_track.mp3
touch $root_dir/06_Releases/Albums/full_album.zip
touch $root_dir/06_Releases/Live_Sessions/live_session.mp3
