## Intro
This is used for pre-processing Witcher 3 audio and dialog data.

## Steps
There are 5 files representing 5 steps.
1. 1_convert_csv.py is for converting the w3dialog_id.txt into audio.csv
2. 2_move_audio.py is for moving audio from a single wav folder into folders of the character's name
3. 3_verify_files.py is to add a column in audio.csv indicating whether it exists in audio folder
4. 4_separate_csv.py is to separate audio.csv into character's csv containing only that character dialog
5. 5_create_script is to generate a dialog.txt suitable for gpt-2 fine-tuning