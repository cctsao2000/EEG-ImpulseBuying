import glob,os
import pandas as pd
import numpy as np

def get_events(id):
    log_df = pd.read_csv(f'../log-related/{id}.csv')
    log_np = log_df.to_numpy()
    event_df = pd.DataFrame(np.reshape(log_np,(-1,2)),columns=['row','event']).dropna()
    event_df['row'] = (np.ceil(event_df['row']/250)).astype(int)
    event_dict = dict([(r,e) for r,e in zip(event_df.row, event_df.event)])
    return event_dict

def eeginsert(filename):
    ori_df = pd.read_csv(filename)
    alpha = pd.DataFrame()
    alpha = ori_df.iloc[:,1:]
    alpha.insert(0, 'event', "")
    event_dict = get_events(filename[0])
    for k in event_dict.keys():
        alpha.at[k,'event'] = event_dict[k]
    alpha.to_csv(f'../eeg-rel/{filename[:-4]}.csv',index=False)


def main():
    os.chdir('../eeg-normalized-item')
    for eeg in glob.glob('*.csv'):
        # print(eeg)
        eeginsert(eeg)

if __name__ == '__main__':
    main()