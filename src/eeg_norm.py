import glob,os
import pandas as pd

# normalize eeg data by comparing it with baseline 
def normalize(filename):
    eeg_band_df = pd.read_csv(filename)
    r_2nd = eeg_band_df.loc[eeg_band_df['event'] == 'R'].index.tolist()[1]
    eeg_band_df_2 = eeg_band_df[:r_2nd]
    last_event = eeg_band_df_2.loc[eeg_band_df_2['event'].isin(['D2','E2','X2'])].index.tolist()[-1]+1
    eeg_macbook = eeg_band_df.iloc[:last_event, :]
    eeg_ipad = eeg_band_df.iloc[last_event:, :]

    r_m = eeg_macbook.loc[eeg_macbook['event'] == 'R'].index.tolist()[0]
    baseline_m = eeg_macbook[r_m-20:r_m].mean(axis='index')[2:]
    mac_baselined = eeg_macbook.iloc[:,2:]-baseline_m
    mac_norm = (mac_baselined/baseline_m)
    mac_norm.insert(0, 'event', eeg_band_df['event'][:last_event])

    r_i = eeg_ipad.loc[eeg_ipad['event'] == 'R'].index.tolist()[0]-last_event
    baseline_i = eeg_ipad[r_i-20:r_i].mean(axis='index')[2:]
    ipad_baselined = eeg_ipad.iloc[:,2:]-baseline_i
    ipad_norm = (ipad_baselined/baseline_i)
    ipad_norm.insert(0, 'event', eeg_band_df['event'][last_event:])

    # all_norm = pd.concat([mac_norm,ipad_norm])
    # all_norm.to_csv(f'../eeg-normalized-item/{filename[:-4]}.csv',index=False)
    mac_norm.to_csv(f'../eeg-normalized/{filename[:-4]}_mac.csv',index=False)
    ipad_norm.to_csv(f'../eeg-normalized/{filename[:-4]}_ipad.csv',index=False)


def main():
    os.chdir('../eeg-band')
    for eeg_band in glob.glob('*.csv'):
        try:
            normalize(eeg_band)
        except:
            print(eeg_band)

if __name__ == '__main__':
    main()