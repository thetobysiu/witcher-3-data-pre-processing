# SIU KING WAI SM4701 Deepstory
# Move the wav folder into speaker folder containing subfolders of characters' audio files
import pandas as pd
import os
import logging
from datetime import datetime

wav_folder = 'wav'
speaker_folder = 'speaker'

now = datetime.now()
logging.basicConfig(filename=f'Error_{now.strftime("%Y-%m-%d_%H:%M:%S")}.log', filemode='w', level=logging.DEBUG)
df = pd.read_csv('audio.csv', encoding='utf-8', sep='|')

for _, row in df.iterrows():
    if not os.path.exists(f'{speaker_folder}/{row["Speaker"]}'):
        os.makedirs(f'{speaker_folder}/{row["Speaker"]}')
    try:
        os.rename(f'{wav_folder}/{row["Audio"]}.wav.ogg.wav', f'{speaker_folder}/{row["Speaker"]}/{row["Audio"]}.wav')
    except FileNotFoundError:
        logging.warning(f'{row["Audio"]} is not found!')

print('done')
