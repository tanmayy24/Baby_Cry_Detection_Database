import os
import json
import shutil
import argparse
import subprocess
import pandas as pd
from glob import glob
from tqdm import tqdm
from youtube_dl import YoutubeDL

def main(args):
    
    data_type = args.data_type
    workspace = args.workspace
    
    # Create directories
    data_path = os.path.join(workspace, 'dataset', data_type)
    os.makedirs(data_path, exist_ok=True)

    if(data_type=='train' or 'validation'):
        csv_path = os.path.join(workspace, 'development set','{}.tsv'.format(data_type))
    if(data_type=='test'):
        csv_path = os.path.join(workspace, 'evaluation set','{}.tsv'.format(data_type))
   
    df = pd.read_csv(csv_path, sep='\t')
    print(df)
    distinct_files = df['name'].unique()
    distinct_set = [(x, df['start'].loc[df['name'] == x].unique()[0]) for x in distinct_files]
    print(len(distinct_set))
    
    root = os.getcwd()
    print('CWD:', root)
    
    # Extract videos from YouTube
    audio_downloader = YoutubeDL({'format':'bestaudio'})
    error_count = 0
    
    for file in tqdm(distinct_set):
        try:
            URL = 'https://www.youtube.com/watch?v={}'.format(file[0])
            command = "ffmpeg -ss " + str(int(file[-1])) + " -t 10 -i $(youtube-dl -f 'bestaudio' -g " + URL + ") -ar " + str(16000) + " -- \"" + '{}/{}_{}'.format(data_path, file[0], int(file[-1])) + ".wav\""
            print('COMMAND:', command)
            os.system((command))
        except Exception:
            error_count += 1
            print("Couldn\'t download the audio")
    print('Number of files that could not be downloaded:', error_count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract AudioSet Dataset')
    parser.add_argument('--workspace', type=str, required=True, help='Directory of your workspace.')
    parser.add_argument('--data_type', type=str, required=True, choices=['train', 'validation', 'test'])
    args = parser.parse_args()

    main(args)