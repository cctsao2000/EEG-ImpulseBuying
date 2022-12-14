import glob,os
import numpy as np
import pandas as pd

# add event marker + output csv by frequency band (4 bands)
def eegbyband(filename):
    ori_df = pd.read_csv(filename)
    timecode = round((ori_df['stamp_i__desc'] - ori_df['stamp_i__desc'][0])*1000).astype(int)
    event_dict = get_events(filename[0])

    alpha = pd.DataFrame()
    alpha = ori_df.iloc[:,7:21]
    alpha.columns = alpha.columns.str.split('_').str[0]
    alpha.insert(0, 'timecode', timecode)
    alpha.insert(1, 'event', "")
    for k in event_dict.keys():
        alpha.at[k,'event'] = event_dict[k]

    low_beta = pd.DataFrame()
    low_beta = ori_df.iloc[:,21:35]
    low_beta.columns = low_beta.columns.str.split('_').str[0]
    low_beta.insert(0, 'timecode', timecode)
    low_beta.insert(1, 'event', "")
    for k in event_dict.keys():
        low_beta.at[k,'event'] = event_dict[k]

    mid_beta = pd.DataFrame()
    mid_beta = ori_df.iloc[:,35:49]
    mid_beta.columns = mid_beta.columns.str.split('_').str[0]
    mid_beta.insert(0, 'timecode', timecode)
    mid_beta.insert(1, 'event', "")
    for k in event_dict.keys():
        mid_beta.at[k,'event'] = event_dict[k]

    high_beta = pd.DataFrame()
    high_beta = ori_df.iloc[:,49:63]
    high_beta.columns = high_beta.columns.str.split('_').str[0]
    high_beta.insert(0, 'timecode', timecode)
    high_beta.insert(1, 'event', "")
    for k in event_dict.keys():
        high_beta.at[k,'event'] = event_dict[k]

    alpha.to_csv(f'../eeg-band/{filename[0]}_alpha.csv',index=False)
    low_beta.to_csv(f'../eeg-band/{filename[0]}_low_beta.csv',index=False)
    mid_beta.to_csv(f'../eeg-band/{filename[0]}_mid_beta.csv',index=False)
    high_beta.to_csv(f'../eeg-band/{filename[0]}_high_beta.csv',index=False)

def get_events(id):
    log_df = pd.read_csv(f'../log-csv/{id}.csv')
    log_np = log_df.to_numpy()
    event_df = pd.DataFrame(np.reshape(log_np,(-1,2)),columns=['row','event']).dropna()
    event_df['row'] = (np.ceil(event_df['row']/250)).astype(int)
    event_df = event_df[1:]
    event_dict = dict([(r,e) for r,e in zip(event_df.row, event_df.event)])
    return event_dict

def main():
    os.chdir('../eeg-raw')
    for logfile in glob.glob('*.csv'):
        eegbyband(logfile)

if __name__ == '__main__':
    main()