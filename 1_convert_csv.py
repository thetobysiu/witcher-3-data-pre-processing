# SIU KING WAI SM4701 Deepstory
# create audio.csv from raw txt
import re
import pandas as pd
import csv

with open('w3dialog_id.txt', 'r', encoding='utf-8') as f:
    audio_list_file = f.read()

audio_list = [re.sub(r'^\s+', '', x) for x in audio_list_file.split('\n') if x]
audio_list = [x for x in audio_list if x[0].isalpha() or x[0].isnumeric()]

data = []
current_scene = ''
for x in audio_list:
    if x[0].isalpha():
        current_scene = x.split('/')[-1].split('.')[0]
    else:
        content_id, audio_id, audio_string = re.split(r'\s+', x, 2)
        char, content = audio_string.split(': ', 1)
        data.append([char, audio_id, current_scene, content_id, content])

df = pd.DataFrame(data, columns=['Speaker', 'Audio', 'Scene', 'ID', 'Content'])
df.drop_duplicates('Audio', inplace=True)
df.to_csv('audio.csv', index=False, encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)

print('done')
