# SIU KING WAI SM4701 Deepstory
# this is a script to create a dialog.txt file from the script to be used for GPT-2 fine tuning
import pandas as pd
import csv

df = pd.read_csv('audio.csv', encoding='utf-8', sep='|', quoting=csv.QUOTE_NONE)
df = df[df['Speaker'] != 'Geralt choice']

# start_token = "<|startoftext|>"
end_token = "<|endoftext|>"
with open('dialog.txt', 'w', encoding='utf-8') as f:
    for scene, scene_df in df.groupby('Scene'):
        if len(scene_df) > 8:
            sentences = scene_df.apply(lambda x: f'{x["Speaker"]}|{x["Content"]}', axis=1)
            dialog = '\n'.join(sentences)
            # f.write(f'{start_token}\n{dialog}\n{end_token}\n')
            f.write(f'{dialog}\n{end_token}\n')
print('done')
