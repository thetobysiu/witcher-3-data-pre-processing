# SIU KING WAI SM4701 Deepstory
# To add a column indicating the existence of audio files, if there's a speaker folder with character name as subfolders
import pandas as pd
import os
import csv

speaker_folder = 'speaker'

df = pd.read_csv('audio.csv', encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)
# used when I'm reading from different directory
# df['Exist'] = df.apply(
#     lambda x: os.path.isfile(
#         f'/home/toby/PycharmProjects/pytorch-dc-tts/datasets/W3Speech/wavs/{x["Audio"]}.wav')
#     if x['Speaker'] == 'Geralt'
#     else os.path.isfile(
#         f'/media/toby/Toby/Users/King/PycharmProjects/parse_audio/speaker/{x["Speaker"]}/{x["Audio"]}.wav'), axis=1)
df['Exist'] = df.apply(lambda x: os.path.isfile(f'{speaker_folder}/{x["Speaker"]}/{x["Audio"]}.wav'), axis=1)
df.to_csv('audio.csv', index=False, encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)

print('done')
