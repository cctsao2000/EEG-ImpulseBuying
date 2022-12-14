import glob,os
import pandas as pd

# analyze eeg data and compare the patterns between impulse buying and non-impulse buying
def ib_anal(band):
    ib_all = pd.DataFrame()
    nib_all = pd.DataFrame()
    for eeg_norm in glob.glob(f'*_{band}_*.csv'):
        eeg_norm_df = pd.read_csv(eeg_norm)
        ib_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['D','E'])].index.tolist()
        ib_events = pd.DataFrame()
        for ib in ib_event_indexes:
            ib_event = eeg_norm_df[ib-20:ib].iloc[:,1:].mean(axis='index') # 1 ib event (5 sec)
            ib_events = pd.concat([ib_events,ib_event],axis=1)
        ib_1p = ib_events.mean(axis='columns') # 1 participant's ib events
        ib_all = pd.concat([ib_all,ib_1p],axis=1) # all participant's ib events
        nib_event_indexes = eeg_norm_df.loc[eeg_norm_df['event'].isin(['X'])].index.tolist()
        nib_events = pd.DataFrame()
        for nib in nib_event_indexes:
            nib_event = eeg_norm_df[nib-20:nib].iloc[:,1:].mean(axis='index')
            nib_events = pd.concat([nib_events,nib_event],axis=1)
        nib_1p = nib_events.mean(axis='columns')
        nib_all = pd.concat([nib_all,nib_1p],axis=1)
    ib_5p = ib_all.mean(axis='columns')
    nib_5p = nib_all.mean(axis='columns')
    ibnib = pd.concat([ib_5p,nib_5p],axis=1)
    ibnib.columns = ["ib", "nib"]
    ibnib.to_csv(f'../eeg-analysis/ibnib_{band}.csv')

def main():
    os.chdir('../eeg-normalized')
    ib_anal('alpha')
    ib_anal('low_beta')
    ib_anal('mid_beta')
    ib_anal('high_beta')

if __name__ == '__main__':
    main()