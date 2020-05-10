# SIU KING WAI SM4701 Deepstory
# this separate the generated audio.csv into csv with filename of that character
import pandas as pd
import os
import csv

output_folder = 'separated'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

df = pd.read_csv('audio.csv', encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)
for speaker, speaker_df in df.groupby('Speaker', sort=False):
    speaker_df.to_csv(f'{output_folder}/{speaker}.csv',
                      index=False, encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)

print('done')
